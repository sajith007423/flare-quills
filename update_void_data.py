import json

void_data = {
    "84.png": {"name": "Abyssal Captain", "occupation": "Captain", "element": "Void/Water", "action": "Nether Harp", "story": "The legendary pirate captain of the Crimson Coast, sailing a ship of blue flame."},
    "85.png": {"name": "Void Chef", "occupation": "Chef", "element": "Void/Fire", "action": "Soul Sear", "story": "He cooks steaks using the blue flames of the netherworld, creating dishes that empower the soul."},
    "86.png": {"name": "Nether Miner", "occupation": "Miner", "element": "Void/Earth", "action": "Pickaxe Strike", "story": "Digs for obsidian and void crystals in the jagged cliffs of the Crimson Coast."},
    "87.png": {"name": "Crimson Sentinel", "occupation": "Guard", "element": "Void/Fire", "action": "Flame Halberd", "story": "A guard stationed at the edge of the magna sea, watching for intruders."},
    "88.png": {"name": "Soul Pirate", "occupation": "Pirate", "element": "Void/Water", "action": "Plunder", "story": "A raider who steals not gold, but the courage of his enemies."},
    "89.png": {"name": "Obsidian Golem", "occupation": "Construct", "element": "Void/Rock", "action": "Obsidian Smash", "story": "A construct animated by blue fire, defending the Void Gastronomes' shores."},
    "90.png": {"name": "Nether Ray", "occupation": "Mount", "element": "Void/Water", "action": "Sting", "story": "A tamed void ray used by the pirates to glide over the magma ocean."},
    "91.png": {"name": "Bluefire Mage", "occupation": "Mage", "element": "Void/Fire", "action": "Azure Bolt", "story": "Channels the unstable blue energy of the region into destructive spells."},
    "92.png": {"name": "Void Butcher", "occupation": "Butcher", "element": "Void", "action": "Cleaver", "story": "Prepares the giant void-beasts for the Chef's kitchen with terrifying precision."},
    "93.png": {"name": "Abyssal Diver", "occupation": "Diver", "element": "Void/Water", "action": "Harpoon", "story": "Dives into the magma depths to retrieve rare ingredients."},
    "94.png": {"name": "Crimson Corsair", "occupation": "Corsair", "element": "Void/Fire", "action": "Dual Cutlass", "story": "An elite dual-wielding fighter of the Captain's crew."},
    "95.png": {"name": "Steak Connoisseur", "occupation": "Noble", "element": "Void", "action": "Taste Test", "story": "A wealthy merchant who travels dimensions just to taste the Void Chef's steak."},
    "96.png": {"name": "Nether Smith", "occupation": "Smith", "element": "Void/Fire", "action": "Forge Hammer", "story": "Forges weapons from black iron and blue flame."},
    "97.png": {"name": "Void Navigator", "occupation": "Navigator", "element": "Void/Star", "action": "Star Chart", "story": "Guides the ships through the inter-dimensional mists."},
    "98.png": {"name": "Abyssal Quartermaster", "occupation": "Quartermaster", "element": "Void", "action": "Supply Drop", "story": "Ensures the crew is fed and armed, managing the ship's strange inventory."},
    "99.png": {"name": "Crimson Oracle", "occupation": "Oracle", "element": "Void/Psychic", "action": "Foresight", "story": "Reads the future in the patterns of the blue flames."},
    "100.png": {"name": "Void Warden", "occupation": "Warden", "element": "Void/Shield", "action": "Void Cage", "story": "The jailer of the Crimson Coast, protecting the realm from chaotic entities."}
}

with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for char in data['flare_quills']:
    if char['id'] in void_data:
        info = void_data[char['id']]
        char['name'] = info['name']
        char['occupation'] = info['occupation']
        char['element'] = info['element']
        char['attack_action'] = info['action']
        char['origin_story'] = info['story']
        char['tribe'] = "Void Gastronomes"
        char['region'] = "Crimson Coast"

with open('flare_quills_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Updates applied to Void Gastronomes (84-100).")
