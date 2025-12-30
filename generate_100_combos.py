
import json
import random

def generate_100_combos():
    json_path = "flare_quills_data.json"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    quills = data['flare_quills']
    quill_names = [q['name'] for q in quills]
    
    prefixes = ["Mystic", "Eternal", "Shattering", "Radiant", "Shadow", "Iron", "Crystal", "Spectral", "Tidal", "Volcanic", "Gale", "Apex", "Divine", "Abyssal", "Prismatic", "Clockwork", "Cyber", "Void", "Solar", "Lunar"]
    actions = ["Burst", "Strike", "Nova", "Vortex", "Phalanx", "Shield", "Surge", "Eruption", "Cascade", "Harmony", "Rebirth", "Annihilation", "Judgment", "Mirage", "Nexus", "Singularity", "Aegis", "Echo", "Loom", "Pulse"]
    themes = ["of the Ancients", "of the Abyss", "of the Stars", "of the Forge", "of the Wilds", "of the Spire", "of the Depths", "of the Void", "of the Skies", "of the Core"]

    new_combos = []
    
    # 100 UNIQUE COMBOS (mixing participants count from 2 to 10)
    for i in range(100):
        # Determine participant count: mostly 2-4, occasionally 5-10
        count = random.choices(range(2, 11), weights=[40, 20, 15, 10, 5, 3, 3, 2, 2])[0]
        participants = random.sample(quill_names, count)
        
        # Build Name
        if count >= 5:
            name = f"{random.choice(prefixes)} {random.choice(actions)} {random.choice(themes)}"
        else:
            name = f"{random.choice(prefixes)} {random.choice(actions)}"
            
        # Determine Type based on first two participants' elements (simplified)
        p1 = next(q for q in quills if q['name'] == participants[0])
        p2 = next(q for q in quills if q['name'] == participants[1])
        combo_type = f"{p1['element']}/{p2['element']}" if p1['element'] != p2['element'] else p1['element']
        
        description = f"A powerful maneuver combining the unique abilities of {', '.join(participants[:-1])} and {participants[-1]} to create a devastating effect on the battlefield."
        
        new_combos.append({
            "name": name,
            "participants": participants,
            "description": description,
            "type": combo_type,
            "is_mega": count >= 3
        })

    data["combo_techniques"] = new_combos
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Successfully generated 100 unique combo techniques in {json_path}.")

if __name__ == "__main__":
    generate_100_combos()
