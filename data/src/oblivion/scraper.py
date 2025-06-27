#!/usr/bin/env python3
"""
Oblivion Data Scraper for BuildCraft AI
Scrapes skills, perks, items, and other game data from UESP wiki
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import re
from typing import Dict, List, Any
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class OblivionScraper:
    def __init__(self):
        self.base_url = "https://en.uesp.net"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'BuildCraft-AI-Scraper/1.0 (Educational Project)'
        })
        
    def get_page(self, url: str) -> BeautifulSoup:
        """Fetch and parse a web page"""
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None

    def scrape_skills(self) -> List[Dict[str, Any]]:
        """Scrape all Oblivion skills"""
        logger.info("Scraping skills...")
        url = f"{self.base_url}/wiki/Oblivion:Skills"
        soup = self.get_page(url)
        
        if not soup:
            return []
        
        skills = []
        # Find the skills table
        tables = soup.find_all('table', class_='wikitable')
        
        for table in tables:
            rows = table.find_all('tr')[1:]  # Skip header row
            for row in rows:
                cells = row.find_all(['td', 'th'])
                if len(cells) >= 3:
                    skill_name = cells[0].get_text(strip=True)
                    governing_attribute = cells[1].get_text(strip=True)
                    specialization = cells[2].get_text(strip=True)
                    
                    if skill_name and skill_name != "Skill":
                        skills.append({
                            "name": skill_name,
                            "governing_attribute": governing_attribute,
                            "specialization": specialization,
                            "type": "skill"
                        })
        
        logger.info(f"Scraped {len(skills)} skills")
        return skills

    def scrape_items(self, item_type: str = "weapons") -> List[Dict[str, Any]]:
        """Scrape items by type (weapons, armor, etc.)"""
        logger.info(f"Scraping {item_type}...")
        
        # Define item type URLs
        item_urls = {
            "weapons": f"{self.base_url}/wiki/Oblivion:Weapons",
            "armor": f"{self.base_url}/wiki/Oblivion:Armor",
            "clothing": f"{self.base_url}/wiki/Oblivion:Clothing",
            "potions": f"{self.base_url}/wiki/Oblivion:Potions",
            "scrolls": f"{self.base_url}/wiki/Oblivion:Scrolls"
        }
        
        url = item_urls.get(item_type)
        if not url:
            logger.error(f"Unknown item type: {item_type}")
            return []
        
        soup = self.get_page(url)
        if not soup:
            return []
        
        items = []
        # Look for item tables
        tables = soup.find_all('table', class_='wikitable')
        
        for table in tables:
            rows = table.find_all('tr')[1:]  # Skip header
            for row in rows:
                cells = row.find_all(['td', 'th'])
                if len(cells) >= 2:
                    item_name = cells[0].get_text(strip=True)
                    if item_name and item_name != "Name":
                        item_data = {
                            "name": item_name,
                            "type": item_type,
                            "category": item_type
                        }
                        
                        # Try to extract additional properties
                        if len(cells) > 1:
                            item_data["properties"] = {}
                            for i, cell in enumerate(cells[1:], 1):
                                text = cell.get_text(strip=True)
                                if text:
                                    item_data["properties"][f"property_{i}"] = text
                        
                        items.append(item_data)
        
        logger.info(f"Scraped {len(items)} {item_type}")
        return items

    def scrape_perks(self) -> List[Dict[str, Any]]:
        """Scrape skill perks and abilities"""
        logger.info("Scraping perks...")
        url = f"{self.base_url}/wiki/Oblivion:Skills"
        soup = self.get_page(url)
        
        if not soup:
            return []
        
        perks = []
        # Look for perk information in skill descriptions
        skill_links = soup.find_all('a', href=re.compile(r'/wiki/Oblivion:.*_Skill'))
        
        for link in skill_links[:5]:  # Limit to first 5 skills for demo
            skill_url = self.base_url + link['href']
            skill_soup = self.get_page(skill_url)
            
            if skill_soup:
                skill_name = link.get_text(strip=True)
                
                # Look for perk information
                perk_sections = skill_soup.find_all(['h2', 'h3'], string=re.compile(r'Perk|Ability|Mastery'))
                
                for section in perk_sections:
                    next_elem = section.find_next_sibling()
                    if next_elem:
                        perk_text = next_elem.get_text(strip=True)
                        if perk_text:
                            perks.append({
                                "name": f"{skill_name} - {section.get_text(strip=True)}",
                                "skill": skill_name,
                                "description": perk_text,
                                "type": "perk"
                            })
            
            time.sleep(1)  # Be respectful to the server
        
        logger.info(f"Scraped {len(perks)} perks")
        return perks

    def scrape_spells(self) -> List[Dict[str, Any]]:
        """Scrape spell information"""
        logger.info("Scraping spells...")
        url = f"{self.base_url}/wiki/Oblivion:Spells"
        soup = self.get_page(url)
        
        if not soup:
            return []
        
        spells = []
        # Look for spell tables
        tables = soup.find_all('table', class_='wikitable')
        
        for table in tables:
            rows = table.find_all('tr')[1:]  # Skip header
            for row in rows:
                cells = row.find_all(['td', 'th'])
                if len(cells) >= 2:
                    spell_name = cells[0].get_text(strip=True)
                    if spell_name and spell_name != "Name":
                        spell_data = {
                            "name": spell_name,
                            "type": "spell"
                        }
                        
                        # Extract spell properties
                        if len(cells) > 1:
                            spell_data["school"] = cells[1].get_text(strip=True) if len(cells) > 1 else ""
                            spell_data["magnitude"] = cells[2].get_text(strip=True) if len(cells) > 2 else ""
                            spell_data["duration"] = cells[3].get_text(strip=True) if len(cells) > 3 else ""
                            spell_data["area"] = cells[4].get_text(strip=True) if len(cells) > 4 else ""
                            spell_data["cost"] = cells[5].get_text(strip=True) if len(cells) > 5 else ""
                        
                        spells.append(spell_data)
        
        logger.info(f"Scraped {len(spells)} spells")
        return spells

    def scrape_all_data(self) -> Dict[str, Any]:
        """Scrape all Oblivion data"""
        logger.info("Starting comprehensive Oblivion data scraping...")
        
        data = {
            "skills": self.scrape_skills(),
            "weapons": self.scrape_items("weapons"),
            "armor": self.scrape_items("armor"),
            "potions": self.scrape_items("potions"),
            "perks": self.scrape_perks(),
            "spells": self.scrape_spells(),
            "metadata": {
                "scraped_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "source": "UESP Wiki",
                "version": "1.0"
            }
        }
        
        logger.info("Data scraping completed!")
        return data

    def save_data(self, data: Dict[str, Any], filename: str = "oblivion_data.json"):
        """Save scraped data to JSON file"""
        output_path = f"../../oblivion/{filename}"
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info(f"Data saved to {output_path}")
        except Exception as e:
            logger.error(f"Error saving data: {e}")

def main():
    """Main function to run the scraper"""
    scraper = OblivionScraper()
    
    # Scrape all data
    data = scraper.scrape_all_data()
    
    # Save to file
    scraper.save_data(data)
    
    # Print summary
    print("\n=== Scraping Summary ===")
    for category, items in data.items():
        if isinstance(items, list):
            print(f"{category.capitalize()}: {len(items)} items")
    
    print(f"\nTotal data points: {sum(len(items) for items in data.values() if isinstance(items, list))}")

if __name__ == "__main__":
    main() 