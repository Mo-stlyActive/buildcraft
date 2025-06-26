# BuildCraft AI - Monorepo

AI-powered game build advisor for multiple RPGs, built with a scalable monorepo architecture.

## Project Structure

```
buildcraft/
├── web/                    # Next.js frontend application
├── api/                    # Backend API services
├── data/                   # Game data scraping and processing
│   ├── oblivion/          # Oblivion-specific data
│   └── shared/            # Shared data structures
├── packages/              # Shared packages/libraries
│   ├── types/            # Shared TypeScript types
│   └── utils/            # Shared utilities
└── docs/                  # Documentation
```

## Workspaces

- **`web`**: Next.js frontend with TypeScript and Tailwind CSS
- **`api`**: Express.js backend API services
- **`data`**: Python/TypeScript scripts for game data scraping
- **`packages/types`**: Shared TypeScript type definitions
- **`packages/utils`**: Shared utility functions

## Getting Started

### Prerequisites
- Node.js >= 18.0.0
- npm >= 8.0.0

### Installation
```bash
# Install all workspace dependencies
npm install

# Start development server (frontend)
npm run dev

# Build all workspaces
npm run build

# Run tests across all workspaces
npm run test
```

### Workspace-specific Commands

#### Frontend (web)
```bash
npm run dev --workspace=web
npm run build --workspace=web
```

#### API (api)
```bash
npm run dev --workspace=api
npm run build --workspace=api
```

#### Data Processing (data)
```bash
npm run scrape:oblivion --workspace=data
npm run process:oblivion --workspace=data
```

## Development Workflow

1. **Frontend Development**: Work in the `web/` directory
2. **Backend Development**: Work in the `api/` directory  
3. **Data Processing**: Work in the `data/` directory
4. **Shared Code**: Use `packages/types` and `packages/utils` for common functionality

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