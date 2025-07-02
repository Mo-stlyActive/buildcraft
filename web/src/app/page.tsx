'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import GameSelector from '@/components/GameSelector';

export default function Home() {
  const router = useRouter();
  const [selectedGame, setSelectedGame] = useState<string>();

  const handleGameSelect = (gameId: string) => {
    setSelectedGame(gameId);
    // Navigate to game-specific page
    router.push(`/${gameId}`);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Header */}
      <div className="bg-white shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center">
              <h1 className="text-2xl font-bold text-gray-900">
                BuildCraft AI
              </h1>
              <span className="ml-3 px-2 py-1 text-xs font-medium bg-purple-100 text-purple-800 rounded-full">
                Anti-Meta Build Advisor
              </span>
            </div>
            <div className="flex items-center space-x-4">
              <button className="text-gray-500 hover:text-gray-700">
                ❓ Help
              </button>
              <button className="text-gray-500 hover:text-gray-700">
                ⭐ GitHub
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="py-12">
        <GameSelector 
          onGameSelect={handleGameSelect}
          selectedGame={selectedGame}
        />
      </div>

      {/* Footer */}
      <div className="text-center py-8 text-gray-500 text-sm">
        <p>Made with ❤️ for creative RPG players who want to break free from meta builds</p>
      </div>
    </div>
  );
}
