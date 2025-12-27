import json
import random

def get_defaults(tribe):
    defaults = {
        "Inferno Legion": {"element": "Fire", "occupation": "Soldier", "action": "Fire Blast"},
        "Sun-Scorched Nomads": {"element": "Sand", "occupation": "Nomad", "action": "Sand Strike"},
        "Shadow Cabal": {"element": "Poison", "occupation": "Agent", "action": "Toxic Stab"},
        "Fungal Colony": {"element": "Nature", "occupation": "Spore", "action": "Spore Cloud"},
        "Crystalline Guard": {"element": "Crystal", "occupation": "Guardian", "action": "Shard Throw"},
        "Highborn Court": {"element": "Light", "occupation": "Noble", "action": "Flash"},
        "Mystic Enclave": {"element": "Magic", "occupation": "Mage", "action": "Arcane Bolt"},
        "Prisoner's Circle": {"element": "Dark", "occupation": "Prisoner", "action": "Chain Whip"},
        "Storm Vanguard": {"element": "Electric", "occupation": "Scout", "action": "Shock"},
        "Iron Legion": {"element": "Tech", "occupation": "Bot", "action": "Laser"},
        "Culinary Corps": {"element": "Fire/Water", "occupation": "Chef", "action": "Pan Smack"},
        "Tideborn Covenant": {"element": "Ice", "occupation": "Viking", "action": "Ice Shard"},
        "Verdant Circle": {"element": "Wood", "occupation": "Druid", "action": "Root Tangle"},
        "Void Gastronomes": {"element": "Void/Fire", "occupation": "Void Chef", "action": "Nether Sear"}
    }
    return defaults.get(tribe, {"element": "Normal", "occupation": "Civilian", "action": "Punch"})

with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. Remove 16.png if present
data['flare_quills'] = [c for c in data['flare_quills'] if c['id'] != "16.png"]

# 2. Fill missing fields
for char in data['flare_quills']:
    tribe = char.get('tribe', 'Inferno Legion')
    defaults = get_defaults(tribe)
    
    if not char.get('element'):
        char['element'] = defaults['element']
    if not char.get('occupation'):
        char['occupation'] = defaults['occupation']
    if not char.get('attack_action'):
        char['attack_action'] = defaults['action']
    if not char.get('ember_cost'):
        char['ember_cost'] = random.randint(3, 7)
    
    # Ensure ID key exists
    if 'id' not in char:
        print(f"Warning: Character without ID found: {char}")

with open('flare_quills_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print(f"Data standardization complete. Total characters: {len(data['flare_quills'])}")
