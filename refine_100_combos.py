
import json
import random

def refine_combos():
    json_path = "flare_quills_data.json"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    quills = data['flare_quills']
    quill_map = {q['name']: q for q in quills}
    quill_names = list(quill_map.keys())

    # Thematic Vocabulary
    element_lexicon = {
        "Fire": {"adj": ["Burning", "Blazing", "Solar", "Volcanic", "Molten"], "noun": ["Phoenix", "Flare", "Cinder", "Inferno", "Pyre"], "verb": ["Incinerate", "Scorch", "Ignite"]},
        "Water": {"adj": ["Tidal", "Azure", "Abyssal", "Fluid", "Mist"], "noun": ["Tsunami", "Torrent", "Geyser", "Cove", "Current"], "verb": ["Drown", "Submerge", "Splash"]},
        "Nature": {"adj": ["Verdant", "Blooming", "Wild", "Thorny", "Rooted"], "noun": ["Grove", "Jungle", "Vine", "Thicket", "Bramble"], "verb": ["Entangle", "Grow", "Flourish"]},
        "Wood": {"adj": ["Ancient", "Splintering", "Timber", "Bark", "Leafy"], "noun": ["Forest", "Trunk", "Leaf", "Sap", "Branch"], "verb": ["Crush", "Ensnare", "Fortify"]},
        "Electric": {"adj": ["Sparking", "Kinetic", "Galvanic", "Static", "Ionized"], "noun": ["Bolt", "Circuit", "Storm", "Pulse", "Voltage"], "verb": ["Paralyze", "Shock", "Overload"]},
        "Ice": {"adj": ["Glacial", "Frozen", "Frosty", "Arctic", "Brittle"], "noun": ["Shard", "Blizzard", "Hail", "Iceberg", "Permafrost"], "verb": ["Freeze", "Shatter", "Chill"]},
        "Earth": {"adj": ["Tectonic", "Stony", "Crushing", "Lithic", "Dusty"], "noun": ["Quake", "Boulder", "Cliff", "Plateau", "Cave"], "verb": ["Bury", "Smash", "Shake"]},
        "Tech": {"adj": ["Cyber", "Mechanical", "Atomic", "Digital", "Clockwork"], "noun": ["Engine", "Drone", "Matrix", "Laser", "Circuit"], "verb": ["Dismantle", "Analyze", "Automate"]},
        "Dark": {"adj": ["Shadowy", "Ebony", "Cursed", "Grim", "Vantablack"], "noun": ["Abyss", "Night", "Grave", "Void", "Specter"], "verb": ["Corrupt", "Blind", "Drain"]},
        "Light": {"adj": ["Radiant", "Holy", "Gleaming", "Solar", "Pure"], "noun": ["Halo", "Prism", "Beam", "Aura", "Star"], "verb": ["Blind", "Purify", "Illuminate"]},
        "Poison": {"adj": ["Toxic", "Venomous", "Miasmic", "Blighted", "Acidic"], "noun": ["Spore", "Gas", "Blight", "Sludge", "Fang"], "verb": ["Contaminate", "Wither", "Dissolve"]}
    }
    
    # Defaults for unknown elements
    default_lex = {"adj": ["Mystic", "Shattering", "Radiant"], "noun": ["Nexus", "Harmony", "Aura"], "verb": ["Impact", "Strike", "Channel"]}

    def get_lex(element):
        return element_lexicon.get(element, default_lex)

    new_combos = []
    
    for i in range(100):
        count = random.choices(range(2, 11), weights=[35, 20, 15, 10, 5, 5, 4, 3, 3])[0]
        participants = random.sample(quill_names, count)
        part_data = [quill_map[name] for name in participants]
        
        # Dominant Elements
        elements = list(set([q['element'] for q in part_data]))
        primary_el = elements[0]
        lex1 = get_lex(primary_el)
        lex2 = get_lex(elements[1]) if len(elements) > 1 else lex1
        
        # Name Generation
        if count >= 5:
            # Mega names
            name = f"{random.choice(lex1['adj'])} {random.choice(lex2['noun'])} {random.choice(['Supernova', 'Cataclysm', 'Singularity', 'Harmony', 'Onslaught'])}"
        else:
            name = f"{random.choice(lex1['adj'])} {random.choice(lex2['noun'])}"

        # Description Generation
        verbs = [random.choice(get_lex(q['element'])['verb']) for q in part_data]
        occupations = [q['occupation'] for q in part_data]
        
        desc_start = f"A {name} involving {', '.join(participants[:-1])} and {participants[-1]}."
        
        if count == 2:
            desc_body = f"The {occupations[0]} and {occupations[1]} synchronize to {verbs[0]} and {verbs[1]} their foes simultaneously."
        elif count < 5:
            desc_body = f"This tactical group combines {primary_el} and {elements[1] if len(elements)>1 else primary_el} powers to {random.choice(verbs)} the entire battlefield."
        else:
            desc_body = f"A legendary Mega Combo that channels the raw power of {len(elements)} elements. The synergy between {participants[0]} and {participants[len(participants)//2]} creates a massive {name} effect."
            
        description = f"{desc_start} {desc_body}"
        
        new_combos.append({
            "name": name,
            "participants": participants,
            "description": description,
            "type": "/".join(elements[:3]), # Show up to 3 elements in the type
            "is_mega": count >= 3
        })

    data["combo_techniques"] = new_combos
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Successfully generated 100 UNIQUE and THEMATIC combo techniques in {json_path}.")

if __name__ == "__main__":
    refine_combos()
