import ChatContainer from '@/components/chat/ChatContainer';

export default function OblivionPage() {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <div className="bg-white border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            <div className="flex items-center">
              <h1 className="text-xl font-bold text-gray-900">
                🏰 The Elder Scrolls IV: Oblivion
              </h1>
              <span className="ml-3 px-2 py-1 text-xs font-medium bg-green-100 text-green-800 rounded-full">
                Build Generator
              </span>
            </div>
            <div className="flex items-center space-x-4">
              <button className="text-gray-500 hover:text-gray-700">
                📚 Guide
              </button>
              <button className="text-gray-500 hover:text-gray-700">
                🔙 Change Game
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-6">
          <h2 className="text-2xl font-bold text-gray-900 mb-2">
            Create Your Perfect Character Build
          </h2>
          <p className="text-gray-600">
            Tell me what kind of character you want to play, and I&apos;ll create a unique build with race recommendations, 
            skill priorities, equipment suggestions, and roleplay flavor.
          </p>
        </div>

        {/* Examples */}
        <div className="mb-8 p-4 bg-blue-50 border border-blue-200 rounded-lg">
          <h3 className="font-semibold text-blue-900 mb-2">Try these examples:</h3>
          <div className="flex flex-wrap gap-2">
            {[
              "stealth archer ninja",
              "fire mage destroyer", 
              "holy paladin tank",
              "poison assassin",
              "necromancer scholar",
              "acrobatic monk"
            ].map((example) => (
              <span 
                key={example}
                className="px-3 py-1 bg-blue-100 text-blue-800 text-sm rounded-full cursor-pointer hover:bg-blue-200 transition-colors"
              >
                &quot;{example}&quot;
              </span>
            ))}
          </div>
        </div>

        <ChatContainer />
      </div>
    </div>
  );
}