'use client';

import { useState } from 'react';
import ChatMessages from './ChatMessages';
import ChatInput from './ChatInput';
import { Message } from '@/types/chat';
import { sendChatMessage } from '@/lib/api';

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
      const response = await sendChatMessage(content);
      
      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: response.message,
        type: 'ai',
        timestamp: new Date(),
        buildSuggestion: response.build,
      };

      setMessages(prev => [...prev, aiMessage]);
    } catch (error) {
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
    <div className="flex flex-col h-screen max-w-4xl mx-auto bg-gray-50">
      {/* Header */}
      <div className="bg-white border-b border-gray-200 px-6 py-4">
        <h1 className="text-2xl font-bold text-gray-900">BuildCraft AI</h1>
        <p className="text-gray-600">AI-powered game build advisor</p>
      </div>

      {/* Chat Messages */}
      <div className="flex-1 overflow-y-auto p-6">
        <ChatMessages messages={messages} isLoading={isLoading} />
      </div>

      {/* Chat Input */}
      <div className="bg-white border-t border-gray-200 p-6">
        <ChatInput 
          onSendMessage={handleSendMessage}
          onClearChat={handleClearChat}
          isLoading={isLoading}
        />
      </div>
    </div>
  );
} 