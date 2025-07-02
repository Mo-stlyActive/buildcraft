'use client';

import { useState } from 'react';
import ChatMessages from './ChatMessages';
import ChatInput from './ChatInput';
import { Message } from '@/types/chat';
import { sendChatMessage, searchItems } from '@/lib/api';

export default function ChatContainer() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);

  const handleSendMessage = async (content: string) => {
    if (!content.trim()) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      content,
      type: 'user',
      timestamp: new Date(),
    };

    setMessages(prev => [...prev, userMessage]);
    setIsLoading(true);

    try {
      // Determine if this is a search request or build request
      const isSearchRequest = content.toLowerCase().includes('search') || 
                             content.toLowerCase().includes('find') ||
                             content.toLowerCase().includes('what') ||
                             content.toLowerCase().includes('show me');
      
      let response;
      if (isSearchRequest) {
        // Extract search query and category
        const searchQuery = content.replace(/search|find|what|show me/gi, '').trim();
        const categoryMatch = content.match(/(skills?|weapons?|armor|spells?|items?)/i);
        const category = categoryMatch ? categoryMatch[1] : undefined;
        
        const searchResponse = await searchItems(searchQuery, category, 5);
        response = {
          success: true,
          search: searchResponse,
          message: searchResponse.reasoning || `Found ${searchResponse.results.length} items for "${searchQuery}"`,
        };
      } else {
        // Treat as build request
        response = await sendChatMessage(content);
      }
      
      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: response.message,
        type: 'ai',
        timestamp: new Date(),
        buildSuggestion: response.build,
        searchResults: response.search,
      };

      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
      console.error('Chat error:', error);
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: 'Sorry, I encountered an error processing your request. Please try again.',
        type: 'ai',
        timestamp: new Date(),
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleClearChat = () => {
    setMessages([]);
  };

  return (
    <div className="flex flex-col h-[80vh] max-w-5xl mx-auto bg-slate-900/50 backdrop-blur-sm border border-purple-500/20 rounded-2xl overflow-hidden shadow-2xl">
      {/* Header */}
      <div className="bg-gradient-to-r from-purple-900/80 to-slate-900/80 backdrop-blur-sm border-b border-purple-500/30 px-6 py-4">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold text-white">⚔️ Build Generator</h1>
            <p className="text-purple-200">AI-powered character optimization</p>
          </div>
          <div className="flex items-center space-x-2">
            <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse"></div>
            <span className="text-sm text-green-300 font-medium">Connected</span>
          </div>
        </div>
      </div>

      {/* Chat Messages */}
      <div className="flex-1 overflow-y-auto p-6 bg-gradient-to-b from-slate-900/30 to-slate-900/60">
        <ChatMessages messages={messages} isLoading={isLoading} />
      </div>

      {/* Chat Input */}
      <div className="bg-slate-900/80 backdrop-blur-sm border-t border-purple-500/30 p-6">
        <ChatInput 
          onSendMessage={handleSendMessage}
          onClearChat={handleClearChat}
          isLoading={isLoading}
        />
      </div>
    </div>
  );
} 