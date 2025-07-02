#!/usr/bin/env python3
"""
Build Composer for BuildCraft AI
Dynamically generates creative, context-aware character builds
"""

import json
import random
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
import re


@dataclass
class BuildComponent:
    """Represents a component of a character build"""
    name: str
    category: str
    description: str
    synergies: List[str]
    score: float = 0.0
    metadata: Dict[str, Any] = None


class OblivionBuildComposer:
    """Composes dynamic character builds for Oblivion based on user preferences"""
    
    def __init__(self):
        self.races_data = {
            "Altmer": {
                "description": "High Elves with natural magical aptitude",
                "bonuses": {"Intelligence": 10, "Willpower": 5},
                "skills": ["Alchemy", "Alteration", "Conjuration", "Destruction", "Illusion", "Mysticism"],
                "playstyles": ["mage", "magic", "scholar", "destruction", "conjuration", "enchantment"],
                "flavor": "Noble and proud, with an innate connection to the magical arts"
            },
            "Argonian": {
                "description": "Reptilian humanoids with natural stealth and disease resistance",
                "bonuses": {"Speed": 10, "Agility": 5},
                "skills": ["Alchemy", "Athletics", "Blade", "Hand to Hand", "Illusion", "Mysticism"],
                "playstyles": ["stealth", "assassin", "swimmer", "survival", "poison", "guerrilla"],
                "flavor": "Swift and adaptable, masters of unconventional warfare"
            },
            "Bosmer": {
                "description": "Wood Elves with exceptional archery and stealth skills",
                "bonuses": {"Agility": 10, "Speed": 5},
                "skills": ["Alchemy", "Light Armor", "Marksman", "Sneak", "Acrobatics"],
                "playstyles": ["archer", "ranger", "stealth", "hunter", "forest", "nimble"],
                "flavor": "Silent hunters who move like shadows through the wilderness"
            },
            "Breton": {
                "description": "Part-elven humans with strong magical resistance",
                "bonuses": {"Intelligence": 10, "Willpower": 5},
                "skills": ["Alchemy", "Alteration", "Conjuration", "Illusion", "Mysticism", "Restoration"],
                "playstyles": ["spellsword", "battlemage", "healer", "support", "versatile", "balanced"],
                "flavor": "Versatile magic users who blend martial and mystical arts"
            },
            "Dunmer": {
                "description": "Dark Elves with fire resistance and balanced abilities",
                "bonuses": {"Speed": 5, "Willpower": 5},
                "skills": ["Athletics", "Blade", "Blunt", "Destruction", "Light Armor", "Mysticism"],
                "playstyles": ["spellsword", "fire", "warrior-mage", "versatile", "destruction", "agile"],
                "flavor": "Fierce warriors who wield blade and spell with equal skill"
            },
            "Imperial": {
                "description": "Humans with natural leadership and diplomatic skills",
                "bonuses": {"Personality": 10},
                "skills": ["Blade", "Blunt", "Hand to Hand", "Heavy Armor", "Mercantile", "Speechcraft"],
                "playstyles": ["knight", "leader", "merchant", "diplomat", "versatile", "social"],
                "flavor": "Natural leaders who inspire others and command respect"
            },
            "Khajiit": {
                "description": "Feline humanoids with exceptional stealth and agility",
                "bonuses": {"Speed": 10, "Agility": 5},
                "skills": ["Acrobatics", "Athletics", "Blade", "Hand to Hand", "Light Armor", "Security"],
                "playstyles": ["thief", "acrobat", "stealth", "ninja", "agile", "cat-burglar"],
                "flavor": "Silent as moonlight, swift as striking serpents"
            },
            "Nord": {
                "description": "Hardy northmen with frost resistance and warrior traditions",
                "bonuses": {"Strength": 10, "Endurance": 5},
                "skills": ["Armorer", "Blade", "Block", "Blunt", "Heavy Armor", "Restoration"],
                "playstyles": ["warrior", "berserker", "tank", "knight", "frost", "traditional"],
                "flavor": "Stalwart warriors who stand firm against any storm"
            },
            "Orc": {
                "description": "Orsimer with incredible strength and smithing prowess",
                "bonuses": {"Strength": 10, "Willpower": 5, "Endurance": 5},
                "skills": ["Armorer", "Block", "Blunt", "Heavy Armor", "Hand to Hand"],
                "playstyles": ["berserker", "tank", "smith", "brutal", "heavy", "unstoppable"],
                "flavor": "Unstoppable forces of nature who forge their own destiny"
            },
            "Redguard": {
                "description": "Desert warriors with exceptional weapon skills",
                "bonuses": {"Strength": 5, "Speed": 5, "Agility": 5},
                "skills": ["Athletics", "Blade", "Blunt", "Heavy Armor", "Mercantile"],
                "playstyles": ["warrior", "swordsman", "duelist", "mobile", "weapon-master", "desert"],
                "flavor": "Master swordsmen whose blades dance like desert winds"
            }
        }
        
        self.build_archetypes = {
            "stealth_archer": {
                "skills": ["Marksman", "Sneak", "Light Armor", "Acrobatics", "Security"],
                "keywords": ["stealth", "archer", "ranger", "hunter", "bow", "silent", "shadow"],
                "description": "A silent hunter who strikes from the shadows"
            },
            "spellsword": {
                "skills": ["Blade", "Destruction", "Restoration", "Light Armor", "Mysticism"],
                "keywords": ["spellsword", "magic", "sword", "battle", "mage", "warrior"],
                "description": "A warrior-mage who combines steel and sorcery"
            },
            "tank": {
                "skills": ["Heavy Armor", "Block", "Restoration", "Endurance", "Armorer"],
                "keywords": ["tank", "defender", "shield", "armor", "tough", "protector"],
                "description": "An immovable fortress who protects allies"
            },
            "assassin": {
                "skills": ["Sneak", "Blade", "Light Armor", "Acrobatics", "Illusion"],
                "keywords": ["assassin", "stealth", "killer", "shadow", "death", "silent"],
                "description": "A silent death that strikes without warning"
            },
            "battlemage": {
                "skills": ["Destruction", "Heavy Armor", "Restoration", "Mysticism", "Blade"],
                "keywords": ["battlemage", "magic", "armor", "spell", "combat", "mage"],
                "description": "A heavily armored spellcaster who dominates the battlefield"
            }
        }

    def analyze_user_intent(self, prompt: str) -> Dict[str, Any]:
        """Analyze user prompt to extract playstyle preferences and themes"""
        prompt_lower = prompt.lower()
        
        # Extract themes and keywords
        themes = []
        playstyle_scores = {}
        
        # Check for archetype keywords
        for archetype, data in self.build_archetypes.items():
            score = 0
            for keyword in data["keywords"]:
                if keyword in prompt_lower:
                    score += 1
            if score > 0:
                playstyle_scores[archetype] = score
                themes.extend(data["keywords"])
        
        # Extract specific gameplay elements
        gameplay_elements = {
            "magic_schools": [],
            "weapon_types": [],
            "armor_preference": "",
            "combat_style": "",
            "special_themes": []
        }
        
        # Magic schools
        magic_schools = ["destruction", "restoration", "illusion", "conjuration", "alteration", "mysticism"]
        for school in magic_schools:
            if school in prompt_lower:
                gameplay_elements["magic_schools"].append(school)
        
        # Weapon types
        weapons = ["sword", "bow", "staff", "dagger", "axe", "mace", "blade"]
        for weapon in weapons:
            if weapon in prompt_lower:
                gameplay_elements["weapon_types"].append(weapon)
        
        # Armor preference
        if "heavy" in prompt_lower and "armor" in prompt_lower:
            gameplay_elements["armor_preference"] = "heavy"
        elif "light" in prompt_lower and "armor" in prompt_lower:
            gameplay_elements["armor_preference"] = "light"
        
        # Special themes
        special_themes = ["fire", "ice", "poison", "shadow", "holy", "dark", "nature", "undead"]
        for theme in special_themes:
            if theme in prompt_lower:
                gameplay_elements["special_themes"].append(theme)
        
        return {
            "themes": list(set(themes)),
            "playstyle_scores": playstyle_scores,
            "gameplay_elements": gameplay_elements,
            "primary_archetype": max(playstyle_scores.keys(), key=playstyle_scores.get) if playstyle_scores else "versatile"
        }

    def recommend_race(self, intent: Dict[str, Any]) -> Dict[str, Any]:
        """Recommend the best race based on user intent"""
        race_scores = {}
        
        for race_name, race_data in self.races_data.items():
            score = 0
            
            # Check playstyle compatibility
            for playstyle in race_data["playstyles"]:
                if playstyle in intent["themes"]:
                    score += 2
            
            # Check specific gameplay elements
            if intent["gameplay_elements"]["magic_schools"]:
                if any(school in race_data["skills"] for school in ["Destruction", "Restoration", "Illusion", "Conjuration", "Alteration", "Mysticism"]):
                    score += 1
            
            race_scores[race_name] = score
        
        # Get the best race or random good option
        if not race_scores or max(race_scores.values()) == 0:
            recommended_race = random.choice(list(self.races_data.keys()))
        else:
            recommended_race = max(race_scores.keys(), key=race_scores.get)
        
        return {
            "name": recommended_race,
            "data": self.races_data[recommended_race],
            "score": race_scores.get(recommended_race, 0)
        }

    def compose_build_from_search_results(self, intent: Dict[str, Any], search_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Compose a creative build from semantic search results"""
        
        # Categorize search results
        categorized_results = {
            "skills": [],
            "weapons": [],
            "armor": [],
            "spells": [],
            "potions": [],
            "misc": []
        }
        
        for result in search_results:
            category = result.get("category", "misc")
            if category in categorized_results:
                categorized_results[category].append(result)
            else:
                categorized_results["misc"].append(result)
        
        # Recommend race
        recommended_race = self.recommend_race(intent)
        
        # Select core skills (5-7 skills)
        primary_skills = self._select_primary_skills(categorized_results["skills"], intent)
        
        # Select equipment
        equipment = self._select_equipment(categorized_results, intent)
        
        # Select spells
        spells = self._select_spells(categorized_results["spells"], intent)
        
        # Generate synergies
        synergies = self._generate_synergies(primary_skills, equipment, spells, intent)
        
        # Generate roleplay flavor
        flavor = self._generate_roleplay_flavor(recommended_race, intent, primary_skills)
        
        # Generate progression hints
        progression = self._generate_progression_hints(primary_skills, equipment, intent)
        
        # Generate build name
        build_name = self._generate_build_name(intent, recommended_race)
        
        return {
            "build_name": build_name,
            "race": recommended_race["name"],
            "race_description": recommended_race["data"]["description"],
            "skills": [skill["name"] for skill in primary_skills[:7]],
            "skill_details": primary_skills[:7],
            "equipment": {
                "weapons": [item["name"] for item in equipment["weapons"][:3]],
                "armor": [item["name"] for item in equipment["armor"][:5]],
                "accessories": [item["name"] for item in equipment.get("accessories", [])[:3]]
            },
            "spells": [spell["name"] for spell in spells[:5]],
            "playstyle": self._generate_playstyle_description(intent),
            "reasoning": self._generate_reasoning(intent, len(search_results)),
            "synergies": synergies,
            "progression": progression,
            "roleplay_flavor": flavor,
            "tips": self._generate_gameplay_tips(intent, primary_skills, equipment)
        }

    def _select_primary_skills(self, skills_results: List[Dict[str, Any]], intent: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Select primary skills based on search results and intent"""
        if not skills_results:
            # Fallback to archetype-based selection
            archetype = intent.get("primary_archetype", "versatile")
            if archetype in self.build_archetypes:
                return [{"name": skill, "category": "skills", "score": 1.0} 
                       for skill in self.build_archetypes[archetype]["skills"][:5]]
            else:
                return [{"name": skill, "category": "skills", "score": 1.0} 
                       for skill in ["Blade", "Light Armor", "Athletics", "Restoration", "Sneak"]]
        
        # Score and sort skills
        scored_skills = []
        for skill in skills_results:
            score = skill.get("score", 0.5)
            
            # Boost score based on intent themes
            for theme in intent["themes"]:
                if theme.lower() in skill["name"].lower():
                    score += 0.3
            
            scored_skills.append({
                "name": skill["name"],
                "category": skill["category"],
                "score": score,
                "properties": skill.get("properties", {})
            })
        
        # Sort by score and return top skills
        return sorted(scored_skills, key=lambda x: x["score"], reverse=True)[:7]

    def _select_equipment(self, categorized_results: Dict[str, List], intent: Dict[str, Any]) -> Dict[str, List]:
        """Select equipment based on search results and intent"""
        equipment = {"weapons": [], "armor": [], "accessories": []}
        
        # Select weapons
        weapons = categorized_results.get("weapons", [])
        if weapons:
            # Prefer weapons that match themes
            scored_weapons = []
            for weapon in weapons:
                score = weapon.get("score", 0.5)
                for theme in intent["themes"]:
                    if theme in weapon["name"].lower():
                        score += 0.4
                scored_weapons.append({"name": weapon["name"], "score": score, "properties": weapon.get("properties", {})})
            
            equipment["weapons"] = sorted(scored_weapons, key=lambda x: x["score"], reverse=True)[:3]
        else:
            # Fallback weapons based on archetype
            archetype = intent.get("primary_archetype", "versatile")
            if "archer" in archetype or "bow" in intent["themes"]:
                equipment["weapons"] = [{"name": "Elven Bow", "score": 1.0, "properties": {}}]
            elif "mage" in archetype or "magic" in intent["themes"]:
                equipment["weapons"] = [{"name": "Mage's Staff", "score": 1.0, "properties": {}}]
            else:
                equipment["weapons"] = [{"name": "Steel Sword", "score": 1.0, "properties": {}}]
        
        # Select armor
        armor = categorized_results.get("armor", [])
        if armor:
            scored_armor = []
            for item in armor:
                score = item.get("score", 0.5)
                # Prefer armor that matches intent
                if intent["gameplay_elements"]["armor_preference"]:
                    if intent["gameplay_elements"]["armor_preference"] in item["name"].lower():
                        score += 0.5
                scored_armor.append({"name": item["name"], "score": score, "properties": item.get("properties", {})})
            
            equipment["armor"] = sorted(scored_armor, key=lambda x: x["score"], reverse=True)[:5]
        else:
            # Fallback armor
            if intent["gameplay_elements"]["armor_preference"] == "heavy":
                equipment["armor"] = [{"name": "Steel Armor", "score": 1.0, "properties": {}}]
            else:
                equipment["armor"] = [{"name": "Leather Armor", "score": 1.0, "properties": {}}]
        
        return equipment

    def _select_spells(self, spells_results: List[Dict[str, Any]], intent: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Select spells based on search results and intent"""
        if not spells_results:
            # Generate default spells based on themes
            default_spells = []
            if "fire" in intent["themes"] or "destruction" in intent["themes"]:
                default_spells.append({"name": "Fireball", "school": "Destruction", "score": 1.0})
            if "healing" in intent["themes"] or "restoration" in intent["themes"]:
                default_spells.append({"name": "Heal", "school": "Restoration", "score": 1.0})
            if "stealth" in intent["themes"] or "illusion" in intent["themes"]:
                default_spells.append({"name": "Invisibility", "school": "Illusion", "score": 1.0})
            
            return default_spells[:5]
        
        # Score spells based on intent
        scored_spells = []
        for spell in spells_results:
            score = spell.get("score", 0.5)
            
            # Boost score for matching schools
            spell_school = spell.get("school", "").lower()
            if spell_school in intent["gameplay_elements"]["magic_schools"]:
                score += 0.4
            
            # Boost score for matching themes
            for theme in intent["themes"]:
                if theme in spell["name"].lower():
                    score += 0.3
            
            scored_spells.append({
                "name": spell["name"],
                "school": spell.get("school", "Unknown"),
                "score": score,
                "properties": spell.get("properties", {})
            })
        
        return sorted(scored_spells, key=lambda x: x["score"], reverse=True)[:5]

    def _generate_synergies(self, skills: List[Dict], equipment: Dict, spells: List[Dict], intent: Dict[str, Any]) -> List[str]:
        """Generate synergy descriptions"""
        synergies = []
        
        # Skill synergies
        skill_names = [skill["name"] for skill in skills]
        if "Marksman" in skill_names and "Sneak" in skill_names:
            synergies.append("Sneak attacks with ranged weapons deal massive damage")
        if "Blade" in skill_names and "Destruction" in skill_names:
            synergies.append("Enchanted weapons complement destruction spells perfectly")
        if "Light Armor" in skill_names and "Acrobatics" in skill_names:
            synergies.append("Mobility and protection work together for hit-and-run tactics")
        if "Heavy Armor" in skill_names and "Block" in skill_names:
            synergies.append("Superior defense allows for aggressive tanking strategies")
        
        # Equipment synergies
        if equipment["weapons"] and equipment["armor"]:
            synergies.append("Weapon and armor choices complement your primary combat style")
        
        # Spell synergies
        if spells:
            spell_schools = [spell.get("school", "") for spell in spells]
            if "Destruction" in spell_schools and "Restoration" in spell_schools:
                synergies.append("Balance offensive magic with healing for sustained combat")
        
        # Theme-based synergies
        if "stealth" in intent["themes"]:
            synergies.append("All equipment choices support a stealthy approach to encounters")
        if "magic" in intent["themes"]:
            synergies.append("Skills and equipment focus on maximizing magical effectiveness")
        
        return synergies[:5]

    def _generate_roleplay_flavor(self, race: Dict[str, Any], intent: Dict[str, Any], skills: List[Dict]) -> str:
        """Generate roleplay flavor text"""
        race_flavor = race["data"]["flavor"]
        primary_archetype = intent.get("primary_archetype", "versatile")
        
        themes = intent["themes"]
        
        if "stealth" in themes and "archer" in themes:
            return f"{race_flavor}. You are a master of the hunt, moving unseen through shadow and striking with precision from afar. Your enemies fall before they even know you're there."
        elif "magic" in themes:
            return f"{race_flavor}. The arcane flows through your veins like lifeblood. You see the world through the lens of mystical possibility, bending reality to your will."
        elif "warrior" in themes or "tank" in themes:
            return f"{race_flavor}. You stand as an immovable force on the battlefield, your presence alone enough to turn the tide of combat. Honor and strength guide your every action."
        elif "assassin" in themes:
            return f"{race_flavor}. Death follows in your wake like a faithful companion. You are the whisper of steel in the dark, the last sight your targets will ever see."
        else:
            return f"{race_flavor}. Your path is one of balance and adaptation, ready to face any challenge with skill and determination."

    def _generate_progression_hints(self, skills: List[Dict], equipment: Dict, intent: Dict[str, Any]) -> List[str]:
        """Generate progression and location hints"""
        progression = []
        
        # Early game progression
        progression.append("Begin by focusing on your core skills through regular practice and training")
        
        # Equipment hints
        if equipment["weapons"]:
            progression.append("Seek out skilled smiths and enchanters to improve your weapons")
        
        # Skill-specific hints
        skill_names = [skill["name"] for skill in skills]
        if "Marksman" in skill_names:
            progression.append("Join the Fighters Guild for archery training and equipment access")
        if "Destruction" in skill_names:
            progression.append("The Mages Guild offers advanced magical training and spell acquisition")
        if "Sneak" in skill_names:
            progression.append("The Thieves Guild can teach advanced stealth techniques")
        
        # Mid-game progression
        progression.append("Explore ancient ruins and caves for unique equipment and knowledge")
        
        # Advanced hints based on themes
        if "magic" in intent["themes"]:
            progression.append("Seek out master wizards in remote towers for powerful spells")
        if "stealth" in intent["themes"]:
            progression.append("The shadows hold many secrets for those who know how to look")
        
        return progression[:6]

    def _generate_build_name(self, intent: Dict[str, Any], race: Dict[str, Any]) -> str:
        """Generate a creative build name"""
        archetype = intent.get("primary_archetype", "versatile")
        race_name = race["name"]
        themes = intent["themes"]
        
        # Archetype-based names
        if archetype == "stealth_archer":
            names = ["Shadow Archer", "Silent Hunter", "Moonlight Stalker", "Whisper Shot"]
        elif archetype == "spellsword":
            names = ["Arcane Warrior", "Spell Blade", "Mystic Knight", "War Mage"]
        elif archetype == "battlemage":
            names = ["Iron Sorcerer", "Armored Mage", "Battle Wizard", "Steel Enchanter"]
        elif archetype == "assassin":
            names = ["Night Blade", "Silent Death", "Shadow Dancer", "Void Walker"]
        elif archetype == "tank":
            names = ["Iron Wall", "Shield Bearer", "Fortress", "Immovable Guardian"]
        else:
            names = ["Versatile Adventurer", "Balanced Explorer", "Multi-Talented Hero"]
        
        # Add racial flair
        base_name = random.choice(names)
        if "fire" in themes:
            base_name = f"Flame {base_name}"
        elif "ice" in themes:
            base_name = f"Frost {base_name}"
        elif "shadow" in themes:
            base_name = f"Shadow {base_name}"
        
        return f"The {race_name} {base_name}"

    def _generate_playstyle_description(self, intent: Dict[str, Any]) -> str:
        """Generate playstyle description"""
        archetype = intent.get("primary_archetype", "versatile")
        themes = intent["themes"]
        
        if archetype == "stealth_archer":
            return "Long-range stealth combat with precision strikes from concealment"
        elif archetype == "spellsword":
            return "Balanced melee and magic combat with weapon enchantments"
        elif archetype == "battlemage":
            return "Heavy armor spellcasting with defensive and offensive magic"
        elif archetype == "assassin":
            return "Close-quarters stealth combat with high burst damage"
        elif archetype == "tank":
            return "Heavy defense with crowd control and party protection"
        else:
            return "Adaptable combat style that can handle various situations"

    def _generate_reasoning(self, intent: Dict[str, Any], result_count: int) -> str:
        """Generate reasoning for build choices"""
        archetype = intent.get("primary_archetype", "versatile")
        themes = ", ".join(intent["themes"][:3])
        
        return f"Built around the {archetype} archetype with themes of {themes}. Drew from {result_count} relevant items in the knowledge base to create synergistic combinations that support your desired playstyle."

    def _generate_gameplay_tips(self, intent: Dict[str, Any], skills: List[Dict], equipment: Dict) -> List[str]:
        """Generate practical gameplay tips"""
        tips = []
        
        # Skill-based tips
        skill_names = [skill["name"] for skill in skills]
        if "Sneak" in skill_names:
            tips.append("Use shadows and sound masking to avoid detection")
        if "Marksman" in skill_names:
            tips.append("Practice your aim and learn enemy weak points")
        if "Heavy Armor" in skill_names:
            tips.append("Your armor rating reduces incoming damage significantly")
        if "Destruction" in skill_names:
            tips.append("Manage your magicka carefully during extended fights")
        
        # Theme-based tips
        if "magic" in intent["themes"]:
            tips.append("Invest in Intelligence and Willpower for better spellcasting")
        if "stealth" in intent["themes"]:
            tips.append("Move slowly and avoid well-lit areas when sneaking")
        
        return tips[:4]