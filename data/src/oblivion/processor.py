#!/usr/bin/env python3
"""
Oblivion Data Processor for BuildCraft AI
Processes and validates scraped data for use in the AI system
"""

import json
import re
from typing import Dict, List, Any, Optional
import logging

logger = logging.getLogger(__name__)

class OblivionDataProcessor:
    def __init__(self):
        self.skill_categories = {
            "combat": ["Blade", "Blunt", "Hand to Hand", "Marksman", "Block", "Heavy Armor", "Light Armor"],
            "magic": ["Alteration", "Conjuration", "Destruction", "Illusion", "Mysticism", "Restoration"],
            "stealth": ["Acrobatics", "Athletics", "Light Armor", "Marksman", "Mercantile", "Sneak", "Speechcraft"],
            "crafting": ["Alchemy", "Armorer", "Enchant", "Mercantile", "Security"]
        }
        
    def load_data(self, filename: str = "oblivion_data.json") -> Dict[str, Any]:
        """Load scraped data from JSON file"""
        try:
            with open(f"data/oblivion/{filename}", 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Data file {filename} not found")
            return {}
        except json.JSONDecodeError as e:
            logger.error(f"Error parsing JSON: {e}")
            return {}

    def clean_text(self, text: str) -> str:
        """Clean and normalize text data"""
        if not text:
            return ""
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text.strip())
        
        # Remove special characters that might cause issues
        text = re.sub(r'[^\w\s\-\.\,\!\?\(\)]', '', text)
        
        return text

    def validate_skill(self, skill: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Validate and clean skill data"""
        if not skill.get("name"):
            return None
            
        cleaned_skill = {
            "name": self.clean_text(skill["name"]),
            "governing_attribute": self.clean_text(skill.get("governing_attribute", "")),
            "specialization": self.clean_text(skill.get("specialization", "")),
            "type": "skill"
        }
        
        # Determine skill category
        for category, skills in self.skill_categories.items():
            if cleaned_skill["name"] in skills:
                cleaned_skill["category"] = category
                break
        else:
            cleaned_skill["category"] = "other"
        
        return cleaned_skill

    def validate_item(self, item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Validate and clean item data"""
        if not item.get("name"):
            return None
            
        cleaned_item = {
            "name": self.clean_text(item["name"]),
            "type": item.get("type", "unknown"),
            "category": item.get("category", "unknown")
        }
        
        # Clean properties
        if "properties" in item:
            cleaned_properties = {}
            for key, value in item["properties"].items():
                cleaned_value = self.clean_text(str(value))
                if cleaned_value:
                    cleaned_properties[key] = cleaned_value
            cleaned_item["properties"] = cleaned_properties
        
        return cleaned_item

    def validate_spell(self, spell: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Validate and clean spell data"""
        if not spell.get("name"):
            return None
            
        cleaned_spell = {
            "name": self.clean_text(spell["name"]),
            "type": "spell",
            "school": self.clean_text(spell.get("school", "")),
            "magnitude": self.clean_text(spell.get("magnitude", "")),
            "duration": self.clean_text(spell.get("duration", "")),
            "area": self.clean_text(spell.get("area", "")),
            "cost": self.clean_text(spell.get("cost", ""))
        }
        
        return cleaned_spell

    def validate_perk(self, perk: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Validate and clean perk data"""
        if not perk.get("name") or not perk.get("description"):
            return None
            
        cleaned_perk = {
            "name": self.clean_text(perk["name"]),
            "skill": self.clean_text(perk.get("skill", "")),
            "description": self.clean_text(perk["description"]),
            "type": "perk"
        }
        
        return cleaned_perk

    def process_data(self, raw_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process and validate all scraped data"""
        logger.info("Processing scraped data...")
        
        processed_data = {
            "skills": [],
            "weapons": [],
            "armor": [],
            "potions": [],
            "perks": [],
            "spells": [],
            "metadata": raw_data.get("metadata", {})
        }
        
        # Process skills
        for skill in raw_data.get("skills", []):
            cleaned_skill = self.validate_skill(skill)
            if cleaned_skill:
                processed_data["skills"].append(cleaned_skill)
        
        # Process items
        for item_type in ["weapons", "armor", "potions"]:
            for item in raw_data.get(item_type, []):
                cleaned_item = self.validate_item(item)
                if cleaned_item:
                    processed_data[item_type].append(cleaned_item)
        
        # Process spells
        for spell in raw_data.get("spells", []):
            cleaned_spell = self.validate_spell(spell)
            if cleaned_spell:
                processed_data["spells"].append(cleaned_spell)
        
        # Process perks
        for perk in raw_data.get("perks", []):
            cleaned_perk = self.validate_perk(perk)
            if cleaned_perk:
                processed_data["perks"].append(cleaned_perk)
        
        # Add processing metadata
        processed_data["metadata"]["processed_at"] = self.get_timestamp()
        processed_data["metadata"]["total_items"] = sum(len(items) for items in processed_data.values() if isinstance(items, list))
        
        logger.info(f"Processed {processed_data['metadata']['total_items']} total items")
        return processed_data

    def get_timestamp(self) -> str:
        """Get current timestamp"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def save_processed_data(self, data: Dict[str, Any], filename: str = "oblivion_processed.json"):
        """Save processed data to JSON file"""
        output_path = f"data/oblivion/{filename}"
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info(f"Processed data saved to {output_path}")
        except Exception as e:
            logger.error(f"Error saving processed data: {e}")

    def generate_summary(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate summary statistics for the processed data"""
        summary = {
            "total_items": data["metadata"]["total_items"],
            "categories": {}
        }
        
        for category, items in data.items():
            if isinstance(items, list):
                summary["categories"][category] = len(items)
        
        return summary

def main():
    """Main function to process scraped data"""
    processor = OblivionDataProcessor()
    
    # Load raw data
    raw_data = processor.load_data()
    if not raw_data:
        print("No data to process. Please run the scraper first.")
        return
    
    # Process data
    processed_data = processor.process_data(raw_data)
    
    # Save processed data
    processor.save_processed_data(processed_data)
    
    # Generate and print summary
    summary = processor.generate_summary(processed_data)
    print("\n=== Processing Summary ===")
    print(f"Total items processed: {summary['total_items']}")
    for category, count in summary['categories'].items():
        print(f"{category.capitalize()}: {count} items")

if __name__ == "__main__":
    main() 