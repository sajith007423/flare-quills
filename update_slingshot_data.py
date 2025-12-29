
import json
import random

def get_unique_technique(char, used_techniques):
    name = char.get("name", "Unknown")
    element = char.get("element", "").lower()
    occupation = char.get("occupation", "").lower()
    powers = char.get("powers", [])
    
    # Action components for creativity
    impact_types = [
        "Shattering Impact", "Spectral Surge", "Kinetic Burst", "Aetheric Pulse", 
        "Tectonic Shift", "Volcanic Venting", "Gale-Force Piercing", "Cryo-Fragmentation",
        "Bio-Organic Overgrowth", "Magnetic Implosion", "Gravitational Collapse", "Solar Flare-Up",
        "Void Phasing", "Plasma Meltdown", "Hydro-Static Crush", "Static Overload",
        "Celestial Alignment", "Earthen Anchoring", "Phantom Echo", "Prismatic Refraction"
    ]
    
    angry_bird_actions = [
        "explodes into smaller fragments that target nearby structures",
        "triggers a high-speed spiral that bores through metal and stone",
        "creates a localized vacuum that pulls loose blocks toward it",
        "releases a radial shockwave that destabilizes tall towers",
        "momentarily phases through the first wall and detonates inside",
        "summons a downward strike from the heavens upon landing",
        "leaves a slippery trail that causes structures to slide and collapse",
        "magnetizes nearby blocks causing them to clump together and fall",
        "expands into a giant version mid-flight for maximum kinetic energy",
        "spawns a defensive barrier that knocks away falling debris"
    ]

    lore_flavor = [
        "inspired by the legends of the old world.",
        "channeled through ancestral spirits.",
        "powered by pure elemental fury.",
        "mastered after centuries of solitude.",
        "defying the laws of standard physics.",
        "turning the battlefield into a chaotic playground.",
        "precision engineered for total demolition.",
        "a technique whispered in secret for eons."
    ]

    # Generate a technique
    while True:
        action_name = random.choice(impact_types)
        action_desc = random.choice(angry_bird_actions)
        flavor = random.choice(lore_flavor)
        
        # Incorporate character identity to ensure high uniqueness
        technique = f"{name}'s {action_name}: It {action_desc}, {flavor}"
        
        if technique not in used_techniques:
            used_techniques.add(technique)
            return technique

def update_data():
    json_path = "flare_quills_data.json"
    used_techniques = set()
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if "flare_quills" in data:
            # Sort or shuffle to ensure different results each time if needed
            # But let's just iterate
            for char in data["flare_quills"]:
                char["slingshot technique"] = get_unique_technique(char, used_techniques)
        else:
            print("Error: 'flare_quills' key not found in JSON.")
            return
            
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
        print(f"Successfully updated {len(data['flare_quills'])} characters with unique slingshot techniques.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_data()

