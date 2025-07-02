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
    <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
      <div className="text-center mb-12">
        <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">
          Choose Your Adventure
        </h2>
        <p className="text-xl text-gray-300 max-w-2xl mx-auto">
          Select a game to start generating unique, creative character builds that break the meta
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {AVAILABLE_GAMES.map((game) => (
          <div
            key={game.id}
            className={`group relative bg-slate-800/50 backdrop-blur-sm border rounded-2xl p-8 cursor-pointer transition-all duration-300 ${
              selectedGame === game.id
                ? 'border-purple-500 bg-purple-500/20 shadow-2xl shadow-purple-500/20 scale-105'
                : hoveredGame === game.id
                ? 'border-purple-500/50 shadow-xl scale-102'
                : 'border-slate-700/50 hover:border-purple-500/30'
            } ${
              game.status === 'coming_soon' 
                ? 'opacity-60 cursor-not-allowed' 
                : 'hover:shadow-xl'
            }`}
            onClick={() => game.status === 'active' && onGameSelect(game.id)}
            onMouseEnter={() => setHoveredGame(game.id)}
            onMouseLeave={() => setHoveredGame(null)}
          >
            {/* Status Badge */}
            {game.status === 'coming_soon' && (
              <div className="absolute top-4 right-4 bg-amber-500/20 border border-amber-500/30 text-amber-300 text-xs font-medium px-3 py-1 rounded-full">
                Coming Soon
              </div>
            )}

            {game.status === 'active' && (
              <div className="absolute top-4 right-4 bg-green-500/20 border border-green-500/30 text-green-300 text-xs font-medium px-3 py-1 rounded-full">
                • Available Now
              </div>
            )}

            {/* Game Icon */}
            <div className="text-7xl mb-6 text-center group-hover:scale-110 transition-transform duration-300">
              {game.image}
            </div>

            {/* Game Info */}
            <div className="text-center">
              <h3 className="text-xl font-bold text-white mb-3 group-hover:text-purple-300 transition-colors">
                {game.name}
              </h3>
              <p className="text-gray-300 mb-6 leading-relaxed">
                {game.description}
              </p>

              {/* Action Button */}
              {game.status === 'active' ? (
                <button className="w-full bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 text-white font-semibold py-3 px-6 rounded-xl transition-all duration-200 shadow-lg hover:shadow-purple-500/25 group-hover:scale-105">
                  ⚔️ Start Building
                </button>
              ) : (
                <button 
                  disabled 
                  className="w-full bg-slate-700/50 text-gray-400 font-semibold py-3 px-6 rounded-xl cursor-not-allowed border border-slate-600/50"
                >
                  🕒 Coming Soon
                </button>
              )}
            </div>

            {/* Hover Effect */}
            <div className="absolute inset-0 bg-gradient-to-r from-purple-500/5 to-indigo-500/5 rounded-2xl opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none"></div>
          </div>
        ))}
      </div>
    </div>
  );
}