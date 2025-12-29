import json

file_path = "flare_quills_data.json"

def update_data():
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    changed_count = 0
    
    for quill in data['flare_quills']:
        # 1. Metal Gunner -> Flare Quill Alchemist
        if quill['name'] == "Metal Gunner":
            print(f"Converting {quill['name']} (ID: {quill['id']})...")
            quill['name'] = "Flare Quill Alchemist"
            quill['tribe'] = "Mystic Enclave" # Alchemy fits best here
            quill['region'] = "Arcane Sanctum"
            quill['occupation'] = "Alchemist"
            quill['element'] = "Alchemy"
            quill['origin_story'] = "A scholar who transmutes base metals into power, seeking the ultimate elixir."
            quill['attack_action'] = "Throws volatile potion flasks that explode with elemental effects."
            quill['powers'] = ["Transmute", "Acid Splash"]
            quill['craftable_resources'] = ["Gold flake", "Empty vial"]
            changed_count += 1

        # 2. Air Knight -> Chef
        elif quill['name'] == "Air Knight":
            print(f"Converting {quill['name']} (ID: {quill['id']})...")
            quill['name'] = "Sky Chef" # Giving a unique name to fit "Air" origin or just "Chef"
            # User said "Chef at Gourmet", implies Culinary Corps
            quill['tribe'] = "Culinary Corps"
            quill['region'] = "Gourmet Galley"
            quill['occupation'] = "Chef"
            quill['element'] = "Air/Food"
            quill['origin_story'] = "A chef who specializes in souffle and airy delights, cooking high in the sky."
            quill['attack_action'] = "Whips up a tornado of sharp cutlery and plates."
            quill['powers'] = ["Aerating Whisk", "Souffle Rise"]
            quill['craftable_resources'] = ["Flour", "Bird egg"]
            changed_count += 1

        # 3. Spice Baker -> Runic Woodcutter
        elif quill['name'] == "Spice Baker":
            print(f"Converting {quill['name']} (ID: {quill['id']})...")
            quill['name'] = "Runic Woodcutter"
            quill['tribe'] = "Highborn Court"
            quill['region'] = "Gilded Spire"
            quill['occupation'] = "Woodcutter"
            quill['element'] = "Wood/Rune"
            quill['origin_story'] = "Carves magical runes into the ancient trees he fells, preserving their spirit."
            quill['attack_action'] = "Swings a rune-enchanted axe that cleaves through magic barriers."
            quill['powers'] = ["Rune Chop", "Timber Shield"]
            quill['craftable_resources'] = ["Rune wood", "Sawdust"]
            changed_count += 1

        # 4. Magma Warden -> Farmer
        # User referred to "87-magma warden", but we match by name to be safe.
        elif quill['name'] == "Magma Warden":
            print(f"Converting {quill['name']} (ID: {quill['id']})...")
            quill['name'] = "Ash Farmer" # "Magma" context -> Ash/Volcanic Farmer? Or just "Farmer"?
            # User just said "Farmer". Let's put them in Verdant Circle (Emerald Grove) or maybe Volcanic Wastes (Ash Farmer)?
            # "Farmer" usually implies Verdant Circle. Let's move them there.
            # But earlier "Crimson Sentinel" (87) was moved to Verdant Circle as Farmer.
            # Let's make this one a "Volcanic Farmer" effectively?
            # Or assume they want a STANDARD Farmer.
            # Let's go with "Ash Farmer" in Volcanic Wastes for now, or "Flare Quill Farmer" in Verdant Circle.
            # "Magma Warden" is currently in Volcanic Wastes.
            # Let's assume standard "Flare Quill Farmer" in Verdant Circle (Emerald Grove) to fit the "Farmer" archetype.
            quill['name'] = "Flare Quill Farmer"
            quill['tribe'] = "Verdant Circle" 
            quill['region'] = "Emerald Grove"
            quill['occupation'] = "Farmer"
            quill['element'] = "Nature/Earth"
            quill['origin_story'] = "A humble farmer who cultivates crops even in the harshest soils."
            quill['attack_action'] = "Swings a hoe or scythe to harvest enemies."
            quill['powers'] = ["Harvest", "Sow Seeds"]
            quill['craftable_resources'] = ["Wheat", "Vegetables"]
            changed_count += 1

    if changed_count > 0:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        print(f"Successfully updated {changed_count} characters.")
    else:
        print("No target characters found.")

if __name__ == "__main__":
    update_data()
