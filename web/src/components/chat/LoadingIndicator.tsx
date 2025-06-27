export default function LoadingIndicator() {
  return (
    <div className="flex justify-start">
      <div className="bg-white text-gray-900 border border-gray-200 px-4 py-2 rounded-lg">
        <div className="flex items-center space-x-2">
          <div className="flex space-x-1">
            <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
            <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
            <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
          </div>
          <span className="text-sm text-gray-500">AI is thinking...</span>
        </div>
      </div>
    </div>
  );
} 