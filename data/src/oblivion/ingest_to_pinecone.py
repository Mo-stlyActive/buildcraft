#!/usr/bin/env python3
"""
Ingest Oblivion Processed Data into Pinecone using HuggingFace Embeddings
"""

import os
import json
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec

# Configuration
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
INDEX_NAME = "oblivion-buildcraft"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
DATA_PATH = "data/oblivion/oblivion_processed.json"

if not PINECONE_API_KEY:
    print("❌ Please set your Pinecone API key as the PINECONE_API_KEY environment variable.")
    exit(1)

def main():
    # Load data
    print(f"Loading data from {DATA_PATH}...")
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Prepare documents for embedding
    all_docs = []
    for category in ["skills", "weapons", "armor", "potions", "spells"]:
        for item in data.get(category, []):
            # Create a text chunk for each item
            doc_text = f"Category: {category}\n"
            for k, v in item.items():
                doc_text += f"{k.capitalize()}: {v}\n"
            
            all_docs.append({
                "text": doc_text,
                "metadata": {
                    "category": category, 
                    "name": item.get("name", ""),
                    "type": item.get("type", "unknown"),
                    "properties": {k: v for k, v in item.items() if k not in ["name", "type", "category"]}
                }
            })

    print(f"Loaded {len(all_docs)} documents for embedding and ingestion.")

    # Initialize embedding model
    print(f"Loading HuggingFace embedding model: {EMBEDDING_MODEL}")
    embedder = SentenceTransformer(EMBEDDING_MODEL)

    # Initialize Pinecone
    pc = Pinecone(api_key=PINECONE_API_KEY)

    # Create index if it doesn't exist
    if INDEX_NAME not in pc.list_indexes().names():
        print(f"Creating Pinecone index: {INDEX_NAME}")
        pc.create_index(
            name=INDEX_NAME,
            dimension=384,  # all-MiniLM-L6-v2 outputs 384-dim vectors
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1")
        )

    # Connect to the index
    pc_index = pc.Index(INDEX_NAME)

    # Embed and ingest data
    print("Embedding and uploading documents to Pinecone...")
    
    batch_size = 64
    for i in tqdm(range(0, len(all_docs), batch_size)):
        batch = all_docs[i:i+batch_size]
        texts = [doc["text"] for doc in batch]
        embeddings = embedder.encode(texts, show_progress_bar=False)
        
        # Prepare Pinecone upsert format
        vectors = []
        for doc, emb in zip(batch, embeddings):
            vectors.append({
                "id": f"{doc['metadata']['category']}-{doc['metadata']['name'].replace(' ', '_')}-{i}",
                "values": emb.tolist(),
                "metadata": doc["metadata"]
            })
        
        pc_index.upsert(vectors)

    print(f"✅ Ingestion complete! {len(all_docs)} documents embedded and uploaded to Pinecone index '{INDEX_NAME}'.")
    print("You can now use semantic search with this data in BuildCraft AI.")

if __name__ == "__main__":
    main() 