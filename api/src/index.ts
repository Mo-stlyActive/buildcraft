import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3001;

// Middleware
app.use(cors());
app.use(express.json());

// Types
interface BuildRequest {
  prompt: string;
  game?: string;
}

interface BuildResponse {
  id: string;
  name: string;
  skills: string[];
  keyItem: string;
  playstyle: string;
  description: string;
}

// Enhanced build generation with more detailed suggestions
function generateBuild(prompt: string): BuildResponse {
  const builds = [
    {
      id: '1',
      name: 'Venom Paladin',
      skills: ['Blade', 'Alchemy', 'Restoration', 'Heavy Armor', 'Block'],
      keyItem: 'Virulent Sword of Poison',
      playstyle: 'Heal allies while poisoning enemies',
      description: 'A holy warrior who uses alchemy to create deadly poisons while maintaining healing abilities. This build combines the defensive capabilities of heavy armor with the utility of restoration magic and the offensive power of alchemical poisons.'
    },
    {
      id: '2',
      name: 'Shadow Alchemist',
      skills: ['Sneak', 'Alchemy', 'Illusion', 'Marksman', 'Light Armor'],
      keyItem: 'Invisibility Potion',
      playstyle: 'Stealth-based combat with alchemical support',
      description: 'A master of stealth who uses alchemy to enhance their sneaking and illusion abilities. This build excels at avoiding detection while using poisons and potions to gain tactical advantages.'
    },
    {
      id: '3',
      name: 'Battle Mage',
      skills: ['Destruction', 'Heavy Armor', 'Enchanting', 'Alteration', 'Restoration'],
      keyItem: 'Staff of Storms',
      playstyle: 'Heavy armor mage with destructive spells',
      description: 'A heavily armored spellcaster who combines destructive magic with physical protection. This build allows you to cast powerful spells while being protected by heavy armor and defensive enchantments.'
    },
    {
      id: '4',
      name: 'Arcane Archer',
      skills: ['Marksman', 'Enchanting', 'Alteration', 'Sneak', 'Light Armor'],
      keyItem: 'Enchanted Bow of Lightning',
      playstyle: 'Ranged combat with magical enhancements',
      description: 'A skilled archer who enhances their arrows with magical enchantments. This build combines the precision of archery with the power of magic to create devastating ranged attacks.'
    },
    {
      id: '5',
      name: 'Spellsword',
      skills: ['Blade', 'Destruction', 'Enchanting', 'Light Armor', 'Alteration'],
      keyItem: 'Enchanted Sword of Fire',
      playstyle: 'Melee combat enhanced with destruction magic',
      description: 'A warrior who wields both sword and magic in perfect harmony. This build allows you to engage in close combat while casting destructive spells and maintaining magical protections.'
    }
  ];

  // Enhanced keyword matching for better build selection
  const lowerPrompt = prompt.toLowerCase();
  
  if (lowerPrompt.includes('stealth') || lowerPrompt.includes('sneak') || lowerPrompt.includes('shadow')) {
    return builds[1];
  } else if (lowerPrompt.includes('mage') || lowerPrompt.includes('magic') || lowerPrompt.includes('spell')) {
    if (lowerPrompt.includes('battle') || lowerPrompt.includes('armor') || lowerPrompt.includes('heavy')) {
      return builds[2];
    } else if (lowerPrompt.includes('sword') || lowerPrompt.includes('blade') || lowerPrompt.includes('melee')) {
      return builds[4];
    } else {
      return builds[2];
    }
  } else if (lowerPrompt.includes('archer') || lowerPrompt.includes('bow') || lowerPrompt.includes('ranged')) {
    return builds[3];
  } else if (lowerPrompt.includes('paladin') || lowerPrompt.includes('holy') || lowerPrompt.includes('heal')) {
    return builds[0];
  } else {
    // Default to a balanced build
    return builds[0];
  }
}

// API Routes
app.post('/api/chat', async (req, res) => {
  try {
    const { prompt, game = 'oblivion' }: BuildRequest = req.body;

    if (!prompt || typeof prompt !== 'string') {
      return res.status(400).json({ error: 'Invalid prompt provided' });
    }

    // Generate build suggestion
    const build = generateBuild(prompt);

    // Simulate processing time
    await new Promise(resolve => setTimeout(resolve, 1000));

    res.json({
      success: true,
      build,
      message: `Here's a ${build.name} build for you! This character focuses on ${build.playstyle.toLowerCase()}. The build emphasizes ${build.skills.slice(0, 2).join(' and ')} as primary skills, with ${build.keyItem} as your signature equipment.`
    });
  } catch (error) {
    console.error('Error processing chat request:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', timestamp: new Date().toISOString() });
});

// Start server
app.listen(PORT, () => {
  console.log(`BuildCraft API server running on port ${PORT}`);
}); 