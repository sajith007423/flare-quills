import json
import random

def get_void_arrays(occupation):
    # Dictionaries for diversity
    powers_db = {
        "Captain": ["Nether Wave", "Command Crew"],
        "Chef": ["Blue Flame Grill", "Soul Seasoning"],
        "Miner": ["Obsidian Crush", "Crystal Find"],
        "Guard": ["Halberd Sweep", "Alert"],
        "Pirate": ["Boarding Party", "Plunder"],
        "Construct": ["Golem Smash", "Hardened Shell"],
        "Mount": ["Glide", "Stinger"],
        "Mage": ["Azure Comet", "Void Shield"],
        "Butcher": ["Cleave", "Tenderize"],
        "Diver": ["Deep Dive", "Pressure Resist"],
        "Corsair": ["Dual Strike", "Evasion"],
        "Noble": ["Bribe", "Fine Taste"],
        "Smith": ["Hammer Strike", "Reforge"],
        "Navigator": ["Star Map", "True North"],
        "Quartermaster": ["Resupply", "Inventory Check"],
        "Oracle": ["Future Sight", "Mind Blast"],
        "Warden": ["Lockdown", "Soul Cage"]
    }
    
    resources_db = {
        "Captain": ["Captain's Hat", "Void Compass"],
        "Chef": ["Blue Coal", "Steak"],
        "Miner": ["Obsidian Shard", "Void Crystal"],
        "Guard": ["Helmet Scrap", "Halberd Head"],
        "Pirate": ["Gold coin", "Bandana"],
        "Construct": ["Golem Core", "Stone"],
        "Mount": ["Ray Fin", "Leather"],
        "Mage": ["Blue Dust", "Spellbook Page"],
        "Butcher": ["Bone", "Meat"],
        "Diver": ["Deep Pearl", "Magma coral"],
        "Corsair": ["Steel", "Cloth"],
        "Noble": ["Gold Ring", "Silk"],
        "Smith": ["Iron Ingot", "Hammer Handle"],
        "Navigator": ["Map Fragment", "Lens"],
        "Quartermaster": ["Crate Wood", "Rope"],
        "Oracle": ["Crystal Ball", "Incense"],
        "Warden": ["Key", "Chain Link"]
    }
    
    p = powers_db.get(occupation, ["Void Strike", "Nether Shield"])
    r = resources_db.get(occupation, ["Void Dust", "Dark Essence"])
    return p, r

with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for char in data['flare_quills']:
    # Check if we are in the 84-100 range (or any that are missing powers)
    if 'powers' not in char or 'craftable_resources' not in char:
        occupation = char.get('occupation', 'Warrior')
        powers, resources = get_void_arrays(occupation)
        
        char['powers'] = powers
        char['craftable_resources'] = resources
        print(f"Fixed {char['id']}: Added powers/resources for {occupation}")

with open('flare_quills_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Arrays added to missing characters.")
