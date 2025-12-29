
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
        "Fire": {
            "adj": ["Burning", "Blazing", "Solar", "Volcanic", "Molten"], 
            "noun": ["Phoenix", "Flare", "Cinder", "Inferno", "Pyre"], 
            "verb": ["Incinerate", "Scorch", "Ignite"],
            "animation": "Vibrant orange and red pixels erupting outward in a radial burst, accompanied by heat distortion ripples."
        },
        "Water": {
            "adj": ["Tidal", "Azure", "Abyssal", "Fluid", "Mist"], 
            "noun": ["Tsunami", "Torrent", "Geyser", "Cove", "Current"], 
            "verb": ["Drown", "Submerge", "Splash"],
            "animation": "Blue and translucent white particle streams cascading across the screen with a fluid, swirling motion."
        },
        "Nature": {
            "adj": ["Verdant", "Blooming", "Wild", "Thorny", "Rooted"], 
            "noun": ["Grove", "Jungle", "Vine", "Thicket", "Bramble"], 
            "verb": ["Entangle", "Grow", "Flourish"],
            "animation": "Green vines rapidly spiraling upward while leaves flutter in a generated wind effect."
        },
        "Wood": {
            "adj": ["Ancient", "Splintering", "Timber", "Bark", "Leafy"], 
            "noun": ["Forest", "Trunk", "Leaf", "Sap", "Branch"], 
            "verb": ["Crush", "Ensnare", "Fortify"],
            "animation": "Brown wooden pillars smashing together, leaving wooden splinter particles that linger on the ground."
        },
        "Electric": {
            "adj": ["Sparking", "Kinetic", "Galvanic", "Static", "Ionized"], 
            "noun": ["Bolt", "Circuit", "Storm", "Pulse", "Voltage"], 
            "verb": ["Paralyze", "Shock", "Overload"],
            "animation": "Jagged yellow and cyan lightning arcs jumping between participants, screen-shaking on impact."
        },
        "Ice": {
            "adj": ["Glacial", "Frozen", "Frosty", "Arctic", "Brittle"], 
            "noun": ["Shard", "Blizzard", "Hail", "Iceberg", "Permafrost"], 
            "verb": ["Freeze", "Shatter", "Chill"],
            "animation": "Cyan crystal fragments forming a blizzard, with a deep blue flash that leaves frost patterns on the UI."
        },
        "Earth": {
            "adj": ["Tectonic", "Stony", "Crushing", "Lithic", "Dusty"], 
            "noun": ["Quake", "Boulder", "Cliff", "Plateau", "Cave"], 
            "verb": ["Bury", "Smash", "Shake"],
            "animation": "Heavy brown pixels slamming down with a screen-shaking 'thud', kicking up a dust cloud."
        },
        "Tech": {
            "adj": ["Cyber", "Mechanical", "Atomic", "Digital", "Clockwork"], 
            "noun": ["Engine", "Drone", "Matrix", "Laser", "Circuit"], 
            "verb": ["Dismantle", "Analyze", "Automate"],
            "animation": "Green neon grid lines expanding outward, with digital glitch effects and floating hexadecimal particles."
        },
        "Dark": {
            "adj": ["Shadowy", "Ebony", "Cursed", "Grim", "Vantablack"], 
            "noun": ["Abyss", "Night", "Grave", "Void", "Specter"], 
            "verb": ["Corrupt", "Blind", "Drain"],
            "animation": "A black hole-like void expanding from the center, sucking in nearby light and particles."
        },
        "Light": {
            "adj": ["Radiant", "Holy", "Gleaming", "Solar", "Pure"], 
            "noun": ["Halo", "Prism", "Beam", "Aura", "Star"], 
            "verb": ["Blind", "Purify", "Illuminate"],
            "animation": "A blinding white flash followed by beams of golden light stabbing through the darkness."
        },
        "Poison": {
            "adj": ["Toxic", "Venomous", "Miasmic", "Blighted", "Acidic"], 
            "noun": ["Spore", "Gas", "Blight", "Sludge", "Fang"], 
            "verb": ["Contaminate", "Wither", "Dissolve"],
            "animation": "Purple and sickly green gas clouds slowly drifting, with bubbling acid bubble particles."
        }
    }
    
    # Defaults for unknown elements
    default_lex = {
        "adj": ["Mystic", "Shattering", "Radiant"], 
        "noun": ["Nexus", "Harmony", "Aura"], 
        "verb": ["Impact", "Strike", "Channel"],
        "animation": "A prismatic shockwave of glowing pixel-dust that illuminates the entire combat zone."
    }

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

        # Animation Explanation
        anim1 = lex1['animation']
        anim2 = lex2['animation']
        animation_desc = f"**Visual Effects:** {anim1} This is then layered with {anim2.lower()}" if primary_el != (elements[1] if len(elements)>1 else primary_el) else f"**Visual Effects:** {anim1}"
            
        description = f"{desc_start} {desc_body}\n\n{animation_desc}"
        
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
