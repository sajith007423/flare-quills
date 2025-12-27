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

    # --- MAPPING LOGIC ---

    # 1. Normalize Existing Tribes
    if tribe == "Stone Keepers":
        tribe = "Crystalline Guard" 
    elif tribe == "Desert Suns":
        tribe = "Inferno Legion" # Merge desert into volcano for now, or maybe Highborn? Let's go Inferno (hot).
    elif tribe == "The Crossroads":
        tribe = "Verdant Circle" # Default to nature/neutral

    # 2. Handle "Cultural Mosaic" (The catch-all that needs splitting)
    if tribe == "Cultural Mosaic" or tribe == "Mercenaries":
        if "Water" in element or "Ice" in element:
            tribe = "Tideborn Covenant"
        elif "Electric" in element or "Wind" in element or "Air" in element or "Sound" in element:
            tribe = "Storm Vanguard"
        elif "Nature" in element or "Wood" in element:
            tribe = "Verdant Circle"
        elif "Fire" in element:
            tribe = "Inferno Legion"
        elif "Poison" in element or "Dark" in element or "Necro" in element:
            tribe = "Shadow Cabal"
        elif "Tech" in element or "Steel" in element:
            tribe = "Cybernetic Front"
        elif "Crystal" in element or "Earth" in element or "Sand" in element:
            tribe = "Crystalline Guard" 
        elif "Light" in element or "Royal" in element or "God" in element:
            tribe = "Highborn Court"
        elif "Magic" in element:
            tribe = "Highborn Court" # Magic fits highborn
        else:
            tribe = "Verdant Circle" # Fallback for musicians/bards -> Nature/Hippie vibe

    # 3. Special Case Overrides (Prisoner's Circle specific themes)
    if "Dead Cells" in char.get('origin_story', '') or "Time" in element:
        tribe = "Prisoner's Circle"

    # --- ASSIGN REGION BASED ON FINAL TRIBE ---
    if tribe == "Inferno Legion":
        region = "Volcanic Wastes"
    elif tribe == "Shadow Cabal":
        region = "Venomous Swamplands"
    elif tribe == "Crystalline Guard":
        region = "Geode Caverns"
    elif tribe == "Highborn Court":
        region = "Gilded Spire"
    elif tribe == "Prisoner's Circle":
        region = "The Black Bridge"
    elif tribe == "Storm Vanguard":
        region = "Thunder Peaks"
    elif tribe == "Cybernetic Front":
        region = "Ironworks"
    elif tribe == "Tideborn Covenant":
        region = "Frozen Fjords"
    elif tribe == "Verdant Circle":
        region = "Emerald Grove"
    elif tribe == "Mystic Enclave": # If any remain, merge them
         tribe = "Highborn Court"
         region = "Gilded Spire"
    else:
        # Final Catch-all if something slipped through
        tribe = "Verdant Circle"
        region = "Emerald Grove"

    char['tribe'] = tribe
    char['region'] = region

# Save back
data['flare_quills'] = characters
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Data refactored successfully.")
