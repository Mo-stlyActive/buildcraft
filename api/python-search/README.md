# BuildCraft AI - Python Search Service

Advanced semantic search service for game build recommendations using Pinecone and HuggingFace embeddings.

## Features

- **Semantic Search**: Find relevant skills, weapons, armor, potions, and spells
- **Build Generation**: AI-powered build recommendations with reasoning
- **Vector Search**: Fast similarity search using Pinecone
- **Local Embeddings**: No API costs using HuggingFace models

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Environment Configuration**:
   ```bash
   cp env.example .env
   # Edit .env with your API keys
   ```

3. **Required Environment Variables**:
   - `PINECONE_API_KEY`: Your Pinecone API key (required)
   - `OPENAI_API_KEY`: OpenAI API key (optional, for future enhancements)

## Running the Service

```bash
# Development
python main.py

# Or with uvicorn directly
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

## API Endpoints

### Health Check
```bash
GET /health
```

### Semantic Search
```bash
POST /search
{
  "query": "stealth archer build",
  "category": "skills",  # optional
  "limit": 5  # optional
}
```

### Build Generation
```bash
POST /build
{
  "prompt": "I want a powerful mage build",
  "playstyle": "aggressive",  # optional
  "difficulty": "hard"  # optional
}
```

## Integration with Node.js API

The Node.js API can call this Python service for advanced queries:

```typescript
// Example: Call Python search service from Node.js
const searchResponse = await fetch('http://localhost:8001/search', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ query: 'stealth build', limit: 5 })
});
```

## Architecture

- **FastAPI**: Web framework for the service
- **Pinecone**: Vector database for semantic search
- **HuggingFace**: Local embeddings (all-MiniLM-L6-v2)
- **Sentence Transformers**: High-quality text embeddings

## Development

The service automatically initializes Pinecone and the embedding model on startup. It connects to the existing `oblivion-buildcraft` index created by the data pipeline. 