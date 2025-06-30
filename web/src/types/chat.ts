export interface Message {
  id: string;
  content: string;
  type: 'user' | 'ai';
  timestamp: Date;
  buildSuggestion?: BuildResponse;
  searchResults?: SearchResponse;
}

export interface SearchResult {
  name: string;
  category: string;
  type: string;
  properties: Record<string, any>;
  score: number;
}

export interface SearchResponse {
  results: SearchResult[];
  reasoning: string;
  suggestions: string[];
}

export interface BuildResponse {
  build_name: string;
  skills: string[];
  key_items: string[];
  playstyle: string;
  reasoning: string;
  synergies: string[];
  progression: string[];
} 