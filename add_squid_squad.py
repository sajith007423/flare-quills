import json

new_chars = [
    {"id": "84.png", "name": "Abyssal Captain", "occupation": "Pirate Lord", "element": "Water/Fire", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 8, "attack_action": "Magma Slash", "origin_story": "A captain who sails the magma seas of the Crimson Coast."},
    {"id": "85.png", "name": "Soul-Flame Chef", "occupation": "Sous Chef", "element": "Fire/Spirit", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 5, "attack_action": "Spirit Sear", "origin_story": "Cooks the rare steaks found in the void."},
    {"id": "86.png", "name": "Void Engineer", "occupation": "Builder", "element": "Tech/Fire", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 6, "attack_action": "Wrench Bash", "origin_story": "Builds the rigs on the Crimson Coast."},
    {"id": "87.png", "name": "Nether Farmer", "occupation": "Harvester", "element": "Nature/Fire", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 4, "attack_action": "Pitchfork Poke", "origin_story": "Harvests fire-resistant crops."},
    {"id": "88.png", "name": "Deep Miner", "occupation": "Miner", "element": "Earth/Fire", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 5, "attack_action": "Pickaxe Strike", "origin_story": "Digs for obsidian and void gems."},
    {"id": "89.png", "name": "Abyssal Smith", "occupation": "Blacksmith", "element": "Fire/Metal", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 6, "attack_action": "Anvil Drop", "origin_story": "Forges weapons in blue flame."},
    {"id": "90.png", "name": "Void Sentry", "occupation": "Guard", "element": "Fire/Electric", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 5, "attack_action": "Shocking Gaze", "origin_story": "Watches the borders of the Crimson Coast."},
    {"id": "91.png", "name": "Magma Diver", "occupation": "Deep Diver", "element": "Water/Fire", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 7, "attack_action": "Harpoon Shot", "origin_story": "Dives into lava to retrieve treasures."},
    {"id": "92.png", "name": "Void Viking", "occupation": "Raider", "element": "Ice/Fire", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 7, "attack_action": "Axe Cleave", "origin_story": "Raids coastal settlements for supplies."},
    {"id": "93.png", "name": "Nether Forgemaster", "occupation": "Smith", "element": "Fire/Metal", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 6, "attack_action": "Hammer Smash", "origin_story": "Master of the Abyssal Forge."},
    {"id": "94.png", "name": "Crystal Prospector", "occupation": "Miner", "element": "Earth/Crystal", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 5, "attack_action": "Gem Throw", "origin_story": "Finds glowing crystals in the dark."},
    {"id": "95.png", "name": "Dread Pirate", "occupation": "Corsair", "element": "Water/Dark", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 7, "attack_action": "Cutlass Fury", "origin_story": "Fear of the Crimson Coast."},
    {"id": "96.png", "name": "Head Chef", "occupation": "Master Chef", "element": "Fire/Spirit", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 8, "attack_action": "Cleaver Chop", "origin_story": "Runs the finest kitchen in the void."},
    {"id": "97.png", "name": "Spirit Wizard", "occupation": "Mage", "element": "Magic/Spirit", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 9, "attack_action": "Void Blast", "origin_story": "Channels the blue flames of the ancestors."},
    {"id": "98.png", "name": "Void Hunter", "occupation": "Ranger", "element": "Nature/Fire", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 6, "attack_action": "Flame Arrow", "origin_story": "Hunts void beasts."},
    {"id": "99.png", "name": "Nether Alchemist", "occupation": "Scientist", "element": "Poison/Fire", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 6, "attack_action": "Potion Toss", "origin_story": "Brews strange concoctions."},
    {"id": "100.png", "name": "Void Warden", "occupation": "Officer", "element": "Order/Fire", "tribe": "Void Gastronomes", "region": "Crimson Coast", "ember_cost": 7, "attack_action": "Baton Strike", "origin_story": "Keeps order in the chaotic coast."}
]

with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Add new if not exists
existing_ids = {c['id'] for c in data['flare_quills']}
count = 0
for char in new_chars:
    if char['id'] not in existing_ids:
        data['flare_quills'].append(char)
        count += 1

with open('flare_quills_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print(f"Added {count} characters to Void Gastronomes.")
