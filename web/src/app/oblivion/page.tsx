'use client';

import { useState } from 'react';
import ChatContainer from '@/components/chat/ChatContainer';

export default function OblivionPage() {
  const [showChat, setShowChat] = useState(false);

  if (showChat) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900/50 to-slate-900">
        <div className="relative z-10">
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div className="mb-6 flex items-center justify-between">
              <div>
                <h1 className="text-3xl font-bold text-white mb-2">
                  🏰 Build Generator Active
                </h1>
                <p className="text-purple-200">
                  Creating your perfect Oblivion character build
                </p>
              </div>
              <button
                onClick={() => setShowChat(false)}
                className="bg-purple-600/20 hover:bg-purple-600/30 text-purple-200 hover:text-white px-4 py-2 rounded-lg transition-all duration-200 border border-purple-500/30"
              >
                ← Back to Landing
              </button>
            </div>
            <ChatContainer />
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900/50 to-slate-900 relative overflow-hidden">
      {/* Background Effects */}
      <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] from-purple-900/20 via-slate-900 to-slate-900"></div>
      <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-3xl animate-pulse"></div>
      <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-amber-500/10 rounded-full blur-3xl animate-pulse delay-1000"></div>
      
      <div className="relative z-10">
        {/* Hero Section */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 pb-16">
          <div className="text-center">
            {/* Main Hero Content */}
            <div className="mb-8">
              <div className="inline-flex items-center px-4 py-2 bg-purple-500/20 border border-purple-500/30 rounded-full text-purple-200 text-sm font-medium mb-8">
                <span className="w-2 h-2 bg-green-400 rounded-full mr-2 animate-pulse"></span>
                AI-Powered Build Generation
              </div>
              
              <h1 className="text-5xl md:text-7xl font-bold text-white mb-6 leading-tight">
                <span className="bg-gradient-to-r from-purple-400 via-amber-300 to-purple-400 bg-clip-text text-transparent">
                  The Elder Scrolls IV
                </span>
                <br />
                <span className="text-4xl md:text-6xl">Oblivion</span>
              </h1>
              
              <p className="text-xl md:text-2xl text-gray-300 mb-8 max-w-3xl mx-auto leading-relaxed">
                Create the <span className="text-amber-300 font-semibold">perfect character build</span> with 
                AI-powered recommendations, optimized skill progression, and immersive roleplay guidance.
              </p>
            </div>

            {/* CTA Button */}
            <div className="mb-16">
              <button
                onClick={() => setShowChat(true)}
                className="group relative bg-gradient-to-r from-purple-600 to-amber-600 hover:from-purple-700 hover:to-amber-700 text-white px-8 py-4 rounded-xl text-lg font-semibold transition-all duration-300 shadow-2xl hover:shadow-purple-500/25 transform hover:scale-105"
              >
                <span className="relative z-10 flex items-center">
                  ⚔️ Start Building Your Character
                  <svg className="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                  </svg>
                </span>
                <div className="absolute inset-0 bg-gradient-to-r from-purple-400 to-amber-400 rounded-xl blur-xl opacity-30 group-hover:opacity-50 transition-opacity"></div>
              </button>
            </div>
          </div>
        </section>

        {/* Features Section */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <div className="text-center mb-16">
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">
              Why Choose Our Build Generator?
            </h2>
            <p className="text-xl text-gray-300 max-w-2xl mx-auto">
              Experience Oblivion like never before with intelligent character optimization
            </p>
          </div>

          <div className="grid md:grid-cols-3 gap-8">
            {/* Feature 1 */}
            <div className="bg-slate-800/50 backdrop-blur-sm border border-purple-500/20 rounded-2xl p-8 hover:border-purple-500/40 transition-all duration-300 group">
              <div className="w-16 h-16 bg-gradient-to-br from-purple-500 to-indigo-600 rounded-xl flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition-transform">
                🧠
              </div>
              <h3 className="text-xl font-bold text-white mb-4">AI-Powered Optimization</h3>
              <p className="text-gray-300 leading-relaxed">
                Our advanced AI analyzes thousands of build combinations to recommend the perfect race, skills, and progression path for your playstyle.
              </p>
            </div>

            {/* Feature 2 */}
            <div className="bg-slate-800/50 backdrop-blur-sm border border-purple-500/20 rounded-2xl p-8 hover:border-purple-500/40 transition-all duration-300 group">
              <div className="w-16 h-16 bg-gradient-to-br from-amber-500 to-orange-600 rounded-xl flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition-transform">
                📜
              </div>
              <h3 className="text-xl font-bold text-white mb-4">Immersive Roleplay</h3>
              <p className="text-gray-300 leading-relaxed">
                Get detailed backstories, personality traits, and roleplay suggestions that bring your character to life in the world of Cyrodiil.
              </p>
            </div>

            {/* Feature 3 */}
            <div className="bg-slate-800/50 backdrop-blur-sm border border-purple-500/20 rounded-2xl p-8 hover:border-purple-500/40 transition-all duration-300 group">
              <div className="w-16 h-16 bg-gradient-to-br from-green-500 to-emerald-600 rounded-xl flex items-center justify-center text-2xl mb-6 group-hover:scale-110 transition-transform">
                ⚡
              </div>
              <h3 className="text-xl font-bold text-white mb-4">Optimized Progression</h3>
              <p className="text-gray-300 leading-relaxed">
                Receive step-by-step skill progression guides, equipment recommendations, and strategic tips to maximize your character&apos;s effectiveness.
              </p>
            </div>
          </div>
        </section>

        {/* Example Builds Section */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
          <div className="text-center mb-12">
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-4">
              Popular Build Archetypes
            </h2>
            <p className="text-xl text-gray-300">
              Get inspired by these powerful character concepts
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[
              { name: "Stealth Archer Ninja", icon: "🏹", color: "from-green-500 to-emerald-600" },
              { name: "Fire Mage Destroyer", icon: "🔥", color: "from-red-500 to-orange-600" },
              { name: "Holy Paladin Tank", icon: "⛪", color: "from-yellow-500 to-amber-600" },
              { name: "Poison Assassin", icon: "☠️", color: "from-purple-500 to-indigo-600" },
              { name: "Necromancer Scholar", icon: "💀", color: "from-gray-500 to-slate-600" },
              { name: "Acrobatic Monk", icon: "🥋", color: "from-blue-500 to-cyan-600" }
            ].map((build) => (
              <div 
                key={build.name}
                className="group bg-slate-800/30 backdrop-blur-sm border border-slate-700/50 rounded-xl p-6 hover:border-purple-500/50 transition-all duration-300 cursor-pointer hover:transform hover:scale-105"
                onClick={() => setShowChat(true)}
              >
                <div className={`w-12 h-12 bg-gradient-to-br ${build.color} rounded-lg flex items-center justify-center text-xl mb-4 group-hover:scale-110 transition-transform`}>
                  {build.icon}
                </div>
                <h3 className="text-lg font-semibold text-white group-hover:text-purple-300 transition-colors">
                  {build.name}
                </h3>
                <p className="text-gray-400 text-sm mt-2 group-hover:text-gray-300 transition-colors">
                  Click to generate this build →
                </p>
              </div>
            ))}
          </div>
        </section>

        {/* Footer CTA */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
          <div className="text-center bg-gradient-to-r from-purple-900/50 to-slate-900/50 backdrop-blur-sm border border-purple-500/20 rounded-3xl p-12">
            <h2 className="text-3xl md:text-4xl font-bold text-white mb-6">
              Ready to Begin Your Adventure?
            </h2>
            <p className="text-xl text-gray-300 mb-8 max-w-2xl mx-auto">
              Join thousands of players who have discovered their perfect Oblivion character builds
            </p>
            <button
              onClick={() => setShowChat(true)}
              className="bg-gradient-to-r from-amber-500 to-orange-600 hover:from-amber-600 hover:to-orange-700 text-white px-10 py-4 rounded-xl text-xl font-bold transition-all duration-300 shadow-2xl hover:shadow-amber-500/25 transform hover:scale-105"
            >
              🚀 Create Your Build Now
            </button>
          </div>
        </section>
      </div>
    </div>
  );
}