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
  properties: Record<string, unknown>;
  score: number;
}

export interface SearchResponse {
  results: SearchResult[];
  reasoning: string;
  suggestions: string[];
}

export interface SkillDetail {
  name: string;
  category: string;
  score: number;
  properties?: Record<string, unknown>;
}

export interface BuildEquipment {
  weapons: string[];
  armor: string[];
  accessories: string[];
}

export interface BuildResponse {
  build_name: string;
  race: string;
  race_description: string;
  skills: string[];
  skill_details: SkillDetail[];
  equipment: BuildEquipment;
  spells: string[];
  playstyle: string;
  reasoning: string;
  synergies: string[];
  progression: string[];
  roleplay_flavor: string;
  tips: string[];
} 