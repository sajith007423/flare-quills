const comboTechniquesData = {
    "combo_techniques": [
        {
            "name": "The Primordial Surge",
            "participants": [
                "Ignis Sentinel",
                "Splash Mage",
                "Golem Lord"
            ],
            "description": "A legendary elemental fusion where fire, water, and earth collide. The Sentinel's flames are cooled by the Mage's splash, creating high-pressure steam that the Golem Lord directs with tectonic force.\n\n**Visual Effects:** A volcanic eruption of red and blue pixels, followed by heavy brown boulders slamming down through a thick white steam cloud.",
            "type": "Fire/Water/Earth",
            "is_mega": true
        },
        {
            "name": "Abyssal Silence",
            "participants": [
                "Shadow Warlock",
                "Void Warden"
            ],
            "description": "A terrifying technique that erases sound and light. The Warlock weaves a web of shadow while the Warden expands a void cage, trapping enemies in an absolute sensory vacuum.\n\n**Visual Effects:** A black hole-like void expanding from the center, sucking in all nearby light and leaving only a faint, spooky purple outline.",
            "type": "Dark/Void",
            "is_mega": false
        },
        {
            "name": "Verdant Blitz",
            "participants": [
                "Forest King",
                "Flora Queen",
                "Zeus Quill"
            ],
            "description": "Nature's ultimate retribution. The King and Queen accelerate the growth of massive vines, while Zeus Quill electrifies them to turn the entire battlefield into a shocking emerald cage.\n\n**Visual Effects:** Rapidly spiraling green vines crackling with jagged yellow lightning arcs that screen-shake on impact.",
            "type": "Nature/Electric",
            "is_mega": true
        },
        {
            "name": "Clockwork Siege",
            "participants": [
                "Iron-Core Machinist",
                "Flare Quill Engineer",
                "Cyber Tech"
            ],
            "description": "The pinnacle of Iron Legion engineering. The Engineer coordinates a tactical assault using the Machinist's defense and Cyber Tech's digital analysis to dismantle enemy formations.\n\n**Visual Effects:** Green neon grid lines expanding outward while heavy metal pillars smash down, accompanied by digital glitch effects.",
            "type": "Tech/Steel",
            "is_mega": true
        },
        {
            "name": "Frozen Echo",
            "participants": [
                "Ice Crystal Monarch",
                "Frost Monarch",
                "Glacial Guide"
            ],
            "description": "The three masters of the north combine to bring a perennial winter. The blizzard they create is so thick it echoes with the whispers of ancient ice spirits.\n\n**Visual Effects:** A blinding white flash transitioning into a dense blizzard of cyan crystals, leaving frost patterns on the UI.",
            "type": "Ice",
            "is_mega": true
        },
        {
            "name": "Solar Purge",
            "participants": [
                "Seraphim Scout",
                "Blaze Monk",
                "Magma Warden"
            ],
            "description": "A divine light coupled with subterranean heat. The Scout illuminates the target for a focused bombardment by the Monk and Warden, turning the ground into molten glass.\n\n**Visual Effects:** Beams of golden light stabbing through the darkness, followed by vibrant red pixels erupting in a massive radial burst.",
            "type": "Light/Fire/Earth",
            "is_mega": true
        },
        {
            "name": "Tidecaller's Wrath",
            "participants": [
                "Tide Caller",
                "Splash Mage",
                "Titan of the Depths",
                "Cyber Squid"
            ],
            "description": "The ocean's deepest secrets rise to the surface. A massive tsunami is channeled through Cyber Squid's tech-tentacles while the Titan anchors the pressure.\n\n**Visual Effects:** Massive blue particle streams cascading across the screen, layered with green digital hexadecimal particles and heavy brown mud clouds.",
            "type": "Water/Tech/Earth",
            "is_mega": true
        },
        {
            "name": "Venomous Thicket",
            "participants": [
                "Venomous King",
                "Toxic Soul",
                "Forest King"
            ],
            "description": "A deadly maze of thorns and gas. The Kings grow a forest of poison-tipped vines that the Toxic Soul saturates with corrosive miasma.\n\n**Visual Effects:** Sickly green gas clouds drifting through spiraling green vines, with bubbling purple acid particles popping on impact.",
            "type": "Poison/Nature",
            "is_mega": true
        },
        {
            "name": "Stormbringer Phalanx",
            "participants": [
                "Storm Elder",
                "Iron-Core Machinist",
                "Zeus Quill"
            ],
            "description": "A storm-powered defensive formation. The Machinist builds a conductive lattice while the Elder and Zeus charge it with enough electricity to power a city.\n\n**Visual Effects:** Jagged cyan lightning arcs jumping between participants, screen-shaking on impact, while neon grid lines pulsate in the background.",
            "type": "Electric/Tech",
            "is_mega": true
        },
        {
            "name": "The Universal Singularity",
            "participants": [
                "Ignis Sentinel",
                "Splash Mage",
                "Forest King",
                "Volt Sage",
                "Ice Emperor",
                "Golem Lord",
                "Cyber Tech",
                "Shadow Warlock",
                "Seraphim Scout",
                "Venomous King"
            ],
            "description": "The ultimate display of harmony between all ten elements. A momentary collapse of the physical realm into a single point of infinite potential, resetting the battlefield.\n\n**Visual Effects:** A blinding white flash followed by a prismatic shockwave of every elemental color, ending with a massive black hole void that sucks in everything.",
            "type": "Ultimate/Omni",
            "is_mega": true
        },
        {
            "name": "Gale-Force Symphony",
            "participants": [
                "Wind Chieftain",
                "Tsar Quill",
                "Sky Chef"
            ],
            "description": "A soaring masterpiece of air and sound. The Chieftain's cyclones carry the Tsar's heroic melodies across the clouds, while the Sky Chef seasons the winds with aromatic spices that confuse and delight the enemy.\n\n**Visual Effects:** Swirling white pixel-dust and musical note particles dancing through a golden-yellow skybox, accompanied by blurred heat-wave ripples.",
            "type": "Air/Sound/Food",
            "is_mega": true
        },
        {
            "name": "Crystalline Aegis",
            "participants": [
                "Amethyst Sentinel",
                "Kunzite Archon",
                "Titan of the Depths"
            ],
            "description": "An unbreakable geological fortress. The Sentinel and Archon project a lattice of purple and pink crystals, anchored by the Titan's mountain-moving strength, creating a barrier that reflects all projectiles.\n\n**Visual Effects:** A grid of glowing magenta and violet crystal shards expanding from the center, leaving a permanent frost pattern on the battlefield floor.",
            "type": "Crystal/Earth/Mythic",
            "is_mega": true
        },
        {
            "name": "Bio-Luminescent Bloom",
            "participants": [
                "Pyro Clover",
                "Vitality Arcanist",
                "Abyssal Diver"
            ],
            "description": "A strange ecology of fire, life, and the deep sea. The Clover's heat sparks a rapid growth in the Arcanist's seeds, while the Diver's pressurized water keeps the plants glowing with intense, radioactive light.\n\n**Visual Effects:** Neon green and blue vines spiraling upward, interspersed with bright white light beams and bubbling blue water particles.",
            "type": "Fire/Nature/Water/Void",
            "is_mega": true
        },
        {
            "name": "Ironclad Judgment",
            "participants": [
                "Spartan Quill",
                "Highlander",
                "Iron-Core Machinist"
            ],
            "description": "The ultimate tactical formation. The Spartan and Highlander hold the line with shield and claymore, while the Machinist calculates the perfect moment to release a high-frequency shockwave through their steel.\n\n**Visual Effects:** Massive grey metal pillars slamming down with a screen-shaking 'thud', followed by jagged lightning arcs jumping between the shields.",
            "type": "Steel/Wind/Tech",
            "is_mega": true
        },
        {
            "name": "Nebula Feast",
            "participants": [
                "Nebula Spellweaver",
                "Abyssal Diver",
                "Flare Quill Chef"
            ],
            "description": "A celestial banquet from the edge of the universe. The Spellweaver condenses star-matter into ingredients that the Diver retrieves from the void, which the Chef then saut\u00e9s into a supernova of flavor.\n\n**Visual Effects:** A prismatic shockwave of glowing purple pixel-dust layered with translucent blue water streams and floating hexadecimal 'recipe' particles.",
            "type": "Star/Void/Food",
            "is_mega": true
        },
        {
            "name": "Static Mirage",
            "participants": [
                "Cyber Squid",
                "Volt Sage",
                "Quantum Drifter"
            ],
            "description": "A digital hallucination that electrocutes the senses. The Squid and Sage saturate the air with ionized particles while the Drifter warps space-time, making it impossible for enemies to find the true source of the shocks.\n\n**Visual Effects:** Jagged cyan lightning arcs interspersed with green digital glitch effects and a black hole-like void that warps the surrounding pixels.",
            "type": "Electric/Tech/Void",
            "is_mega": true
        },
        {
            "name": "Tomb of the Sun-King",
            "participants": [
                "Cursed Pharaoh",
                "Ignis Sentinel",
                "Blaze Monk"
            ],
            "description": "An ancient hex fueled by solar fire. The Pharaoh summons the buried sands while the Sentinel and Monk ignite the air, trapping foes in a glass-walled tomb of searing heat.\n\n**Visual Effects:** Golden sand particles swirling in a massive vortex, layered with vibrant red pixel eruptions and heat distortion ripples.",
            "type": "Sand/Undead/Fire",
            "is_mega": true
        },
        {
            "name": "Oceanic Overdrive",
            "participants": [
                "Cyber Squid",
                "Tide Caller",
                "Splash Mage"
            ],
            "description": "A hydraulic mechanical assault. The Tide Caller control the currents to feed the Squid's high-pressure water jets, while the Splash Mage adds volatile bubble clusters to the mix.\n\n**Visual Effects:** High-speed blue particle streams and white splash effects, layered with green neon grid lines and mechanical HUD overlays.",
            "type": "Water/Tech",
            "is_mega": true
        },
        {
            "name": "Spectral Harvest",
            "participants": [
                "Shadow Alchemist",
                "Skull Shaman",
                "Necro Flame"
            ],
            "description": "A dark alchemy that converts spirit energy into raw power. The Shaman calls the souls, the Alchemist stabilizes the mixture, and the Necro Flame ignites it into a terrifying green firestorm.\n\n**Visual Effects:** Sickly green gas clouds and purple miasmic particles swirling around a black void, with green fire pixels erupting at the edges.",
            "type": "Dark/Spirit/Necro",
            "is_mega": true
        },
        {
            "name": "Titan's Forge",
            "participants": [
                "Mythic Blacksmith",
                "Ember-Steel Smith",
                "Titan of the Depths"
            ],
            "description": "The creation of a god-tier weapon mid-combat. The Titans of the forge hammer the core elements of the earth together using star-metal and volcanic heat, causing the ground to pulse with the rhythm of creation.\n\n**Visual Effects:** Massive white-hot sparks and radial orange fire bursts, accompanied by a heavy screen-shake and brown dust clouds from the hammer blows.",
            "type": "Fire/Steel/Mythic/Earth",
            "is_mega": true
        },
        {
            "name": "Abyssal Feedback",
            "participants": [
                "Abyssal Diver",
                "Volt Sage",
                "Void Warden"
            ],
            "description": "A high-risk underwater containment field. The Diver stabilizes the pressure while the Sage pumps high-voltage currents into the Warden's void cage, creating a localized event horizon of pure energy.\n\n**Visual Effects:** A black hole-like void expanding from the center, layered with jagged yellow and cyan lightning arcs that flicker with digital glitch effects.",
            "type": "Void/Water/Electric",
            "is_mega": true
        },
        {
            "name": "Emerald Flare",
            "participants": [
                "Flora Queen",
                "Ignis Sentinel",
                "Runic Woodcutter"
            ],
            "description": "The ritual of the burning grove. The Queen and Woodcutter sacrifice ancient runic timber to fuel the Sentinel's flames, resulting in a holy fire that purges corruption and incinerates armor.\n\n**Visual Effects:** Rapidly spiraling green vines engulfed in vibrant orange pixels, leaving behind charcoal-black residues and glowing runic embers.",
            "type": "Nature/Fire/Wood/Rune",
            "is_mega": true
        },
        {
            "name": "Machina Deluge",
            "participants": [
                "Iron-Core Machinist",
                "Splash Mage",
                "Cyber Squid"
            ],
            "description": "An automated flood system. The Machinist builds a network of high-pressure pipes that the Mage fills with volatile liquid, while the Squid uses its tentacles to fire concentrated beams of water.\n\n**Visual Effects:** High-speed blue particle streams spraying across the UI, layered with green neon grid lines and floating hexadecimal data scrolls.",
            "type": "Tech/Water",
            "is_mega": true
        },
        {
            "name": "Cursed Geyser",
            "participants": [
                "Cursed Pharaoh",
                "Tide Caller",
                "Toxic Soul"
            ],
            "description": "The ocean's most toxic secret. The Pharaoh's ancient curse transforms the Tide Caller's waves into a boiling sludge of corrosive waste, manipulated by the Toxic Soul to target specific enemies.\n\n**Visual Effects:** Sickly green gas clouds drifting over massive blue particle streams, with purple acid bubbles popping and leaving 'poisoned' status overlays.",
            "type": "Sand/Water/Poison",
            "is_mega": true
        },
        {
            "name": "Prismatic Waltz",
            "participants": [
                "Seraphim Scout",
                "Sapphire Mystic",
                "Pyromancer"
            ],
            "description": "A lethal dance of light and flame. The Scout's holy beams are refracted through the Mystic's crystal armor, while the Pyromancer adds a swirling inferno to create a mesmerizing, deadly light show.\n\n**Visual Effects:** Blinding white light beams stabbing through a radial fire burst, with blue crystal shards spinning and reflecting the light into multiple rainbows.",
            "type": "Light/Ice/Fire",
            "is_mega": true
        },
        {
            "name": "Terran Overload",
            "participants": [
                "Golem Lord",
                "Zeus Quill",
                "Deep-Vein Excavator"
            ],
            "description": "A tectonic discharge from the world's core. The Golem and Excavator pull stones from the deep earth while Zeus strikes them with lightning upon impact, turning every boulder into a massive ionic bomb.\n\n**Visual Effects:** Heavy brown pixels slamming down with screen-shaking 'thuds', followed by explosive cyan lightning arcs that illuminate the entire combat zone.",
            "type": "Earth/Electric",
            "is_mega": true
        },
        {
            "name": "Star-Crossed Blades",
            "participants": [
                "Royal Spellblade",
                "Void Navigator",
                "Spartan Quill"
            ],
            "description": "A tactical assault from a different dimension. The Navigator opens a star-gate, allowing the Spellblade and Spartan to strike from multiple angles simultaneously, their blades leaving trails of cosmic energy.\n\n**Visual Effects:** Thin purple and silver pixel trails following the character icons as they dash, with a central white flash that leaves a constellation pattern on the screen.",
            "type": "Magic/Void/Steel",
            "is_mega": true
        },
        {
            "name": "Blighted Harvest",
            "participants": [
                "Venomous King",
                "Forest King",
                "Skull Shaman"
            ],
            "description": "The cycle of growth and decay turned into a weapon. The Forest King accelerates growth only for the Venomous King to rot it, while the Shaman channels the resulting necro-energy into a devastating wave of blight.\n\n**Visual Effects:** Rapidly growing green vines that wither and turn grey in real-time, releasing clouds of purple gas and shadowy spirit manifestations.",
            "type": "Nature/Poison/Dark",
            "is_mega": true
        },
        {
            "name": "Glacial Siege",
            "participants": [
                "Frost Monarch",
                "Highlander",
                "Ice Crystal Monarch"
            ],
            "description": "The north's final stand. The Monarchs freeze the very air to create a jagged icy fortress, while the Highlander defends the walls with a massive, frost-enchanted claymore.\n\n**Visual Effects:** A dense blizzard of cyan crystals accompanied by a deep blue flash that leaves frost patterns and heavy blue pillars on the UI.",
            "type": "Ice/Wind",
            "is_mega": true
        },
        {
            "name": "Alchemical Nova",
            "participants": [
                "Flare Quill Alchemist",
                "Blaze Monk",
                "Molten Forge-Lord"
            ],
            "description": "The ultimate transformation of matter. The Alchemist uses the Monk's fire and the Forge-Lord's metal as base components to trigger a chain reaction that converts the entire battlefield into pure energy.\n\n**Visual Effects:** A blinding white flash that transitions into vibrant orange and red pixels erupting outward, with golden sparks and heat distortion ripples.",
            "type": "Alchemy/Fire",
            "is_mega": true
        },
        {
            "name": "Haunted Harvest",
            "participants": [
                "Oktober-Quill",
                "Necro Flame",
                "Forest King"
            ],
            "description": "The autumnal ritual of the departed. Oktober-Quill's spectral pumpkins are carved with Necro Flame's green fire, while the Forest King provides a backdrop of decaying wood to amplify the spooky energy.\n\n**Visual Effects:** Glowing orange pumpkin pixels floating in a circle, exploding into green fire particles and withered brown leaves.",
            "type": "Wood/Dark/Fire",
            "is_mega": true
        },
        {
            "name": "Cyber-Coffee Overload",
            "participants": [
                "Barista Bot 9000",
                "Cyber Tech",
                "Breakfast Bot"
            ],
            "description": "The ultimate morning routine. Barista Bot 9000's high-pressure espresso is infused with Cyber Tech's overclocking algorithms, delivered via Breakfast Bot's rapid-fire serving systems.\n\n**Visual Effects:** Brown steaming liquid particles spraying across the screen, layered with green digital grid lines and floating 'energy bar' icons.",
            "type": "Water/Tech/Food",
            "is_mega": true
        },
        {
            "name": "Crimson Phalanx",
            "participants": [
                "Crimson Shade",
                "Crimson Arbalest",
                "Spartan Quill"
            ],
            "description": "A blood-red defensive wall. Shade and Arbalest provide long-range fire support while the Spartan anchors the formation, turning the battlefield into a field of crimson steel.\n\n**Visual Effects:** A rain of red pixel-arrows stabbing into the ground, followed by a massive red shield pulse that knocks back all nearby enemies.",
            "type": "Dark/Fire/Steel",
            "is_mega": true
        },
        {
            "name": "Echoes of the Arena",
            "participants": [
                "El Mariachi",
                "Tiger Eye Warrior",
                "Highlander"
            ],
            "description": "A heroic anthem for the front lines. El Mariachi's strings vibrate with the intensity of the Tiger Eye's strikes, while the Highlander's war cries add a layer of intimidation to the sonic wave.\n\n**Visual Effects:** Gold and red soundwave rings pulsating outward, accompanied by blurred 'afterimage' trails of the character icons as they swing their weapons.",
            "type": "Sound/Earth/Wind",
            "is_mega": true
        },
        {
            "name": "Industrial Blizzard",
            "participants": [
                "Frost Wizard",
                "Iron-Core Machinist",
                "Sanitation Sentinel"
            ],
            "description": "A mechanical winter. The Wizard's frost is channeled through the Machinist's cooling vents, while the Sanitation Sentinel scrubs the air of heat, creating a perma-frost zone.\n\n**Visual Effects:** Dense white pixel-fog and cyan ice crystals blowing out of mechanical pipes, leaving grey 'slush' patterns on the UI.",
            "type": "Ice/Tech",
            "is_mega": true
        },
        {
            "name": "Toxic Broadcast",
            "participants": [
                "Broadcast Unit",
                "Toxic Soul",
                "Cinema Bot"
            ],
            "description": "The spread of viral corruption. The Broadcast Unit amplifies the Toxic Soul's miasma through inter-dimensional airwaves, while Cinema Bot proyekts terrifying images to paralyze the foe.\n\n**Visual Effects:** Static-filled purple gas clouds and digital glitch effects, with flickering 'low signal' warnings and skull icons appearing on the UI.",
            "type": "Poison/Tech/Void",
            "is_mega": true
        },
        {
            "name": "Magmatic Gastronomy",
            "participants": [
                "Abyssal Diver",
                "Flare Quill Chef",
                "Magma Warden"
            ],
            "description": "Cooking with the core's heat. The Diver retrieves rare deep-sea spices while the Warden provides the perfect volcanic hearth for the Chef to prepare a truly explosive meal.\n\n**Visual Effects:** Bubbling blue water mixing with orange lava pixels, ending in a massive fire-flecked splash that leaves 'steam' particles everywhere.",
            "type": "Fire/Water/Food",
            "is_mega": true
        },
        {
            "name": "Emerald Infiltration",
            "participants": [
                "Emerald Vanquisher",
                "Shadow Warlock",
                "Runic Woodcutter"
            ],
            "description": "Nature's stealthy vengeance. The Vanquisher moves through the shadows created by the Warlock, using the Woodcutter's runic carvings to silence their passage through the forest.\n\n**Visual Effects:** Green and black pixel-shroud masks the character icons, followed by sudden green flashes and wooden splinter particles from unseen strikes.",
            "type": "Nature/Dark/Rune",
            "is_mega": true
        },
        {
            "name": "Solar Juggernaut",
            "participants": [
                "Infernal Juggernaut",
                "Seraphim Scout",
                "Ignis Sentinel"
            ],
            "description": "The unstoppable herald of light. The Juggernaut's armor is blessed with holy light by the Scout and ignited by the Sentinel, turning the tank into a living sun-bomb.\n\n**Visual Effects:** A blinding golden-white trail following a massive red-and-orange icon, ending in a screen-clearing explosion of pure white and yellow pixels.",
            "type": "Fire/Light/Mythic",
            "is_mega": true
        },
        {
            "name": "Quantum Quarantine",
            "participants": [
                "Quantum Drifter",
                "Void Warden",
                "Cyber Tech"
            ],
            "description": "An inter-dimensional containment protocol. The Drifter warps the space-time around the target while the Warden locks the cage, and Cyber Tech stabilizers the erratic energy.\n\n**Visual Effects:** A black hole void layered with vibrating purple grid lines and digital hexadecimal particles that 'freeze' in mid-air.",
            "type": "Void/Time/Tech",
            "is_mega": true
        },
        {
            "name": "Chrono-Stellar Rift",
            "participants": [
                "The Time Keeper",
                "Void Navigator",
                "Nebula Spellweaver"
            ],
            "description": "A collapse of time and space. The Navigator points the way, the Spellweaver powers the gate, and the Time Keeper ensures the event remains stable long enough to erase the targets from history.\n\n**Visual Effects:** Purple star-matter particles drifting through a distorted temporal field, ending in a massive white clock-face that shatters into glass-like shards.",
            "type": "Time/Void/Star",
            "is_mega": true
        },
        {
            "name": "Midnight Serenade",
            "participants": [
                "Tsar Quill",
                "Shadow Warlock",
                "El Mariachi"
            ],
            "description": "A hauntingly beautiful melody that drains the light from the room. The Tsar's epic song is twisted by the Warlock's dark magic, while El Mariachi provides a rhythmic pulse that echoes through the shadows.\n\n**Visual Effects:** Magenta and black musical notes swirling in a vortex, with ghostly purple flames appearing and disappearing to the beat.",
            "type": "Ice/Dark/Sound",
            "is_mega": true
        },
        {
            "name": "Frostfire Forge",
            "participants": [
                "Mythic Blacksmith",
                "Frost Monarch",
                "Glacial Guide"
            ],
            "description": "A legendary forge technique where absolute zero meets star-metal heat. The resulting thermal shock shatters even the strongest armor.\n\n**Visual Effects:** Vibrant red fire pixels clashing with cyan ice crystals, creating a massive white steam explosion that leaves frost on the UI edges and heat waves in the center.",
            "type": "Fire/Ice/Mythic",
            "is_mega": true
        },
        {
            "name": "Tectonic Thunder",
            "participants": [
                "Golem Lord",
                "Zeus Quill",
                "Tribal Drummer"
            ],
            "description": "A rhythmic assault on the bedrock. The Drummer sets the pace, the Golem stomps the ground, and Zeus punctuates every beat with a bolt from the heavens.\n\n**Visual Effects:** Screen-shaking brown dust clouds synchronized with yellow lightning strikes and gold soundwave rings.",
            "type": "Earth/Electric/God",
            "is_mega": true
        },
        {
            "name": "Arcane Harvest",
            "participants": [
                "Forest King",
                "Vitality Arcanist",
                "Runic Woodcutter"
            ],
            "description": "The rapid acceleration of the natural cycle. The King and Woodcutter prepare the ground with runic timber, while the Arcanist pours pure life-force into it, causing a jungle to grow and consume the enemy in seconds.\n\n**Visual Effects:** Rapidly spiraling emerald vines layered with white light beams and exploding 'seed' particles that leave green leaves everywhere.",
            "type": "Nature/Rune/Life",
            "is_mega": true
        },
        {
            "name": "Bio-Toxic Breach",
            "participants": [
                "Venomous King",
                "Cyber Squid",
                "Toxic Soul"
            ],
            "description": "A fusion of biological warfare and mechanical precision. The Squid injects the Toxic Soul's miasma directly into the enemy's weak points using tech-enhanced tentacles.\n\n**Visual Effects:** Blue water jets turning sickly green mid-air, layered with purple gas clouds and digital glitch effects.",
            "type": "Poison/Water/Tech",
            "is_mega": true
        },
        {
            "name": "Royal Vanguard",
            "participants": [
                "King Quill",
                "Spartan Quill",
                "Highlander"
            ],
            "description": "The ultimate defensive line of the Quill kingdom. Three generations of leaders standing back-to-back, creating a golden aura of invincibility.\n\n**Visual Effects:** Three overlapping golden shield pulses followed by a massive white light flash and golden crown particles.",
            "type": "Royal/Steel/Wind",
            "is_mega": true
        },
        {
            "name": "The Feast of Souls",
            "participants": [
                "Abyssal Diver",
                "Flare Quill Chef",
                "Void Warden"
            ],
            "description": "A meal so deep and dark it consumes the diner's spirit. The Diver finds the ingredients in the void, the Warden keeps them contained, and the Chef seasons them with existential dread.\n\n**Visual Effects:** Black hole-void pulses layered with floating recipe hexadecimal particles and blue water bubbles.",
            "type": "Void/Food/Shield",
            "is_mega": true
        },
        {
            "name": "Infernal Logistics",
            "participants": [
                "Iron-Core Machinist",
                "Ember-Steel Smith",
                "Molten Forge-Lord"
            ],
            "description": "The Iron Legion's production line turned into a weapon of war. A continuous stream of white-hot steel and clockwork precision that grinds anything in its path.\n\n**Visual Effects:** Red-hot metal sparks and green neon grid lines, with massive grey pillars slamming down in a rapid, machine-like rhythm.",
            "type": "Tech/Steel/Fire",
            "is_mega": true
        },
        {
            "name": "Celestial Aligment",
            "participants": [
                "Seraphim Scout",
                "Void Navigator",
                "Nebula Spellweaver"
            ],
            "description": "Mapping the heavens to summon a focused solar discharge. The Scout spots the target, the Navigator aligns the stars, and the Spellweaver pulls the trigger.\n\n**Visual Effects:** A map of constellations appearing in the sky, followed by a concentrated beam of blinding white light that incinerates the target zone.",
            "type": "Light/Star/Magic",
            "is_mega": true
        },
        {
            "name": "Sonic Overdrive",
            "participants": [
                "El Mariachi",
                "Zeus Quill",
                "Tribal Drummer"
            ],
            "description": "A rhythmic bombardment that shakes the heavens. The Drummer and Mariachi create a standing wave of sound that Zeus uses as a conductor for a continuous stream of divine lightning.\n\n**Visual Effects:** Gold and yellow soundwave rings pulsating rapidly, layered with jagged yellow lightning arcs that screen-shake on every beat.",
            "type": "Sound/Electric/God",
            "is_mega": true
        },
        {
            "name": "Magma Harvest",
            "participants": [
                "Pyro Clover",
                "Magma Warden",
                "Ember-Steel Smith"
            ],
            "description": "The cultivation of volatile minerals. The Clover identifies the heat-veins, the Smith prepares the extraction tools, and the Warden protects the operation from the intense volcanic pressure.\n\n**Visual Effects:** Vibrant orange and red pixels erupting from cracks in the ground, layered with heavy brown dust clouds and glowing sparks from hammer strikes.",
            "type": "Fire/Earth",
            "is_mega": true
        },
        {
            "name": "Digital Mirage",
            "participants": [
                "Cyber Tech",
                "Cinema Bot",
                "Void Navigator"
            ],
            "description": "An inter-dimensional broadcast that overwrites reality. The Navigator finds a stable frequency in the void for Cinema Bot to proyek a digital duplicate of the battlefield, controlled by Cyber Tech.\n\n**Visual Effects:** Green neon grid lines expanding outward, layered with flickering inter-dimensional static and floating 'binary' code particles.",
            "type": "Tech/Star/Void",
            "is_mega": true
        },
        {
            "name": "Absolute Zero Containment",
            "participants": [
                "Ice Emperor",
                "Frost Monarch",
                "Void Warden"
            ],
            "description": "The perfect prison. The Monarchs bring the temperature down to absolute zero, while the Warden wraps the target in a void field that prevents even heat-vibrations from escaping.\n\n**Visual Effects:** A blinding white flash followed by a dense blizzard of cyan crystals, ending in a static, purple-outlined void cage that leaves frost on the UI.",
            "type": "Ice/Void/Shield",
            "is_mega": true
        },
        {
            "name": "Gourmet Gale",
            "participants": [
                "Flare Quill Chef",
                "Wind Chieftain",
                "Sky Chef"
            ],
            "description": "A culinary storm that feeds and protects. The Chieftains guide the winds to distribute the Chefs' high-calorie delicacies across the entire frontline, providing an instant morale and energy boost.\n\n**Visual Effects:** Swirling white pixel-dust and floating 'food' icons (bread, meat, soup) dancing through a golden-yellow skybox with blurred heat-waves.",
            "type": "Food/Air",
            "is_mega": true
        },
        {
            "name": "Tectonic Drill",
            "participants": [
                "Deep-Vein Excavator",
                "Tunnel Vanguard",
                "Golem Lord"
            ],
            "description": "A massive coordinated excavation. The Excavator and Vanguard clear the path with specialized tools while the Golem Lord provides the sheer muscle to move entire tectonic plates.\n\n**Visual Effects:** Heavy brown pixels slamming down in a rapid sequence, creating a deep 'drilling' screen-shake effect and thick clouds of subterranean dust.",
            "type": "Earth",
            "is_mega": true
        },
        {
            "name": "Spectral Alchemistry",
            "participants": [
                "Shadow Alchemist",
                "Necro Flame",
                "Flare Quill Alchemist"
            ],
            "description": "The transmutation of the afterlife. The Alchemists stabilize the volatile necro-energy of the Flame, creating a liquid shadow that can dissolve both physical and spiritual barriers.\n\n**Visual Effects:** Sickly green fire pixels mixing with bubbling purple liquid particles, layered with sickly green gas clouds that drift across the screen.",
            "type": "Alchemy/Dark/Fire",
            "is_mega": true
        },
        {
            "name": "Industrial Storm",
            "participants": [
                "Iron-Core Machinist",
                "Storm Elder",
                "Zeus Quill"
            ],
            "description": "A power plant on the move. The Machinist builds a conductive network of metal pillars that allow the Elder and Zeus to discharge their lightning with 100% efficiency.\n\n**Visual Effects:** Massive grey metal pillars slamming down, connected by jagged cyan lightning arcs that pulse with green neon digital glitch effects.",
            "type": "Tech/Electric",
            "is_mega": true
        },
        {
            "name": "Abyssal Bloom",
            "participants": [
                "Abyssal Diver",
                "Flora Queen",
                "Vitality Arcanist"
            ],
            "description": "The growth of a deep-sea garden. The Diver provides pressurized nutrients from the abyss, which the Queen and Arcanist use to grow glowing, bioluminescent vines in the blink of an eye.\n\n**Visual Effects:** Neon green and blue vines spiraling upward through translucent blue water streams, interspersed with bright white light beams.",
            "type": "Water/Nature/Life",
            "is_mega": true
        },
        {
            "name": "Royal Decree",
            "participants": [
                "King Quill",
                "The Fallen King",
                "Ruby Sovereign"
            ],
            "description": "A judgment passed by the three highest thrones. Their combined authority creates a field of absolute order where only the strongest survive.\n\n**Visual Effects:** Three overlapping golden crown pulses followed by a massive red and white light flash that leaves a 'ruby' crystal pattern on the floor.",
            "type": "Royal/Crystal/Fire",
            "is_mega": true
        },
        {
            "name": "Chrono-Mechanical Singularity",
            "participants": [
                "The Time Keeper",
                "Iron-Core Machinist",
                "Cyber Tech"
            ],
            "description": "A synchronization of clockwork precision and digital oversight. The Time Keeper slows the target to a crawl while the Machinist and Tech build a recursive loop of self-assembling turrets that fire outside of traditional time.\n\n**Visual Effects:** Golden clock-face particles layered with green neon grid lines and rapid-fire grey metallic projectiles.",
            "type": "Time/Tech",
            "is_mega": true
        },
        {
            "name": "Abyssal Pressure-Wash",
            "participants": [
                "Abyssal Diver",
                "Cyber Squid",
                "Sanitation Sentinel"
            ],
            "description": "Deep-sea hydraulics meets industrial cleaning. The Diver and Squid provide the high-pressure water source, while the Sentinel adds abrasive industrial detergents to scrub even the strongest armor.\n\n**Visual Effects:** High-speed blue particle streams layered with white splash effects and digital 'cleaning' HUD overlays.",
            "type": "Water/Tech",
            "is_mega": true
        },
        {
            "name": "Nature's Final Stand",
            "participants": [
                "Flora Queen",
                "Forest King",
                "Runic Woodcutter",
                "Emerald Vanquisher"
            ],
            "description": "The full might of the Green Grove. The Royals call for absolute growth, the Woodcutter provides the runic fuel, and the Vanquisher strikes from the heart of the resulting impenetrable jungle.\n\n**Visual Effects:** Rapidly spiraling emerald vines layered with brown wooden pillars smashing together and sudden green flashes of light.",
            "type": "Nature/Rune",
            "is_mega": true
        },
        {
            "name": "Supernova Stir-Fry",
            "participants": [
                "Flare Quill Chef",
                "Pyromancer",
                "Ignis Sentinel",
                "Blaze Monk"
            ],
            "description": "The ultimate culinary technique. Using the heat of a collapsed star to flash-cook an entire battlefield into a manageable, energy-rich snack.\n\n**Visual Effects:** Vibrant orange and red pixels erupting in a radial burst, layered with floating 'food' icons and heat distortion ripples.",
            "type": "Fire/Food",
            "is_mega": true
        },
        {
            "name": "Crystalline Bastion",
            "participants": [
                "Amethyst Sentinel",
                "Kunzite Archon",
                "Sapphire Mystic",
                "Ice Crystal Monarch"
            ],
            "description": "An unbreakable fortress formed from compressed geometric energy. The Archon and Sentinel channel the base minerals, while the Mystic and Monarch temper them with absolute cold.\n\n**Visual Effects:** A jagged formation of blue and purple crystal shards appearing on screen, accompanied by a deep blue flash and frost patterns.",
            "type": "Crystal/Ice",
            "is_mega": true
        },
        {
            "name": "Storm-Born Decree",
            "participants": [
                "Zeus Quill",
                "Wind Chieftain",
                "Cloud Master"
            ],
            "description": "The sky itself passes judgment. The Master and Chieftain create a massive localized cyclone that Zeus uses to focus a single, planetary-scale lightning strike.\n\n**Visual Effects:** Dark grey clouds swirling in a vortex, layered with jagged yellow lightning arcs that screen-shake with intense white flashes.",
            "type": "Electric/Air/God",
            "is_mega": true
        },
        {
            "name": "Spectral Infiltration",
            "participants": [
                "Void Walker",
                "Shadow Alchemist",
                "Necro Flame",
                "Venom Shade"
            ],
            "description": "A multi-layered assault from the spirit realm. The flame provides the distraction while the Alchemist and Shades dissolve the physical boundaries of their targets.\n\n**Visual Effects:** Sickly green fire pixels layered with purple gas clouds and a black hole-like void expanding from the center.",
            "type": "Dark/Dark/Alchemy/Spirit",
            "is_mega": true
        },
        {
            "name": "Titan's Unearthing",
            "participants": [
                "Titan of the Depths",
                "Deep-Vein Excavator",
                "Golem Lord",
                "Tunnel Vanguard"
            ],
            "description": "Reversing the geological clock. The Heavy-Quills work in unison to pull ancient, forgotten strata to the surface, crushing anything caught in the upheaval.\n\n**Visual Effects:** Massive brown pixels slamming down with screen-shaking 'thuds', kicking up thick dust clouds and brown wooden splinter particles.",
            "type": "Earth",
            "is_mega": true
        },
        {
            "name": "Royal Alchemical Blast",
            "participants": [
                "King Quill",
                "Ruby Sovereign",
                "Flare Quill Alchemist"
            ],
            "description": "Converting political power into raw energy. The Kings provide the 'sovereign weight' while the Alchemist uses it as a catalyst to trigger a ruby-colored explosion.\n\n**Visual Effects:** Three overlapping golden crown pulses followed by a massive red pixel eruption that leaves prismatic crystal fragments.",
            "type": "Royal/Alchemy/Crystal",
            "is_mega": true
        },
        {
            "name": "Universal Reset",
            "participants": [
                "The Gatekeeper",
                "Quantum Drifter",
                "Space Marine",
                "Void Navigator"
            ],
            "description": "The ultimate fallback protocol. The Gatekeeper opens the 'backdoor' of reality, the Navigator confirms the coordinates, the Drifter warps the local space, and the Marine provides the final 'kick'.\n\n**Visual Effects:** A blinding white flash that transitions into a massive black hole void, layered with binary code digital glitch effects and star-matter particles.",
            "type": "Void/Space/Shield",
            "is_mega": true
        },
        {
            "name": "Obsidian Overdrive",
            "participants": [
                "The Hunter",
                "Flare Quill Alchemist",
                "Tribal Drummer",
                "Abyssal Diver"
            ],
            "description": "A volcanic extraction ritual. The Diver and Hunter locate deep obsidian veins while the Drummer's rhythm stabilizes the ground, allowing the Alchemist to transmute raw stone into explosive glass shards.\n\n**Visual Effects:** Heavy brown pixels slamming down followed by sharp black crystal shards erupting, layered with vibrant red pixel-sparks and golden soundwave rings.",
            "type": "Earth/Fire/Dark/Alchemy",
            "is_mega": true
        },
        {
            "name": "Harvesting Whirlwind",
            "participants": [
                "Flare Quill Farmer",
                "Forest King"
            ],
            "description": "The synchronization of growth and harvest. The King commands the forest to expand at impossible speeds, while the Farmer uses specialized tools to convert that growth into a shredding whirlwind of organic matter.\n\n**Visual Effects:** Green vines rapidly spiraling upward while brown wooden splinters and leaves flutter in a high-speed wind effect.",
            "type": "Wood/Nature/Earth",
            "is_mega": false
        },
        {
            "name": "Chrono-Vault Lock",
            "participants": [
                "Kunzite Archon",
                "The Collector",
                "The Time Keeper",
                "Abyssal Captain"
            ],
            "description": "A multi-dimensional containment procedure. The Time Keeper pauses the target, the Captain anchors them in the void, and the Collector uses the Archon's crystal energy to lock the target in a permanent prismatic vault.\n\n**Visual Effects:** A static golden clock-face appearing in the center, layered with translucent blue water beams and a formation of purple crystal shards.",
            "type": "Time/Void/Crystal",
            "is_mega": true
        },
        {
            "name": "Void-Sailor's Wake",
            "participants": [
                "Abyssal Captain",
                "Wind Chieftain"
            ],
            "description": "Navigating the currents between worlds. The Captain steers through the void while the Chieftain fills the sails with spectral winds, creating a high-speed wake that disintegrates anything it touches.\n\n**Visual Effects:** A black hole-like void trail following the icons, layered with swirling white pixel-dust and blue particle splashes.",
            "type": "Void/Water/Wind",
            "is_mega": false
        },
        {
            "name": "Seraphic Singularity",
            "participants": [
                "Emerald Vanquisher",
                "Seraphim Scout",
                "Quantum Drifter",
                "Chrono-Warlock",
                "Sapphire Mystic",
                "Abyssal Diver",
                "Sanitation Sentinel",
                "Devil Quill",
                "The Giant"
            ],
            "description": "The ultimate celestial cleansing. A massive coordination of light, time, and void powers to reset a localized area to its primordial state, scrubbed clean of all corruption by the Sentinel.\n\n**Visual Effects:** A blinding white flash that shatters into green and blue crystal shards, layered with golden soundwave rings and a slow-expanding purple void field.",
            "type": "Light/Time/Void/Nature",
            "is_mega": true
        },
        {
            "name": "Divine Deluge",
            "participants": [
                "Pyro Clover",
                "Azure Pyrite Knight",
                "Tidecaller Deity",
                "Seraphim Scout"
            ],
            "description": "A baptism of holy fire and water. The Deity and Scout provide the divine source, the Knight provides the steel focus, and the Clover adds volatile organic catalysts to the flood.\n\n**Visual Effects:** High-speed blue particle streams layered with vibrant orange fire pixels and beams of golden light stabbing through the deluge.",
            "type": "Water/Divine/Light/Fire",
            "is_mega": true
        },
        {
            "name": "Tectonic Tremor",
            "participants": [
                "Oktober-Quill",
                "Golem Lord"
            ],
            "description": "A rhythm of the deep earth. The Golem's stomps are amplified by Oktober-Quill's brewing vats, creating a resonance frequency that liquifies the ground beneath the enemy.\n\n**Visual Effects:** Heavy brown pixels slamming down in a rapid sequence, creating a liquid-like 'ripple' effect on the UI with thick dust clouds.",
            "type": "Earth",
            "is_mega": false
        },
        {
            "name": "Star-Forge Eruption",
            "participants": [
                "The Time Keeper",
                "Deep-Vein Excavator",
                "Ignis Sentinel",
                "Seraphim Scout",
                "Crimson Shade",
                "Ice Crystal Monarch"
            ],
            "description": "Forging a star in the heart of the earth. The Excavator and Sentinel create a pressurized volcanic core, which is then ignited by the Scout's light and frozen in place by the Monarch to create a stable, explosive solar nursery.\n\n**Visual Effects:** Vibrant red and orange pixels erupting outward, layered with cyan ice crystals and a central sun-like white flash.",
            "type": "Fire/Earth/Light/Ice",
            "is_mega": true
        },
        {
            "name": "Caffeine Overgrowth",
            "participants": [
                "The Giant",
                "Flora Queen",
                "Barista Bot 9000"
            ],
            "description": "Nature on a caffeine high. The Queen's plants are watered with Barista Bot's high-octane espresso, causing them to develop jagged, jittery thorns and move with erratic, lightning-fast speed.\n\n**Visual Effects:** Neon green vines vibrating and spiraling rapidly, layered with brown coffee splashes and yellow jagged lightning arcs.",
            "type": "Nature/Food/Electric",
            "is_mega": true
        },
        {
            "name": "Alchemical Tsunami",
            "participants": [
                "Arcane Wizard",
                "Deep-Vein Excavator",
                "Flare Quill Chef",
                "Cyber Tech",
                "Magma Warden",
                "Kunzite Archon",
                "Cyber Arcanist",
                "Ashbound Assassin",
                "Splash Mage"
            ],
            "description": "A chaotic flood of transmuted matter. A massive wave of liquid crystal, magma, and volatile spices that overwrites the physical properties of the entire combat zone.\n\n**Visual Effects:** A multicolored wave (blue, red, purple) cascading across the screen, layered with digital glitch effects and floating hexadecimal data particles.",
            "type": "Alchemy/Water/Fire/Crystal/Tech",
            "is_mega": true
        },
        {
            "name": "Elemental Apex",
            "participants": [
                "Sapphire Mystic",
                "Magma Warden",
                "Cloud Master",
                "Vitality Arcanist",
                "Ashbound Assassin",
                "Tidecaller Deity"
            ],
            "description": "A perfect convergence of the six fundamental forces. The Warden and Deity provide the earth and sea, the Master provides the sky, the Mystic and Arcanist stabilize the magic, and the Assassin delivers the finishing blow in the eye of the storm.\n\n**Visual Effects:** A rotating disk of six different colored pixels (blue, red, white, green, orange, yellow), followed by a massive white flash that levels the screen.",
            "type": "Fire/Earth/Life/Magic/Air/Water",
            "is_mega": true
        },
        {
            "name": "Divine Brunch",
            "participants": [
                "Breakfast Bot",
                "Zeus Quill",
                "The Hunter"
            ],
            "description": "A meal truly fit for a god. The Hunter provides the rarest game, Zeus provides the lightning to flash-sear it, and Breakfast Bot serves it with mechanical efficiency to restore the entire team's spirits.\n\n**Visual Effects:** A rapid sequence of yellow lightning bolts hitting a tray of 'food' icons, followed by a golden aura that heals the UI edges.",
            "type": "God/Electric/Food",
            "is_mega": true
        },
        {
            "name": "Volcanic Petrification",
            "participants": [
                "Cursed Pharaoh",
                "Pyromancer",
                "Necro Flame",
                "Lumberjack Quill",
                "Cyber Squid",
                "Arcane Wizard",
                "Spartan Quill",
                "Emerald Vanquisher",
                "Crimson Arbalest"
            ],
            "description": "A terrifying cross-tribal offensive. The Pharaoh's curse turns enemies to stone, while the combined fire and tech of nine specialists ensures that even the statues are vaporized into fine dust.\n\n**Visual Effects:** Screen-wide grey 'stone' filter that shatters into a massive explosion of orange and red fire pixels.",
            "type": "Sand/Undead/Fire/Tech",
            "is_mega": true
        },
        {
            "name": "Chrono-Culinary Alignment",
            "participants": [
                "Dark Iron Warlock",
                "Flare Quill Chef",
                "The Time Keeper",
                "Flare Quill Alchemist",
                "Chrono-Warlock"
            ],
            "description": "Manipulating the timelines of ingredients to achieve the ultimate flavor and power. The Time Keepers ensure the meal stays fresh across aeons, while the Alchemist and Warlock infuse it with dark, potent magic.\n\n**Visual Effects:** Golden clock-face particles swirling around a bubbling purple cauldron, leaving behind glowing 'star' pixels.",
            "type": "Time/Food/Alchemy/Dark",
            "is_mega": true
        },
        {
            "name": "Frozen Tech Nova",
            "participants": [
                "Cyber Squid",
                "Frost Monarch",
                "Iron-Core Machinist"
            ],
            "description": "Absolute zero powered by digital overclocking. The Machinist pushes the cooling systems to the limit while the Monarch and Squid unleash a localized ice age.\n\n**Visual Effects:** Cyan ice crystals exploding from a green neon grid, leaving frost patterns on the UI and 'static' digital glitch effects.",
            "type": "Ice/Tech/Water",
            "is_mega": true
        },
        {
            "name": "Spectral Siege",
            "participants": [
                "Shadow Alchemist",
                "Spartan Quill",
                "Void Warden"
            ],
            "description": "An impenetrable defense from the void. The Warden holds the gates, the Spartan provides the steel, and the Alchemist creates a shroud of shadows to confuse the attackers.\n\n**Visual Effects:** A black hole-like void expanding from the center, protected by a ring of red pixel-shields and purple mist.",
            "type": "Dark/Void/Steel/Shield",
            "is_mega": true
        },
        {
            "name": "Gaea's Wrath",
            "participants": [
                "Forest King",
                "Golem Lord",
                "Deep-Vein Excavator"
            ],
            "description": "The earth itself rises to reclaim its own. The Golem and Excavator tunnel beneath the foe while the King commands a forest of roots to drag them into the depths.\n\n**Visual Effects:** Massive brown pixels slamming down while neon green vines wrap around the screen, followed by a deep screen-shake 'thud'.",
            "type": "Nature/Earth",
            "is_mega": true
        },
        {
            "name": "Neon Spirit Pulse",
            "participants": [
                "Crystalis Spirit",
                "Cyber Tech",
                "Spark Mage"
            ],
            "description": "A high-frequency energy discharge. The Spirit provides the raw essence, the Mage pumps in the voltage, and the Tech stabilizes the frequency into a lethal neon pulse.\n\n**Visual Effects:** Bright magenta and cyan rings pulsating outward, layered with jagged lightning arcs and digital data scrolls.",
            "type": "Spirit/Tech/Electric",
            "is_mega": true
        },
        {
            "name": "Abyssal Cargo Drop",
            "participants": [
                "Abyssal Captain",
                "Space Marine",
                "Sky Chef"
            ],
            "description": "Strategic logistics from the deep. The Captain and Marine drop a payload of void-sealed supplies (and explosives) while the Chef ensures the delivery is 'well-seasoned'.\n\n**Visual Effects:** Translucent blue water streams falling from the top of the UI, exploding into black void clouds and floating 'crate' icons.",
            "type": "Void/Water/Space/Food",
            "is_mega": true
        },
        {
            "name": "Runic Pyre",
            "participants": [
                "Runic Woodcutter",
                "Blaze Monk",
                "Infernal Juggernaut"
            ],
            "description": "Sacrificing ancient runic timber to fuel a hellish inferno. The Juggernaut anchors the site while the Woodcutter and Monk feed the flames with holy-engraved wood.\n\n**Visual Effects:** Vibrant orange fire pixels consuming glowing green runic carvings, leaving behind black charcoal residue and sparks.",
            "type": "Rune/Fire/Wood",
            "is_mega": true
        },
        {
            "name": "Soul-Binding Strike",
            "participants": [
                "Venomblade Hunter",
                "Skull Shaman"
            ],
            "description": "An assassination technique that targets the spirit. The Hunter delivers a physical strike while the Shaman anchors the target's soul to the spot using ancient spirit-runes.\n\n**Visual Effects:** A sharp green pixel-slash followed by a purple miasmic aura that 'locks' the target's icon in place with spectral chains.",
            "type": "Spirit/Poison/Dark",
            "is_mega": false
        },
        {
            "name": "Volcanic Bastion",
            "participants": [
                "Tunnel Vanguard",
                "Blaze Monk",
                "Magma Warden",
                "Highlander"
            ],
            "description": "The ultimate defensive wall of the inner earth. The Vanguard and Warden raise the ground, the Monk ignites it, and the Highlander guards the flaming ramparts with a steel blade.\n\n**Visual Effects:** Massive brown pixels slamming down to form a wall, layered with a radial orange fire burst and heat distortion ripples.",
            "type": "Earth/Fire/Wind",
            "is_mega": true
        },
        {
            "name": "The Great Unearthing",
            "participants": [
                "Tunnel Vanguard",
                "Oktober-Quill"
            ],
            "description": "A collaborative excavation that reveals treasures and terrors alike. The Vanguard clears the earth while Oktober-Quill uses geological intuition to find the perfect point of impact.\n\n**Visual Effects:** Heavy brown pixels slamming down repeatedly, kicking up thick dust clouds and golden 'artifact' sparkles.",
            "type": "Earth",
            "is_mega": false
        },
        {
            "name": "Obsidian Eclipse",
            "participants": [
                "Dark Iron Warlock",
                "Emerald Vanquisher"
            ],
            "description": "A field of crystalline darkness. The Warlock drains the light while the Vanquisher uses the darkness to teleport behind enemies, striking with obsidian-glass daggers.\n\n**Visual Effects:** A black hole-like void expanding, layered with sharp black crystal shards and sudden green flashes of light.",
            "type": "Dark/Fire/Crystal",
            "is_mega": false
        },
        {
            "name": "Stellar Splashdown",
            "participants": [
                "Space Marine",
                "Splash Mage",
                "Abyssal Diver",
                "Ruby Sovereign",
                "Cloud Master"
            ],
            "description": "An orbital water-bombing operation. The Marine provides the target coordinates, the Master creates a localized vacuum, and the Mage-Diver duo drops a concentrated mass of elemental water from the upper atmosphere.\n\n**Visual Effects:** Multiple blue particle streams falling at high speed, ending in a massive white splash layered with star-matter purple particles.",
            "type": "Water/Air/Void/Space",
            "is_mega": true
        },
        {
            "name": "Time-Frozen Gale",
            "participants": [
                "Frost Monarch",
                "Temporal Stormguard"
            ],
            "description": "A localized cessation of movement. The Monarch brings the cold while the Stormguard freezes the flow of time itself, leaving enemies trapped in a perpetual blizzard.\n\n**Visual Effects:** A dense blizzard of cyan crystals that 'freezes' in mid-air, layered with golden clock-face particles that slow down and stop.",
            "type": "Ice/Time/Electric",
            "is_mega": false
        },
        {
            "name": "Absolute Zero Protocol",
            "participants": [
                "Cyber Squid",
                "Iron-Core Machinist",
                "Ice Crystal Monarch"
            ],
            "description": "A mechanical refrigeration miracle. The Machinist builds a cryo-array that the Monarch fuels with ancient ice, while the Squid uses its tentacles to distribute the cold with digital precision.\n\n**Visual Effects:** Cyan crystal fragments forming a vortex, layered with green neon grid lines and digital glitch effects.",
            "type": "Ice/Tech/Water",
            "is_mega": true
        },
        {
            "name": "Titan's High Feast",
            "participants": [
                "Titan of the Depths",
                "Flare Quill Chef",
                "Gourmet Automaton"
            ],
            "description": "A meal of such massive proportions it requires a giant to eat it\u2014and two master chefs to prepare it. The resulting energy release can be seen from space.\n\n**Visual Effects:** A blinding white flash followed by a rain of 'food' icons and golden steam particles that fill the combat zone.",
            "type": "Earth/Food/Steel",
            "is_mega": true
        },
        {
            "name": "Divine Broadcast",
            "participants": [
                "Zeus Quill",
                "Broadcast Unit",
                "Cinema Bot"
            ],
            "description": "The ultimate PR move for a god. Zeus's lightning strikes are captured and broadcasted across all dimensions simultaneously, paralyzing enemies with both the shock and the terrifying imagery.\n\n**Visual Effects:** Jagged yellow lightning arcs layered with flickering digital static and cinema-reel 'frame' overlays.",
            "type": "God/Electric/Tech",
            "is_mega": true
        },
        {
            "name": "THE UNIVERSAL HARMONY",
            "participants": [
                "The Gatekeeper",
                "The Collector",
                "The Time Keeper",
                "The Universal Singularity"
            ],
            "description": "The final chord of existence. A synchronization of the archive, the gateway, and the timeline, overseen by the Singularity itself. A move that exists beyond win or loss.\n\n**Visual Effects:** A blinding white screen that slowly fades into a rotating galaxy of every pixel color and effect used in the game, ending with a single, perfect golden crown pulse.",
            "type": "Universal/Infinite",
            "is_mega": true
        }

    ]
}
    ;
