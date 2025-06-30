#!/usr/bin/env python3
"""
BuildCraft AI - Python Search Service
Advanced semantic search and build recommendations for RPG games
"""

import os
from typing import List, Dict, Any, Optional
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

# Vector search imports
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec

# Load environment variables
load_dotenv()

# Configuration
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
INDEX_NAME = "oblivion-buildcraft"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Global variables
pc = None
pinecone_index = None
embed_model = None

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
    skills: List[str]
    key_items: List[str]
    playstyle: str
    reasoning: str
    synergies: List[str]
    progression: List[str]

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize and cleanup resources"""
    global pc, pinecone_index, embed_model
    
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
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )
    
    # Connect to index
    pinecone_index = pc.Index(INDEX_NAME)
    
    # Initialize embedding model
    embed_model = SentenceTransformer(EMBEDDING_MODEL)
    
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
        # Generate embedding for the query
        query_embedding = embed_model.encode(request.query).tolist()
        
        # Search in Pinecone
        search_results = pinecone_index.query(
            vector=query_embedding,
            top_k=request.limit,
            include_metadata=True
        )
        
        # Process results
        results = []
        for match in search_results.matches:
            if match.metadata:
                results.append({
                    "name": match.metadata.get("name", "Unknown"),
                    "category": match.metadata.get("category", "unknown"),
                    "type": match.metadata.get("type", "unknown"),
                    "properties": match.metadata.get("properties", {}),
                    "score": match.score
                })
        
        # Generate reasoning and suggestions
        reasoning = f"Found {len(results)} relevant items for '{request.query}'"
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
        # Create a comprehensive build query
        build_query = f"build recommendation {request.prompt} {request.playstyle or ''} {request.difficulty}"
        
        # Generate embedding for the build query
        query_embedding = embed_model.encode(build_query).tolist()
        
        # Search in Pinecone
        search_results = pinecone_index.query(
            vector=query_embedding,
            top_k=10,
            include_metadata=True
        )
        
        # Process results to extract build components
        build_data = parse_build_results(search_results.matches, request.prompt)
        
        return BuildResponse(**build_data)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Build generation error: {str(e)}")

def parse_build_results(matches: List, original_prompt: str) -> Dict[str, Any]:
    """Parse search results into build format"""
    skills = []
    key_items = []
    
    for match in matches:
        if match.metadata:
            name = match.metadata.get("name", "")
            category = match.metadata.get("category", "")
            
            if category == "skills":
                skills.append(name)
            elif category in ["weapons", "armor", "potions", "spells"]:
                key_items.append(name)
    
    # Add default suggestions if not enough found
    if not skills:
        skills = ["Blade", "Alchemy", "Restoration"]
    if not key_items:
        key_items = ["Iron Sword", "Healing Potion"]
    
    return {
        "build_name": f"Custom Build for {original_prompt[:30]}...",
        "skills": skills[:5],
        "key_items": key_items[:3],
        "playstyle": "Balanced combat with support abilities",
        "reasoning": f"Generated build based on {len(matches)} relevant items from the knowledge base",
        "synergies": ["Skills complement each other", "Equipment enhances abilities"],
        "progression": ["Start with basic skills", "Advance to specialized techniques"]
    }

def generate_suggestions(query: str, results: List[Dict[str, Any]]) -> List[str]:
    """Generate follow-up suggestions based on search results"""
    suggestions = []
    
    # Analyze results to generate suggestions
    categories = set(result.get("category", "") for result in results)
    
    if "weapons" in categories:
        suggestions.append("Try searching for armor to complement these weapons")
    if "skills" in categories:
        suggestions.append("Search for perks that enhance these skills")
    if "spells" in categories:
        suggestions.append("Look for items that reduce spell costs")
    
    # Add general suggestions
    suggestions.extend([
        "Search for build synergies",
        "Find equipment recommendations",
        "Look for advanced techniques"
    ])
    
    return suggestions[:5]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) 