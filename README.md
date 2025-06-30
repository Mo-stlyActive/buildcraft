# BuildCraft AI - Monorepo

AI-powered game build advisor for RPGs, starting with The Elder Scrolls IV: Oblivion. Built with a scalable monorepo architecture featuring semantic search and intelligent build generation.

## 🎮 Current Status

**✅ WORKING FEATURES:**
- **Search Service**: Python FastAPI with HuggingFace embeddings and Pinecone vector database
- **Frontend**: Next.js chat interface with real-time search and build generation
- **Smart Request Routing**: Automatically detects search vs build requests
- **Beautiful UI**: Responsive design with search results and build suggestion cards
- **Local AI**: No external API dependencies, fully self-contained

## Project Structure

```
buildcraft/
├── web/                           # Next.js frontend application
│   ├── src/components/chat/      # Chat interface components
│   ├── src/lib/api.ts           # API integration
│   └── src/types/chat.ts        # TypeScript types
├── api/python-search/            # Python FastAPI search service
│   ├── main.py                  # FastAPI application
│   ├── requirements.txt         # Python dependencies
│   └── data/                    # Game data storage
├── data/                        # Game data scraping and processing
│   ├── oblivion/               # Oblivion-specific data
│   └── shared/                 # Shared data structures
├── packages/                    # Shared packages/libraries
│   ├── types/                  # Shared TypeScript types
│   └── utils/                  # Shared utilities
└── docs/                       # Documentation
```

## 🚀 Quick Start

### Prerequisites
- Node.js >= 18.0.0
- Python 3.10+
- Pinecone API key

### Installation & Setup

1. **Clone and install dependencies:**
```bash
git clone <repository-url>
cd buildcraft
npm install
```

2. **Set up the search service:**
```bash
cd api/python-search
pip install -r requirements.txt
export PINECONE_API_KEY="your-pinecone-api-key"
python3 main.py
```

3. **Start the frontend:**
```bash
cd web
npm run dev
```

4. **Access the application:**
- Frontend: http://localhost:3000
- Search API: http://localhost:8001

## 🎯 Features

### **Search Functionality**
- Semantic search across game items, skills, and equipment
- Category-based filtering (skills, weapons, armor, spells, items)
- Intelligent reasoning and suggestions
- Real-time results with relevance scoring

### **Build Generation**
- AI-powered character build creation
- Skill recommendations with synergies
- Equipment suggestions and progression paths
- Playstyle-specific recommendations

### **Smart Interface**
- Natural language processing for request detection
- Automatic routing between search and build requests
- Beautiful, responsive UI components
- Real-time chat interface

## Workspaces

- **`web`**: Next.js frontend with TypeScript, Tailwind CSS, and chat interface
- **`api/python-search`**: Python FastAPI service with HuggingFace embeddings and Pinecone
- **`data`**: Game data processing and storage
- **`packages/types`**: Shared TypeScript type definitions
- **`packages/utils`**: Shared utility functions

## 🛠️ Development

### Workspace-specific Commands

#### Frontend (web)
```bash
cd web
npm run dev          # Start development server
npm run build        # Build for production
npm run lint         # Run ESLint
```

#### Search Service (api/python-search)
```bash
cd api/python-search
python3 main.py      # Start FastAPI server
pip install -r requirements.txt  # Install dependencies
```

#### Data Processing (data)
```bash
cd data
python3 -m pip install -r requirements.txt
python3 oblivion/scraper.py      # Scrape Oblivion data
python3 oblivion/processor.py    # Process scraped data
```

## 🔧 API Endpoints

### Search Service (Port 8001)

- `GET /health` - Service health check
- `POST /search` - Semantic search with reasoning
- `POST /build` - AI-powered build generation

### Example Usage

```bash
# Search for items
curl -X POST http://localhost:8001/search \
  -H "Content-Type: application/json" \
  -d '{"query": "stealth archer", "category": "skills", "limit": 5}'

# Generate a build
curl -X POST http://localhost:8001/build \
  -H "Content-Type: application/json" \
  -d '{"prompt": "stealth archer build", "playstyle": "ranged", "difficulty": "normal"}'
```

## 🎮 Usage Examples

### Frontend Interface
1. **Search Requests**: "Search for stealth skills", "Find weapons for archer"
2. **Build Requests**: "Create a stealth archer build", "Make a battle mage"

### Smart Features
- Automatic request detection (search vs build)
- Category extraction from natural language
- Real-time results with beautiful UI cards
- Responsive design for all devices

## Adding New Games

To add support for a new game:
1. Create a new directory in `data/[game-name]/`
2. Add game-specific scraping scripts
3. Update shared types in `packages/types/`
4. Add game-specific UI components in `web/`

## Contributing

Follow the project's version control and branching strategy outlined in CONTRIBUTING.md.

## Version Control & Branching Strategy

- All work is done on feature branches (e.g., `feat/feature-name`, `fix/bug-description`).
- All changes to `main` must go through a pull request (PR) and require at least one review.
- Use Conventional Commits for commit messages.
- Tag releases on `main` as `v1.0.0`, `v1.1.0`, etc.
- See [CONTRIBUTING.md](CONTRIBUTING.md) for full details. 