#!/usr/bin/env python3
"""
Comprehensive Oblivion Game Data
Rich database of skills, items, spells, and other game elements with detailed metadata
"""

OBLIVION_GAMEDATA = {
    "skills": [
        {
            "name": "Blade",
            "category": "combat",
            "governing_attribute": "Strength",
            "description": "Mastery of sword combat and blade techniques",
            "tags": ["combat", "melee", "sword", "weapon", "warrior"],
            "synergies": ["Heavy Armor", "Block", "Armorer"],
            "combat_role": "damage_dealer",
            "primary_stat": "Strength"
        },
        {
            "name": "Blunt",
            "category": "combat", 
            "governing_attribute": "Strength",
            "description": "Expertise with maces, hammers, and crushing weapons",
            "tags": ["combat", "melee", "mace", "hammer", "warrior", "crush"],
            "synergies": ["Heavy Armor", "Block", "Armorer"],
            "combat_role": "damage_dealer",
            "primary_stat": "Strength"
        },
        {
            "name": "Hand to Hand",
            "category": "combat",
            "governing_attribute": "Strength", 
            "description": "Unarmed combat and martial arts mastery",
            "tags": ["combat", "unarmed", "martial", "monk", "brawler"],
            "synergies": ["Acrobatics", "Athletics", "Unarmored"],
            "combat_role": "damage_dealer",
            "primary_stat": "Strength"
        },
        {
            "name": "Marksman",
            "category": "combat",
            "governing_attribute": "Agility",
            "description": "Precision with bows and ranged weapons",
            "tags": ["combat", "ranged", "bow", "arrow", "archer", "hunter"],
            "synergies": ["Sneak", "Light Armor", "Acrobatics"],
            "combat_role": "damage_dealer",
            "primary_stat": "Agility"
        },
        {
            "name": "Block",
            "category": "combat",
            "governing_attribute": "Endurance",
            "description": "Shield mastery and defensive techniques",
            "tags": ["combat", "defense", "shield", "protection", "tank"],
            "synergies": ["Heavy Armor", "Blade", "Blunt"],
            "combat_role": "tank",
            "primary_stat": "Endurance"
        },
        {
            "name": "Armorer",
            "category": "crafting",
            "governing_attribute": "Endurance",
            "description": "Armor and weapon maintenance and crafting",
            "tags": ["crafting", "repair", "maintenance", "smith", "armor"],
            "synergies": ["Heavy Armor", "Light Armor", "Block"],
            "combat_role": "support",
            "primary_stat": "Endurance"
        },
        {
            "name": "Heavy Armor",
            "category": "combat",
            "governing_attribute": "Endurance",
            "description": "Mastery of heavy armor and defensive tactics",
            "tags": ["combat", "defense", "armor", "protection", "tank"],
            "synergies": ["Block", "Blade", "Blunt"],
            "combat_role": "tank",
            "primary_stat": "Endurance"
        },
        {
            "name": "Light Armor",
            "category": "stealth",
            "governing_attribute": "Speed",
            "description": "Agile armor usage and mobility tactics",
            "tags": ["stealth", "agility", "mobility", "light", "nimble"],
            "synergies": ["Sneak", "Acrobatics", "Marksman"],
            "combat_role": "damage_dealer",
            "primary_stat": "Speed"
        },
        {
            "name": "Acrobatics",
            "category": "stealth",
            "governing_attribute": "Speed",
            "description": "Jumping, climbing, and aerial maneuvers",
            "tags": ["stealth", "mobility", "jump", "climb", "parkour"],
            "synergies": ["Light Armor", "Sneak", "Athletics"],
            "combat_role": "mobility",
            "primary_stat": "Speed"
        },
        {
            "name": "Athletics",
            "category": "stealth",
            "governing_attribute": "Speed",
            "description": "Running speed and endurance",
            "tags": ["stealth", "speed", "endurance", "running", "stamina"],
            "synergies": ["Acrobatics", "Light Armor", "Hand to Hand"],
            "combat_role": "mobility",
            "primary_stat": "Speed"
        },
        {
            "name": "Sneak",
            "category": "stealth",
            "governing_attribute": "Agility",
            "description": "Stealth movement and concealment",
            "tags": ["stealth", "hidden", "shadow", "assassin", "thief"],
            "synergies": ["Light Armor", "Marksman", "Security"],
            "combat_role": "damage_dealer",
            "primary_stat": "Agility"
        },
        {
            "name": "Security",
            "category": "stealth",
            "governing_attribute": "Agility",
            "description": "Lockpicking and trap detection",
            "tags": ["stealth", "lockpick", "trap", "thief", "burglar"],
            "synergies": ["Sneak", "Light Armor", "Mercantile"],
            "combat_role": "utility",
            "primary_stat": "Agility"
        },
        {
            "name": "Mercantile",
            "category": "social",
            "governing_attribute": "Personality",
            "description": "Trading and negotiation skills",
            "tags": ["social", "trade", "merchant", "negotiation", "money"],
            "synergies": ["Speechcraft", "Security", "Alchemy"],
            "combat_role": "support",
            "primary_stat": "Personality"
        },
        {
            "name": "Speechcraft",
            "category": "social",
            "governing_attribute": "Personality",
            "description": "Persuasion and social manipulation",
            "tags": ["social", "persuade", "charm", "diplomat", "leader"],
            "synergies": ["Mercantile", "Illusion", "Restoration"],
            "combat_role": "support",
            "primary_stat": "Personality"
        },
        {
            "name": "Alchemy",
            "category": "magic",
            "governing_attribute": "Intelligence",
            "description": "Potion brewing and ingredient knowledge",
            "tags": ["magic", "potion", "brew", "ingredient", "alchemist"],
            "synergies": ["Restoration", "Destruction", "Mysticism"],
            "combat_role": "support",
            "primary_stat": "Intelligence"
        },
        {
            "name": "Conjuration",
            "category": "magic",
            "governing_attribute": "Intelligence",
            "description": "Summoning creatures and bound weapons",
            "tags": ["magic", "summon", "bound", "creature", "conjurer"],
            "synergies": ["Mysticism", "Destruction", "Illusion"],
            "combat_role": "damage_dealer",
            "primary_stat": "Intelligence"
        },
        {
            "name": "Mysticism",
            "category": "magic",
            "governing_attribute": "Intelligence",
            "description": "Teleportation and soul manipulation",
            "tags": ["magic", "teleport", "soul", "mystic", "arcane"],
            "synergies": ["Conjuration", "Enchant", "Alchemy"],
            "combat_role": "utility",
            "primary_stat": "Intelligence"
        },
        {
            "name": "Alteration",
            "category": "magic",
            "governing_attribute": "Willpower",
            "description": "Reality manipulation and protective magic",
            "tags": ["magic", "protection", "alter", "shield", "barrier"],
            "synergies": ["Restoration", "Mysticism", "Destruction"],
            "combat_role": "support",
            "primary_stat": "Willpower"
        },
        {
            "name": "Destruction",
            "category": "magic",
            "governing_attribute": "Willpower",
            "description": "Offensive magic and elemental attacks",
            "tags": ["magic", "fire", "ice", "shock", "damage", "destruction"],
            "synergies": ["Alteration", "Conjuration", "Blade"],
            "combat_role": "damage_dealer",
            "primary_stat": "Willpower"
        },
        {
            "name": "Illusion",
            "category": "magic",
            "governing_attribute": "Personality",
            "description": "Mind manipulation and invisibility magic",
            "tags": ["magic", "illusion", "invisible", "charm", "mind"],
            "synergies": ["Sneak", "Speechcraft", "Conjuration"],
            "combat_role": "utility",
            "primary_stat": "Personality"
        },
        {
            "name": "Restoration",
            "category": "magic",
            "governing_attribute": "Willpower",
            "description": "Healing and protective divine magic",
            "tags": ["magic", "heal", "protection", "divine", "holy"],
            "synergies": ["Alteration", "Alchemy", "Block"],
            "combat_role": "support",
            "primary_stat": "Willpower"
        }
    ],
    
    "weapons": [
        {
            "name": "Iron Sword",
            "category": "weapons",
            "type": "blade",
            "description": "Basic one-handed sword for new warriors",
            "tags": ["blade", "sword", "melee", "basic", "warrior"],
            "damage_type": "slash",
            "skill_required": "Blade",
            "enchantable": True,
            "rarity": "common"
        },
        {
            "name": "Steel Sword",
            "category": "weapons",
            "type": "blade",
            "description": "Reliable steel blade favored by soldiers",
            "tags": ["blade", "sword", "melee", "steel", "soldier"],
            "damage_type": "slash",
            "skill_required": "Blade",
            "enchantable": True,
            "rarity": "common"
        },
        {
            "name": "Elven Longsword",
            "category": "weapons",
            "type": "blade",
            "description": "Elegant elven craftsmanship with superior balance",
            "tags": ["blade", "sword", "elven", "elegant", "light"],
            "damage_type": "slash",
            "skill_required": "Blade",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Dwarven Claymore",
            "category": "weapons",
            "type": "blade",
            "description": "Heavy two-handed sword of dwarven make",
            "tags": ["blade", "sword", "dwarven", "heavy", "two-handed"],
            "damage_type": "slash",
            "skill_required": "Blade",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Glass Sword",
            "category": "weapons",
            "type": "blade",
            "description": "Razor-sharp volcanic glass weapon",
            "tags": ["blade", "sword", "glass", "sharp", "fragile"],
            "damage_type": "slash",
            "skill_required": "Blade",
            "enchantable": True,
            "rarity": "rare"
        },
        {
            "name": "Ebony Blade",
            "category": "weapons",
            "type": "blade",
            "description": "Dark ebony sword with sinister properties",
            "tags": ["blade", "sword", "ebony", "dark", "evil"],
            "damage_type": "slash",
            "skill_required": "Blade",
            "enchantable": True,
            "rarity": "legendary"
        },
        {
            "name": "Hunting Bow",
            "category": "weapons",
            "type": "bow",
            "description": "Simple bow for hunting and basic archery",
            "tags": ["bow", "ranged", "hunting", "basic", "wood"],
            "damage_type": "pierce",
            "skill_required": "Marksman",
            "enchantable": True,
            "rarity": "common"
        },
        {
            "name": "Elven Bow",
            "category": "weapons",
            "type": "bow",
            "description": "Masterfully crafted elven longbow",
            "tags": ["bow", "ranged", "elven", "elegant", "precise"],
            "damage_type": "pierce",
            "skill_required": "Marksman",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Daedric Bow",
            "category": "weapons",
            "type": "bow",
            "description": "Terrifying bow forged in Oblivion",
            "tags": ["bow", "ranged", "daedric", "evil", "powerful"],
            "damage_type": "pierce",
            "skill_required": "Marksman",
            "enchantable": True,
            "rarity": "legendary"
        },
        {
            "name": "Iron Mace",
            "category": "weapons",
            "type": "blunt",
            "description": "Heavy crushing weapon",
            "tags": ["mace", "blunt", "crush", "heavy", "basic"],
            "damage_type": "crush",
            "skill_required": "Blunt",
            "enchantable": True,
            "rarity": "common"
        },
        {
            "name": "Dwarven Warhammer",
            "category": "weapons",
            "type": "blunt",
            "description": "Massive two-handed crushing weapon",
            "tags": ["hammer", "blunt", "dwarven", "two-handed", "crush"],
            "damage_type": "crush",
            "skill_required": "Blunt",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Silver Dagger",
            "category": "weapons",
            "type": "blade",
            "description": "Blessed silver blade effective against undead",
            "tags": ["dagger", "blade", "silver", "undead", "holy"],
            "damage_type": "slash",
            "skill_required": "Blade",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Bound Sword",
            "category": "weapons",
            "type": "conjured",
            "description": "Magically summoned daedric blade",
            "tags": ["conjured", "magic", "daedric", "temporary", "bound"],
            "damage_type": "slash",
            "skill_required": "Conjuration",
            "enchantable": False,
            "rarity": "spell"
        },
        {
            "name": "Akaviri Katana",
            "category": "weapons",
            "type": "blade",
            "description": "Curved blade from the distant land of Akavir",
            "tags": ["blade", "katana", "akaviri", "curved", "exotic", "samurai"],
            "damage_type": "slash",
            "skill_required": "Blade",
            "enchantable": True,
            "rarity": "rare"
        },
        {
            "name": "Umbra",
            "category": "weapons",
            "type": "blade",
            "description": "Legendary ebony sword with soul-stealing powers",
            "tags": ["blade", "legendary", "ebony", "soul", "evil", "artifact"],
            "damage_type": "slash",
            "skill_required": "Blade",
            "enchantable": False,
            "rarity": "artifact"
        },
        {
            "name": "Chillrend",
            "category": "weapons",
            "type": "blade",
            "description": "Frost-enchanted glass sword of great power",
            "tags": ["blade", "glass", "frost", "ice", "enchanted", "legendary"],
            "damage_type": "slash",
            "skill_required": "Blade",
            "enchantable": False,
            "rarity": "legendary"
        },
        {
            "name": "Blackwater Blade",
            "category": "weapons",
            "type": "blade",
            "description": "Enchanted silver sword effective against undead",
            "tags": ["blade", "silver", "undead", "enchanted", "holy", "vampire"],
            "damage_type": "slash",
            "skill_required": "Blade",
            "enchantable": False,
            "rarity": "rare"
        },
        {
            "name": "Mehrunes' Razor",
            "category": "weapons",
            "type": "dagger",
            "description": "Daedric artifact dagger with instant kill chance",
            "tags": ["dagger", "daedric", "artifact", "assassin", "instant", "kill"],
            "damage_type": "stab",
            "skill_required": "Blade",
            "enchantable": False,
            "rarity": "artifact"
        },
        {
            "name": "Shadowhunt",
            "category": "weapons",
            "type": "bow",
            "description": "Enchanted elven bow with stealth bonuses",
            "tags": ["bow", "elven", "stealth", "shadow", "enchanted", "archer"],
            "damage_type": "pierce",
            "skill_required": "Marksman",
            "enchantable": False,
            "rarity": "rare"
        },
        {
            "name": "Bow of Infliction",
            "category": "weapons",
            "type": "bow",
            "description": "Cursed bow that damages health and drains attributes",
            "tags": ["bow", "cursed", "drain", "damage", "evil", "dark"],
            "damage_type": "pierce",
            "skill_required": "Marksman",
            "enchantable": False,
            "rarity": "rare"
        },
        {
            "name": "Hatreds Heart",
            "category": "weapons",
            "type": "bow",
            "description": "Powerful daedric bow with fire enchantment",
            "tags": ["bow", "daedric", "fire", "hatred", "powerful", "enchanted"],
            "damage_type": "pierce",
            "skill_required": "Marksman",
            "enchantable": False,
            "rarity": "legendary"
        },
        {
            "name": "Volendrung",
            "category": "weapons",
            "type": "blunt",
            "description": "Legendary dwarven warhammer artifact",
            "tags": ["hammer", "dwarven", "legendary", "artifact", "massive", "crusher"],
            "damage_type": "crush",
            "skill_required": "Blunt",
            "enchantable": False,
            "rarity": "artifact"
        },
        {
            "name": "Mace of Molag Bal",
            "category": "weapons",
            "type": "blunt",
            "description": "Daedric mace that drains strength and magicka",
            "tags": ["mace", "daedric", "artifact", "drain", "evil", "molag"],
            "damage_type": "crush",
            "skill_required": "Blunt",
            "enchantable": False,
            "rarity": "artifact"
        },
        {
            "name": "Skull Crusher",
            "category": "weapons",
            "type": "blunt",
            "description": "Orcish mace designed for devastating impact",
            "tags": ["mace", "orcish", "skull", "crush", "devastating", "brutal"],
            "damage_type": "crush",
            "skill_required": "Blunt",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Staff of Worms",
            "category": "weapons",
            "type": "staff",
            "description": "Necromantic staff that raises undead minions",
            "tags": ["staff", "necromancy", "undead", "raise", "dark", "magic"],
            "damage_type": "magic",
            "skill_required": "Destruction",
            "enchantable": False,
            "rarity": "legendary"
        },
        {
            "name": "Staff of Firebolts",
            "category": "weapons",
            "type": "staff",
            "description": "Enchanted staff that casts powerful firebolts",
            "tags": ["staff", "fire", "destruction", "magic", "enchanted", "mage"],
            "damage_type": "magic",
            "skill_required": "Destruction",
            "enchantable": False,
            "rarity": "uncommon"
        },
        {
            "name": "Bound Dagger",
            "category": "weapons",
            "type": "conjured",
            "description": "Magically summoned daedric dagger",
            "tags": ["conjured", "dagger", "daedric", "temporary", "bound", "assassin"],
            "damage_type": "stab",
            "skill_required": "Conjuration",
            "enchantable": False,
            "rarity": "spell"
        },
        {
            "name": "Bound Bow",
            "category": "weapons",
            "type": "conjured",
            "description": "Magically summoned daedric bow with infinite arrows",
            "tags": ["conjured", "bow", "daedric", "temporary", "bound", "archer"],
            "damage_type": "pierce",
            "skill_required": "Conjuration",
            "enchantable": False,
            "rarity": "spell"
        }
    ],
    
    "armor": [
        {
            "name": "Leather Armor",
            "category": "armor",
            "type": "light",
            "description": "Basic leather protection for rogues",
            "tags": ["light", "leather", "stealth", "basic", "flexible"],
            "skill_required": "Light Armor",
            "enchantable": True,
            "rarity": "common"
        },
        {
            "name": "Chainmail Hauberk",
            "category": "armor",
            "type": "light",
            "description": "Flexible metal ring protection",
            "tags": ["light", "chainmail", "metal", "flexible", "protection"],
            "skill_required": "Light Armor",
            "enchantable": True,
            "rarity": "common"
        },
        {
            "name": "Elven Armor",
            "category": "armor",
            "type": "light",
            "description": "Elegant elven crafted light armor",
            "tags": ["light", "elven", "elegant", "graceful", "protection"],
            "skill_required": "Light Armor",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Glass Armor",
            "category": "armor",
            "type": "light",
            "description": "Volcanic glass armor with superior protection",
            "tags": ["light", "glass", "volcanic", "superior", "protection"],
            "skill_required": "Light Armor",
            "enchantable": True,
            "rarity": "rare"
        },
        {
            "name": "Iron Armor",
            "category": "armor",
            "type": "heavy",
            "description": "Basic heavy armor for warriors",
            "tags": ["heavy", "iron", "protection", "basic", "warrior"],
            "skill_required": "Heavy Armor",
            "enchantable": True,
            "rarity": "common"
        },
        {
            "name": "Steel Armor",
            "category": "armor",
            "type": "heavy",
            "description": "Reliable steel plate protection",
            "tags": ["heavy", "steel", "plate", "reliable", "protection"],
            "skill_required": "Heavy Armor",
            "enchantable": True,
            "rarity": "common"
        },
        {
            "name": "Dwarven Armor",
            "category": "armor",
            "type": "heavy",
            "description": "Superior dwarven metal craftsmanship",
            "tags": ["heavy", "dwarven", "superior", "metal", "crafted"],
            "skill_required": "Heavy Armor",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Ebony Armor",
            "category": "armor",
            "type": "heavy",
            "description": "Dark volcanic ebony plate armor",
            "tags": ["heavy", "ebony", "volcanic", "dark", "superior"],
            "skill_required": "Heavy Armor",
            "enchantable": True,
            "rarity": "rare"
        },
        {
            "name": "Daedric Armor",
            "category": "armor",
            "type": "heavy",
            "description": "Terrifying armor forged in Oblivion",
            "tags": ["heavy", "daedric", "evil", "terrifying", "ultimate"],
            "skill_required": "Heavy Armor",
            "enchantable": True,
            "rarity": "legendary"
        },
        {
            "name": "Mage Robes",
            "category": "armor",
            "type": "clothing",
            "description": "Enchanted robes that enhance magical abilities",
            "tags": ["clothing", "magic", "robes", "enchanted", "mage"],
            "skill_required": "Unarmored",
            "enchantable": True,
            "rarity": "common"
        },
        {
            "name": "Orcish Armor",
            "category": "armor",
            "type": "heavy",
            "description": "Brutally effective orcish plate armor",
            "tags": ["heavy", "orcish", "brutal", "plate", "warrior", "orc"],
            "skill_required": "Heavy Armor",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Mithril Armor",
            "category": "armor",
            "type": "light",
            "description": "Rare elven armor made from precious mithril",
            "tags": ["light", "mithril", "elven", "rare", "precious", "magical"],
            "skill_required": "Light Armor",
            "enchantable": True,
            "rarity": "rare"
        },
        {
            "name": "Fur Armor",
            "category": "armor",
            "type": "light",
            "description": "Warm fur armor favored by barbarians",
            "tags": ["light", "fur", "barbarian", "warm", "savage", "primitive"],
            "skill_required": "Light Armor",
            "enchantable": True,
            "rarity": "common"
        },
        {
            "name": "Legion Armor",
            "category": "armor",
            "type": "heavy",
            "description": "Standard heavy armor of the Imperial Legion",
            "tags": ["heavy", "legion", "imperial", "standard", "military", "soldier"],
            "skill_required": "Heavy Armor",
            "enchantable": True,
            "rarity": "common"
        },
        {
            "name": "Madness Armor",
            "category": "armor",
            "type": "heavy",
            "description": "Crystalline armor from the Shivering Isles",
            "tags": ["heavy", "madness", "crystal", "sheogorath", "insanity", "unique"],
            "skill_required": "Heavy Armor",
            "enchantable": True,
            "rarity": "legendary"
        },
        {
            "name": "Amber Armor",
            "category": "armor",
            "type": "light",
            "description": "Light crystalline armor from the Shivering Isles",
            "tags": ["light", "amber", "crystal", "sheogorath", "golden", "unique"],
            "skill_required": "Light Armor",
            "enchantable": True,
            "rarity": "legendary"
        },
        {
            "name": "Dark Brotherhood Shrouded Armor",
            "category": "armor",
            "type": "light",
            "description": "Black leather armor of the infamous assassins guild",
            "tags": ["light", "brotherhood", "assassin", "dark", "stealth", "guild"],
            "skill_required": "Light Armor",
            "enchantable": True,
            "rarity": "rare"
        },
        {
            "name": "Thieves Guild Leather",
            "category": "armor",
            "type": "light",
            "description": "Specialized armor for professional thieves",
            "tags": ["light", "thieves", "guild", "stealth", "professional", "lockpick"],
            "skill_required": "Light Armor",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Blades Armor",
            "category": "armor",
            "type": "heavy",
            "description": "Ceremonial armor of the Emperor's Blades",
            "tags": ["heavy", "blades", "ceremonial", "emperor", "elite", "guard"],
            "skill_required": "Heavy Armor",
            "enchantable": True,
            "rarity": "rare"
        },
        {
            "name": "Mythril Chainmail",
            "category": "armor",
            "type": "light",
            "description": "Lightweight mythril chain armor",
            "tags": ["light", "mythril", "chain", "lightweight", "magical", "precious"],
            "skill_required": "Light Armor",
            "enchantable": True,
            "rarity": "rare"
        },
        {
            "name": "Arena Raiment",
            "category": "armor",
            "type": "light",
            "description": "Flashy armor worn by Arena champions",
            "tags": ["light", "arena", "champion", "flashy", "gladiator", "combat"],
            "skill_required": "Light Armor",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Apprentice Robes",
            "category": "armor",
            "type": "clothing",
            "description": "Simple robes for beginning mages",
            "tags": ["clothing", "apprentice", "mage", "simple", "learning", "basic"],
            "skill_required": "Unarmored",
            "enchantable": True,
            "rarity": "common"
        },
        {
            "name": "Necromancer Robes",
            "category": "armor",
            "type": "clothing",
            "description": "Dark robes that enhance necromantic magic",
            "tags": ["clothing", "necromancer", "dark", "death", "undead", "evil"],
            "skill_required": "Unarmored",
            "enchantable": True,
            "rarity": "rare"
        },
        {
            "name": "Arch-Mage Robes",
            "category": "armor",
            "type": "clothing",
            "description": "Magnificent robes of the Mages Guild leader",
            "tags": ["clothing", "arch-mage", "guild", "leader", "magnificent", "powerful"],
            "skill_required": "Unarmored",
            "enchantable": True,
            "rarity": "legendary"
        },
        {
            "name": "Monk Robes",
            "category": "armor",
            "type": "clothing",
            "description": "Simple robes that aid unarmed combat",
            "tags": ["clothing", "monk", "unarmed", "simple", "martial", "discipline"],
            "skill_required": "Unarmored",
            "enchantable": True,
            "rarity": "uncommon"
        }
    ],
    
    "spells": [
        {
            "name": "Fireball",
            "category": "spells",
            "school": "Destruction",
            "description": "Explosive fire projectile",
            "tags": ["fire", "destruction", "projectile", "explosive", "damage"],
            "effect": "Fire Damage",
            "magnitude": "15-45",
            "area": "10 feet",
            "rarity": "common"
        },
        {
            "name": "Heal",
            "category": "spells",
            "school": "Restoration",
            "description": "Basic healing magic",
            "tags": ["heal", "restoration", "health", "recovery", "basic"],
            "effect": "Restore Health",
            "magnitude": "10-30",
            "area": "Self",
            "rarity": "common"
        },
        {
            "name": "Invisibility",
            "category": "spells",
            "school": "Illusion",
            "description": "Become completely invisible",
            "tags": ["invisibility", "illusion", "stealth", "hidden", "concealment"],
            "effect": "Invisibility",
            "magnitude": "100%",
            "duration": "30 seconds",
            "rarity": "uncommon"
        },
        {
            "name": "Bound Sword",
            "category": "spells",
            "school": "Conjuration",
            "description": "Summon a daedric sword",
            "tags": ["bound", "conjuration", "sword", "daedric", "weapon"],
            "effect": "Bound Weapon",
            "duration": "120 seconds",
            "rarity": "common"
        },
        {
            "name": "Shield",
            "category": "spells",
            "school": "Alteration",
            "description": "Magical armor enhancement",
            "tags": ["shield", "alteration", "protection", "armor", "defense"],
            "effect": "Shield",
            "magnitude": "5-25",
            "duration": "30 seconds",
            "rarity": "common"
        },
        {
            "name": "Feather",
            "category": "spells",
            "school": "Alteration",
            "description": "Reduce weight of carried items",
            "tags": ["feather", "alteration", "weight", "burden", "utility"],
            "effect": "Feather",
            "magnitude": "5-25",
            "duration": "120 seconds",
            "rarity": "common"
        },
        {
            "name": "Charm",
            "category": "spells",
            "school": "Illusion",
            "description": "Increase disposition of target",
            "tags": ["charm", "illusion", "disposition", "social", "persuasion"],
            "effect": "Charm",
            "magnitude": "10-50",
            "duration": "30 seconds",
            "rarity": "common"
        },
        {
            "name": "Soul Trap",
            "category": "spells",
            "school": "Mysticism",
            "description": "Capture souls for enchanting",
            "tags": ["soul", "mysticism", "trap", "enchanting", "capture"],
            "effect": "Soul Trap",
            "duration": "60 seconds",
            "rarity": "uncommon"
        },
        {
            "name": "Telekinesis",
            "category": "spells",
            "school": "Mysticism",
            "description": "Manipulate objects at distance",
            "tags": ["telekinesis", "mysticism", "manipulation", "distance", "utility"],
            "effect": "Telekinesis",
            "magnitude": "5-25",
            "duration": "10 seconds",
            "rarity": "common"
        },
        {
            "name": "Lightning Bolt",
            "category": "spells",
            "school": "Destruction",
            "description": "Shock damage projectile",
            "tags": ["lightning", "shock", "destruction", "projectile", "damage"],
            "effect": "Shock Damage",
            "magnitude": "10-40",
            "rarity": "common"
        },
        {
            "name": "Ice Spike",
            "category": "spells",
            "school": "Destruction",
            "description": "Frost damage projectile",
            "tags": ["ice", "frost", "destruction", "projectile", "damage"],
            "effect": "Frost Damage",
            "magnitude": "15-35",
            "rarity": "common"
        },
        {
            "name": "Summon Skeleton",
            "category": "spells",
            "school": "Conjuration",
            "description": "Summon an undead warrior",
            "tags": ["summon", "conjuration", "skeleton", "undead", "minion"],
            "effect": "Summon Skeleton",
            "duration": "60 seconds",
            "rarity": "uncommon"
        },
        {
            "name": "Summon Dremora",
            "category": "spells",
            "school": "Conjuration",
            "description": "Summon a powerful daedric warrior",
            "tags": ["summon", "conjuration", "dremora", "daedric", "powerful", "warrior"],
            "effect": "Summon Dremora",
            "duration": "60 seconds",
            "rarity": "rare"
        },
        {
            "name": "Summon Storm Atronach",
            "category": "spells",
            "school": "Conjuration",
            "description": "Summon an elemental creature of lightning",
            "tags": ["summon", "conjuration", "atronach", "storm", "lightning", "elemental"],
            "effect": "Summon Storm Atronach",
            "duration": "60 seconds",
            "rarity": "rare"
        },
        {
            "name": "Summon Flame Atronach",
            "category": "spells",
            "school": "Conjuration",
            "description": "Summon an elemental creature of fire",
            "tags": ["summon", "conjuration", "atronach", "flame", "fire", "elemental"],
            "effect": "Summon Flame Atronach",
            "duration": "60 seconds",
            "rarity": "uncommon"
        },
        {
            "name": "Summon Frost Atronach",
            "category": "spells",
            "school": "Conjuration",
            "description": "Summon an elemental creature of ice",
            "tags": ["summon", "conjuration", "atronach", "frost", "ice", "elemental"],
            "effect": "Summon Frost Atronach",
            "duration": "60 seconds",
            "rarity": "uncommon"
        },
        {
            "name": "Finger of the Mountain",
            "category": "spells",
            "school": "Destruction",
            "description": "Devastating shock spell that can kill instantly",
            "tags": ["destruction", "shock", "lightning", "devastating", "instant", "death"],
            "effect": "Shock Damage",
            "magnitude": "100-200",
            "rarity": "legendary"
        },
        {
            "name": "Disintegrate Weapon",
            "category": "spells",
            "school": "Destruction",
            "description": "Destroys the target's weapon",
            "tags": ["destruction", "disintegrate", "weapon", "destroy", "disable"],
            "effect": "Disintegrate Weapon",
            "duration": "10 seconds",
            "rarity": "rare"
        },
        {
            "name": "Disintegrate Armor",
            "category": "spells",
            "school": "Destruction",
            "description": "Destroys the target's armor",
            "tags": ["destruction", "disintegrate", "armor", "destroy", "disable"],
            "effect": "Disintegrate Armor",
            "duration": "10 seconds",
            "rarity": "rare"
        },
        {
            "name": "Water Walking",
            "category": "spells",
            "school": "Alteration",
            "description": "Walk on water as if it were solid ground",
            "tags": ["alteration", "water", "walking", "surface", "travel", "utility"],
            "effect": "Water Walking",
            "duration": "120 seconds",
            "rarity": "uncommon"
        },
        {
            "name": "Water Breathing",
            "category": "spells",
            "school": "Alteration",
            "description": "Breathe underwater indefinitely",
            "tags": ["alteration", "water", "breathing", "underwater", "survival", "utility"],
            "effect": "Water Breathing",
            "duration": "120 seconds",
            "rarity": "uncommon"
        },
        {
            "name": "Open Lock",
            "category": "spells",
            "school": "Alteration",
            "description": "Magically unlock doors and containers",
            "tags": ["alteration", "open", "lock", "utility", "thief", "unlock"],
            "effect": "Open Lock",
            "magnitude": "25-100",
            "rarity": "common"
        },
        {
            "name": "Detect Life",
            "category": "spells",
            "school": "Mysticism",
            "description": "Reveals nearby living creatures",
            "tags": ["mysticism", "detect", "life", "reveal", "creatures", "awareness"],
            "effect": "Detect Life",
            "area": "120 feet",
            "duration": "60 seconds",
            "rarity": "common"
        },
        {
            "name": "Reflect Spell",
            "category": "spells",
            "school": "Mysticism",
            "description": "Reflects hostile spells back at caster",
            "tags": ["mysticism", "reflect", "spell", "protection", "counter", "magic"],
            "effect": "Reflect Spell",
            "magnitude": "25-50%",
            "duration": "30 seconds",
            "rarity": "rare"
        },
        {
            "name": "Spell Absorption",
            "category": "spells",
            "school": "Mysticism",
            "description": "Absorb hostile spells to restore magicka",
            "tags": ["mysticism", "absorb", "spell", "magicka", "restoration", "defense"],
            "effect": "Spell Absorption",
            "magnitude": "25-50%",
            "duration": "30 seconds",
            "rarity": "rare"
        },
        {
            "name": "Dispel",
            "category": "spells",
            "school": "Mysticism",
            "description": "Remove magical effects from target",
            "tags": ["mysticism", "dispel", "remove", "magic", "cleanse", "counter"],
            "effect": "Dispel",
            "magnitude": "25-100",
            "rarity": "uncommon"
        },
        {
            "name": "Mark",
            "category": "spells",
            "school": "Mysticism",
            "description": "Mark current location for recall",
            "tags": ["mysticism", "mark", "location", "travel", "utility", "recall"],
            "effect": "Mark",
            "rarity": "common"
        },
        {
            "name": "Recall",
            "category": "spells",
            "school": "Mysticism",
            "description": "Return to marked location instantly",
            "tags": ["mysticism", "recall", "teleport", "travel", "utility", "return"],
            "effect": "Recall",
            "rarity": "common"
        },
        {
            "name": "Silence",
            "category": "spells",
            "school": "Illusion",
            "description": "Prevent target from casting spells",
            "tags": ["illusion", "silence", "disable", "mage", "counter", "spell"],
            "effect": "Silence",
            "duration": "30 seconds",
            "rarity": "uncommon"
        },
        {
            "name": "Paralyze",
            "category": "spells",
            "school": "Illusion",
            "description": "Completely immobilize the target",
            "tags": ["illusion", "paralyze", "immobilize", "disable", "control"],
            "effect": "Paralyze",
            "duration": "10 seconds",
            "rarity": "rare"
        },
        {
            "name": "Frenzy",
            "category": "spells",
            "school": "Illusion",
            "description": "Send target into murderous rage",
            "tags": ["illusion", "frenzy", "rage", "berserk", "chaos", "mind"],
            "effect": "Frenzy",
            "magnitude": "25-100",
            "duration": "30 seconds",
            "rarity": "uncommon"
        },
        {
            "name": "Calm",
            "category": "spells",
            "school": "Illusion",
            "description": "Pacify hostile creatures",
            "tags": ["illusion", "calm", "pacify", "peace", "hostility", "mind"],
            "effect": "Calm",
            "magnitude": "25-100",
            "duration": "30 seconds",
            "rarity": "common"
        },
        {
            "name": "Night Eye",
            "category": "spells",
            "school": "Illusion",
            "description": "See clearly in complete darkness",
            "tags": ["illusion", "night", "eye", "vision", "darkness", "utility"],
            "effect": "Night Eye",
            "duration": "60 seconds",
            "rarity": "common"
        },
        {
            "name": "Greater Heal",
            "category": "spells",
            "school": "Restoration",
            "description": "Powerful healing magic",
            "tags": ["restoration", "heal", "health", "powerful", "recovery", "divine"],
            "effect": "Restore Health",
            "magnitude": "50-100",
            "rarity": "uncommon"
        },
        {
            "name": "Cure Disease",
            "category": "spells",
            "school": "Restoration",
            "description": "Remove diseases from the target",
            "tags": ["restoration", "cure", "disease", "cleanse", "health", "divine"],
            "effect": "Cure Disease",
            "rarity": "common"
        },
        {
            "name": "Turn Undead",
            "category": "spells",
            "school": "Restoration",
            "description": "Force undead creatures to flee",
            "tags": ["restoration", "turn", "undead", "flee", "divine", "holy"],
            "effect": "Turn Undead",
            "magnitude": "25-100",
            "duration": "30 seconds",
            "rarity": "uncommon"
        },
        {
            "name": "Fortify Health",
            "category": "spells",
            "school": "Restoration",
            "description": "Temporarily increase maximum health",
            "tags": ["restoration", "fortify", "health", "enhance", "temporary", "boost"],
            "effect": "Fortify Health",
            "magnitude": "25-100",
            "duration": "60 seconds",
            "rarity": "common"
        }
    ],
    
    "enchantments": [
        {
            "name": "Fire Damage",
            "category": "enchantments",
            "type": "weapon",
            "description": "Adds fire damage to weapon strikes",
            "tags": ["fire", "damage", "weapon", "elemental", "destruction"],
            "effect": "Fire Damage",
            "magnitude": "1-10"
        },
        {
            "name": "Frost Damage",
            "category": "enchantments", 
            "type": "weapon",
            "description": "Adds frost damage and slows enemies",
            "tags": ["frost", "damage", "weapon", "slow", "ice"],
            "effect": "Frost Damage",
            "magnitude": "1-10"
        },
        {
            "name": "Shock Damage",
            "category": "enchantments",
            "type": "weapon", 
            "description": "Adds shock damage and drains magicka",
            "tags": ["shock", "damage", "weapon", "magicka", "lightning"],
            "effect": "Shock Damage",
            "magnitude": "1-10"
        },
        {
            "name": "Fortify Strength",
            "category": "enchantments",
            "type": "armor",
            "description": "Increases physical strength",
            "tags": ["fortify", "strength", "armor", "enhancement", "power"],
            "effect": "Fortify Attribute",
            "magnitude": "1-20"
        },
        {
            "name": "Fortify Magicka",
            "category": "enchantments",
            "type": "armor",
            "description": "Increases maximum magicka",
            "tags": ["fortify", "magicka", "armor", "enhancement", "magic"],
            "effect": "Fortify Magicka",
            "magnitude": "10-50"
        },
        {
            "name": "Reflect Damage",
            "category": "enchantments",
            "type": "armor",
            "description": "Reflects some damage back to attacker",
            "tags": ["reflect", "damage", "armor", "protection", "retaliation"],
            "effect": "Reflect Damage",
            "magnitude": "5-25%"
        },
        {
            "name": "Soul Trap",
            "category": "enchantments",
            "type": "weapon",
            "description": "Captures souls of slain enemies",
            "tags": ["soul", "trap", "weapon", "capture", "enchanting"],
            "effect": "Soul Trap",
            "duration": "10 seconds"
        },
        {
            "name": "Paralyze",
            "category": "enchantments",
            "type": "weapon",
            "description": "Chance to paralyze enemies on hit",
            "tags": ["paralyze", "weapon", "disable", "immobilize", "control"],
            "effect": "Paralyze",
            "duration": "3-8 seconds"
        },
        {
            "name": "Drain Health",
            "category": "enchantments",
            "type": "weapon",
            "description": "Drains health from enemies and heals wielder",
            "tags": ["drain", "health", "weapon", "vampiric", "life"],
            "effect": "Drain Health",
            "magnitude": "5-25"
        },
        {
            "name": "Fortify Speed",
            "category": "enchantments",
            "type": "armor",
            "description": "Increases movement and attack speed",
            "tags": ["fortify", "speed", "armor", "movement", "agility"],
            "effect": "Fortify Speed",
            "magnitude": "5-25"
        },
        {
            "name": "Resist Magic",
            "category": "enchantments",
            "type": "armor",
            "description": "Reduces damage from magical attacks",
            "tags": ["resist", "magic", "armor", "protection", "spell"],
            "effect": "Resist Magic",
            "magnitude": "10-50%"
        },
        {
            "name": "Resist Fire",
            "category": "enchantments",
            "type": "armor",
            "description": "Reduces damage from fire attacks",
            "tags": ["resist", "fire", "armor", "protection", "flame"],
            "effect": "Resist Fire",
            "magnitude": "10-50%"
        },
        {
            "name": "Resist Frost",
            "category": "enchantments",
            "type": "armor",
            "description": "Reduces damage from frost attacks",
            "tags": ["resist", "frost", "armor", "protection", "ice"],
            "effect": "Resist Frost",
            "magnitude": "10-50%"
        },
        {
            "name": "Resist Shock",
            "category": "enchantments",
            "type": "armor",
            "description": "Reduces damage from shock attacks",
            "tags": ["resist", "shock", "armor", "protection", "lightning"],
            "effect": "Resist Shock",
            "magnitude": "10-50%"
        },
        {
            "name": "Invisibility",
            "category": "enchantments",
            "type": "armor",
            "description": "Grants temporary invisibility",
            "tags": ["invisibility", "armor", "stealth", "hidden", "concealment"],
            "effect": "Invisibility",
            "duration": "30 seconds"
        },
        {
            "name": "Feather",
            "category": "enchantments",
            "type": "armor",
            "description": "Reduces weight of carried items",
            "tags": ["feather", "armor", "weight", "burden", "carry"],
            "effect": "Feather",
            "magnitude": "25-100"
        },
        {
            "name": "Water Walking",
            "category": "enchantments",
            "type": "armor",
            "description": "Allows walking on water surface",
            "tags": ["water", "walking", "armor", "surface", "travel"],
            "effect": "Water Walking"
        }
    ],
    
    "potions": [
        {
            "name": "Potion of Healing",
            "category": "potions",
            "type": "restoration",
            "description": "Restores health when consumed",
            "tags": ["heal", "health", "restoration", "recovery", "potion"],
            "effect": "Restore Health",
            "magnitude": "25-75"
        },
        {
            "name": "Potion of Magicka",
            "category": "potions",
            "type": "restoration",
            "description": "Restores magicka when consumed",
            "tags": ["magicka", "magic", "restoration", "recovery", "potion"],
            "effect": "Restore Magicka",
            "magnitude": "25-75"
        },
        {
            "name": "Potion of Stamina",
            "category": "potions",
            "type": "restoration",
            "description": "Restores fatigue when consumed",
            "tags": ["stamina", "fatigue", "restoration", "recovery", "potion"],
            "effect": "Restore Fatigue",
            "magnitude": "25-75"
        },
        {
            "name": "Potion of Strength",
            "category": "potions",
            "type": "enhancement",
            "description": "Temporarily increases strength",
            "tags": ["strength", "enhancement", "temporary", "buff", "potion"],
            "effect": "Fortify Strength",
            "magnitude": "5-25",
            "duration": "60 seconds"
        },
        {
            "name": "Potion of Invisibility",
            "category": "potions",
            "type": "illusion",
            "description": "Makes user invisible",
            "tags": ["invisibility", "illusion", "stealth", "hidden", "potion"],
            "effect": "Invisibility",
            "duration": "30 seconds"
        },
        {
            "name": "Poison of Paralysis",
            "category": "potions",
            "type": "poison",
            "description": "Paralyzes target when applied to weapon",
            "tags": ["poison", "paralysis", "weapon", "disable", "illusion"],
            "effect": "Paralyze",
            "duration": "5-15 seconds"
        },
        {
            "name": "Potion of Waterwalking",
            "category": "potions",
            "type": "utility",
            "description": "Allows walking on water surface",
            "tags": ["waterwalking", "utility", "travel", "surface", "potion"],
            "effect": "Water Walking",
            "duration": "60 seconds"
        },
        {
            "name": "Potion of Detect Life",
            "category": "potions",
            "type": "utility",
            "description": "Reveals nearby living creatures",
            "tags": ["detect", "life", "utility", "awareness", "potion"],
            "effect": "Detect Life",
            "duration": "60 seconds"
        },
        {
            "name": "Potion of Spell Resistance",
            "category": "potions",
            "type": "protection",
            "description": "Increases resistance to magic",
            "tags": ["spell", "resistance", "magic", "protection", "potion"],
            "effect": "Resist Magic",
            "magnitude": "25-75%",
            "duration": "60 seconds"
        },
        {
            "name": "Skooma",
            "category": "potions",
            "type": "narcotic",
            "description": "Illegal drug that boosts speed but causes addiction",
            "tags": ["skooma", "drug", "speed", "illegal", "addiction"],
            "effect": "Fortify Speed",
            "magnitude": "20",
            "duration": "60 seconds"
        },
        {
            "name": "Poison of Burden",
            "category": "potions",
            "type": "poison",
            "description": "Increases target's encumbrance when applied to weapon",
            "tags": ["poison", "burden", "weight", "encumbrance", "disable"],
            "effect": "Burden",
            "magnitude": "50-150",
            "duration": "30 seconds"
        }
    ],
    
    "ingredients": [
        {
            "name": "Nightshade",
            "category": "ingredients",
            "type": "plant",
            "description": "Dark purple flower with magical properties",
            "tags": ["plant", "flower", "poison", "alchemy", "ingredient"],
            "effects": ["Damage Health", "Burden", "Damage Magicka", "Fortify Destruction"],
            "rarity": "common",
            "location_hint": "Found in shadowy areas and ruins"
        },
        {
            "name": "Mandrake Root",
            "category": "ingredients",
            "type": "plant",
            "description": "Valuable root used in powerful potions",
            "tags": ["plant", "root", "valuable", "alchemy", "ingredient"],
            "effects": ["Cure Disease", "Fortify Intelligence", "Damage Health", "Paralyze"],
            "rarity": "uncommon",
            "location_hint": "Grows in fertile soil near settlements"
        },
        {
            "name": "Daedra Heart",
            "category": "ingredients",
            "type": "organ",
            "description": "Heart of a daedric creature, extremely valuable",
            "tags": ["organ", "daedra", "heart", "valuable", "rare"],
            "effects": ["Restore Health", "Damage Magicka", "Damage Stamina", "Fear"],
            "rarity": "rare",
            "location_hint": "Only found when slaying powerful daedra"
        },
        {
            "name": "Vampire Dust",
            "category": "ingredients",
            "type": "remains",
            "description": "Ash remains of a destroyed vampire",
            "tags": ["remains", "vampire", "dust", "undead", "ingredient"],
            "effects": ["Resist Disease", "Invisibility", "Regenerate Health", "Cure Common Disease"],
            "rarity": "rare",
            "location_hint": "Obtained from defeated vampires"
        },
        {
            "name": "Glow Dust",
            "category": "ingredients",
            "type": "remains",
            "description": "Glowing powder from will-o-the-wisps",
            "tags": ["remains", "glow", "dust", "wisp", "magical"],
            "effects": ["Damage Magicka", "Light", "Reflect Spell", "Resist Shock"],
            "rarity": "uncommon",
            "location_hint": "Harvest from will-o-the-wisps in swamps"
        },
        {
            "name": "Black Pearl",
            "category": "ingredients",
            "type": "gem",
            "description": "Rare dark pearl with mystical properties",
            "tags": ["gem", "pearl", "black", "mystical", "water"],
            "effects": ["Water Breathing", "Resist Normal Weapons", "Water Walking", "Fortify Magicka"],
            "rarity": "rare",
            "location_hint": "Found in underwater caves and shipwrecks"
        },
        {
            "name": "Mort Flesh",
            "category": "ingredients",
            "type": "organ",
            "description": "Corrupted flesh from undead creatures",
            "tags": ["organ", "flesh", "undead", "corrupted", "evil"],
            "effects": ["Damage Health", "Damage Fatigue", "Burden", "Drain Intelligence"],
            "rarity": "uncommon",
            "location_hint": "Cut from zombies and other undead"
        },
        {
            "name": "Void Salts",
            "category": "ingredients",
            "type": "mineral",
            "description": "Crystalline salts from storm atronachs",
            "tags": ["mineral", "salts", "crystal", "storm", "atronach"],
            "effects": ["Shock Damage", "Dispel", "Cure Paralysis", "Silence"],
            "rarity": "uncommon",
            "location_hint": "Harvested from defeated storm atronachs"
        },
        {
            "name": "Fire Salts",
            "category": "ingredients",
            "type": "mineral",
            "description": "Burning crystalline salts from flame atronachs",
            "tags": ["mineral", "salts", "fire", "flame", "atronach"],
            "effects": ["Fire Damage", "Resist Frost", "Restore Fatigue", "Fire Shield"],
            "rarity": "uncommon",
            "location_hint": "Harvested from defeated flame atronachs"
        },
        {
            "name": "Frost Salts",
            "category": "ingredients",
            "type": "mineral",
            "description": "Frozen crystalline salts from frost atronachs",
            "tags": ["mineral", "salts", "frost", "ice", "atronach"],
            "effects": ["Frost Damage", "Resist Fire", "Silence", "Frost Shield"],
            "rarity": "uncommon",
            "location_hint": "Harvested from defeated frost atronachs"
        }
    ],
    
    "artifacts": [
        {
            "name": "Azura's Star",
            "category": "artifacts",
            "type": "soul_gem",
            "description": "Reusable soul gem of infinite capacity",
            "tags": ["artifact", "soul", "gem", "azura", "daedric", "infinite"],
            "effect": "Infinite soul capacity",
            "quest_related": True,
            "rarity": "artifact",
            "lore": "Gift of the Daedric Prince Azura"
        },
        {
            "name": "Skeleton Key",
            "category": "artifacts",
            "type": "lockpick",
            "description": "Unbreakable lockpick that opens any lock",
            "tags": ["artifact", "lockpick", "skeleton", "key", "thieves", "nocturnal"],
            "effect": "Opens any lock, never breaks",
            "quest_related": True,
            "rarity": "artifact",
            "lore": "Sacred relic of the Thieves Guild"
        },
        {
            "name": "Ring of Khajiiti",
            "category": "artifacts",
            "type": "jewelry",
            "description": "Ancient ring that grants invisibility and speed",
            "tags": ["artifact", "ring", "khajiit", "invisibility", "speed", "stealth"],
            "effect": "Invisibility and Fortify Speed",
            "quest_related": True,
            "rarity": "artifact",
            "lore": "Legendary treasure of the Khajiit people"
        },
        {
            "name": "Boots of Springheel Jak",
            "category": "artifacts",
            "type": "boots",
            "description": "Magical boots that enhance jumping ability",
            "tags": ["artifact", "boots", "jumping", "acrobatics", "thief", "legendary"],
            "effect": "Fortify Acrobatics 50 points",
            "quest_related": True,
            "rarity": "artifact",
            "lore": "Once worn by the legendary thief Springheel Jak"
        },
        {
            "name": "Cowl of Nocturnal",
            "category": "artifacts",
            "type": "helmet",
            "description": "Hood that grants stealth bonuses and detect life",
            "tags": ["artifact", "cowl", "nocturnal", "stealth", "detect", "thieves"],
            "effect": "Fortify Sneak, Detect Life",
            "quest_related": True,
            "rarity": "artifact",
            "lore": "Sacred artifact of the Thieves Guild"
        },
        {
            "name": "Amulet of Kings",
            "category": "artifacts",
            "type": "amulet",
            "description": "Imperial regalia worn by Dragonborn emperors",
            "tags": ["artifact", "amulet", "kings", "imperial", "dragonborn", "emperor"],
            "effect": "Unknown magical properties",
            "quest_related": True,
            "rarity": "artifact",
            "lore": "Symbol of the Dragonborn bloodline"
        },
        {
            "name": "Staff of Everscamp",
            "category": "artifacts",
            "type": "staff",
            "description": "Cursed staff that summons annoying scamps",
            "tags": ["artifact", "staff", "cursed", "scamp", "summon", "annoying"],
            "effect": "Continuously summons scamps",
            "quest_related": True,
            "rarity": "artifact",
            "lore": "A joke item created by mischievous daedra"
        }
    ],
    
    "jewelry": [
        {
            "name": "Ring of Burden",
            "category": "jewelry",
            "type": "ring",
            "description": "Cursed ring that increases carrying capacity but slows movement",
            "tags": ["ring", "burden", "cursed", "carry", "weight"],
            "effect": "Feather 100, Burden 50",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Amulet of Spell Absorption",
            "category": "jewelry",
            "type": "amulet",
            "description": "Absorbs hostile spells to restore magicka",
            "tags": ["amulet", "spell", "absorption", "magicka", "protection"],
            "effect": "Spell Absorption 25%",
            "enchantable": True,
            "rarity": "rare"
        },
        {
            "name": "Ring of Namira",
            "category": "jewelry",
            "type": "ring",
            "description": "Daedric artifact ring that reflects spells",
            "tags": ["ring", "namira", "daedric", "artifact", "reflect", "spell"],
            "effect": "Reflect Spell 25%",
            "quest_related": True,
            "rarity": "artifact"
        },
        {
            "name": "Necklace of Swords",
            "category": "jewelry",
            "type": "amulet",
            "description": "Enhances blade combat effectiveness",
            "tags": ["amulet", "swords", "blade", "combat", "warrior"],
            "effect": "Fortify Blade 10",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Ring of the Iron Fist",
            "category": "jewelry",
            "type": "ring",
            "description": "Increases hand-to-hand combat damage",
            "tags": ["ring", "iron", "fist", "hand", "combat", "monk"],
            "effect": "Fortify Hand to Hand 15",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Mundane Ring",
            "category": "jewelry",
            "type": "ring",
            "description": "Provides complete spell resistance but prevents spellcasting",
            "tags": ["ring", "mundane", "spell", "resistance", "anti", "magic"],
            "effect": "Resist Magic 100%, Silence",
            "enchantable": False,
            "rarity": "rare"
        }
    ],
    
    "shields": [
        {
            "name": "Iron Shield",
            "category": "shields",
            "type": "shield",
            "description": "Basic round shield for new warriors",
            "tags": ["shield", "iron", "basic", "protection", "warrior"],
            "skill_required": "Block",
            "enchantable": True,
            "rarity": "common"
        },
        {
            "name": "Steel Tower Shield",
            "category": "shields",
            "type": "shield",
            "description": "Large shield providing excellent protection",
            "tags": ["shield", "steel", "tower", "large", "protection"],
            "skill_required": "Block",
            "enchantable": True,
            "rarity": "common"
        },
        {
            "name": "Elven Shield",
            "category": "shields",
            "type": "shield",
            "description": "Lightweight elven crafted shield",
            "tags": ["shield", "elven", "light", "elegant", "protection"],
            "skill_required": "Block",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Dwarven Shield",
            "category": "shields",
            "type": "shield",
            "description": "Sturdy dwarven metal shield",
            "tags": ["shield", "dwarven", "sturdy", "metal", "protection"],
            "skill_required": "Block",
            "enchantable": True,
            "rarity": "uncommon"
        },
        {
            "name": "Glass Shield",
            "category": "shields",
            "type": "shield",
            "description": "Volcanic glass shield with superior protection",
            "tags": ["shield", "glass", "volcanic", "superior", "protection"],
            "skill_required": "Block",
            "enchantable": True,
            "rarity": "rare"
        },
        {
            "name": "Ebony Shield",
            "category": "shields",
            "type": "shield",
            "description": "Dark volcanic ebony shield",
            "tags": ["shield", "ebony", "volcanic", "dark", "protection"],
            "skill_required": "Block",
            "enchantable": True,
            "rarity": "rare"
        },
        {
            "name": "Daedric Shield",
            "category": "shields",
            "type": "shield",
            "description": "Terrifying shield forged in Oblivion",
            "tags": ["shield", "daedric", "evil", "terrifying", "ultimate"],
            "skill_required": "Block",
            "enchantable": True,
            "rarity": "legendary"
        },
        {
            "name": "Escutcheon of Chorrol",
            "category": "shields",
            "type": "shield",
            "description": "Enchanted shield that reflects spells",
            "tags": ["shield", "chorrol", "enchanted", "reflect", "spell"],
            "skill_required": "Block",
            "effect": "Reflect Spell 30%",
            "enchantable": False,
            "rarity": "rare"
        }
    ],
    
    "books": [
        {
            "name": "The Lusty Argonian Maid",
            "category": "books",
            "type": "literature",
            "description": "A popular romance novel throughout Tamriel",
            "tags": ["book", "literature", "romance", "argonian", "popular"],
            "skill_bonus": None,
            "rarity": "common",
            "value": "Entertainment"
        },
        {
            "name": "2920, The Last Year of the First Era",
            "category": "books",
            "type": "skill_book",
            "description": "Historical account that teaches illusion magic",
            "tags": ["book", "skill", "illusion", "history", "magic"],
            "skill_bonus": "Illusion",
            "rarity": "uncommon",
            "value": "Increases Illusion skill"
        },
        {
            "name": "The Armorer's Challenge",
            "category": "books",
            "type": "skill_book",
            "description": "Manual on armor repair and maintenance",
            "tags": ["book", "skill", "armorer", "repair", "maintenance"],
            "skill_bonus": "Armorer",
            "rarity": "uncommon",
            "value": "Increases Armorer skill"
        },
        {
            "name": "A Dance in Fire",
            "category": "books",
            "type": "skill_book",
            "description": "Adventure tale that teaches acrobatics",
            "tags": ["book", "skill", "acrobatics", "adventure", "agility"],
            "skill_bonus": "Acrobatics",
            "rarity": "uncommon",
            "value": "Increases Acrobatics skill"
        },
        {
            "name": "The Black Arts On Trial",
            "category": "books",
            "type": "skill_book",
            "description": "Dark tome teaching destruction magic",
            "tags": ["book", "skill", "destruction", "dark", "magic"],
            "skill_bonus": "Destruction",
            "rarity": "uncommon",
            "value": "Increases Destruction skill"
        },
        {
            "name": "Thief of Virtue",
            "category": "books",
            "type": "skill_book",
            "description": "Guide to stealth and sneaking techniques",
            "tags": ["book", "skill", "sneak", "stealth", "thief"],
            "skill_bonus": "Sneak",
            "rarity": "uncommon",
            "value": "Increases Sneak skill"
        },
        {
            "name": "The Wolf Queen",
            "category": "books",
            "type": "literature",
            "description": "Historical biography of Queen Potema",
            "tags": ["book", "literature", "history", "queen", "potema"],
            "skill_bonus": None,
            "rarity": "common",
            "value": "Historical knowledge"
        }
    ],
    
    "soul_gems": [
        {
            "name": "Petty Soul Gem",
            "category": "soul_gems",
            "type": "soul_container",
            "description": "Small gem that can hold weak souls",
            "tags": ["soul", "gem", "petty", "small", "enchanting"],
            "capacity": "Petty souls only",
            "uses": "Basic enchanting",
            "rarity": "common"
        },
        {
            "name": "Lesser Soul Gem",
            "category": "soul_gems",
            "type": "soul_container",
            "description": "Medium gem for moderate souls",
            "tags": ["soul", "gem", "lesser", "medium", "enchanting"],
            "capacity": "Lesser souls and below",
            "uses": "Moderate enchanting",
            "rarity": "common"
        },
        {
            "name": "Common Soul Gem",
            "category": "soul_gems",
            "type": "soul_container",
            "description": "Standard gem for average souls",
            "tags": ["soul", "gem", "common", "standard", "enchanting"],
            "capacity": "Common souls and below",
            "uses": "Standard enchanting",
            "rarity": "common"
        },
        {
            "name": "Greater Soul Gem",
            "category": "soul_gems",
            "type": "soul_container",
            "description": "Large gem for powerful souls",
            "tags": ["soul", "gem", "greater", "large", "enchanting"],
            "capacity": "Greater souls and below",
            "uses": "Powerful enchanting",
            "rarity": "uncommon"
        },
        {
            "name": "Grand Soul Gem",
            "category": "soul_gems",
            "type": "soul_container",
            "description": "Massive gem for the most powerful souls",
            "tags": ["soul", "gem", "grand", "massive", "enchanting"],
            "capacity": "Grand souls and below",
            "uses": "Ultimate enchanting",
            "rarity": "rare"
        },
        {
            "name": "Black Soul Gem",
            "category": "soul_gems",
            "type": "soul_container",
            "description": "Forbidden gem that can capture humanoid souls",
            "tags": ["soul", "gem", "black", "forbidden", "humanoid"],
            "capacity": "Black souls (humanoid)",
            "uses": "Necromantic enchanting",
            "rarity": "rare"
        }
    ],
    
    "miscellaneous": [
        {
            "name": "Lockpick",
            "category": "miscellaneous",
            "type": "tool",
            "description": "Basic tool for opening locks",
            "tags": ["lockpick", "tool", "thief", "security", "unlock"],
            "uses": "Opens locks, breaks on failure",
            "skill_required": "Security",
            "rarity": "common"
        },
        {
            "name": "Repair Hammer",
            "category": "miscellaneous",
            "type": "tool",
            "description": "Tool for repairing weapons and armor",
            "tags": ["repair", "hammer", "tool", "maintenance", "armorer"],
            "uses": "Repairs equipment condition",
            "skill_required": "Armorer",
            "rarity": "common"
        },
        {
            "name": "Mortar and Pestle",
            "category": "miscellaneous",
            "type": "tool",
            "description": "Alchemy equipment for brewing potions",
            "tags": ["mortar", "pestle", "alchemy", "brewing", "tool"],
            "uses": "Required for advanced potion making",
            "skill_required": "Alchemy",
            "rarity": "common"
        },
        {
            "name": "Alembic",
            "category": "miscellaneous",
            "type": "tool",
            "description": "Advanced alchemy apparatus",
            "tags": ["alembic", "alchemy", "apparatus", "advanced", "tool"],
            "uses": "Improves potion quality",
            "skill_required": "Alchemy",
            "rarity": "uncommon"
        },
        {
            "name": "Calcinater",
            "category": "miscellaneous",
            "type": "tool",
            "description": "Heating device for alchemy",
            "tags": ["calcinater", "alchemy", "heating", "device", "tool"],
            "uses": "Enhances potion effects",
            "skill_required": "Alchemy",
            "rarity": "uncommon"
        },
        {
            "name": "Retort",
            "category": "miscellaneous",
            "type": "tool",
            "description": "Distillation equipment for master alchemists",
            "tags": ["retort", "alchemy", "distillation", "master", "tool"],
            "uses": "Creates the finest potions",
            "skill_required": "Alchemy",
            "rarity": "rare"
        },
        {
            "name": "Torch",
            "category": "miscellaneous",
            "type": "light",
            "description": "Provides light in dark places",
            "tags": ["torch", "light", "fire", "illumination", "utility"],
            "uses": "Lights dark areas",
            "duration": "240 seconds",
            "rarity": "common"
        },
        {
            "name": "Varla Stone",
            "category": "miscellaneous",
            "type": "magical_item",
            "description": "Ancient welkynd stone that recharges magical items",
            "tags": ["varla", "stone", "magical", "recharge", "ancient"],
            "uses": "Fully recharges enchanted items",
            "rarity": "rare",
            "location_hint": "Found in Ayleid ruins"
        },
        {
            "name": "Welkynd Stone",
            "category": "miscellaneous",
            "type": "magical_item",
            "description": "Glowing stone that restores magicka",
            "tags": ["welkynd", "stone", "magical", "magicka", "restore"],
            "uses": "Restores magicka when used",
            "effect": "Restore Magicka 150",
            "rarity": "uncommon",
            "location_hint": "Found in Ayleid ruins"
        },
        {
            "name": "Paintbrush",
            "category": "miscellaneous",
            "type": "quest_item",
            "description": "Magical paintbrush with unusual properties",
            "tags": ["paintbrush", "magical", "quest", "unusual", "floating"],
            "uses": "Quest item with physics glitch properties",
            "rarity": "unique",
            "special_note": "Can be used for creative movement exploits"
        }
    ]
}