#!/usr/bin/env python3
"""
Data Validation Script for BuildCraft AI
Validates the processed Oblivion data for quality and completeness
"""

import json
from typing import Dict, List, Any

def validate_data_structure(data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate the structure and quality of processed data"""
    validation_results = {
        "total_items": 0,
        "categories": {},
        "quality_issues": [],
        "structure_valid": True
    }
    
    # Check required categories
    required_categories = ["skills", "weapons", "armor", "potions", "perks", "spells", "metadata"]
    
    for category in required_categories:
        if category not in data:
            validation_results["quality_issues"].append(f"Missing category: {category}")
            validation_results["structure_valid"] = False
        else:
            if category == "metadata":
                # Metadata should be a dictionary, not a list
                if not isinstance(data[category], dict):
                    validation_results["quality_issues"].append(f"Category {category} should be a dictionary")
            elif isinstance(data[category], list):
                count = len(data[category])
                validation_results["categories"][category] = count
                validation_results["total_items"] += count
            else:
                validation_results["quality_issues"].append(f"Category {category} is not a list")
    
    # Validate individual items
    for category, items in data.items():
        if isinstance(items, list):
            for i, item in enumerate(items):
                if not isinstance(item, dict):
                    validation_results["quality_issues"].append(f"Item {i} in {category} is not a dictionary")
                    continue
                
                # Check for required fields based on type
                if category == "skills":
                    if "name" not in item:
                        validation_results["quality_issues"].append(f"Skill {i} missing name")
                elif category in ["weapons", "armor", "potions"]:
                    if "name" not in item:
                        validation_results["quality_issues"].append(f"{category[:-1]} {i} missing name")
                elif category == "spells":
                    if "name" not in item:
                        validation_results["quality_issues"].append(f"Spell {i} missing name")
    
    return validation_results

def print_validation_report(results: Dict[str, Any]):
    """Print a formatted validation report"""
    print("=== Data Validation Report ===")
    print(f"Total items: {results['total_items']}")
    print(f"Structure valid: {results['structure_valid']}")
    
    print("\nCategory breakdown:")
    for category, count in results["categories"].items():
        print(f"  {category.capitalize()}: {count} items")
    
    if results["quality_issues"]:
        print(f"\nQuality issues found: {len(results['quality_issues'])}")
        for issue in results["quality_issues"][:10]:  # Show first 10 issues
            print(f"  - {issue}")
        if len(results["quality_issues"]) > 10:
            print(f"  ... and {len(results['quality_issues']) - 10} more issues")
    else:
        print("\nNo quality issues found!")

def main():
    """Main validation function"""
    try:
        # Load processed data
        with open("../../oblivion/oblivion_processed.json", 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Validate data
        results = validate_data_structure(data)
        
        # Print report
        print_validation_report(results)
        
        # Return success/failure
        if results["structure_valid"] and not results["quality_issues"]:
            print("\n✅ Data validation PASSED")
            return True
        else:
            print("\n❌ Data validation FAILED")
            return False
            
    except FileNotFoundError:
        print("❌ Processed data file not found. Please run the scraper and processor first.")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    main() 