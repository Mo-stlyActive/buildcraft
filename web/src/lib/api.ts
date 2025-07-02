const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8001';

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

export interface BuildResponse {
  build_name: string;
  race: string;
  race_description: string;
  skills: string[];
  skill_details: Array<{name: string; category: string; score: number}>;
  equipment: {
    weapons: string[];
    armor: string[];
    accessories: string[];
  };
  spells: string[];
  playstyle: string;
  reasoning: string;
  synergies: string[];
  progression: string[];
  roleplay_flavor: string;
  tips: string[];
}

export interface ChatResponse {
  success: boolean;
  build?: BuildResponse;
  search?: SearchResponse;
  message: string;
}

export async function searchItems(query: string, category?: string, limit: number = 5): Promise<SearchResponse> {
  try {
    const response = await fetch(`${API_BASE_URL}/search`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query, category, limit }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error searching items:', error);
    throw error;
  }
}

export async function generateBuild(prompt: string, playstyle?: string, difficulty: string = 'normal'): Promise<BuildResponse> {
  try {
    const response = await fetch(`${API_BASE_URL}/build`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt, playstyle, difficulty }),
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error generating build:', error);
    throw error;
  }
}

export async function sendChatMessage(prompt: string): Promise<ChatResponse> {
  try {
    // First try to generate a build
    const buildResponse = await generateBuild(prompt);
    
    return {
      success: true,
      build: buildResponse,
      message: buildResponse.reasoning || `Generated build: ${buildResponse.build_name}`,
    };
  } catch (error) {
    console.error('Error sending chat message:', error);
    throw error;
  }
}

export async function checkApiHealth(): Promise<boolean> {
  try {
    const response = await fetch(`${API_BASE_URL}/health`);
    return response.ok;
  } catch (error) {
    console.error('API health check failed:', error);
    return false;
  }
} 