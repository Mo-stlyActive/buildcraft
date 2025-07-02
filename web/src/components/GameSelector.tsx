'use client';

import { useState } from 'react';

interface Game {
  id: string;
  name: string;
  description: string;
  status: 'active' | 'coming_soon';
  image: string;
}

const AVAILABLE_GAMES: Game[] = [
  {
    id: 'oblivion',
    name: 'The Elder Scrolls IV: Oblivion',
    description: 'Classic fantasy RPG with deep character customization',
    status: 'active',
    image: '🏰'
  },
  {
    id: 'ashes_of_creation',
    name: 'Ashes of Creation',
    description: 'Upcoming MMORPG with dynamic world systems',
    status: 'coming_soon',
    image: '⚔️'
  },
  {
    id: 'skyrim',
    name: 'The Elder Scrolls V: Skyrim',
    description: 'Nordic adventure with shouts and dragons',
    status: 'coming_soon',
    image: '🐉'
  }
];

interface GameSelectorProps {
  onGameSelect: (gameId: string) => void;
  selectedGame?: string;
}

export default function GameSelector({ onGameSelect, selectedGame }: GameSelectorProps) {
  const [hoveredGame, setHoveredGame] = useState<string | null>(null);

  return (
    <div className="max-w-4xl mx-auto p-6">
      <div className="text-center mb-8">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          Choose Your Adventure
        </h1>
        <p className="text-lg text-gray-600">
          Select a game to start generating unique, creative character builds
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {AVAILABLE_GAMES.map((game) => (
          <div
            key={game.id}
            className={`relative bg-white border-2 rounded-xl p-6 cursor-pointer transition-all duration-200 ${
              selectedGame === game.id
                ? 'border-blue-500 bg-blue-50 shadow-lg scale-105'
                : hoveredGame === game.id
                ? 'border-gray-400 shadow-md scale-102'
                : 'border-gray-200 hover:border-gray-300'
            } ${
              game.status === 'coming_soon' 
                ? 'opacity-60 cursor-not-allowed' 
                : ''
            }`}
            onClick={() => game.status === 'active' && onGameSelect(game.id)}
            onMouseEnter={() => setHoveredGame(game.id)}
            onMouseLeave={() => setHoveredGame(null)}
          >
            {/* Status Badge */}
            {game.status === 'coming_soon' && (
              <div className="absolute top-3 right-3 bg-yellow-100 text-yellow-800 text-xs font-medium px-2 py-1 rounded-full">
                Coming Soon
              </div>
            )}

            {/* Game Icon */}
            <div className="text-6xl mb-4 text-center">
              {game.image}
            </div>

            {/* Game Info */}
            <div className="text-center">
              <h3 className="text-xl font-bold text-gray-900 mb-2">
                {game.name}
              </h3>
              <p className="text-sm text-gray-600 mb-4">
                {game.description}
              </p>

              {/* Action Button */}
              {game.status === 'active' ? (
                <button className="w-full bg-blue-500 text-white font-medium py-2 px-4 rounded-lg hover:bg-blue-600 transition-colors">
                  Start Building
                </button>
              ) : (
                <button 
                  disabled 
                  className="w-full bg-gray-300 text-gray-500 font-medium py-2 px-4 rounded-lg cursor-not-allowed"
                >
                  Coming Soon
                </button>
              )}
            </div>
          </div>
        ))}
      </div>

      {/* Feature Preview */}
      <div className="mt-12 text-center">
        <h2 className="text-2xl font-bold text-gray-900 mb-4">
          What Makes BuildCraft Special?
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-center">
          <div className="p-4">
            <div className="text-3xl mb-2">🤖</div>
            <h3 className="font-semibold text-gray-900 mb-2">AI-Powered</h3>
            <p className="text-sm text-gray-600">
              Advanced AI analyzes your preferences to create unique builds
            </p>
          </div>
          <div className="p-4">
            <div className="text-3xl mb-2">🎯</div>
            <h3 className="font-semibold text-gray-900 mb-2">Anti-Meta</h3>
            <p className="text-sm text-gray-600">
              Focus on creativity and fun over optimization and min-maxing
            </p>
          </div>
          <div className="p-4">
            <div className="text-3xl mb-2">🎭</div>
            <h3 className="font-semibold text-gray-900 mb-2">Roleplay Rich</h3>
            <p className="text-sm text-gray-600">
              Get immersive backstories and character motivations
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}