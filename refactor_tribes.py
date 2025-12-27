import json
import os

file_path = 'flare_quills_data.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

characters = data['flare_quills']

for char in characters:
    tribe = char.get('tribe')
    element = char.get('element', '')
    occupation = char.get('occupation', '')

    # Default Region
    region = "Unknown"

    # --- MAPPING LOGIC (13-Region Structure) ---

    # 1. Normalize Old/Generic Tribes first
    if tribe == "Stone Keepers": tribe = "Crystalline Guard" 
    if tribe == "Desert Suns": tribe = "Sun-Scorched Nomads"
    if tribe == "The Crossroads": tribe = "Verdant Circle"

    # 2. SUBDIVISIONS & RE-CLASSIFICATION

    # Cybernetic Front Split: Kitchen vs Factory
    if tribe == "Cybernetic Front" or "Tech" in element or "Steel" in element:
        if any(x in occupation for x in ["Chef", "Cook", "Baker", "Brewer", "Appliance", "Vendor", "Cleaner"]) or \
           any(x in char.get('origin_story', '') for x in ["kitchen", "culinary", "feast", "snack", "coffee", "toaster"]):
            tribe = "Culinary Corps"
        else:
            tribe = "Iron Legion"

    # Inferno Split: Volcano vs Desert
    if tribe == "Inferno Legion" or "Fire" in element:
        if "Sand" in element or "Desert" in char.get('origin_story', '') or "Dune" in char.get('origin_story', ''):
             tribe = "Sun-Scorched Nomads"
        else:
             tribe = "Inferno Legion"

    # Shadow Split: Swamp vs Mushroom
    if tribe == "Shadow Cabal" or "Poison" in element or "Dark" in element:
        if "Mushroom" in char.get('origin_story', '') or "Fungi" in char.get('origin_story', '') or "Spore" in char.get('origin_story', ''):
            tribe = "Fungal Colony"
        else:
            tribe = "Shadow Cabal"

    # Highborn Split: Royalty vs Wizards
    if tribe == "Highborn Court" or "Light" in element or "Magic" in element:
        if any(x in occupation for x in ["King", "Queen", "Prince", "Princess", "Royal", "Sovereign", "Knight", "Noble"]):
            tribe = "Highborn Court"
        elif any(x in occupation for x in ["Wizard", "Mage", "Warlock", "Sorcerer", "Spirit", "Apprentice"]):
            tribe = "Mystic Enclave"
        else:
            # Default for misc magic/light
            tribe = "Highborn Court"

    # 3. Handle "Cultural Mosaic" / "Mercenaries" Catch-all
    if tribe == "Cultural Mosaic" or tribe == "Mercenaries":
        if "Water" in element or "Ice" in element: tribe = "Tideborn Covenant"
        elif "Electric" in element or "Wind" in element: tribe = "Storm Vanguard"
        elif "Nature" in element or "Wood" in element: tribe = "Verdant Circle"
        elif "Crystal" in element or "Earth" in element: tribe = "Crystalline Guard"
        elif "Time" in element: tribe = "Prisoner's Circle"
        else: tribe = "Verdant Circle" # Ultimate fallback

    # 4. Specific Overrides
    if "Dead Cells" in char.get('origin_story', '') or "Time" in element:
        tribe = "Prisoner's Circle"
    
    # Void Gastronomes (New Region 14)
    if "Squid" in char.get('origin_story', '') or "Void" in char.get('origin_story', '') or "Nether" in char.get('origin_story', ''):
        tribe = "Void Gastronomes"

    # --- ASSIGN REGION BASED ON FINAL TRIBE (14 Zones) ---
    region_map = {
        "Inferno Legion": "Volcanic Wastes",
        "Sun-Scorched Nomads": "Sun-Bleached Dunes",
        "Shadow Cabal": "Venomous Swamplands",
        "Fungal Colony": "Mushroom Forest",
        "Crystalline Guard": "Geode Caverns",
        "Highborn Court": "Gilded Spire",
        "Mystic Enclave": "Arcane Sanctum",
        "Prisoner's Circle": "The Black Bridge",
        "Storm Vanguard": "Thunder Peaks",
        "Iron Legion": "Ironworks",
        "Culinary Corps": "Gourmet Galley",
        "Tideborn Covenant": "Frozen Fjords",
        "Verdant Circle": "Emerald Grove",
        "Void Gastronomes": "Crimson Coast"
    }

    region = region_map.get(tribe, "Unknown Region")
    
    char['tribe'] = tribe
    char['region'] = region

# Save back
data['flare_quills'] = characters
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Data refactored successfully.")
