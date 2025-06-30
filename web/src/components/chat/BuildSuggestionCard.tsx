import { BuildResponse } from '@/types/chat';

interface BuildSuggestionCardProps {
  build: BuildResponse;
}

export default function BuildSuggestionCard({ build }: BuildSuggestionCardProps) {
  const getSkillCategory = (skill: string) => {
    const combatSkills = ['Blade', 'Blunt', 'Hand to Hand', 'Marksman', 'Block', 'Heavy Armor', 'Light Armor'];
    const magicSkills = ['Alteration', 'Conjuration', 'Destruction', 'Illusion', 'Mysticism', 'Restoration'];
    const stealthSkills = ['Acrobatics', 'Athletics', 'Light Armor', 'Marksman', 'Mercantile', 'Sneak', 'Speechcraft'];
    
    if (combatSkills.includes(skill)) return 'combat';
    if (magicSkills.includes(skill)) return 'magic';
    if (stealthSkills.includes(skill)) return 'stealth';
    return 'other';
  };

  const getSkillColor = (skill: string) => {
    const category = getSkillCategory(skill);
    switch (category) {
      case 'combat': return 'bg-red-100 text-red-800';
      case 'magic': return 'bg-purple-100 text-purple-800';
      case 'stealth': return 'bg-green-100 text-green-800';
      default: return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="bg-white border border-gray-200 rounded-lg p-6 shadow-lg max-w-md">
      {/* Header */}
      <div className="flex items-center mb-4">
        <span className="text-3xl mr-3">🎮</span>
        <div>
          <h3 className="text-xl font-bold text-gray-900">{build.build_name}</h3>
          <p className="text-sm text-gray-600">Character Build</p>
        </div>
      </div>
      
      {/* Skills Section */}
      <div className="mb-4">
        <h4 className="font-semibold text-gray-800 mb-2 flex items-center">
          <span className="text-lg mr-2">⚔️</span>
          Primary Skills
        </h4>
        <div className="flex flex-wrap gap-2">
          {build.skills.map((skill, index) => (
            <span
              key={index}
              className={`px-3 py-1 text-sm font-medium rounded-full ${getSkillColor(skill)}`}
            >
              {skill}
            </span>
          ))}
        </div>
      </div>
      
      {/* Key Item Section */}
      <div className="mb-4">
        <h4 className="font-semibold text-gray-800 mb-2 flex items-center">
          <span className="text-lg mr-2">🗡️</span>
          Key Equipment
        </h4>
        <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-3">
          <p className="text-gray-900 font-medium">{build.key_items.join(', ')}</p>
        </div>
      </div>
      
      {/* Playstyle Section */}
      <div className="mb-4">
        <h4 className="font-semibold text-gray-800 mb-2 flex items-center">
          <span className="text-lg mr-2">🎯</span>
          Playstyle
        </h4>
        <p className="text-gray-700 leading-relaxed">{build.playstyle}</p>
      </div>
      
      {/* Description Section */}
      <div className="mb-6">
        <h4 className="font-semibold text-gray-800 mb-2 flex items-center">
          <span className="text-lg mr-2">📖</span>
          Build Overview
        </h4>
        <p className="text-gray-700 leading-relaxed text-sm">{build.reasoning}</p>
      </div>
      
      {/* Action Buttons */}
      <div className="flex flex-col sm:flex-row gap-2">
        <button className="flex-1 px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors font-medium">
          💾 Save Build
        </button>
        <button className="flex-1 px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition-colors font-medium">
          🔗 Share
        </button>
        <button className="flex-1 px-4 py-2 bg-gray-500 text-white rounded-lg hover:bg-gray-600 transition-colors font-medium">
          🔄 Regenerate
        </button>
      </div>
      
      {/* Tips Section */}
      <div className="mt-4 pt-4 border-t border-gray-200">
        <h4 className="font-semibold text-gray-800 mb-2 flex items-center">
          <span className="text-lg mr-2">💡</span>
          Quick Tips
        </h4>
        <ul className="text-sm text-gray-600 space-y-1">
          <li>• Focus on leveling your primary skills first</li>
          <li>• Use {build.key_items.join(', ')} as your main equipment</li>
          <li>• Practice {build.playstyle.toLowerCase()} in combat</li>
        </ul>
      </div>
    </div>
  );
} 