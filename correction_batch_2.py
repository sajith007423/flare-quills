import json

corrections = {
    # 96: Nether Smith -> Mythic Miner
    "96.png": {
        "name": "Mythic Miner", "occupation": "Miner", "tribe": "Crystalline Guard", "region": "Geode Caverns",
        "element": "Earth/Mythic", "action": "Legendary Pickaxe", 
        "story": "A legendary miner who dug so deep he found the world's core.",
        "powers": ["Core Strike", "Gem Storm"], "resources": ["Diamond", "Core Stone"]
    },
    # 98: Abyssal Quartermaster -> Regular Flare Quill Chef
    "98.png": {
        "name": "Flare Quill Chef", "occupation": "Chef", "tribe": "Culinary Corps", "region": "Gourmet Galley",
        "element": "Fire/Food", "action": "Chopping Frenzy", 
        "story": "Can chop vegetables at the speed of sound.",
        "powers": ["Speed Chop", "Feast"], "resources": ["Vegetable", "Knife"]
    },
    # 99: Crimson Oracle -> Regular Alchemist
    "99.png": {
        "name": "Flare Quill Alchemist", "occupation": "Alchemist", "tribe": "Mystic Enclave", "region": "Arcane Sanctum",
        "element": "Magic/Potion", "action": "Potion Throw", 
        "story": "Brews volatile mixtures that can heal or harm.",
        "powers": ["Explosive Potion", "Elixir"], "resources": ["Glass Vial", "Herb"]
    }
}

with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for char in data['flare_quills']:
    if char['id'] in corrections:
        update = corrections[char['id']]
        char.update(update)
        print(f"Updated {char['id']} -> {update['name']}")

with open('flare_quills_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)
