
import json

def curate_sixth_10():
    json_path = "flare_quills_data.json"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    curated = [
        {
            "name": "Sonic Overdrive",
            "participants": ["El Mariachi", "Zeus Quill", "Tribal Drummer"],
            "description": "A rhythmic bombardment that shakes the heavens. The Drummer and Mariachi create a standing wave of sound that Zeus uses as a conductor for a continuous stream of divine lightning.\n\n**Visual Effects:** Gold and yellow soundwave rings pulsating rapidly, layered with jagged yellow lightning arcs that screen-shake on every beat.",
            "type": "Sound/Electric/God",
            "is_mega": True
        },
        {
            "name": "Magma Harvest",
            "participants": ["Pyro Clover", "Magma Warden", "Ember-Steel Smith"],
            "description": "The cultivation of volatile minerals. The Clover identifies the heat-veins, the Smith prepares the extraction tools, and the Warden protects the operation from the intense volcanic pressure.\n\n**Visual Effects:** Vibrant orange and red pixels erupting from cracks in the ground, layered with heavy brown dust clouds and glowing sparks from hammer strikes.",
            "type": "Fire/Earth",
            "is_mega": True
        },
        {
            "name": "Digital Mirage",
            "participants": ["Cyber Tech", "Cinema Bot", "Void Navigator"],
            "description": "An inter-dimensional broadcast that overwrites reality. The Navigator finds a stable frequency in the void for Cinema Bot to proyek a digital duplicate of the battlefield, controlled by Cyber Tech.\n\n**Visual Effects:** Green neon grid lines expanding outward, layered with flickering inter-dimensional static and floating 'binary' code particles.",
            "type": "Tech/Star/Void",
            "is_mega": True
        },
        {
            "name": "Absolute Zero Containment",
            "participants": ["Ice Emperor", "Frost Monarch", "Void Warden"],
            "description": "The perfect prison. The Monarchs bring the temperature down to absolute zero, while the Warden wraps the target in a void field that prevents even heat-vibrations from escaping.\n\n**Visual Effects:** A blinding white flash followed by a dense blizzard of cyan crystals, ending in a static, purple-outlined void cage that leaves frost on the UI.",
            "type": "Ice/Void/Shield",
            "is_mega": True
        },
        {
            "name": "Gourmet Gale",
            "participants": ["Flare Quill Chef", "Wind Chieftain", "Sky Chef"],
            "description": "A culinary storm that feeds and protects. The Chieftains guide the winds to distribute the Chefs' high-calorie delicacies across the entire frontline, providing an instant morale and energy boost.\n\n**Visual Effects:** Swirling white pixel-dust and floating 'food' icons (bread, meat, soup) dancing through a golden-yellow skybox with blurred heat-waves.",
            "type": "Food/Air",
            "is_mega": True
        },
        {
            "name": "Tectonic Drill",
            "participants": ["Deep-Vein Excavator", "Tunnel Vanguard", "Golem Lord"],
            "description": "A massive coordinated excavation. The Excavator and Vanguard clear the path with specialized tools while the Golem Lord provides the sheer muscle to move entire tectonic plates.\n\n**Visual Effects:** Heavy brown pixels slamming down in a rapid sequence, creating a deep 'drilling' screen-shake effect and thick clouds of subterranean dust.",
            "type": "Earth",
            "is_mega": True
        },
        {
            "name": "Spectral Alchemistry",
            "participants": ["Shadow Alchemist", "Necro Flame", "Flare Quill Alchemist"],
            "description": "The transmutation of the afterlife. The Alchemists stabilize the volatile necro-energy of the Flame, creating a liquid shadow that can dissolve both physical and spiritual barriers.\n\n**Visual Effects:** Sickly green fire pixels mixing with bubbling purple liquid particles, layered with sickly green gas clouds that drift across the screen.",
            "type": "Alchemy/Dark/Fire",
            "is_mega": True
        },
        {
            "name": "Industrial Storm",
            "participants": ["Iron-Core Machinist", "Storm Elder", "Zeus Quill"],
            "description": "A power plant on the move. The Machinist builds a conductive network of metal pillars that allow the Elder and Zeus to discharge their lightning with 100% efficiency.\n\n**Visual Effects:** Massive grey metal pillars slamming down, connected by jagged cyan lightning arcs that pulse with green neon digital glitch effects.",
            "type": "Tech/Electric",
            "is_mega": True
        },
        {
            "name": "Abyssal Bloom",
            "participants": ["Abyssal Diver", "Flora Queen", "Vitality Arcanist"],
            "description": "The growth of a deep-sea garden. The Diver provides pressurized nutrients from the abyss, which the Queen and Arcanist use to grow glowing, bioluminescent vines in the blink of an eye.\n\n**Visual Effects:** Neon green and blue vines spiraling upward through translucent blue water streams, interspersed with bright white light beams.",
            "type": "Water/Nature/Life",
            "is_mega": True
        },
        {
            "name": "Royal Decree",
            "participants": ["King Quill", "The Fallen King", "Ruby Sovereign"],
            "description": "A judgment passed by the three highest thrones. Their combined authority creates a field of absolute order where only the strongest survive.\n\n**Visual Effects:** Three overlapping golden crown pulses followed by a massive red and white light flash that leaves a 'ruby' crystal pattern on the floor.",
            "type": "Royal/Crystal/Fire",
            "is_mega": True
        }
    ]
    
    # Overwrite indices 50 to 59 (the sixth 10)
    data["combo_techniques"][50:60] = curated
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Successfully curated the sixth 10 combo techniques in {json_path}.")

if __name__ == "__main__":
    curate_sixth_10()
