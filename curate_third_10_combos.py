
import json

def curate_third_10():
    json_path = "flare_quills_data.json"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    curated = [
        {
            "name": "Abyssal Feedback",
            "participants": ["Abyssal Diver", "Volt Sage", "Void Warden"],
            "description": "A high-risk underwater containment field. The Diver stabilizes the pressure while the Sage pumps high-voltage currents into the Warden's void cage, creating a localized event horizon of pure energy.\n\n**Visual Effects:** A black hole-like void expanding from the center, layered with jagged yellow and cyan lightning arcs that flicker with digital glitch effects.",
            "type": "Void/Water/Electric",
            "is_mega": True
        },
        {
            "name": "Emerald Flare",
            "participants": ["Flora Queen", "Ignis Sentinel", "Runic Woodcutter"],
            "description": "The ritual of the burning grove. The Queen and Woodcutter sacrifice ancient runic timber to fuel the Sentinel's flames, resulting in a holy fire that purges corruption and incinerates armor.\n\n**Visual Effects:** Rapidly spiraling green vines engulfed in vibrant orange pixels, leaving behind charcoal-black residues and glowing runic embers.",
            "type": "Nature/Fire/Wood/Rune",
            "is_mega": True
        },
        {
            "name": "Machina Deluge",
            "participants": ["Iron-Core Machinist", "Splash Mage", "Cyber Squid"],
            "description": "An automated flood system. The Machinist builds a network of high-pressure pipes that the Mage fills with volatile liquid, while the Squid uses its tentacles to fire concentrated beams of water.\n\n**Visual Effects:** High-speed blue particle streams spraying across the UI, layered with green neon grid lines and floating hexadecimal data scrolls.",
            "type": "Tech/Water",
            "is_mega": True
        },
        {
            "name": "Cursed Geyser",
            "participants": ["Cursed Pharaoh", "Tide Caller", "Toxic Soul"],
            "description": "The ocean's most toxic secret. The Pharaoh's ancient curse transforms the Tide Caller's waves into a boiling sludge of corrosive waste, manipulated by the Toxic Soul to target specific enemies.\n\n**Visual Effects:** Sickly green gas clouds drifting over massive blue particle streams, with purple acid bubbles popping and leaving 'poisoned' status overlays.",
            "type": "Sand/Water/Poison",
            "is_mega": True
        },
        {
            "name": "Prismatic Waltz",
            "participants": ["Seraphim Scout", "Sapphire Mystic", "Pyromancer"],
            "description": "A lethal dance of light and flame. The Scout's holy beams are refracted through the Mystic's crystal armor, while the Pyromancer adds a swirling inferno to create a mesmerizing, deadly light show.\n\n**Visual Effects:** Blinding white light beams stabbing through a radial fire burst, with blue crystal shards spinning and reflecting the light into multiple rainbows.",
            "type": "Light/Ice/Fire",
            "is_mega": True
        },
        {
            "name": "Terran Overload",
            "participants": ["Golem Lord", "Zeus Quill", "Deep-Vein Excavator"],
            "description": "A tectonic discharge from the world's core. The Golem and Excavator pull stones from the deep earth while Zeus strikes them with lightning upon impact, turning every boulder into a massive ionic bomb.\n\n**Visual Effects:** Heavy brown pixels slamming down with screen-shaking 'thuds', followed by explosive cyan lightning arcs that illuminate the entire combat zone.",
            "type": "Earth/Electric",
            "is_mega": True
        },
        {
            "name": "Star-Crossed Blades",
            "participants": ["Royal Spellblade", "Void Navigator", "Spartan Quill"],
            "description": "A tactical assault from a different dimension. The Navigator opens a star-gate, allowing the Spellblade and Spartan to strike from multiple angles simultaneously, their blades leaving trails of cosmic energy.\n\n**Visual Effects:** Thin purple and silver pixel trails following the character icons as they dash, with a central white flash that leaves a constellation pattern on the screen.",
            "type": "Magic/Void/Steel",
            "is_mega": True
        },
        {
            "name": "Blighted Harvest",
            "participants": ["Venomous King", "Forest King", "Skull Shaman"],
            "description": "The cycle of growth and decay turned into a weapon. The Forest King accelerates growth only for the Venomous King to rot it, while the Shaman channels the resulting necro-energy into a devastating wave of blight.\n\n**Visual Effects:** Rapidly growing green vines that wither and turn grey in real-time, releasing clouds of purple gas and shadowy spirit manifestations.",
            "type": "Nature/Poison/Dark",
            "is_mega": True
        },
        {
            "name": "Glacial Siege",
            "participants": ["Frost Monarch", "Highlander", "Ice Crystal Monarch"],
            "description": "The north's final stand. The Monarchs freeze the very air to create a jagged icy fortress, while the Highlander defends the walls with a massive, frost-enchanted claymore.\n\n**Visual Effects:** A dense blizzard of cyan crystals accompanied by a deep blue flash that leaves frost patterns and heavy blue pillars on the UI.",
            "type": "Ice/Wind",
            "is_mega": True
        },
        {
            "name": "Alchemical Nova",
            "participants": ["Flare Quill Alchemist", "Blaze Monk", "Molten Forge-Lord"],
            "description": "The ultimate transformation of matter. The Alchemist uses the Monk's fire and the Forge-Lord's metal as base components to trigger a chain reaction that converts the entire battlefield into pure energy.\n\n**Visual Effects:** A blinding white flash that transitions into vibrant orange and red pixels erupting outward, with golden sparks and heat distortion ripples.",
            "type": "Alchemy/Fire",
            "is_mega": True
        }
    ]
    
    # Overwrite indices 20 to 29 (the third 10)
    data["combo_techniques"][20:30] = curated
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Successfully curated the third 10 combo techniques in {json_path}.")

if __name__ == "__main__":
    curate_third_10()
