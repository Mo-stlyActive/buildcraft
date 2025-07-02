'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import GameSelector from '@/components/GameSelector';

export default function Home() {
  const router = useRouter();
  const [selectedGame, setSelectedGame] = useState<string>();

  const handleGameSelect = (gameId: string) => {
    setSelectedGame(gameId);
    router.push(`/${gameId}`);
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900/50 to-slate-900 relative overflow-hidden">
      {/* Background Effects */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-purple-900/20 via-slate-900 to-slate-900"></div>
      <div className="absolute top-1/3 left-1/6 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl animate-pulse"></div>
      <div className="absolute bottom-1/3 right-1/6 w-96 h-96 bg-amber-500/10 rounded-full blur-3xl animate-pulse delay-1000"></div>
      
      <div className="relative z-10">
        {/* Hero Section */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 pb-12">
          <div className="text-center mb-16">
            <div className="inline-flex items-center px-4 py-2 bg-purple-500/20 border border-purple-500/30 rounded-full text-purple-200 text-sm font-medium mb-8">
              <span className="w-2 h-2 bg-green-400 rounded-full mr-2 animate-pulse"></span>
              Anti-Meta AI Build Generation
            </div>
            
            <h1 className="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight">
              <span className="bg-gradient-to-r from-purple-400 via-amber-300 to-purple-400 bg-clip-text text-transparent">
                BuildCraft
              </span>
              <br />
              <span className="text-4xl md:text-5xl text-gray-200">Remastered</span>
            </h1>
            
            <p className="text-xl md:text-2xl text-gray-300 mb-12 max-w-4xl mx-auto leading-relaxed">
              Break free from <span className="line-through text-gray-500">meta builds</span> and discover 
              <span className="text-amber-300 font-semibold"> truly creative character concepts</span> powered by advanced AI
            </p>
          </div>
        </section>

        {/* Game Selection */}
        <section className="py-12">
          <GameSelector 
            onGameSelect={handleGameSelect}
            selectedGame={selectedGame}
          />
        </section>

        {/* Features Section */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">
              Why BuildCraft Remastered?
            </h2>
            <p className="text-xl text-gray-300 max-w-3xl mx-auto">
              Experience RPGs the way they were meant to be played - with creativity, immersion, and unlimited possibilities
            </p>
          </div>

          <div className="grid md:grid-cols-4 gap-8">
            <div className="text-center group">
              <div className="w-16 h-16 bg-gradient-to-br from-purple-500 to-indigo-600 rounded-xl flex items-center justify-center text-2xl mb-4 mx-auto group-hover:scale-110 transition-transform">
                🤖
              </div>
              <h3 className="text-lg font-bold text-white mb-2">AI-Powered</h3>
              <p className="text-gray-400 text-sm">
                Advanced AI analyzes game mechanics to create perfectly balanced, unique builds
              </p>
            </div>

            <div className="text-center group">
              <div className="w-16 h-16 bg-gradient-to-br from-amber-500 to-orange-600 rounded-xl flex items-center justify-center text-2xl mb-4 mx-auto group-hover:scale-110 transition-transform">
                🎯
              </div>
              <h3 className="text-lg font-bold text-white mb-2">Anti-Meta</h3>
              <p className="text-gray-400 text-sm">
                Focus on fun and creativity over min-maxing and cookie-cutter optimization
              </p>
            </div>

            <div className="text-center group">
              <div className="w-16 h-16 bg-gradient-to-br from-green-500 to-emerald-600 rounded-xl flex items-center justify-center text-2xl mb-4 mx-auto group-hover:scale-110 transition-transform">
                🎭
              </div>
              <h3 className="text-lg font-bold text-white mb-2">Roleplay Rich</h3>
              <p className="text-gray-400 text-sm">
                Get immersive backstories, motivations, and character depth for true roleplay
              </p>
            </div>

            <div className="text-center group">
              <div className="w-16 h-16 bg-gradient-to-br from-blue-500 to-cyan-600 rounded-xl flex items-center justify-center text-2xl mb-4 mx-auto group-hover:scale-110 transition-transform">
                ⚡
              </div>
              <h3 className="text-lg font-bold text-white mb-2">Instant Results</h3>
              <p className="text-gray-400 text-sm">
                Generate complete builds in seconds with detailed progression guides
              </p>
            </div>
          </div>
        </section>

        {/* Footer */}
        <footer className="text-center py-12 border-t border-purple-500/20">
          <div className="max-w-4xl mx-auto px-4">
            <p className="text-gray-400 mb-4">
              Made with ❤️ for creative RPG players who dare to be different
            </p>
            <div className="flex justify-center space-x-6 text-sm text-gray-500">
              <span>❓ Help</span>
              <span>⭐ GitHub</span>
              <span>📧 Contact</span>
              <span>🔒 Privacy</span>
            </div>
          </div>
        </footer>
      </div>
    </div>
  );
}
