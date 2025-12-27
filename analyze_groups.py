import json

with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Potential New Categories
groups = {
    "Kitchen/Appliance": [],
    "Desert/Sand": [],
    "Magic/Wizard (No Royal)": [],
    "Mushroom/Fungi": [],
    "Cosmic/Space": []
}

for char in data['flare_quills']:
    name = char.get('name', '')
    story = char.get('origin_story', '')
    elem = char.get('element', '')
    occ = char.get('occupation', '')

    desc = f"{name} ({elem}, {occ})"

    if "Kitchen" in occ or "Chef" in occ or "Appliance" in occ or "Toaster" in story:
        groups["Kitchen/Appliance"].append(desc)
    
    if "Sand" in elem or "Desert" in story or "Dune" in story:
        groups["Desert/Sand"].append(desc)

    if ("Magic" in elem or "Wizard" in occ or "Mage" in occ) and not ("Royal" in elem or "King" in name or "Queen" in name):
        groups["Magic/Wizard (No Royal)"].append(desc)

    if "Mushroom" in story or "Fungi" in story or "Spore" in story:
        groups["Mushroom/Fungi"].append(desc)
    
    if "Space" in elem or "Cosmic" in elem or "Star" in story:
        groups["Cosmic/Space"].append(desc)

for g, members in groups.items():
    print(f"--- {g} ({len(members)}) ---")
    for m in members:
        print(f"  - {m}")
    print("")
