# BuildCraft AI - Data Scraping

This directory contains the data scraping and processing tools for BuildCraft AI.

## Overview

The data scraping system extracts game information from the UESP (Unofficial Elder Scrolls Pages) wiki to provide comprehensive data for the AI build generation system.

## Files

- `src/oblivion/scraper.py` - Main scraping script for Oblivion data
- `src/oblivion/processor.py` - Data cleaning and validation processor
- `requirements.txt` - Python dependencies
- `oblivion/` - Output directory for scraped data

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Run the scraper:
```bash
cd src/oblivion
python scraper.py
```

3. Process the data:
```bash
python processor.py
```

## Data Types Scraped

### Skills
- All 21 Oblivion skills
- Governing attributes
- Specializations (Combat, Magic, Stealth)
- Skill categories for AI classification

### Items
- Weapons (swords, bows, etc.)
- Armor (light, heavy, shields)
- Potions and alchemical ingredients
- Clothing and accessories

### Spells
- Spell names and schools
- Magnitude, duration, area, cost
- Spell effects and descriptions

### Perks
- Skill-specific perks and abilities
- Mastery bonuses
- Special abilities

## Output Files

- `oblivion_data.json` - Raw scraped data
- `oblivion_processed.json` - Cleaned and validated data

## Usage in BuildCraft AI

The processed data is used by:
1. The backend API for build generation
2. Vector database for semantic search
3. AI model training and fine-tuning

## Ethical Considerations

- Respectful scraping with delays between requests
- Educational use only
- Proper attribution to UESP wiki
- No commercial redistribution of scraped data

## Future Enhancements

- Support for other Elder Scrolls games
- Real-time data updates
- Enhanced spell and item descriptions
- Quest and location data 