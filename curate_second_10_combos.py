
import json

def curate_second_10():
    json_path = "flare_quills_data.json"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    curated = [
        {
            "name": "Gale-Force Symphony",
            "participants": ["Wind Chieftain", "Tsar Quill", "Sky Chef"],
            "description": "A soaring masterpiece of air and sound. The Chieftain's cyclones carry the Tsar's heroic melodies across the clouds, while the Sky Chef seasons the winds with aromatic spices that confuse and delight the enemy.\n\n**Visual Effects:** Swirling white pixel-dust and musical note particles dancing through a golden-yellow skybox, accompanied by blurred heat-wave ripples.",
            "type": "Air/Sound/Food",
            "is_mega": True
        },
        {
            "name": "Crystalline Aegis",
            "participants": ["Amethyst Sentinel", "Kunzite Archon", "Titan of the Depths"],
            "description": "An unbreakable geological fortress. The Sentinel and Archon project a lattice of purple and pink crystals, anchored by the Titan's mountain-moving strength, creating a barrier that reflects all projectiles.\n\n**Visual Effects:** A grid of glowing magenta and violet crystal shards expanding from the center, leaving a permanent frost pattern on the battlefield floor.",
            "type": "Crystal/Earth/Mythic",
            "is_mega": True
        },
        {
            "name": "Bio-Luminescent Bloom",
            "participants": ["Pyro Clover", "Vitality Arcanist", "Abyssal Diver"],
            "description": "A strange ecology of fire, life, and the deep sea. The Clover's heat sparks a rapid growth in the Arcanist's seeds, while the Diver's pressurized water keeps the plants glowing with intense, radioactive light.\n\n**Visual Effects:** Neon green and blue vines spiraling upward, interspersed with bright white light beams and bubbling blue water particles.",
            "type": "Fire/Nature/Water/Void",
            "is_mega": True
        },
        {
            "name": "Ironclad Judgment",
            "participants": ["Spartan Quill", "Highlander", "Iron-Core Machinist"],
            "description": "The ultimate tactical formation. The Spartan and Highlander hold the line with shield and claymore, while the Machinist calculates the perfect moment to release a high-frequency shockwave through their steel.\n\n**Visual Effects:** Massive grey metal pillars slamming down with a screen-shaking 'thud', followed by jagged lightning arcs jumping between the shields.",
            "type": "Steel/Wind/Tech",
            "is_mega": True
        },
        {
            "name": "Nebula Feast",
            "participants": ["Nebula Spellweaver", "Abyssal Diver", "Flare Quill Chef"],
            "description": "A celestial banquet from the edge of the universe. The Spellweaver condenses star-matter into ingredients that the Diver retrieves from the void, which the Chef then sautés into a supernova of flavor.\n\n**Visual Effects:** A prismatic shockwave of glowing purple pixel-dust layered with translucent blue water streams and floating hexadecimal 'recipe' particles.",
            "type": "Star/Void/Food",
            "is_mega": True
        },
        {
            "name": "Static Mirage",
            "participants": ["Cyber Squid", "Volt Sage", "Quantum Drifter"],
            "description": "A digital hallucination that electrocutes the senses. The Squid and Sage saturate the air with ionized particles while the Drifter warps space-time, making it impossible for enemies to find the true source of the shocks.\n\n**Visual Effects:** Jagged cyan lightning arcs interspersed with green digital glitch effects and a black hole-like void that warps the surrounding pixels.",
            "type": "Electric/Tech/Void",
            "is_mega": True
        },
        {
            "name": "Tomb of the Sun-King",
            "participants": ["Cursed Pharaoh", "Ignis Sentinel", "Blaze Monk"],
            "description": "An ancient hex fueled by solar fire. The Pharaoh summons the buried sands while the Sentinel and Monk ignite the air, trapping foes in a glass-walled tomb of searing heat.\n\n**Visual Effects:** Golden sand particles swirling in a massive vortex, layered with vibrant red pixel eruptions and heat distortion ripples.",
            "type": "Sand/Undead/Fire",
            "is_mega": True
        },
        {
            "name": "Oceanic Overdrive",
            "participants": ["Cyber Squid", "Tide Caller", "Splash Mage"],
            "description": "A hydraulic mechanical assault. The Tide Caller control the currents to feed the Squid's high-pressure water jets, while the Splash Mage adds volatile bubble clusters to the mix.\n\n**Visual Effects:** High-speed blue particle streams and white splash effects, layered with green neon grid lines and mechanical HUD overlays.",
            "type": "Water/Tech",
            "is_mega": True
        },
        {
            "name": "Spectral Harvest",
            "participants": ["Shadow Alchemist", "Skull Shaman", "Necro Flame"],
            "description": "A dark alchemy that converts spirit energy into raw power. The Shaman calls the souls, the Alchemist stabilizes the mixture, and the Necro Flame ignites it into a terrifying green firestorm.\n\n**Visual Effects:** Sickly green gas clouds and purple miasmic particles swirling around a black void, with green fire pixels erupting at the edges.",
            "type": "Dark/Spirit/Necro",
            "is_mega": True
        },
        {
            "name": "Titan's Forge",
            "participants": ["Mythic Blacksmith", "Ember-Steel Smith", "Titan of the Depths"],
            "description": "The creation of a god-tier weapon mid-combat. The Titans of the forge hammer the core elements of the earth together using star-metal and volcanic heat, causing the ground to pulse with the rhythm of creation.\n\n**Visual Effects:** Massive white-hot sparks and radial orange fire bursts, accompanied by a heavy screen-shake and brown dust clouds from the hammer blows.",
            "type": "Fire/Steel/Mythic/Earth",
            "is_mega": True
        }
    ]
    
    # Overwrite indices 10 to 19 (the second 10)
    data["combo_techniques"][10:20] = curated
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Successfully curated the second 10 combo techniques in {json_path}.")

if __name__ == "__main__":
    curate_second_10()
