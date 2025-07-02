'use client';

import { useState } from 'react';

interface ChatInputProps {
  onSendMessage: (content: string) => void;
  onClearChat: () => void;
  isLoading: boolean;
}

export default function ChatInput({ onSendMessage, onClearChat, isLoading }: ChatInputProps) {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (inputValue.trim() && !isLoading) {
      onSendMessage(inputValue);
      setInputValue('');
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex items-end space-x-4">
      <div className="flex-1 relative">
        <textarea
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Describe your ideal character build... (e.g., 'stealthy fire mage', 'holy warrior tank')"
          className="w-full px-4 py-3 bg-slate-800/50 border border-purple-500/30 rounded-xl text-white placeholder-gray-400 resize-none focus:outline-none focus:ring-2 focus:ring-purple-500 focus:border-purple-500 transition-all duration-200 backdrop-blur-sm"
          rows={2}
          disabled={isLoading}
        />
        {/* Character count or status indicator */}
        <div className="absolute bottom-2 right-2 text-xs text-gray-400">
          {inputValue.length > 0 && `${inputValue.length} characters`}
        </div>
      </div>
      <div className="flex space-x-2">
        <button
          type="submit"
          disabled={!inputValue.trim() || isLoading}
          className="group relative px-6 py-3 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-700 hover:to-indigo-700 disabled:from-slate-600 disabled:to-slate-700 text-white rounded-xl font-medium transition-all duration-200 shadow-lg hover:shadow-purple-500/25 disabled:cursor-not-allowed disabled:shadow-none"
        >
          <span className="relative z-10 flex items-center">
            {isLoading ? (
              <>
                <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                Creating...
              </>
            ) : (
              <>
                ⚡ Generate
                <svg className="ml-1 w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 7l5 5m0 0l-5 5m5-5H6" />
                </svg>
              </>
            )}
          </span>
        </button>
        <button
          type="button"
          onClick={onClearChat}
          className="px-4 py-3 bg-slate-700/50 hover:bg-slate-600/50 text-gray-300 hover:text-white rounded-xl transition-all duration-200 border border-slate-600/50 hover:border-slate-500/50"
          title="Clear chat history"
        >
          🗑️
        </button>
      </div>
    </form>
  );
} 