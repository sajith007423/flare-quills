
import json

def curate_ninth_10():
    json_path = "flare_quills_data.json"
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    curated = [
        {
            "name": "Elemental Apex",
            "participants": ["Sapphire Mystic", "Magma Warden", "Cloud Master", "Vitality Arcanist", "Ashbound Assassin", "Tidecaller Deity"],
            "description": "A perfect convergence of the six fundamental forces. The Warden and Deity provide the earth and sea, the Master provides the sky, the Mystic and Arcanist stabilize the magic, and the Assassin delivers the finishing blow in the eye of the storm.\n\n**Visual Effects:** A rotating disk of six different colored pixels (blue, red, white, green, orange, yellow), followed by a massive white flash that levels the screen.",
            "type": "Fire/Earth/Life/Magic/Air/Water",
            "is_mega": True
        },
        {
            "name": "Divine Brunch",
            "participants": ["Breakfast Bot", "Zeus Quill", "The Hunter"],
            "description": "A meal truly fit for a god. The Hunter provides the rarest game, Zeus provides the lightning to flash-sear it, and Breakfast Bot serves it with mechanical efficiency to restore the entire team's spirits.\n\n**Visual Effects:** A rapid sequence of yellow lightning bolts hitting a tray of 'food' icons, followed by a golden aura that heals the UI edges.",
            "type": "God/Electric/Food",
            "is_mega": True
        },
        {
            "name": "Volcanic Petrification",
            "participants": ["Cursed Pharaoh", "Pyromancer", "Necro Flame", "Lumberjack Quill", "Cyber Squid", "Arcane Wizard", "Spartan Quill", "Emerald Vanquisher", "Crimson Arbalest"],
            "description": "A terrifying cross-tribal offensive. The Pharaoh's curse turns enemies to stone, while the combined fire and tech of nine specialists ensures that even the statues are vaporized into fine dust.\n\n**Visual Effects:** Screen-wide grey 'stone' filter that shatters into a massive explosion of orange and red fire pixels.",
            "type": "Sand/Undead/Fire/Tech",
            "is_mega": True
        },
        {
            "name": "Chrono-Culinary Alignment",
            "participants": ["Dark Iron Warlock", "Flare Quill Chef", "The Time Keeper", "Flare Quill Alchemist", "Chrono-Warlock"],
            "description": "Manipulating the timelines of ingredients to achieve the ultimate flavor and power. The Time Keepers ensure the meal stays fresh across aeons, while the Alchemist and Warlock infuse it with dark, potent magic.\n\n**Visual Effects:** Golden clock-face particles swirling around a bubbling purple cauldron, leaving behind glowing 'star' pixels.",
            "type": "Time/Food/Alchemy/Dark",
            "is_mega": True
        },
        {
            "name": "Frozen Tech Nova",
            "participants": ["Cyber Squid", "Frost Monarch", "Iron-Core Machinist"],
            "description": "Absolute zero powered by digital overclocking. The Machinist pushes the cooling systems to the limit while the Monarch and Squid unleash a localized ice age.\n\n**Visual Effects:** Cyan ice crystals exploding from a green neon grid, leaving frost patterns on the UI and 'static' digital glitch effects.",
            "type": "Ice/Tech/Water",
            "is_mega": True
        },
        {
            "name": "Spectral Siege",
            "participants": ["Shadow Alchemist", "Spartan Quill", "Void Warden"],
            "description": "An impenetrable defense from the void. The Warden holds the gates, the Spartan provides the steel, and the Alchemist creates a shroud of shadows to confuse the attackers.\n\n**Visual Effects:** A black hole-like void expanding from the center, protected by a ring of red pixel-shields and purple mist.",
            "type": "Dark/Void/Steel/Shield",
            "is_mega": True
        },
        {
            "name": "Gaea's Wrath",
            "participants": ["Forest King", "Golem Lord", "Deep-Vein Excavator"],
            "description": "The earth itself rises to reclaim its own. The Golem and Excavator tunnel beneath the foe while the King commands a forest of roots to drag them into the depths.\n\n**Visual Effects:** Massive brown pixels slamming down while neon green vines wrap around the screen, followed by a deep screen-shake 'thud'.",
            "type": "Nature/Earth",
            "is_mega": True
        },
        {
            "name": "Neon Spirit Pulse",
            "participants": ["Crystalis Spirit", "Cyber Tech", "Spark Mage"],
            "description": "A high-frequency energy discharge. The Spirit provides the raw essence, the Mage pumps in the voltage, and the Tech stabilizes the frequency into a lethal neon pulse.\n\n**Visual Effects:** Bright magenta and cyan rings pulsating outward, layered with jagged lightning arcs and digital data scrolls.",
            "type": "Spirit/Tech/Electric",
            "is_mega": True
        },
        {
            "name": "Abyssal Cargo Drop",
            "participants": ["Abyssal Captain", "Space Marine", "Sky Chef"],
            "description": "Strategic logistics from the deep. The Captain and Marine drop a payload of void-sealed supplies (and explosives) while the Chef ensures the delivery is 'well-seasoned'.\n\n**Visual Effects:** Translucent blue water streams falling from the top of the UI, exploding into black void clouds and floating 'crate' icons.",
            "type": "Void/Water/Space/Food",
            "is_mega": True
        },
        {
            "name": "Runic Pyre",
            "participants": ["Runic Woodcutter", "Blaze Monk", "Infernal Juggernaut"],
            "description": "Sacrificing ancient runic timber to fuel a hellish inferno. The Juggernaut anchors the site while the Woodcutter and Monk feed the flames with holy-engraved wood.\n\n**Visual Effects:** Vibrant orange fire pixels consuming glowing green runic carvings, leaving behind black charcoal residue and sparks.",
            "type": "Rune/Fire/Wood",
            "is_mega": True
        }
    ]
    
    # Overwrite indices 80 to 89 (the ninth 10)
    data["combo_techniques"][80:90] = curated
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print(f"Successfully curated the ninth 10 combo techniques in {json_path}.")

if __name__ == "__main__":
    curate_ninth_10()
