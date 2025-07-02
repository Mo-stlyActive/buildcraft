import { Message } from '@/types/chat';
import BuildSuggestionCard from './BuildSuggestionCard';
import SearchResultsCard from './SearchResultsCard';

interface MessageBubbleProps {
  message: Message;
}

export default function MessageBubble({ message }: MessageBubbleProps) {
  const isUser = message.type === 'user';
  
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'} mb-6`}>
      <div className="max-w-sm lg:max-w-2xl">
        <div className="flex items-start space-x-3">
          {/* Avatar */}
          {!isUser && (
            <div className="flex-shrink-0 w-8 h-8 bg-gradient-to-br from-purple-500 to-indigo-600 rounded-full flex items-center justify-center">
              <span className="text-sm font-bold text-white">AI</span>
            </div>
          )}
          
          <div className="flex-1">
            <div
              className={`px-4 py-3 rounded-2xl ${
                isUser
                  ? 'bg-gradient-to-r from-purple-600 to-indigo-600 text-white ml-auto max-w-md shadow-lg'
                  : 'bg-slate-800/60 backdrop-blur-sm text-gray-100 border border-purple-500/20 shadow-lg'
              }`}
            >
              <p className="text-sm leading-relaxed whitespace-pre-wrap">{message.content}</p>
              <p className={`text-xs mt-2 opacity-70 ${
                isUser ? 'text-purple-100' : 'text-gray-400'
              }`}>
                {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
              </p>
            </div>
            
            {/* Display build suggestion if available */}
            {!isUser && message.buildSuggestion && (
              <div className="mt-4">
                <BuildSuggestionCard build={message.buildSuggestion} />
              </div>
            )}
            
            {/* Display search results if available */}
            {!isUser && message.searchResults && (
              <div className="mt-4">
                <SearchResultsCard searchResults={message.searchResults} />
              </div>
            )}
          </div>
          
          {/* User Avatar */}
          {isUser && (
            <div className="flex-shrink-0 w-8 h-8 bg-gradient-to-br from-amber-500 to-orange-600 rounded-full flex items-center justify-center">
              <span className="text-sm font-bold text-white">U</span>
            </div>
          )}
        </div>
      </div>
    </div>
  );
} 