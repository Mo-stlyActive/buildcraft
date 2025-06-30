import { Message } from '@/types/chat';
import BuildSuggestionCard from './BuildSuggestionCard';
import SearchResultsCard from './SearchResultsCard';

interface MessageBubbleProps {
  message: Message;
}

export default function MessageBubble({ message }: MessageBubbleProps) {
  const isUser = message.type === 'user';
  
  return (
    <div className={`flex ${isUser ? 'justify-end' : 'justify-start'}`}>
      <div className="max-w-xs lg:max-w-md">
        <div
          className={`px-4 py-2 rounded-lg ${
            isUser
              ? 'bg-blue-500 text-white'
              : 'bg-white text-gray-900 border border-gray-200'
          }`}
        >
          <p className="text-sm">{message.content}</p>
          <p className={`text-xs mt-1 ${isUser ? 'text-blue-100' : 'text-gray-500'}`}>
            {message.timestamp.toLocaleTimeString()}
          </p>
        </div>
        
        {/* Display build suggestion if available */}
        {!isUser && message.buildSuggestion && (
          <div className="mt-3">
            <BuildSuggestionCard build={message.buildSuggestion} />
          </div>
        )}
        
        {/* Display search results if available */}
        {!isUser && message.searchResults && (
          <div className="mt-3">
            <SearchResultsCard searchResults={message.searchResults} />
          </div>
        )}
      </div>
    </div>
  );
} 