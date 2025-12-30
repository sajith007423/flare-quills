
import json

def curate_fourth_10():
    json_path = "flare_quills_data.json"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    curated = [
        {
            "name": "Haunted Harvest",
            "participants": ["Oktober-Quill", "Necro Flame", "Forest King"],
            "description": "The autumnal ritual of the departed. Oktober-Quill's spectral pumpkins are carved with Necro Flame's green fire, while the Forest King provides a backdrop of decaying wood to amplify the spooky energy.\n\n**Visual Effects:** Glowing orange pumpkin pixels floating in a circle, exploding into green fire particles and withered brown leaves.",
            "type": "Wood/Dark/Fire",
            "is_mega": True
        },
        {
            "name": "Cyber-Coffee Overload",
            "participants": ["Barista Bot 9000", "Cyber Tech", "Breakfast Bot"],
            "description": "The ultimate morning routine. Barista Bot 9000's high-pressure espresso is infused with Cyber Tech's overclocking algorithms, delivered via Breakfast Bot's rapid-fire serving systems.\n\n**Visual Effects:** Brown steaming liquid particles spraying across the screen, layered with green digital grid lines and floating 'energy bar' icons.",
            "type": "Water/Tech/Food",
            "is_mega": True
        },
        {
            "name": "Crimson Phalanx",
            "participants": ["Crimson Shade", "Crimson Arbalest", "Spartan Quill"],
            "description": "A blood-red defensive wall. Shade and Arbalest provide long-range fire support while the Spartan anchors the formation, turning the battlefield into a field of crimson steel.\n\n**Visual Effects:** A rain of red pixel-arrows stabbing into the ground, followed by a massive red shield pulse that knocks back all nearby enemies.",
            "type": "Dark/Fire/Steel",
            "is_mega": True
        },
        {
            "name": "Echoes of the Arena",
            "participants": ["El Mariachi", "Tiger Eye Warrior", "Highlander"],
            "description": "A heroic anthem for the front lines. El Mariachi's strings vibrate with the intensity of the Tiger Eye's strikes, while the Highlander's war cries add a layer of intimidation to the sonic wave.\n\n**Visual Effects:** Gold and red soundwave rings pulsating outward, accompanied by blurred 'afterimage' trails of the character icons as they swing their weapons.",
            "type": "Sound/Earth/Wind",
            "is_mega": True
        },
        {
            "name": "Industrial Blizzard",
            "participants": ["Frost Wizard", "Iron-Core Machinist", "Sanitation Sentinel"],
            "description": "A mechanical winter. The Wizard's frost is channeled through the Machinist's cooling vents, while the Sanitation Sentinel scrubs the air of heat, creating a perma-frost zone.\n\n**Visual Effects:** Dense white pixel-fog and cyan ice crystals blowing out of mechanical pipes, leaving grey 'slush' patterns on the UI.",
            "type": "Ice/Tech",
            "is_mega": True
        },
        {
            "name": "Toxic Broadcast",
            "participants": ["Broadcast Unit", "Toxic Soul", "Cinema Bot"],
            "description": "The spread of viral corruption. The Broadcast Unit amplifies the Toxic Soul's miasma through inter-dimensional airwaves, while Cinema Bot proyekts terrifying images to paralyze the foe.\n\n**Visual Effects:** Static-filled purple gas clouds and digital glitch effects, with flickering 'low signal' warnings and skull icons appearing on the UI.",
            "type": "Poison/Tech/Void",
            "is_mega": True
        },
        {
            "name": "Magmatic Gastronomy",
            "participants": ["Abyssal Diver", "Flare Quill Chef", "Magma Warden"],
            "description": "Cooking with the core's heat. The Diver retrieves rare deep-sea spices while the Warden provides the perfect volcanic hearth for the Chef to prepare a truly explosive meal.\n\n**Visual Effects:** Bubbling blue water mixing with orange lava pixels, ending in a massive fire-flecked splash that leaves 'steam' particles everywhere.",
            "type": "Fire/Water/Food",
            "is_mega": True
        },
        {
            "name": "Emerald Infiltration",
            "participants": ["Emerald Vanquisher", "Shadow Warlock", "Runic Woodcutter"],
            "description": "Nature's stealthy vengeance. The Vanquisher moves through the shadows created by the Warlock, using the Woodcutter's runic carvings to silence their passage through the forest.\n\n**Visual Effects:** Green and black pixel-shroud masks the character icons, followed by sudden green flashes and wooden splinter particles from unseen strikes.",
            "type": "Nature/Dark/Rune",
            "is_mega": True
        },
        {
            "name": "Solar Juggernaut",
            "participants": ["Infernal Juggernaut", "Seraphim Scout", "Ignis Sentinel"],
            "description": "The unstoppable herald of light. The Juggernaut's armor is blessed with holy light by the Scout and ignited by the Sentinel, turning the tank into a living sun-bomb.\n\n**Visual Effects:** A blinding golden-white trail following a massive red-and-orange icon, ending in a screen-clearing explosion of pure white and yellow pixels.",
            "type": "Fire/Light/Mythic",
            "is_mega": True
        },
        {
            "name": "Quantum Quarantine",
            "participants": ["Quantum Drifter", "Void Warden", "Cyber Tech"],
            "description": "An inter-dimensional containment protocol. The Drifter warps the space-time around the target while the Warden locks the cage, and Cyber Tech stabilizers the erratic energy.\n\n**Visual Effects:** A black hole void layered with vibrating purple grid lines and digital hexadecimal particles that 'freeze' in mid-air.",
            "type": "Void/Time/Tech",
            "is_mega": True
        }
    ]
    
    # Overwrite indices 30 to 39 (the fourth 10)
    data["combo_techniques"][30:40] = curated
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Successfully curated the fourth 10 combo techniques in {json_path}.")

if __name__ == "__main__":
    curate_fourth_10()
