#!/usr/bin/env python3
"""
BuildCraft AI - Python Search Service
Advanced semantic search and build recommendations for RPG games
"""

import os
import json
from typing import List, Dict, Any, Optional
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Vector search imports
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec

# Local imports
from build_composer import OblivionBuildComposer
from oblivion_gamedata import OBLIVION_GAMEDATA

# Load environment variables
load_dotenv()

# Configuration
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_REGION = os.getenv("PINECONE_REGION", "us-east-1")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
INDEX_NAME = "oblivion-buildcraft"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Global variables
pc = None
pinecone_index = None
embed_model = None
build_composer = None
game_data = None

# Pydantic models
class SearchRequest(BaseModel):
    query: str
    category: Optional[str] = None  # skills, weapons, armor, potions, spells
    limit: Optional[int] = 5

class SearchResponse(BaseModel):
    results: List[Dict[str, Any]]
    reasoning: str
    suggestions: List[str]

class BuildRequest(BaseModel):
    prompt: str
    playstyle: Optional[str] = None
    difficulty: Optional[str] = "normal"

class BuildResponse(BaseModel):
    build_name: str
    race: str
    race_description: str
    skills: List[str]
    skill_details: List[Dict[str, Any]]
    equipment: Dict[str, List[str]]
    spells: List[str]
    playstyle: str
    reasoning: str
    synergies: List[str]
    progression: List[str]
    roleplay_flavor: str
    tips: List[str]

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize and cleanup resources"""
    global pc, pinecone_index, embed_model, build_composer, game_data
    
    # Startup
    if not PINECONE_API_KEY:
        raise ValueError("PINECONE_API_KEY environment variable is required")
    
    if not OPENAI_API_KEY:
        print("Warning: OPENAI_API_KEY not set. Using local embeddings only.")
    
    # Initialize Pinecone
    pc = Pinecone(api_key=PINECONE_API_KEY)
    
    # Check if index exists
    if INDEX_NAME not in pc.list_indexes().names():
        print(f"Creating Pinecone index: {INDEX_NAME}")
        pc.create_index(
            name=INDEX_NAME,
            dimension=384,  # all-MiniLM-L6-v2 dimension
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region=PINECONE_REGION)
        )
    
    # Connect to index
    pinecone_index = pc.Index(INDEX_NAME)
    
    # Initialize embedding model
    embed_model = SentenceTransformer(EMBEDDING_MODEL)
    
    # Initialize build composer
    build_composer = OblivionBuildComposer()
    
    # Load game data
    game_data = OBLIVION_GAMEDATA
    
    # Check if database is already populated
    try:
        stats = pinecone_index.describe_index_stats()
        total_vectors = stats.total_vector_count
        if total_vectors > 0:
            print(f"✅ Database already contains {total_vectors} vectors, skipping population")
        else:
            print("📊 Database empty, populating with game data...")
            await populate_vector_database()
    except Exception as e:
        print(f"Warning: Could not check database status: {e}")
        print("Proceeding without population check...")
    
    print("✅ Search service initialized successfully!")
    
    yield
    
    # Shutdown (cleanup if needed)
    print("Shutting down search service...")

# Initialize FastAPI app
app = FastAPI(
    title="BuildCraft AI Search Service",
    description="Advanced semantic search and build recommendations for RPG games",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "buildcraft-search"}

@app.post("/search", response_model=SearchResponse)
async def semantic_search(request: SearchRequest):
    """Semantic search for game items and skills"""
    try:
        # Create enhanced query with category filter if specified
        enhanced_query = request.query
        if request.category:
            enhanced_query += f" {request.category}"
        
        # Generate embedding for the query
        query_embedding = embed_model.encode(enhanced_query).tolist()
        
        # Search in Pinecone
        search_results = pinecone_index.query(
            vector=query_embedding,
            top_k=request.limit or 5,
            include_metadata=True
        )
        
        # Process results
        results = []
        for match in search_results.matches:
            if match.metadata:
                result_item = {
                    "name": match.metadata.get("name", "Unknown"),
                    "category": match.metadata.get("category", "unknown"),
                    "type": match.metadata.get("type", "unknown"),
                    "description": match.metadata.get("description", ""),
                    "tags": match.metadata.get("tags", []),
                    "properties": match.metadata.get("properties", {}),
                    "score": round(match.score, 3)
                }
                
                # Filter by category if requested
                if request.category:
                    if (request.category.lower() in result_item["category"].lower() or 
                        request.category.lower() in result_item["type"].lower() or
                        request.category.lower() in [tag.lower() for tag in result_item["tags"]]):
                        results.append(result_item)
                else:
                    results.append(result_item)
        
        # Generate reasoning and suggestions
        if results:
            categories = set(result["category"] for result in results)
            reasoning = f"Found {len(results)} relevant items across {len(categories)} categories: {', '.join(categories)}"
        else:
            reasoning = f"No items found matching '{request.query}'. Try different keywords or broader terms."
        
        suggestions = generate_suggestions(request.query, results)
        
        return SearchResponse(
            results=results,
            reasoning=reasoning,
            suggestions=suggestions
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Search error: {str(e)}")

@app.post("/build", response_model=BuildResponse)
async def generate_build(request: BuildRequest):
    """Generate build recommendations based on user preferences"""
    try:
        # Analyze user intent
        intent = build_composer.analyze_user_intent(request.prompt)
        
        # Create a comprehensive build query
        build_query = f"{request.prompt} {request.playstyle or ''} {request.difficulty} {' '.join(intent['themes'])}"
        
        # Generate embedding for the build query
        query_embedding = embed_model.encode(build_query).tolist()
        
        # Search in Pinecone for relevant items
        search_results = pinecone_index.query(
            vector=query_embedding,
            top_k=30,  # Get more results for better composition
            include_metadata=True
        )
        
        # Convert pinecone results to format expected by build composer
        formatted_results = []
        for match in search_results.matches:
            if match.metadata:
                formatted_results.append({
                    "name": match.metadata.get("name", "Unknown"),
                    "category": match.metadata.get("category", "unknown"),
                    "type": match.metadata.get("type", "unknown"),
                    "properties": match.metadata.get("properties", {}),
                    "score": match.score,
                    "tags": match.metadata.get("tags", []),
                    "description": match.metadata.get("description", "")
                })
        
        # Generate dynamic build using the composer
        build_data = build_composer.compose_build_from_search_results(intent, formatted_results)
        
        return BuildResponse(**build_data)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Build generation error: {str(e)}")

async def populate_vector_database():
    """Populate Pinecone with rich game data"""
    print("Populating vector database with game data...")
    
    # Use OBLIVION_GAMEDATA directly
    data_source = OBLIVION_GAMEDATA if game_data is None else game_data
    
    # Prepare documents for embedding
    documents = []
    
    for category, items in data_source.items():
        for item in items:
            # Create rich text representation for embedding
            text_parts = [
                item["name"],
                item.get("description", ""),
                " ".join(item.get("tags", [])),
                item.get("category", ""),
                item.get("type", "")
            ]
            
            # Add category-specific information
            if category == "skills":
                text_parts.extend([
                    item.get("governing_attribute", ""),
                    item.get("combat_role", ""),
                    " ".join(item.get("synergies", []))
                ])
            elif category == "weapons":
                text_parts.extend([
                    item.get("skill_required", ""),
                    item.get("damage_type", ""),
                    item.get("rarity", "")
                ])
            elif category == "spells":
                text_parts.extend([
                    item.get("school", ""),
                    item.get("effect", "")
                ])
            
            # Create document text
            doc_text = " ".join(filter(None, text_parts))
            
            documents.append({
                "id": f"{category}_{len(documents)}",
                "text": doc_text,
                "metadata": {
                    "name": item["name"],
                    "category": category,
                    "type": item.get("type", category),
                    "description": item.get("description", ""),
                    "tags": ",".join(item.get("tags", [])) if item.get("tags") else "",
                }
            })
    
    # Generate embeddings and upsert to Pinecone
    batch_size = 100
    for i in range(0, len(documents), batch_size):
        batch = documents[i:i + batch_size]
        
        # Generate embeddings
        texts = [doc["text"] for doc in batch]
        embeddings = embed_model.encode(texts).tolist()
        
        # Prepare upsert data
        upsert_data = []
        for j, doc in enumerate(batch):
            upsert_data.append({
                "id": doc["id"],
                "values": embeddings[j],
                "metadata": doc["metadata"]
            })
        
        # Upsert to Pinecone
        pinecone_index.upsert(vectors=upsert_data)
    
    print(f"✅ Populated vector database with {len(documents)} items")

def generate_suggestions(query: str, results: List[Dict[str, Any]]) -> List[str]:
    """Generate follow-up suggestions based on search results"""
    suggestions = []
    
    # Analyze results to generate suggestions
    categories = set(result.get("category", "") for result in results)
    
    if "weapons" in categories:
        suggestions.append("Try searching for armor to complement these weapons")
    if "skills" in categories:
        suggestions.append("Search for synergistic skills and abilities")
    if "spells" in categories:
        suggestions.append("Look for enchantments that enhance spell effects")
    if "armor" in categories:
        suggestions.append("Find weapons that match your armor style")
    
    # Add build-specific suggestions
    if any("stealth" in result.get("tags", []) for result in results):
        suggestions.append("Create a stealth archer or assassin build")
    if any("magic" in result.get("tags", []) for result in results):
        suggestions.append("Generate a spellsword or battlemage build")
    if any("warrior" in result.get("tags", []) for result in results):
        suggestions.append("Build a tank or berserker character")
    
    # Add general suggestions
    suggestions.extend([
        "Generate a complete character build",
        "Find racial recommendations",
        "Explore advanced build combinations"
    ])
    
    return suggestions[:5]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 