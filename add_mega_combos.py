
import json

def add_mega_combos():
    json_path = "flare_quills_data.json"
    
    mega_combos = [
        {
            "name": "Elemental Harmony",
            "participants": ["Ignis Sentinel", "Splash Mage", "Ice Crystal Monarch", "Flora Queen", "Spark Mage", "Golem Lord"],
            "description": "A convergence of the six primal forces, creating a vortex of absolute elemental chaos that reconstructs the battlefield.",
            "type": "Omni-Element",
            "is_mega": True
        },
        {
            "name": "The Grand Alliance",
            "participants": [
                "Ignis Sentinel", "Splash Mage", "Forest King", "Iron Legionary", 
                "Ice Crystal Monarch", "Shadow Warlock", "Cyber Tech", "Time Keeper", 
                "Zeus Quill", "Seraphim Scout"
            ],
            "description": "The ultimate union of the ten great tribes. A legendary maneuver that guarantees victory by overwhelming every possible defense.",
            "type": "Ultimate",
            "is_mega": True
        },
        {
            "name": "Void Annihilation",
            "participants": ["Void Walker", "Void Warden", "Void Navigator", "Shadow Warlock", "Abyss Sentinel"],
            "description": "Participants tear open a massive rift to the Outer Void, erasing all nearby threats from existence.",
            "type": "Void/Dark",
            "is_mega": True
        },
        {
            "name": "Nature's Rebirth",
            "participants": ["Forest King", "Flora Queen", "Lumberjack Quill", "Pyro Clover"],
            "description": "A rapid growth of sentient, fire-resistant forest that traps enemies and heals allies instantly.",
            "type": "Nature/Fire",
            "is_mega": True
        },
        {
            "name": "Techno-Organic Singularity",
            "participants": ["Cyber Tech", "Cyber Squid", "Flare Quill Engineer", "Flora Queen", "Spark Mage"],
            "description": "Fuses mechanical precision with organic adaptability, creating a sentient nanobot swarm that consumes enemy tech.",
            "type": "Tech/Nature",
            "is_mega": True
        },
        {
            "name": "Glacial Fortress",
            "participants": ["Glacial Guide", "Ice Weaver", "Golem Lord", "Iron Legionary"],
            "description": "Summons a massive, mobile castle of enchanted ice and iron that provides absolute protection to the entire army.",
            "type": "Ice/Earth",
            "is_mega": True
        },
        {
            "name": "Solar Flare Storm",
            "participants": ["Blaze Monk", "Spark Mage", "Sky Chef", "Ignis Sentinel", "Seraphim Scout"],
            "description": "Converts culinary energy and sacred light into a blinding solar storm that purifies the land.",
            "type": "Fire/Light",
            "is_mega": True
        },
        {
            "name": "Tide-born Tsunami",
            "participants": ["Tide Caller", "Splash Mage", "Cyber Squid", "Void Warden"],
            "description": "A crushing wave of abyssal water and mechanical tentacles that drags enemies to the bottom of the world.",
            "type": "Water/Void",
            "is_mega": True
        },
        {
            "name": "Iron Legion Phalanx",
            "participants": ["Iron Legionary", "Heavy Trooper", "Inferno Soldier", "Flare Quill Engineer", "Mythic Iron Knight", "Ember-Steel Smith"],
            "description": "An unbreakable formation of steel and steam. The ultimate defensive and offensive wall of the Industrial North.",
            "type": "Tech/Fire",
            "is_mega": True
        },
        {
            "name": "Celestial Judgement",
            "participants": ["Seraphim Scout", "Zeus Quill", "Time Keeper", "Space Marine"],
            "description": "Calls down a strike of temporal lightning from the high heavens, freezing enemies in time before they are struck.",
            "type": "Light/Electric/Time",
            "is_mega": True
        }
    ]

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if "combo_techniques" not in data:
            data["combo_techniques"] = []
            
        data["combo_techniques"].extend(mega_combos)
            
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
        print(f"Successfully added 10 Mega Combos to {json_path}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    add_mega_combos()
