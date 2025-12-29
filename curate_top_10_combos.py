
import json

def curate_top_10():
    json_path = "flare_quills_data.json"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    curated = [
        {
            "name": "The Primordial Surge",
            "participants": ["Ignis Sentinel", "Splash Mage", "Golem Lord"],
            "description": "A legendary elemental fusion where fire, water, and earth collide. The Sentinel's flames are cooled by the Mage's splash, creating high-pressure steam that the Golem Lord directs with tectonic force.\n\n**Visual Effects:** A volcanic eruption of red and blue pixels, followed by heavy brown boulders slamming down through a thick white steam cloud.",
            "type": "Fire/Water/Earth",
            "is_mega": True
        },
        {
            "name": "Abyssal Silence",
            "participants": ["Shadow Warlock", "Void Warden"],
            "description": "A terrifying technique that erases sound and light. The Warlock weaves a web of shadow while the Warden expands a void cage, trapping enemies in an absolute sensory vacuum.\n\n**Visual Effects:** A black hole-like void expanding from the center, sucking in all nearby light and leaving only a faint, spooky purple outline.",
            "type": "Dark/Void",
            "is_mega": False
        },
        {
            "name": "Verdant Blitz",
            "participants": ["Forest King", "Flora Queen", "Zeus Quill"],
            "description": "Nature's ultimate retribution. The King and Queen accelerate the growth of massive vines, while Zeus Quill electrifies them to turn the entire battlefield into a shocking emerald cage.\n\n**Visual Effects:** Rapidly spiraling green vines crackling with jagged yellow lightning arcs that screen-shake on impact.",
            "type": "Nature/Electric",
            "is_mega": True
        },
        {
            "name": "Clockwork Siege",
            "participants": ["Iron-Core Machinist", "Flare Quill Engineer", "Cyber Tech"],
            "description": "The pinnacle of Iron Legion engineering. The Engineer coordinates a tactical assault using the Machinist's defense and Cyber Tech's digital analysis to dismantle enemy formations.\n\n**Visual Effects:** Green neon grid lines expanding outward while heavy metal pillars smash down, accompanied by digital glitch effects.",
            "type": "Tech/Steel",
            "is_mega": True
        },
        {
            "name": "Frozen Echo",
            "participants": ["Ice Crystal Monarch", "Frost Monarch", "Glacial Guide"],
            "description": "The three masters of the north combine to bring a perennial winter. The blizzard they create is so thick it echoes with the whispers of ancient ice spirits.\n\n**Visual Effects:** A blinding white flash transitioning into a dense blizzard of cyan crystals, leaving frost patterns on the UI.",
            "type": "Ice",
            "is_mega": True
        },
        {
            "name": "Solar Purge",
            "participants": ["Seraphim Scout", "Blaze Monk", "Magma Warden"],
            "description": "A divine light coupled with subterranean heat. The Scout illuminates the target for a focused bombardment by the Monk and Warden, turning the ground into molten glass.\n\n**Visual Effects:** Beams of golden light stabbing through the darkness, followed by vibrant red pixels erupting in a massive radial burst.",
            "type": "Light/Fire/Earth",
            "is_mega": True
        },
        {
            "name": "Tidecaller's Wrath",
            "participants": ["Tide Caller", "Splash Mage", "Titan of the Depths", "Cyber Squid"],
            "description": "The ocean's deepest secrets rise to the surface. A massive tsunami is channeled through Cyber Squid's tech-tentacles while the Titan anchors the pressure.\n\n**Visual Effects:** Massive blue particle streams cascading across the screen, layered with green digital hexadecimal particles and heavy brown mud clouds.",
            "type": "Water/Tech/Earth",
            "is_mega": True
        },
        {
            "name": "Venomous Thicket",
            "participants": ["Venomous King", "Toxic Soul", "Forest King"],
            "description": "A deadly maze of thorns and gas. The Kings grow a forest of poison-tipped vines that the Toxic Soul saturates with corrosive miasma.\n\n**Visual Effects:** Sickly green gas clouds drifting through spiraling green vines, with bubbling purple acid particles popping on impact.",
            "type": "Poison/Nature",
            "is_mega": True
        },
        {
            "name": "Stormbringer Phalanx",
            "participants": ["Storm Elder", "Iron-Core Machinist", "Zeus Quill"],
            "description": "A storm-powered defensive formation. The Machinist builds a conductive lattice while the Elder and Zeus charge it with enough electricity to power a city.\n\n**Visual Effects:** Jagged cyan lightning arcs jumping between participants, screen-shaking on impact, while neon grid lines pulsate in the background.",
            "type": "Electric/Tech",
            "is_mega": True
        },
        {
            "name": "The Universal Singularity",
            "participants": ["Ignis Sentinel", "Splash Mage", "Forest King", "Volt Sage", "Ice Emperor", "Golem Lord", "Cyber Tech", "Shadow Warlock", "Seraphim Scout", "Venomous King"],
            "description": "The ultimate display of harmony between all ten elements. A momentary collapse of the physical realm into a single point of infinite potential, resetting the battlefield.\n\n**Visual Effects:** A blinding white flash followed by a prismatic shockwave of every elemental color, ending with a massive black hole void that sucks in everything.",
            "type": "Ultimate/Omni",
            "is_mega": True
        }
    ]
    
    # Overwrite the first 10
    data["combo_techniques"][:10] = curated
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Successfully curated the top 10 combo techniques in {json_path}.")

if __name__ == "__main__":
    curate_top_10()
