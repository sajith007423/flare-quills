
import json

def curate_tenth_10():
    json_path = "flare_quills_data.json"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    curated = [
        {
            "name": "Soul-Binding Strike",
            "participants": ["Venomblade Hunter", "Skull Shaman"],
            "description": "An assassination technique that targets the spirit. The Hunter delivers a physical strike while the Shaman anchors the target's soul to the spot using ancient spirit-runes.\n\n**Visual Effects:** A sharp green pixel-slash followed by a purple miasmic aura that 'locks' the target's icon in place with spectral chains.",
            "type": "Spirit/Poison/Dark",
            "is_mega": False
        },
        {
            "name": "Volcanic Bastion",
            "participants": ["Tunnel Vanguard", "Blaze Monk", "Magma Warden", "Highlander"],
            "description": "The ultimate defensive wall of the inner earth. The Vanguard and Warden raise the ground, the Monk ignites it, and the Highlander guards the flaming ramparts with a steel blade.\n\n**Visual Effects:** Massive brown pixels slamming down to form a wall, layered with a radial orange fire burst and heat distortion ripples.",
            "type": "Earth/Fire/Wind",
            "is_mega": True
        },
        {
            "name": "The Great Unearthing",
            "participants": ["Tunnel Vanguard", "Oktober-Quill"],
            "description": "A collaborative excavation that reveals treasures and terrors alike. The Vanguard clears the earth while Oktober-Quill uses geological intuition to find the perfect point of impact.\n\n**Visual Effects:** Heavy brown pixels slamming down repeatedly, kicking up thick dust clouds and golden 'artifact' sparkles.",
            "type": "Earth",
            "is_mega": False
        },
        {
            "name": "Obsidian Eclipse",
            "participants": ["Dark Iron Warlock", "Emerald Vanquisher"],
            "description": "A field of crystalline darkness. The Warlock drains the light while the Vanquisher uses the darkness to teleport behind enemies, striking with obsidian-glass daggers.\n\n**Visual Effects:** A black hole-like void expanding, layered with sharp black crystal shards and sudden green flashes of light.",
            "type": "Dark/Fire/Crystal",
            "is_mega": False
        },
        {
            "name": "Stellar Splashdown",
            "participants": ["Space Marine", "Splash Mage", "Abyssal Diver", "Ruby Sovereign", "Cloud Master"],
            "description": "An orbital water-bombing operation. The Marine provides the target coordinates, the Master creates a localized vacuum, and the Mage-Diver duo drops a concentrated mass of elemental water from the upper atmosphere.\n\n**Visual Effects:** Multiple blue particle streams falling at high speed, ending in a massive white splash layered with star-matter purple particles.",
            "type": "Water/Air/Void/Space",
            "is_mega": True
        },
        {
            "name": "Time-Frozen Gale",
            "participants": ["Frost Monarch", "Temporal Stormguard"],
            "description": "A localized cessation of movement. The Monarch brings the cold while the Stormguard freezes the flow of time itself, leaving enemies trapped in a perpetual blizzard.\n\n**Visual Effects:** A dense blizzard of cyan crystals that 'freezes' in mid-air, layered with golden clock-face particles that slow down and stop.",
            "type": "Ice/Time/Electric",
            "is_mega": False
        },
        {
            "name": "Absolute Zero Protocol",
            "participants": ["Cyber Squid", "Iron-Core Machinist", "Ice Crystal Monarch"],
            "description": "A mechanical refrigeration miracle. The Machinist builds a cryo-array that the Monarch fuels with ancient ice, while the Squid uses its tentacles to distribute the cold with digital precision.\n\n**Visual Effects:** Cyan crystal fragments forming a vortex, layered with green neon grid lines and digital glitch effects.",
            "type": "Ice/Tech/Water",
            "is_mega": True
        },
        {
            "name": "Titan's High Feast",
            "participants": ["Titan of the Depths", "Flare Quill Chef", "Gourmet Automaton"],
            "description": "A meal of such massive proportions it requires a giant to eat it—and two master chefs to prepare it. The resulting energy release can be seen from space.\n\n**Visual Effects:** A blinding white flash followed by a rain of 'food' icons and golden steam particles that fill the combat zone.",
            "type": "Earth/Food/Steel",
            "is_mega": True
        },
        {
            "name": "Divine Broadcast",
            "participants": ["Zeus Quill", "Broadcast Unit", "Cinema Bot"],
            "description": "The ultimate PR move for a god. Zeus's lightning strikes are captured and broadcasted across all dimensions simultaneously, paralyzing enemies with both the shock and the terrifying imagery.\n\n**Visual Effects:** Jagged yellow lightning arcs layered with flickering digital static and cinema-reel 'frame' overlays.",
            "type": "God/Electric/Tech",
            "is_mega": True
        },
        {
            "name": "THE UNIVERSAL HARMONY",
            "participants": ["The Gatekeeper", "The Collector", "The Time Keeper", "The Universal Singularity"],
            "description": "The final chord of existence. A synchronization of the archive, the gateway, and the timeline, overseen by the Singularity itself. A move that exists beyond win or loss.\n\n**Visual Effects:** A blinding white screen that slowly fades into a rotating galaxy of every pixel color and effect used in the game, ending with a single, perfect golden crown pulse.",
            "type": "Universal/Infinite",
            "is_mega": True
        }
    ]
    
    # Overwrite indices 90 to 99 (the tenth 10)
    data["combo_techniques"][90:100] = curated
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Successfully curated the tenth 10 combo techniques in {json_path}.")

if __name__ == "__main__":
    curate_tenth_10()
