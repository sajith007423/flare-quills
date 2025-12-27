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

    # Refactoring Rules
    if tribe == "Inferno Legion":
        region = "Volcanic Wastes"
    
    elif tribe == "Shadow Cabal":
        region = "Venomous Swamplands"
    
    elif tribe == "Stone Keepers":
        char['tribe'] = "Crystalline Guard"
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
        
    elif tribe == "Cultural Mosaic":
        if "Nature" in element or "Wood" in element:
            char['tribe'] = "Verdant Circle"
            region = "Emerald Grove"
        elif any(x in occupation for x in ["Wizard", "Mage", "Warlock", "Spirit", "Alchemist", "Apprentice"]):
             # Move magic users to Mystic Enclave
             char['tribe'] = "Mystic Enclave"
             region = "Arcane Sanctum"
        elif "Sand" in element:
             char['tribe'] = "Desert Suns"
             region = "Sun-Bleached Dunes"
        else:
            region = "The Crossroads"
            
    # New Tribes Logic (for new characters that might not have old tribes or need shifting)
    # Check Dead Cells specific if mistakenly placed
    if "Time" in element or "Dead Cells" in char.get('origin_story', ''):
        char['tribe'] = "Prisoner's Circle"
        region = "The Black Bridge"

    # Explicit Overrides for recent Adds if they kept old tribes
    if char.get('id') in ["11.png", "71.png", "74.png", "75.png", "76.png"]: # Crystal types
        char['tribe'] = "Crystalline Guard"
        region = "Geode Caverns"

    char['region'] = region

# Save back
data['flare_quills'] = characters
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Data refactored successfully.")
