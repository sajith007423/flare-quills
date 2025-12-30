
import json

def curate_seventh_10():
    json_path = "flare_quills_data.json"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    curated = [
        {
            "name": "Chrono-Mechanical Singularity",
            "participants": ["The Time Keeper", "Iron-Core Machinist", "Cyber Tech"],
            "description": "A synchronization of clockwork precision and digital oversight. The Time Keeper slows the target to a crawl while the Machinist and Tech build a recursive loop of self-assembling turrets that fire outside of traditional time.\n\n**Visual Effects:** Golden clock-face particles layered with green neon grid lines and rapid-fire grey metallic projectiles.",
            "type": "Time/Tech",
            "is_mega": True
        },
        {
            "name": "Abyssal Pressure-Wash",
            "participants": ["Abyssal Diver", "Cyber Squid", "Sanitation Sentinel"],
            "description": "Deep-sea hydraulics meets industrial cleaning. The Diver and Squid provide the high-pressure water source, while the Sentinel adds abrasive industrial detergents to scrub even the strongest armor.\n\n**Visual Effects:** High-speed blue particle streams layered with white splash effects and digital 'cleaning' HUD overlays.",
            "type": "Water/Tech",
            "is_mega": True
        },
        {
            "name": "Nature's Final Stand",
            "participants": ["Flora Queen", "Forest King", "Runic Woodcutter", "Emerald Vanquisher"],
            "description": "The full might of the Green Grove. The Royals call for absolute growth, the Woodcutter provides the runic fuel, and the Vanquisher strikes from the heart of the resulting impenetrable jungle.\n\n**Visual Effects:** Rapidly spiraling emerald vines layered with brown wooden pillars smashing together and sudden green flashes of light.",
            "type": "Nature/Rune",
            "is_mega": True
        },
        {
            "name": "Supernova Stir-Fry",
            "participants": ["Flare Quill Chef", "Pyromancer", "Ignis Sentinel", "Blaze Monk"],
            "description": "The ultimate culinary technique. Using the heat of a collapsed star to flash-cook an entire battlefield into a manageable, energy-rich snack.\n\n**Visual Effects:** Vibrant orange and red pixels erupting in a radial burst, layered with floating 'food' icons and heat distortion ripples.",
            "type": "Fire/Food",
            "is_mega": True
        },
        {
            "name": "Crystalline Bastion",
            "participants": ["Amethyst Sentinel", "Kunzite Archon", "Sapphire Mystic", "Ice Crystal Monarch"],
            "description": "An unbreakable fortress formed from compressed geometric energy. The Archon and Sentinel channel the base minerals, while the Mystic and Monarch temper them with absolute cold.\n\n**Visual Effects:** A jagged formation of blue and purple crystal shards appearing on screen, accompanied by a deep blue flash and frost patterns.",
            "type": "Crystal/Ice",
            "is_mega": True
        },
        {
            "name": "Storm-Born Decree",
            "participants": ["Zeus Quill", "Wind Chieftain", "Cloud Master"],
            "description": "The sky itself passes judgment. The Master and Chieftain create a massive localized cyclone that Zeus uses to focus a single, planetary-scale lightning strike.\n\n**Visual Effects:** Dark grey clouds swirling in a vortex, layered with jagged yellow lightning arcs that screen-shake with intense white flashes.",
            "type": "Electric/Air/God",
            "is_mega": True
        },
        {
            "name": "Spectral Infiltration",
            "participants": ["Void Walker", "Shadow Alchemist", "Necro Flame", "Venom Shade"],
            "description": "A multi-layered assault from the spirit realm. The flame provides the distraction while the Alchemist and Shades dissolve the physical boundaries of their targets.\n\n**Visual Effects:** Sickly green fire pixels layered with purple gas clouds and a black hole-like void expanding from the center.",
            "type": "Dark/Dark/Alchemy/Spirit",
            "is_mega": True
        },
        {
            "name": "Titan's Unearthing",
            "participants": ["Titan of the Depths", "Deep-Vein Excavator", "Golem Lord", "Tunnel Vanguard"],
            "description": "Reversing the geological clock. The Heavy-Quills work in unison to pull ancient, forgotten strata to the surface, crushing anything caught in the upheaval.\n\n**Visual Effects:** Massive brown pixels slamming down with screen-shaking 'thuds', kicking up thick dust clouds and brown wooden splinter particles.",
            "type": "Earth",
            "is_mega": True
        },
        {
            "name": "Royal Alchemical Blast",
            "participants": ["King Quill", "Ruby Sovereign", "Flare Quill Alchemist"],
            "description": "Converting political power into raw energy. The Kings provide the 'sovereign weight' while the Alchemist uses it as a catalyst to trigger a ruby-colored explosion.\n\n**Visual Effects:** Three overlapping golden crown pulses followed by a massive red pixel eruption that leaves prismatic crystal fragments.",
            "type": "Royal/Alchemy/Crystal",
            "is_mega": True
        },
        {
            "name": "Universal Reset",
            "participants": ["The Gatekeeper", "Quantum Drifter", "Space Marine", "Void Navigator"],
            "description": "The ultimate fallback protocol. The Gatekeeper opens the 'backdoor' of reality, the Navigator confirms the coordinates, the Drifter warps the local space, and the Marine provides the final 'kick'.\n\n**Visual Effects:** A blinding white flash that transitions into a massive black hole void, layered with binary code digital glitch effects and star-matter particles.",
            "type": "Void/Space/Shield",
            "is_mega": True
        }
    ]
    
    # Overwrite indices 60 to 69 (the seventh 10)
    data["combo_techniques"][60:70] = curated
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Successfully curated the seventh 10 combo techniques in {json_path}.")

if __name__ == "__main__":
    curate_seventh_10()
