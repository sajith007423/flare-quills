import json

file_path = 'flare_quills_data.json'

new_characters = [
    {
        "id": "78.png",
        "name": "Gourmet Automaton",
        "origin_story": "A culinary construct designed to prepare feasts for the Ironworks elite, now armed with high-velocity blade attachments.",
        "attack_action": "Blender Vortex",
        "element": "Steel/Fire",
        "tribe": "Cybernetic Front",
        "occupation": "Battle Chef",
        "ember_cost": 4,
        "powers": ["Slice", "Puree", "Heat Ray"],
        "craftable_resources": ["Steel Plating", "Gourmet Meal"],
        "region": "Ironworks"
    },
    {
        "id": "79.png",
        "name": "Breakfast Bot",
        "origin_story": "Originally a morning service unit, this bot now launches superheated toast projectiles at intruders.",
        "attack_action": "Toast Launch",
        "element": "Electric/Heat",
        "tribe": "Cybernetic Front",
        "occupation": "Service Unit",
        "ember_cost": 3,
        "powers": ["Popup Attack", "Crumb Smokescreen"],
        "craftable_resources": ["Burnt Circuit", "Bread"],
        "region": "Ironworks"
    },
    {
        "id": "80.png",
        "name": "Barista Bot 9000",
        "origin_story": "This high-pressure caffeine dispenser operates at dangerous temperatures, scalding enemies with precision streams.",
        "attack_action": "Scalding Stream",
        "element": "Water/Electric",
        "tribe": "Cybernetic Front",
        "occupation": "Beverage Dispenser",
        "ember_cost": 3,
        "powers": ["Caffeine Boost", "Steam Vent"],
        "craftable_resources": ["Coffee Bean", "Glass Shard"],
        "region": "Ironworks"
    },
    {
        "id": "81.png",
        "name": "Sanitation Sentinel",
        "origin_story": "A vacuum-based cleaner modified for combat. It can reverse its airflow to expel debris at lethal speeds.",
        "attack_action": "Reverse Suction",
        "element": "Air/Electric",
        "tribe": "Cybernetic Front",
        "occupation": "Cleaner",
        "ember_cost": 3,
        "powers": ["Dust Storm", "High Suction"],
        "craftable_resources": ["Dust Bunny", "Motor Coil"],
        "region": "Ironworks"
    },
    {
        "id": "82.png",
        "name": "Broadcast Unit",
        "origin_story": "A walking CRT monitor that broadcasts hypnotic signals to disorient enemies on the battlefield.",
        "attack_action": "Static Shock",
        "element": "Electric/Sound",
        "tribe": "Cybernetic Front",
        "occupation": "Signal Broadcaster",
        "ember_cost": 4,
        "powers": ["Hypnotism", "Sonic Boom"],
        "craftable_resources": ["Copper Wire", "Glass Screen"],
        "region": "Ironworks"
    },
    {
        "id": "83.png",
        "name": "Cinema Bot",
        "origin_story": "A joyous popcorn machine turned artillery unit. It fires explosive kernels that pop on impact.",
        "attack_action": "Kernel Barrage",
        "element": "Fire/Nature",
        "tribe": "Cybernetic Front",
        "occupation": "Snack Vendor",
        "ember_cost": 3,
        "powers": ["Pop Explosion", "Butter Slick"],
        "craftable_resources": ["Corn Kernel", "Heating Element"],
        "region": "Ironworks"
    }
]

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

existing_ids = [c['id'] for c in data['flare_quills']]

for new_char in new_characters:
    if new_char['id'] not in existing_ids:
        data['flare_quills'].append(new_char)
        print(f"Added {new_char['name']}")
    else:
        # Update existing
        for i, char in enumerate(data['flare_quills']):
            if char['id'] == new_char['id']:
                data['flare_quills'][i] = new_char
                print(f"Updated {new_char['name']}")

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

print("Character data updated successfully.")
