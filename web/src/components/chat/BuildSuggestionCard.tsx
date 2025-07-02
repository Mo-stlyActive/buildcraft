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
          <p className="text-sm text-gray-600">{build.race} - {build.playstyle}</p>
        </div>
      </div>
      
      {/* Race Section */}
      <div className="mb-4 bg-blue-50 border border-blue-200 rounded-lg p-3">
        <h4 className="font-semibold text-gray-800 mb-1 flex items-center">
          <span className="text-lg mr-2">👤</span>
          {build.race}
        </h4>
        <p className="text-sm text-gray-700">{build.race_description}</p>
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
      
      {/* Equipment Section */}
      <div className="mb-4">
        <h4 className="font-semibold text-gray-800 mb-2 flex items-center">
          <span className="text-lg mr-2">🗡️</span>
          Equipment
        </h4>
        <div className="space-y-2">
          {build.equipment.weapons.length > 0 && (
            <div className="bg-red-50 border border-red-200 rounded-lg p-2">
              <p className="text-sm font-medium text-gray-800">Weapons:</p>
              <p className="text-sm text-gray-900">{build.equipment.weapons.join(', ')}</p>
            </div>
          )}
          {build.equipment.armor.length > 0 && (
            <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-2">
              <p className="text-sm font-medium text-gray-800">Armor:</p>
              <p className="text-sm text-gray-900">{build.equipment.armor.join(', ')}</p>
            </div>
          )}
        </div>
      </div>
      
      {/* Spells Section */}
      {build.spells.length > 0 && (
        <div className="mb-4">
          <h4 className="font-semibold text-gray-800 mb-2 flex items-center">
            <span className="text-lg mr-2">✨</span>
            Key Spells
          </h4>
          <div className="bg-purple-50 border border-purple-200 rounded-lg p-3">
            <p className="text-gray-900 text-sm">{build.spells.join(', ')}</p>
          </div>
        </div>
      )}
      
      {/* Roleplay Flavor */}
      <div className="mb-4 bg-green-50 border border-green-200 rounded-lg p-3">
        <h4 className="font-semibold text-gray-800 mb-2 flex items-center">
          <span className="text-lg mr-2">🎭</span>
          Roleplay
        </h4>
        <p className="text-gray-700 leading-relaxed text-sm italic">{build.roleplay_flavor}</p>
      </div>
      
      {/* Synergies Section */}
      {build.synergies.length > 0 && (
        <div className="mb-4">
          <h4 className="font-semibold text-gray-800 mb-2 flex items-center">
            <span className="text-lg mr-2">⚡</span>
            Synergies
          </h4>
          <ul className="text-sm text-gray-700 space-y-1">
            {build.synergies.map((synergy, index) => (
              <li key={index} className="flex items-start">
                <span className="text-green-500 mr-2">•</span>
                {synergy}
              </li>
            ))}
          </ul>
        </div>
      )}
      
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
      {build.tips.length > 0 && (
        <div className="mt-4 pt-4 border-t border-gray-200">
          <h4 className="font-semibold text-gray-800 mb-2 flex items-center">
            <span className="text-lg mr-2">💡</span>
            Tips
          </h4>
          <ul className="text-sm text-gray-600 space-y-1">
            {build.tips.map((tip, index) => (
              <li key={index} className="flex items-start">
                <span className="text-blue-500 mr-2">•</span>
                {tip}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
} 