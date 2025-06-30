# BuildCraft AI - Deployment Guide

## Overview

This guide covers deploying the BuildCraft AI system in different environments.

## Prerequisites

- Node.js >= 18.0.0
- Python 3.10+
- Pinecone account and API key
- Git

## Local Development Deployment

### 1. Clone the Repository

```bash
git clone <repository-url>
cd buildcraft
```

### 2. Set Up Search Service

```bash
cd api/python-search

# Install Python dependencies
pip install -r requirements.txt

# Set environment variables
export PINECONE_API_KEY="your-pinecone-api-key"

# Start the service
python3 main.py
```

The search service will be available at `http://localhost:8001`

### 3. Set Up Frontend

```bash
cd web

# Install Node.js dependencies
npm install

# Start development server
npm run dev
```

The frontend will be available at `http://localhost:3000`

## Production Deployment

### Option 1: Docker Deployment

#### Create Dockerfile for Search Service

```dockerfile
# api/python-search/Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8001

CMD ["python3", "main.py"]
```

#### Create Dockerfile for Frontend

```dockerfile
# web/Dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --only=production

COPY . .
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]
```

#### Docker Compose Setup

```yaml
# docker-compose.yml
version: '3.8'

services:
  search-service:
    build: ./api/python-search
    ports:
      - "8001:8001"
    environment:
      - PINECONE_API_KEY=${PINECONE_API_KEY}
    restart: unless-stopped

  frontend:
    build: ./web
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_API_URL=http://localhost:8001
    depends_on:
      - search-service
    restart: unless-stopped
```

### Option 2: Cloud Deployment

#### Deploy to Railway

1. **Search Service:**
```bash
cd api/python-search
railway login
railway init
railway up
```

2. **Frontend:**
```bash
cd web
railway login
railway init
railway up
```

#### Deploy to Heroku

1. **Search Service:**
```bash
cd api/python-search
heroku create buildcraft-search
heroku config:set PINECONE_API_KEY=your-key
git push heroku main
```

2. **Frontend:**
```bash
cd web
heroku create buildcraft-frontend
heroku config:set NEXT_PUBLIC_API_URL=https://your-search-service.herokuapp.com
git push heroku main
```

#### Deploy to Vercel (Frontend)

```bash
cd web
vercel --prod
```

## Environment Variables

### Search Service

| Variable | Description | Required |
|----------|-------------|----------|
| `PINECONE_API_KEY` | Pinecone vector database API key | Yes |
| `PINECONE_INDEX_NAME` | Pinecone index name | Yes |
| `EMBEDDING_MODEL` | HuggingFace embedding model | No (default: all-MiniLM-L6-v2) |

### Frontend

| Variable | Description | Required |
|----------|-------------|----------|
| `NEXT_PUBLIC_API_URL` | Search service URL | Yes |

## Monitoring and Logging

### Search Service Logs

```bash
# View logs
docker logs buildcraft-search-service

# Or if running directly
tail -f /var/log/buildcraft-search.log
```

### Frontend Logs

```bash
# View logs
docker logs buildcraft-frontend

# Or if running directly
tail -f /var/log/buildcraft-frontend.log
```

## Health Checks

### Search Service Health

```bash
curl http://localhost:8001/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "buildcraft-search"
}
```

### Frontend Health

```bash
curl http://localhost:3000
```

Should return the main page HTML.

## Troubleshooting

### Common Issues

1. **Search Service Won't Start**
   - Check Pinecone API key is set correctly
   - Verify Python dependencies are installed
   - Check port 8001 is not in use

2. **Frontend Can't Connect to API**
   - Verify `NEXT_PUBLIC_API_URL` is set correctly
   - Check CORS settings in search service
   - Ensure search service is running

3. **Vector Search Not Working**
   - Verify Pinecone index exists and has data
   - Check embedding model is downloading correctly
   - Review search service logs for errors

### Performance Optimization

1. **Search Service**
   - Use GPU acceleration for embeddings if available
   - Implement caching for frequent queries
   - Consider using a production ASGI server like Gunicorn

2. **Frontend**
   - Enable Next.js production optimizations
   - Implement request caching
   - Use CDN for static assets

## Security Considerations

1. **API Security**
   - Add API key authentication
   - Implement rate limiting
   - Use HTTPS in production
   - Validate all input parameters

2. **Data Security**
   - Secure Pinecone API key storage
   - Implement proper CORS policies
   - Sanitize user inputs

3. **Infrastructure Security**
   - Use secure container images
   - Implement network policies
   - Regular security updates 