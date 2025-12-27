import json
import re

def get_tribe_and_region(char):
    name = char.get("name", "")
    story = char.get("origin_story", "")
    element = char.get("element", "")
    
    # Combined text for searching
    text = (name + " " + story + " " + element).lower()

    # --- SPECIFIC TRIBE LOGIC ---
    
    # 1. Void Gastronomes (Void, Steak context, Crimson)
    if any(x in text for x in ["void", "nether", "crimson", "abyssal captain", "soul-flame"]):
        return "Void Gastronomes", "Crimson Coast"

    # 2. Culinary Corps (Food, Chef, Bavarian, Appliance)
    if any(x in text for x in ["chef", "cook", "food", "steak", "bavarian", "oktober", "gourmet", "kitchen", "galley", "appliance", "bot", "blender", "toaster"]):
        return "Culinary Corps", "Gourmet Galley"

    # 3. Sun-Scorched Nomads (Desert, Pharaoh, Sand)
    if any(x in text for x in ["pharaoh", "desert", "sand", "dune", "pyramid", "mummy", "ankh"]):
        return "Sun-Scorched Nomads", "Sun-Bleached Dunes"

    # 4. Fungal Colony (Mushroom, Spore)
    if any(x in text for x in ["mushroom", "spore", "fungal", "fungus", "mycelium"]):
        return "Fungal Colony", "Mushroom Forest"
    
    # 5. Prisoner's Circle (Prisoner, Chain, Dead Cells)
    if any(x in text for x in ["prisoner", "chain", "dead cells", "shackle", "captive"]):
        return "Prisoner's Circle", "The Black Bridge"

    # 6. Iron Legion (Tech, Space, Cyber, Robot, Factory)
    if any(x in text for x in ["tech", "cyborg", "robot", "marine", "space", "laser", "plasma", "iron", "factory", "gear"]):
        return "Iron Legion", "Ironworks"

    # 7. Storm Vanguard (Electric, Storm, Thunder, Music, Wind)
    if any(x in text for x in ["electric", "storm", "thunder", "lightning", "music", "bard", "sonic", "voltage", "zap"]):
        return "Storm Vanguard", "Thunder Peaks"

    # 8. Highborn Court (Light, Angel, Holy, Gold, Royal)
    if any(x in text for x in ["light", "angel", "holy", "divine", "gold", "royal", "queen", "king", "prince", "throne"]):
        # Note: 'King' might conflict with Ice King. Check element.
        if "ice" not in text and "frost" not in text:
             return "Highborn Court", "Gilded Spire"

    # 9. Mystic Enclave (Magic, Wizard, Arcane)
    if any(x in text for x in ["magic", "wizard", "mage", "arcane", "spell", "sorcer"]):
         if "ice" not in text and "water" not in text and "fire" not in text: # Pure magic
             return "Mystic Enclave", "Arcane Sanctum"
         if "spark" in text: # Spark Mage -> Storm
             return "Storm Vanguard", "Thunder Peaks"
         if "splash" in text:
             return "Tideborn Covenant", "Frozen Fjords"

    # 10. Verdant Circle (Nature, Wood, Plant)
    if any(x in text for x in ["nature", "wood", "plant", "tree", "forest", "druid", "leaf", "verdant"]):
        return "Verdant Circle", "Emerald Grove"

    # 11. Tideborn Covenant (Ice, Water, Frozen, Snow)
    if any(x in text for x in ["ice", "water", "frozen", "snow", "frost", "cold", "blizzard", "tide", "ocean", "sea"]):
        return "Tideborn Covenant", "Frozen Fjords"

    # 12. Crystalline Guard (Crystal, Geode, Earth, Stone)
    if any(x in text for x in ["crystal", "geode", "gem", "stone", "rock", "earth", "golem", "miner"]):
        return "Crystalline Guard", "Geode Caverns"

    # 13. Shadow Cabal (Poison, Dark, Shadow)
    if any(x in text for x in ["poison", "toxic", "shadow", "dark", "necrom", "swamp", "venom", "undead", "skull"]):
        return "Shadow Cabal", "Venomous Swamplands"
    
    # 14. Inferno Legion (Fire, Lava, Magma) - Fallback for fire types
    if any(x in text for x in ["fire", "lava", "magma", "burn", "flame", "pyro", "ignis"]):
         return "Inferno Legion", "Volcanic Wastes"

    return "Unknown Tribe", "Unknown Region"

with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for char in data['flare_quills']:
    tribe, region = get_tribe_and_region(char)
    if tribe != "Unknown Tribe":
        char['tribe'] = tribe
        char['region'] = region
    
    # --- FLAVOR TEXT UPDATE ---
    # Ensure they are referred to as "Quills" or "Squids"
    if "human" in char.get("origin_story", "").lower():
        char["origin_story"] = char["origin_story"].replace("human", "Quill")
    
    # Add generic flavor if missing
    if "Quill" not in char.get("origin_story", "") and "Squid" not in char.get("origin_story", ""):
        # Don't overwrite, just ensure it feels right. 
        pass

with open('flare_quills_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Global Tribe Fix Complete.")
