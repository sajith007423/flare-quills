import json
import random

def get_standard_tribes_data():
    return {
        "Inferno Legion": {"region": "Volcanic Wastes", "elements": ["Fire", "Magma", "Ash"], "jobs": ["Soldier", "Pyromancer", "Warden"]},
        "Highborn Court": {"region": "Gilded Spire", "elements": ["Air", "Light", "Nature"], "jobs": ["Noble", "Knight", "Mage"]},
        "Tideborn Covenant": {"region": "Frozen Fjords", "elements": ["Ice", "Water", "Frost"], "jobs": ["Fisher", "Guardian", "Shaman"]},
        "Storm Vanguard": {"region": "Thunder Peaks", "elements": ["Electric", "Wind", "Storm"], "jobs": ["Raider", "Caller", "Scout"]},
        "Iron Legion": {"region": "Ironworks", "elements": ["Tech", "Metal", "Steam"], "jobs": ["Engineer", "Pilot", "Gunner"]},
        "Void Gastronomes": {"region": "Crimson Coast", "elements": ["Dark", "Void", "Cosmic"], "jobs": ["Chef", "Hunter", "Devourer"]},
        "Crystalline Guard": {"region": "Geode Caverns", "elements": ["Earth", "Crystal", "Rock"], "jobs": ["Defender", "Miner", "Sentry"]},
        "Culinary Corps": {"region": "Gourmet Galley", "elements": ["Food", "Heat", "Spice"], "jobs": ["Cook", "Baker", "Brewer"]},
        "Shadow Cabal": {"region": "Venomous Swamplands", "elements": ["Poison", "Shadow", "Necro"], "jobs": ["Assassin", "Witch", "Rogue"]}
    }

def regenerate_character(char, target_id):
    standards = get_standard_tribes_data()
    tribe_names = list(standards.keys())
    
    # Pick a random new tribe
    new_tribe = random.choice(tribe_names)
    tribe_data = standards[new_tribe]
    
    # Update Character
    char['tribe'] = new_tribe
    char['region'] = tribe_data['region']
    char['element'] = random.choice(tribe_data['elements'])
    char['occupation'] = random.choice(tribe_data['jobs'])
    
    # Regenerate specifics based on new element/tribe to make it consistent
    char['name'] = f"{char['element']} {char['occupation']}"
    char['origin_story'] = f"A {char['occupation'].lower()} from {tribe_data['region']} who mastered the power of {char['element']}."
    char['attack_action'] = f"Uses {char['element'].lower()} attacks to defeat enemies."
    
    # Update Powers (Generic placeholders for now, can be refined)
    char['powers'] = [f"{char['element']} Strike", f"{new_tribe.split()[0]} Blessing"]
    
    # Update Craftable Resources
    char['craftable_resources'] = [f"{char['element']} Essence", "Scrap"]

    print(f"Regenerated {target_id}: Now a {char['name']} of {new_tribe} in {char['region']}")
    return char

def cleanup_tribes():
    filepath = 'flare_quills_data.json'
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: File not found.")
        return

    targets = ["19.png", "2.png", "98.png", "99.png"]
    
    # Additional check for any other leftovers in these tribes
    target_tribes = ["Sun-Scorched Nomads", "Verdant Circle", "Sun-Bleached Dunes", "Mushroom Forest", "Emerald Grove"]

    modified_count = 0
    for char in data.get('flare_quills', []): # Access list safely
        is_target_id = char.get('id') in targets
        is_target_tribe = char.get('tribe') in target_tribes or char.get('region') in target_tribes
        
        if is_target_id or is_target_tribe:
            regenerate_character(char, char.get('id'))
            modified_count += 1

    if modified_count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"\nSuccessfully updated {modified_count} characters.")
    else:
        print("\nNo characters required updates.")

if __name__ == "__main__":
    cleanup_tribes()
