
import json

def curate_fifth_10():
    json_path = "flare_quills_data.json"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    curated = [
        {
            "name": "Chrono-Stellar Rift",
            "participants": ["The Time Keeper", "Void Navigator", "Nebula Spellweaver"],
            "description": "A collapse of time and space. The Navigator points the way, the Spellweaver powers the gate, and the Time Keeper ensures the event remains stable long enough to erase the targets from history.\n\n**Visual Effects:** Purple star-matter particles drifting through a distorted temporal field, ending in a massive white clock-face that shatters into glass-like shards.",
            "type": "Time/Void/Star",
            "is_mega": True
        },
        {
            "name": "Midnight Serenade",
            "participants": ["Tsar Quill", "Shadow Warlock", "El Mariachi"],
            "description": "A hauntingly beautiful melody that drains the light from the room. The Tsar's epic song is twisted by the Warlock's dark magic, while El Mariachi provides a rhythmic pulse that echoes through the shadows.\n\n**Visual Effects:** Magenta and black musical notes swirling in a vortex, with ghostly purple flames appearing and disappearing to the beat.",
            "type": "Ice/Dark/Sound",
            "is_mega": True
        },
        {
            "name": "Frostfire Forge",
            "participants": ["Mythic Blacksmith", "Frost Monarch", "Glacial Guide"],
            "description": "A legendary forge technique where absolute zero meets star-metal heat. The resulting thermal shock shatters even the strongest armor.\n\n**Visual Effects:** Vibrant red fire pixels clashing with cyan ice crystals, creating a massive white steam explosion that leaves frost on the UI edges and heat waves in the center.",
            "type": "Fire/Ice/Mythic",
            "is_mega": True
        },
        {
            "name": "Tectonic Thunder",
            "participants": ["Golem Lord", "Zeus Quill", "Tribal Drummer"],
            "description": "A rhythmic assault on the bedrock. The Drummer sets the pace, the Golem stomps the ground, and Zeus punctuates every beat with a bolt from the heavens.\n\n**Visual Effects:** Screen-shaking brown dust clouds synchronized with yellow lightning strikes and gold soundwave rings.",
            "type": "Earth/Electric/God",
            "is_mega": True
        },
        {
            "name": "Arcane Harvest",
            "participants": ["Forest King", "Vitality Arcanist", "Runic Woodcutter"],
            "description": "The rapid acceleration of the natural cycle. The King and Woodcutter prepare the ground with runic timber, while the Arcanist pours pure life-force into it, causing a jungle to grow and consume the enemy in seconds.\n\n**Visual Effects:** Rapidly spiraling emerald vines layered with white light beams and exploding 'seed' particles that leave green leaves everywhere.",
            "type": "Nature/Rune/Life",
            "is_mega": True
        },
        {
            "name": "Bio-Toxic Breach",
            "participants": ["Venomous King", "Cyber Squid", "Toxic Soul"],
            "description": "A fusion of biological warfare and mechanical precision. The Squid injects the Toxic Soul's miasma directly into the enemy's weak points using tech-enhanced tentacles.\n\n**Visual Effects:** Blue water jets turning sickly green mid-air, layered with purple gas clouds and digital glitch effects.",
            "type": "Poison/Water/Tech",
            "is_mega": True
        },
        {
            "name": "Royal Vanguard",
            "participants": ["King Quill", "Spartan Quill", "Highlander"],
            "description": "The ultimate defensive line of the Quill kingdom. Three generations of leaders standing back-to-back, creating a golden aura of invincibility.\n\n**Visual Effects:** Three overlapping golden shield pulses followed by a massive white light flash and golden crown particles.",
            "type": "Royal/Steel/Wind",
            "is_mega": True
        },
        {
            "name": "The Feast of Souls",
            "participants": ["Abyssal Diver", "Flare Quill Chef", "Void Warden"],
            "description": "A meal so deep and dark it consumes the diner's spirit. The Diver finds the ingredients in the void, the Warden keeps them contained, and the Chef seasons them with existential dread.\n\n**Visual Effects:** Black hole-void pulses layered with floating recipe hexadecimal particles and blue water bubbles.",
            "type": "Void/Food/Shield",
            "is_mega": True
        },
        {
            "name": "Infernal Logistics",
            "participants": ["Iron-Core Machinist", "Ember-Steel Smith", "Molten Forge-Lord"],
            "description": "The Iron Legion's production line turned into a weapon of war. A continuous stream of white-hot steel and clockwork precision that grinds anything in its path.\n\n**Visual Effects:** Red-hot metal sparks and green neon grid lines, with massive grey pillars slamming down in a rapid, machine-like rhythm.",
            "type": "Tech/Steel/Fire",
            "is_mega": True
        },
        {
            "name": "Celestial Aligment",
            "participants": ["Seraphim Scout", "Void Navigator", "Nebula Spellweaver"],
            "description": "Mapping the heavens to summon a focused solar discharge. The Scout spots the target, the Navigator aligns the stars, and the Spellweaver pulls the trigger.\n\n**Visual Effects:** A map of constellations appearing in the sky, followed by a concentrated beam of blinding white light that incinerates the target zone.",
            "type": "Light/Star/Magic",
            "is_mega": True
        }
    ]
    
    # Overwrite indices 40 to 49 (the fifth 10)
    data["combo_techniques"][40:50] = curated
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Successfully curated the fifth 10 combo techniques in {json_path}.")

if __name__ == "__main__":
    curate_fifth_10()
