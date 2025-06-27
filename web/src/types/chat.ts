export interface Message {
  id: string;
  content: string;
  type: 'user' | 'ai';
  timestamp: Date;
  buildSuggestion?: BuildSuggestion;
}

export interface BuildSuggestion {
  id: string;
  name: string;
  skills: string[];
  keyItem: string;
  playstyle: string;
  description: string;
} 