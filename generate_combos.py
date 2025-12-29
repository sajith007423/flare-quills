
import json

def add_combos():
    json_path = "flare_quills_data.json"
    
    combos = [
        {"name": "Steam Eruption", "participants": ["Ignis Sentinel", "Splash Mage"], "description": "A massive cloud of scalding steam that blinds and damages all enemies.", "type": "Fire/Water"},
        {"name": "Crystal Storm", "participants": ["Ice Crystal Monarch", "Storm Elder"], "description": "Frozen spikes electrified with chain lightning, shattering upon impact.", "type": "Ice/Electric"},
        {"name": "Venomous Bloom", "participants": ["Forest King", "Toxic Soul"], "description": "Erupting vines that release toxic spores, poisoning anyone they entangle.", "type": "Nature/Poison"},
        {"name": "Iron Wall", "participants": ["Inferno Soldier", "Heavy Trooper"], "description": "A reinforced line of defense that reflects all incoming projectiles.", "type": "Fire/Tech"},
        {"name": "Magnetic Pulse", "participants": ["Cyber Tech", "Spark Mage"], "description": "A powerful electromagnetic field that disables mechanical enemies.", "type": "Tech/Electric"},
        {"name": "Magma Surge", "participants": ["Magma Warden", "Pyro Clover"], "description": "Molten lava roots that trap and cremate attackers.", "type": "Fire/Nature"},
        {"name": "Lunar Eclipse", "participants": ["Shadow Warlock", "Seraphim Scout"], "description": "Blighted light that slows enemies while healing allies.", "type": "Dark/Light"},
        {"name": "Sonic Boom", "participants": ["Cloud Master", "Tribal Drummer"], "description": "A deafening roar of wind that knocks back all nearby objects.", "type": "Air/Earth"},
        {"name": "Abyssal Anchor", "participants": ["Void Walker", "Tide Caller"], "description": "Void portals that pull enemies into the depths of a dark ocean.", "type": "Dark/Water"},
        {"name": "Hellfire Chain", "participants": ["Devil Quill", "Necro Flame"], "description": "Spectral chains of fire that bind souls to the burning abyss.", "type": "Dark/Necro"},
        {"name": "Techno-Organic Growth", "participants": ["Flora Queen", "Cyber Squid"], "description": "Nanobot-infused flowers that reconstruct damaged structures.", "type": "Nature/Tech"},
        {"name": "Glacial Shield", "participants": ["Glacial Guide", "Golem Lord"], "description": "A barrier of permafrost-infused rock, nearly indestructible.", "type": "Ice/Earth"},
        {"name": "Solar Wind", "participants": ["Blaze Monk", "Spark Mage"], "description": "A high-velocity stream of ionized particles that ignites steel.", "type": "Fire/Electric"},
        {"name": "Toxic Rainfall", "participants": ["Venom Shade", "Sky Chef"], "description": "A downpour of corrosive acid hidden within harmless-looking rain.", "type": "Poison/Air"},
        {"name": "Clockwork Precision", "participants": ["Time Keeper", "Space Marine"], "description": "Temporal rifts that allow for impossibly accurate rapid fire.", "type": "Tech/Time"},
        {"name": "Aurora Barrier", "participants": ["Ice Weaver", "Seraphim Scout"], "description": "A shimmering wall of light and ice that reflects spells.", "type": "Ice/Light"},
        {"name": "Cursed Mirage", "participants": ["Cursed Pharaoh", "Void Walker"], "description": "Spectral sandstorms that cause enemies to attack their own allies.", "type": "Sand/Dark"},
        {"name": "Gourmet Explosion", "participants": ["Oktober-Quill", "Pyro Clover"], "description": "Highly unstable magma-infused hops that explode into a sticky mess.", "type": "Earth/Fire"},
        {"name": "Void Warp", "participants": ["Void Navigator", "Shadow Warlock"], "description": "Tethers enemies to parallel dimensions, splitting their current form.", "type": "Void/Dark"},
        {"name": "Thunder Stomp", "participants": ["Zeus Quill", "Golem Lord"], "description": "A stomp so powerful it summons localized lighting bolts.", "type": "Electric/Earth"},
        {"name": "Nature's Wrath", "participants": ["Lumberjack Quill", "Flora Queen"], "description": "A tidal wave of sentient logs and blooming thorns.", "type": "Wood/Nature"},
        {"name": "Mechanical Swarm", "participants": ["Flare Quill Engineer", "Cyber Tech"], "description": "Thousands of micro-drones that dismantle enemy armor systematically.", "type": "Tech/Tech"},
        {"name": "Arcane Reflection", "participants": ["Arcane Wizard", "Crystalis Spirit"], "description": "A field of crystalline shards that amplifies and splits spells.", "type": "Magic/Ice"},
        {"name": "Steam Hammer", "participants": ["Ember-Steel Smith", "Splash Mage"], "description": "A pressurized blast of steam followed by a heavy metallic strike.", "type": "Fire/Water"},
        {"name": "Electro-Net", "participants": ["Spark Mage", "Cyber Squid"], "description": "Electrified ink webs that paralyze multiple targets at once.", "type": "Electric/Water"},
        {"name": "Souldrain Vortex", "participants": ["Vampire Lord", "Void Warden"], "description": "A swirling abyss that funnels life energy from foes to the nearest ally.", "type": "Dark/Void"},
        {"name": "Emerald Flare", "participants": ["Flora Queen", "Ignis Sentinel"], "description": "A flash of brilliant green fire that rejuvenates nature and burns machines.", "type": "Nature/Fire"},
        {"name": "Tectonic Shift", "participants": ["Golem Lord", "Tribal Drummer"], "description": "Resonant earthquake frequencies that cause structures to liquefy.", "type": "Earth/Earth"},
        {"name": "Shadow Cloak", "participants": ["Shadow Warlock", "Void Walker"], "description": "A veil of total darkness that makes an entire army invisible.", "type": "Dark/Dark"},
        {"name": "Plasma Rain", "participants": ["Space Marine", "Sky Chef"], "description": "Superheated plasma dropped from high altitudes in culinary containers.", "type": "Tech/Fire"}
    ]

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        data["combo_techniques"] = combos
            
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
        print(f"Successfully added 30 combo techniques to {json_path}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    add_combos()
