export default function LoadingIndicator() {
  return (
    <div className="flex justify-start mb-6">
      <div className="flex items-start space-x-3">
        {/* AI Avatar */}
        <div className="flex-shrink-0 w-8 h-8 bg-gradient-to-br from-purple-500 to-indigo-600 rounded-full flex items-center justify-center">
          <span className="text-sm font-bold text-white">AI</span>
        </div>
        
        <div className="bg-slate-800/60 backdrop-blur-sm border border-purple-500/20 px-6 py-4 rounded-2xl shadow-lg">
          <div className="flex items-center space-x-3">
            <div className="flex space-x-1">
              <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce"></div>
              <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
              <div className="w-2 h-2 bg-purple-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
            </div>
            <span className="text-sm text-purple-200">AI is crafting your perfect build...</span>
          </div>
        </div>
      </div>
    </div>
  );
} 