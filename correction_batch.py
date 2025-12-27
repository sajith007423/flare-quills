import json

corrections = {
    # 85: Void Chef -> Regular Flare Quill Chef
    "85.png": {
        "name": "Flare Quill Chef", "occupation": "Chef", "tribe": "Culinary Corps", "region": "Gourmet Galley",
        "element": "Fire/Food", "action": "Pan Sear", 
        "story": "A master chef of the Culinary Corps, known for his perfect steaks.",
        "powers": ["Seasoning", "Grill Master"], "resources": ["Steak", "Spice"]
    },
    # 86: Nether Miner -> Regular Flare Quill Engineering
    "86.png": {
        "name": "Flare Quill Engineer", "occupation": "Engineer", "tribe": "Iron Legion", "region": "Ironworks",
        "element": "Tech", "action": "Wrench Throw", 
        "story": "Maintains the heavy machinery of the Ironworks with precision.",
        "powers": ["Repair", "Turret Build"], "resources": ["Gear", "Oil"]
    },
    # 87: Crimson Sentinel -> Regular Flare Quill Farmer
    "87.png": {
        "name": "Flare Quill Farmer", "occupation": "Farmer", "tribe": "Verdant Circle", "region": "Emerald Grove",
        "element": "Nature", "action": "Pitchfork Poke", 
        "story": "tends to the crops in the Emerald Grove, ensuring a bountiful harvest.",
        "powers": ["Harvest", "Growth"], "resources": ["Wheat", "Vegetable"] # Fixed typo "Vegetble"
    },
    # 88: Soul Pirate -> Regular Flare Quill Miner
    "88.png": {
        "name": "Flare Quill Miner", "occupation": "Miner", "tribe": "Crystalline Guard", "region": "Geode Caverns",
        "element": "Earth", "action": "Pickaxe Swing", 
        "story": "Digs deep into the Geode Caverns for rare gems and minerals.",
        "powers": ["Mining", "Headlamp"], "resources": ["Ore", "Gem"]
    },
    # 89: Obsidian Golem -> Mythic Inferno Blacksmith
    "89.png": {
        "name": "Mythic Inferno Blacksmith", "occupation": "Blacksmith", "tribe": "Inferno Legion", "region": "Volcanic Wastes",
        "element": "Fire/Mythic", "action": "Grand Forge Strike", 
        "story": "A legendary blacksmith forged from the volcano itself, creating weapons for the gods.",
        "powers": ["Master Forge", "Magma Temper"], "resources": ["Mythril", "Obsidian"]
    },
    # 90: Nether Ray -> Healing Wizard
    "90.png": {
        "name": "Healing Wizard", "occupation": "Wizard", "tribe": "Mystic Enclave", "region": "Arcane Sanctum",
        "element": "Life/Magic", "action": "Restoring Light", 
        "story": "Uses ancient arcane arts to heal the wounded and restore balance.",
        "powers": ["Great Heal", "Ward"], "resources": ["Herb", "Scroll"]
    },
    # 91: Bluefire Mage -> Regular Flare Quill Blacksmith
    "91.png": {
        "name": "Flare Quill Blacksmith", "occupation": "Blacksmith", "tribe": "Inferno Legion", "region": "Volcanic Wastes",
        "element": "Fire", "action": "Hammer Strike", 
        "story": "A standard blacksmith of the legion, keeping the army's weapons sharp.",
        "powers": ["Sharpen", "Repair"], "resources": ["Iron", "Coal"]
    },
    # 92: Void Butcher -> Medieval Flare Quill Regular Miner
    "92.png": {
        "name": "Medieval Miner", "occupation": "Miner", "tribe": "Crystalline Guard", "region": "Geode Caverns",
        "element": "Earth", "action": "Old Pickaxe", 
        "story": "Uses traditional mining techniques passed down through generations.",
        "powers": ["Tunnel", "Find Gold"], "resources": ["Gold Nugget", "Stone"]
    },
    # 94: Crimson Corsair -> Runic Woodcutter
    "94.png": {
        "name": "Runic Woodcutter", "occupation": "Woodcutter", "tribe": "Verdant Circle", "region": "Emerald Grove",
        "element": "Wood/Magic", "action": "Runic Axe Chop", 
        "story": "Carves magical runes into the trees he fells to release their energy.",
        "powers": ["Timber!", "Rune Carve"], "resources": ["Magic Log", "Sap"]
    },
    # 95: Steak Connoisseur -> Mythic Blacksmith
    "95.png": {
        "name": "Mythic Blacksmith", "occupation": "Blacksmith", "tribe": "Inferno Legion", "region": "Volcanic Wastes",
        "element": "Fire/Mythic", "action": "Legendary Hammer", 
        "story": "A mythic figure whose hammer strikes thunder across the volcanic plains.",
        "powers": ["Thunder Strike", "Forge God"], "resources": ["Titanium", "Star Metal"]
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
