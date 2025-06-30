# BuildCraft AI - API Documentation

## Overview

The BuildCraft AI search service provides semantic search and build generation capabilities for RPG games, starting with The Elder Scrolls IV: Oblivion.

**Base URL**: `http://localhost:8001`

## Endpoints

### Health Check

**GET** `/health`

Check if the service is running.

**Response:**
```json
{
  "status": "healthy",
  "service": "buildcraft-search"
}
```

### Semantic Search

**POST** `/search`

Search for game items, skills, or equipment using semantic similarity.

**Request Body:**
```json
{
  "query": "stealth archer",
  "category": "skills",
  "limit": 5
}
```

**Parameters:**
- `query` (string, required): Search query
- `category` (string, optional): Filter by category (skills, weapons, armor, spells, items)
- `limit` (number, optional): Maximum number of results (default: 5)

**Response:**
```json
{
  "results": [
    {
      "name": "Agility",
      "category": "skills",
      "type": "unknown",
      "properties": {},
      "score": 0.312035263
    }
  ],
  "reasoning": "Found 3 relevant items for 'stealth archer'",
  "suggestions": [
    "Try searching for armor to complement these weapons",
    "Search for perks that enhance these skills"
  ]
}
```

### Build Generation

**POST** `/build`

Generate an AI-powered character build based on a description.

**Request Body:**
```json
{
  "prompt": "stealth archer build",
  "playstyle": "ranged",
  "difficulty": "normal"
}
```

**Parameters:**
- `prompt` (string, required): Build description
- `playstyle` (string, optional): Preferred playstyle
- `difficulty` (string, optional): Game difficulty (easy, normal, hard)

**Response:**
```json
{
  "build_name": "Custom Build for stealth archer build...",
  "skills": ["Agility", "Strength"],
  "key_items": ["Spell 000C48A5", "Spell 000C48A4"],
  "playstyle": "Balanced combat with support abilities",
  "reasoning": "Generated build based on 10 relevant items from the knowledge base",
  "synergies": ["Skills complement each other", "Equipment enhances abilities"],
  "progression": ["Start with basic skills", "Advance to specialized techniques"]
}
```

## Error Responses

All endpoints may return the following error responses:

**400 Bad Request:**
```json
{
  "detail": "Invalid request parameters"
}
```

**500 Internal Server Error:**
```json
{
  "detail": "Search error: [error message]"
}
```

## CORS

The API supports CORS for frontend integration. All endpoints accept OPTIONS requests for preflight checks.

## Rate Limiting

Currently no rate limiting is implemented. Consider implementing rate limiting for production use.

## Authentication

Currently no authentication is required. Consider adding API key authentication for production use. 