
import json

def curate_eighth_10():
    json_path = "flare_quills_data.json"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    curated = [
        {
            "name": "Obsidian Overdrive",
            "participants": ["The Hunter", "Flare Quill Alchemist", "Tribal Drummer", "Abyssal Diver"],
            "description": "A volcanic extraction ritual. The Diver and Hunter locate deep obsidian veins while the Drummer's rhythm stabilizes the ground, allowing the Alchemist to transmute raw stone into explosive glass shards.\n\n**Visual Effects:** Heavy brown pixels slamming down followed by sharp black crystal shards erupting, layered with vibrant red pixel-sparks and golden soundwave rings.",
            "type": "Earth/Fire/Dark/Alchemy",
            "is_mega": True
        },
        {
            "name": "Harvesting Whirlwind",
            "participants": ["Flare Quill Farmer", "Forest King"],
            "description": "The synchronization of growth and harvest. The King commands the forest to expand at impossible speeds, while the Farmer uses specialized tools to convert that growth into a shredding whirlwind of organic matter.\n\n**Visual Effects:** Green vines rapidly spiraling upward while brown wooden splinters and leaves flutter in a high-speed wind effect.",
            "type": "Wood/Nature/Earth",
            "is_mega": False
        },
        {
            "name": "Chrono-Vault Lock",
            "participants": ["Kunzite Archon", "The Collector", "The Time Keeper", "Abyssal Captain"],
            "description": "A multi-dimensional containment procedure. The Time Keeper pauses the target, the Captain anchors them in the void, and the Collector uses the Archon's crystal energy to lock the target in a permanent prismatic vault.\n\n**Visual Effects:** A static golden clock-face appearing in the center, layered with translucent blue water beams and a formation of purple crystal shards.",
            "type": "Time/Void/Crystal",
            "is_mega": True
        },
        {
            "name": "Void-Sailor's Wake",
            "participants": ["Abyssal Captain", "Wind Chieftain"],
            "description": "Navigating the currents between worlds. The Captain steers through the void while the Chieftain fills the sails with spectral winds, creating a high-speed wake that disintegrates anything it touches.\n\n**Visual Effects:** A black hole-like void trail following the icons, layered with swirling white pixel-dust and blue particle splashes.",
            "type": "Void/Water/Wind",
            "is_mega": False
        },
        {
            "name": "Seraphic Singularity",
            "participants": ["Emerald Vanquisher", "Seraphim Scout", "Quantum Drifter", "Chrono-Warlock", "Sapphire Mystic", "Abyssal Diver", "Sanitation Sentinel", "Devil Quill", "The Giant"],
            "description": "The ultimate celestial cleansing. A massive coordination of light, time, and void powers to reset a localized area to its primordial state, scrubbed clean of all corruption by the Sentinel.\n\n**Visual Effects:** A blinding white flash that shatters into green and blue crystal shards, layered with golden soundwave rings and a slow-expanding purple void field.",
            "type": "Light/Time/Void/Nature",
            "is_mega": True
        },
        {
            "name": "Divine Deluge",
            "participants": ["Pyro Clover", "Azure Pyrite Knight", "Tidecaller Deity", "Seraphim Scout"],
            "description": "A baptism of holy fire and water. The Deity and Scout provide the divine source, the Knight provides the steel focus, and the Clover adds volatile organic catalysts to the flood.\n\n**Visual Effects:** High-speed blue particle streams layered with vibrant orange fire pixels and beams of golden light stabbing through the deluge.",
            "type": "Water/Divine/Light/Fire",
            "is_mega": True
        },
        {
            "name": "Tectonic Tremor",
            "participants": ["Oktober-Quill", "Golem Lord"],
            "description": "A rhythm of the deep earth. The Golem's stomps are amplified by Oktober-Quill's brewing vats, creating a resonance frequency that liquifies the ground beneath the enemy.\n\n**Visual Effects:** Heavy brown pixels slamming down in a rapid sequence, creating a liquid-like 'ripple' effect on the UI with thick dust clouds.",
            "type": "Earth",
            "is_mega": False
        },
        {
            "name": "Star-Forge Eruption",
            "participants": ["The Time Keeper", "Deep-Vein Excavator", "Ignis Sentinel", "Seraphim Scout", "Crimson Shade", "Ice Crystal Monarch"],
            "description": "Forging a star in the heart of the earth. The Excavator and Sentinel create a pressurized volcanic core, which is then ignited by the Scout's light and frozen in place by the Monarch to create a stable, explosive solar nursery.\n\n**Visual Effects:** Vibrant red and orange pixels erupting outward, layered with cyan ice crystals and a central sun-like white flash.",
            "type": "Fire/Earth/Light/Ice",
            "is_mega": True
        },
        {
            "name": "Caffeine Overgrowth",
            "participants": ["The Giant", "Flora Queen", "Barista Bot 9000"],
            "description": "Nature on a caffeine high. The Queen's plants are watered with Barista Bot's high-octane espresso, causing them to develop jagged, jittery thorns and move with erratic, lightning-fast speed.\n\n**Visual Effects:** Neon green vines vibrating and spiraling rapidly, layered with brown coffee splashes and yellow jagged lightning arcs.",
            "type": "Nature/Food/Electric",
            "is_mega": True
        },
        {
            "name": "Alchemical Tsunami",
            "participants": ["Arcane Wizard", "Deep-Vein Excavator", "Flare Quill Chef", "Cyber Tech", "Magma Warden", "Kunzite Archon", "Cyber Arcanist", "Ashbound Assassin", "Splash Mage"],
            "description": "A chaotic flood of transmuted matter. A massive wave of liquid crystal, magma, and volatile spices that overwrites the physical properties of the entire combat zone.\n\n**Visual Effects:** A multicolored wave (blue, red, purple) cascading across the screen, layered with digital glitch effects and floating hexadecimal data particles.",
            "type": "Alchemy/Water/Fire/Crystal/Tech",
            "is_mega": True
        }
    ]
    
    # Overwrite indices 70 to 79 (the eighth 10)
    data["combo_techniques"][70:80] = curated
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Successfully curated the eighth 10 combo techniques in {json_path}.")

if __name__ == "__main__":
    curate_eighth_10()
