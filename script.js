// Main Logic
document.addEventListener('DOMContentLoaded', () => {
    const cardGrid = document.getElementById('cardGrid');
    const searchInput = document.getElementById('searchInput');
    const statsCounter = document.getElementById('statsCounter');
    const modal = document.getElementById('modal');
    const modalBody = document.getElementById('modalBody');
    const closeBtn = document.querySelector('.close-btn');
    const sortSelect = document.getElementById('sortSelect');
    const tribeSelect = document.getElementById('tribeSelect'); // New Tribe Filter

    // Access data from data.js
    const allCards = flareQuillsData.flare_quills;
    const allCombos = comboTechniquesData.combo_techniques || [];

    // Map names to IDs for quick lookup (icons)
    const nameToQuillMap = {};
    allCards.forEach(q => {
        nameToQuillMap[q.name] = q;
    });

    let viewMode = 'characters'; // 'characters' or 'combos'

    const showCharactersBtn = document.getElementById('showCharacters');
    const showCombosBtn = document.getElementById('showCombos');

    // --- Populate Tribe Select ---
    if (tribeSelect) {
        const distinctTribes = [...new Set(allCards.map(q => q.tribe).filter(t => t))].sort();
        distinctTribes.forEach(tribe => {
            const option = document.createElement('option');
            option.value = tribe;
            option.textContent = `TRIBE: ${tribe.toUpperCase()}`;
            tribeSelect.appendChild(option);
        });
    }

    // --- Global Function for Map Clicks ---
    window.filterByTribe = (tribeName) => {
        if (tribeSelect) {
            tribeSelect.value = tribeName;
            // Validate if value exists (e.g. if tribe map name differs), fallback to all
            if (tribeSelect.value !== tribeName) {
                // Try loose matching if exact match fails
                const options = Array.from(tribeSelect.options);
                const match = options.find(opt => opt.value.includes(tribeName.split(' ')[0]));
                if (match) tribeSelect.value = match.value;
            }

            // Trigger change event manually
            const event = new Event('change');
            tribeSelect.dispatchEvent(event);

            // Scroll to grid
            document.getElementById('cardGrid').scrollIntoView({ behavior: 'smooth' });
        }
    };

    // --- Helper Functions ---

    function createCardElement(quill) {
        const card = document.createElement('div');
        card.classList.add('card');
        card.setAttribute('data-id', quill.id);

        // Rarity determination based on ember cost (Visual flair)
        let rarityClass = 'common';
        if (quill.ember_cost >= 5) rarityClass = 'rare';
        if (quill.ember_cost >= 7) rarityClass = 'legendary';
        card.classList.add(rarityClass);

        card.innerHTML = `
            <div class="card-image-container">
                <img src="${quill.id}" alt="${quill.name}" class="card-img" loading="lazy" decoding="async" onerror="this.src='https://via.placeholder.com/200?text=No+Image'">
            </div>
            <div class="card-content">
                <div class="card-header">
                    <h2 class="card-name">${quill.name}</h2>
                    <div style="display: flex; flex-direction: column; align-items: flex-end;">
                        <span class="ember-cost">${quill.ember_cost} <span class="ember-icon">🔥</span></span>
                        <span class="hp-stat" style="font-size: 0.75rem; color: #ff4d4d; font-weight: bold;">${quill.hitpoints} <span class="hp-icon">❤️</span></span>
                    </div>
                </div>
                <p class="card-occupation">${quill.occupation}</p>
                <div class="stat-badges">
                    <span class="stat-badge element-${quill.element.toLowerCase().replace(/[^a-z0-9]/g, '-')}">${quill.element}</span>
                    <span class="stat-badge" style="background:#444; border:1px solid #666; font-size:0.7em;">${quill.tribe || 'Mercenary'}</span>
                </div>
                <p class="card-region" style="font-size: 0.8em; color: #aaa; margin-top: 4px;">📍 ${quill.region || 'Unknown Region'}</p>
                <p class="card-attack"><strong>⚔️ Action:</strong> ${quill.attack_action}</p>
            </div>
        `;

        // Add click event to open modal
        card.addEventListener('click', () => openModal(quill));

        return card;
    }

    function createComboCardElement(combo) {
        const card = document.createElement('div');
        card.classList.add('card', 'combo-card');

        card.innerHTML = `
            <div class="card-content">
                <div class="card-header">
                    <h2 class="card-name" style="font-size: 0.8rem;">${combo.name}</h2>
                </div>
                <div class="combo-participants">
                    ${combo.participants.join(' + ')}
                </div>
                <p class="card-attack" style="font-size: 0.75rem;">${combo.description}</p>
                <span class="combo-type-badge">${combo.type}</span>
                ${combo.is_mega ? '<div class="mega-badge">MEGA COMBO</div>' : ''}
            </div>
        `;

        card.addEventListener('click', () => openComboModal(combo));

        return card;
    }

    // --- Core Logic ---

    // Function to render cards with sectioning
    function renderCards(cardsToRender, isSortedOrFiltered = false) {
        cardGrid.innerHTML = ''; // Clear existing cards

        if (viewMode === 'combos') {
            const searchTerm = searchInput.value.toLowerCase();
            const filteredCombos = allCombos.filter(c =>
                c.name.toLowerCase().includes(searchTerm) ||
                c.description.toLowerCase().includes(searchTerm) ||
                c.participants.some(p => p.toLowerCase().includes(searchTerm))
            );

            statsCounter.textContent = `COMBOS: ${filteredCombos.length}/${allCombos.length}`;

            filteredCombos.forEach(combo => {
                const card = createComboCardElement(combo);
                cardGrid.appendChild(card);
            });
            return;
        }

        if (cardsToRender.length === 0) {
            cardGrid.innerHTML = '<p style="color: white; text-align: center; grid-column: 1/-1;">No Flare Quills found.</p>';
            statsCounter.textContent = `DISCOVERED: 0/${allCards.length}`;
            return;
        }

        // Update Counter
        statsCounter.textContent = `DISCOVERED: ${cardsToRender.length}/${allCards.length}`;

        // If active sort or filter is applied (meaning not default thematic view), render as a flat list
        if (isSortedOrFiltered) {
            cardsToRender.forEach(quill => {
                const card = createCardElement(quill);
                cardGrid.appendChild(card);
            });
            return;
        }

        // Default View: Group items by "Tribe"
        const tribes = {};
        cardsToRender.forEach(quill => {
            const tribeName = quill.tribe || 'Mercenaries';
            if (!tribes[tribeName]) {
                tribes[tribeName] = [];
            }
            tribes[tribeName].push(quill);
        });

        // Render each tribe section
        Object.keys(tribes).forEach(tribeName => {
            // Create Section Header
            const sectionHeader = document.createElement('h2');
            sectionHeader.className = 'tribe-header';
            sectionHeader.textContent = tribeName.toUpperCase();
            sectionHeader.style.gridColumn = '1 / -1';
            sectionHeader.style.textAlign = 'center';
            sectionHeader.style.color = 'var(--accent-color)';
            sectionHeader.style.marginTop = '2rem';
            sectionHeader.style.marginBottom = '1rem';
            sectionHeader.style.textShadow = '2px 2px 0 #000';
            sectionHeader.style.borderBottom = '4px solid var(--accent-color)';
            sectionHeader.style.display = 'flex'; // Changed to flex for icon alignment
            sectionHeader.style.justifySelf = 'center';
            sectionHeader.style.padding = '0 20px';
            sectionHeader.style.cursor = 'pointer'; // Make it clickable

            // Add toggle icon
            const icon = document.createElement('span');
            icon.textContent = ' ▼';
            icon.style.marginLeft = '10px';
            icon.style.fontSize = '1rem';
            sectionHeader.appendChild(icon);

            cardGrid.appendChild(sectionHeader);

            // Container for this tribe's cards (to easily toggle visibility)
            // We can't wrap them in a div easily with CSS Grid unless we use subgrids or change layout.
            // EASIER APPROACH: Give all cards in this tribe a specific class/data-attr and toggle display on them.

            const tribeCards = [];
            tribes[tribeName].forEach(quill => {
                const card = createCardElement(quill);
                card.setAttribute('data-tribe-section', tribeName);
                cardGrid.appendChild(card);
                tribeCards.push(card);
            });

            // Toggle Logic
            let isCollapsed = false;
            sectionHeader.addEventListener('click', () => {
                isCollapsed = !isCollapsed;
                icon.style.transform = isCollapsed ? 'rotate(-90deg)' : 'rotate(0deg)';
                tribeCards.forEach(card => {
                    card.style.display = isCollapsed ? 'none' : 'block';
                });
                sectionHeader.classList.toggle('collapsed', isCollapsed);
            });
        });
    }

    function sortCards(cards, criteria) {
        // Create a shallow copy to sort
        const sorted = [...cards];
        switch (criteria) {
            case 'name':
                return sorted.sort((a, b) => a.name.localeCompare(b.name));
            case 'cost-asc':
                return sorted.sort((a, b) => a.ember_cost - b.ember_cost);
            case 'cost-desc':
                return sorted.sort((a, b) => b.ember_cost - a.ember_cost);
            case 'thematic':
            default:
                // For thematic, we rely on the original JSON order. 
                // Since we passed 'allCards' or a filtered subset that respects original order,
                // we technically don't need to 'sort' it back if we didn't mutate it in place.
                // However, filtered subsets usually keep order. 
                return sorted;
        }
    }

    function filterAndSort() {
        const searchTerm = searchInput.value.toLowerCase();
        const sortValue = sortSelect.value;
        const tribeValue = tribeSelect ? tribeSelect.value : 'all'; // Safe access

        // 1. Filter
        let filteredCards = allCards.filter(quill => {
            const matchesSearch = quill.name.toLowerCase().includes(searchTerm) ||
                quill.element.toLowerCase().includes(searchTerm) ||
                quill.occupation.toLowerCase().includes(searchTerm);

            const matchesTribe = (tribeValue === 'all') || (quill.tribe === tribeValue);

            return matchesSearch && matchesTribe;
        });

        // 2. Sort
        // "thematic" is a special case where we don't want to re-order the array if possible,
        // but if we are filtering, maintaining relative order is automatic.
        let finalCards = sortCards(filteredCards, sortValue);

        // Determine if we should show sections or flat list
        // Show flat list if: User is searching OR User has explicitly sorted by Name/Cost
        // NOTE: Filtering by tribe alone allows section headers (shows single tribe section).
        const isSortedOrFiltered = (searchTerm !== '') || (sortValue !== 'thematic');

        renderCards(finalCards, isSortedOrFiltered);
    }

    // --- Keyword Highlighting ---
    function highlightKeywords(text) {
        if (!text) return text;

        const map = [
            { rx: /\b(Fire|Burn|Flame|Magma|Ember|Heat|Ignis|Inferno)\b/gi, cls: 'text-fire' },
            { rx: /\b(Water|Aqua|Splash|Tide|Ocean|Rain|Hydro)\b/gi, cls: 'text-water' },
            { rx: /\b(Ice|Frost|Frozen|Cold|Chill|Blizzard|Snow|Cryo)\b/gi, cls: 'text-ice' },
            { rx: /\b(Nature|Poison|Root|Leaf|Vine|Thorn|Spore|Bloom|Forest|Venom)\b/gi, cls: 'text-nature' },
            { rx: /\b(Electric|Lightning|Shock|Thunder|Volt|Zap|Storm)\b/gi, cls: 'text-electric' },
            { rx: /\b(Air|Wind|Gust|Breeze|Aero|Sky)\b/gi, cls: 'text-air' },
            { rx: /\b(Earth|Rock|Stone|Quake|Sand|Mountain|Terra)\b/gi, cls: 'text-earth' },
            { rx: /\b(Dark|Void|Shadow|Curse|Necro|Abyss|Night|Fear)\b/gi, cls: 'text-dark' },
            { rx: /\b(Light|Holy|Divine|Radiant|Sun|Flash|Celestial|Lumina)\b/gi, cls: 'text-light' },
            { rx: /\b(Damage|Strike|Hit|Critical|Attack|Bash|Crush|Slash|Pierce)\b/gi, cls: 'text-damage' },
            { rx: /\b(Shield|Protect|Guard|Armor|Block|Resist|Defense|Barrier|Wall)\b/gi, cls: 'text-defense' },
            { rx: /\b(Heal|Restore|Cure|Mend|Revive|Regen|Health)\b/gi, cls: 'text-heal' },
            { rx: /\b(Stun|Sleep|Slow|Silence|Blind|Confuse|Paralyze)\b/gi, cls: 'text-status' }
        ];

        let result = text;
        map.forEach(item => {
            result = result.replace(item.rx, (match) => `<span class="${item.cls}">${match}</span>`);
        });
        return result;
    }

    function openModal(card) {
        // Apply highlighting to text fields
        const story = highlightKeywords(card.origin_story);
        const attackAction = highlightKeywords(card.attack_action);

        // Helper for element color mapping (simple check)
        const getElementClass = (el) => {
            const e = el.toLowerCase();
            if (e.includes('fire')) return 'text-fire';
            if (e.includes('water')) return 'text-water';
            if (e.includes('ice')) return 'text-ice';
            if (e.includes('nature')) return 'text-nature';
            if (e.includes('electric')) return 'text-electric';
            if (e.includes('dark')) return 'text-dark';
            if (e.includes('light')) return 'text-light';
            if (e.includes('earth')) return 'text-earth';
            if (e.includes('wind') || e.includes('air')) return 'text-air';
            return '';
        };

        const elementClass = getElementClass(card.element);

        modalBody.innerHTML = `
            <h2 style="margin-bottom: 20px; color: var(--highlight); text-align: center;">${card.name}</h2>
            <div class="modal-details">
                <div class="modal-img-container">
                    <img src="${card.id}" alt="${card.name}" style="width: 100%; image-rendering: pixelated; display: block; border: 4px solid var(--border-color);">
                </div>
                <div class="modal-info">
                    <div class="stat-block">
                        <span class="stat-label">ORIGIN STORY</span>
                        <p>${story}</p>
                    </div>
                    
                    <div class="stat-block">
                        <span class="stat-label">ATTACK ACTION</span>
                        <p>${attackAction}</p>
                        <p style="font-size: 0.8em; color: #aaa; margin-top: 4px; display: flex; gap: 15px;">
                            <span>⚔️ DMG: <strong style="color: #ffcccc;">${card.attack_damage || '?'}</strong></span>
                            <span>💧 COST: <strong style="color: #ccccff;">${card.attack_mana_cost || 5}</strong></span>
                        </p>
                    </div>

                    <div class="stat-block">
                        <span class="stat-label">STATS</span>
                        <p><strong>OCCUPATION:</strong> <span style="color: #ffcc00;">${card.occupation}</span></p>
                        <p><strong>ELEMENT:</strong> <span class="${elementClass}" style="text-transform:uppercase;">${card.element}</span></p>
                        <p><strong>EMBER COST:</strong> ${card.ember_cost} 🔥</p>
                        <p><strong>HITPOINTS:</strong> <span style="color: #ff6b6b;">${card.hitpoints} ❤️</span></p>
                        <p><strong>MANA POINTS:</strong> <span style="color: #4facfe;">${card.mana_points || '?'} 💧</span></p>
                        <p><strong>TRIBE:</strong> <span style="color: #aaa;">${card.tribe}</span></p>
                    </div>

                    <div class="stat-block">
                        <span class="stat-label">POWERS</span>
                        <ul style="list-style-type: none; padding-left: 0;">
                            ${card.powers.map((p, index) => {
            const cost = card.power_mana_costs ? card.power_mana_costs[index] : '?';
            const damage = card.power_damages ? card.power_damages[index] : 0;
            const defense = card.power_defense_boosts ? card.power_defense_boosts[index] : 0;
            const heal = card.power_heal_amounts ? card.power_heal_amounts[index] : 0;
            const isDrain = card.power_is_drain ? card.power_is_drain[index] : false;

            let statBadge = '';

            if (heal > 0) {
                statBadge = `<span style="color: #69db7c; font-size: 0.8em; margin-left:8px;">(💚 +${heal})</span>`;
            } else if (isDrain && damage > 0) {
                statBadge = `<span style="color: #d0bfff; font-size: 0.8em; margin-left:8px;">(🩸 ${damage})</span>`;
            } else if (damage > 0) {
                statBadge = `<span style="color: #ff9999; font-size: 0.8em; margin-left:8px;">(💥 ${damage})</span>`;
            } else if (defense > 0) {
                statBadge = `<span style="color: #99ff99; font-size: 0.8em; margin-left:8px;">(🛡️ +${defense})</span>`;
            }

            // Highlight power explanation if it exists
            const explanation = (card.power_explanations && card.power_explanations[index])
                ? highlightKeywords(card.power_explanations[index])
                : '';

            return `
                                <li style="margin-bottom: 8px;">
                                    <div style="display: flex; justify-content: space-between; align-items: center;">
                                        <span class="${getElementClass(p)}"><strong>• ${p}</strong>${statBadge}</span>
                                        <span style="font-size: 0.8em; color: #aaf; white-space: nowrap;">${cost} 💧</span>
                                    </div>
                                    ${explanation ?
                    `<div style="font-size: 0.85em; color: #ccc; margin-left: 15px; font-style: italic;">${explanation}</div>`
                    : ''}
                                </li>`;
        }).join('')}
                        </ul>
                    </div>

                    <div class="stat-block" style="border: none;">
                        <span class="stat-label">CRAFTABLE RESOURCES</span>
                        <div class="resource-list">
                            ${card.craftable_resources.map(r => `<span class="resource-item">${r}</span>`).join('')}
                        </div>
                    </div>
                </div>
            </div>
        `;
        modal.classList.remove('hidden');
    }

    function openComboModal(combo) {
        const participantsData = combo.participants.map(name => {
            const quill = nameToQuillMap[name];
            return quill || { name: name, id: 'https://via.placeholder.com/100?text=?', element: 'Unknown' };
        });

        modalBody.innerHTML = `
            <div style="text-align: center; margin-bottom: 20px;">
                <h2 style="color: var(--highlight); margin-bottom: 5px;">${combo.name}</h2>
                <span class="combo-type-badge" style="padding: 4px 12px; font-size: 0.8rem;">${combo.type}</span>
                ${combo.is_mega ? '<br><div class="mega-badge">MEGA COMBO</div>' : ''}
            </div>
            
            <div class="modal-details" style="display: flex; flex-direction: column; align-items: center; gap: 20px;">
                <div class="combo-visuals" style="display: flex; gap: 15px; justify-content: center; align-items: center; background: rgba(0,0,0,0.3); padding: 15px; border: 2px solid var(--border-color); flex-wrap: wrap; max-width: 100%;">
                    ${participantsData.map(p => {
            const iconSize = participantsData.length > 6 ? '50px' : (participantsData.length > 3 ? '65px' : '80px');
            const fontSize = participantsData.length > 6 ? '0.5rem' : '0.7rem';
            return `
                        <div style="text-align: center;">
                            <img src="${p.id}" alt="${p.name}" class="combo-participant-icon" loading="lazy" decoding="async" style="width: ${iconSize}; height: ${iconSize}; image-rendering: pixelated; border: 2px solid white; background: #000;">
                            <p style="font-size: ${fontSize}; color: #fff; margin-top: 5px; font-family: 'Press Start 2P', cursive; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; max-width: ${iconSize};">${p.name.split(' ')[0]}</p>
                        </div>
                    `}).join(participantsData.length > 6 ? '' : '<span style="font-size: 1.5rem; color: var(--highlight);">+</span>')}
                </div>
                
                <div class="stat-block" style="width: 100%; border-top: 2px solid var(--border-color); padding-top: 20px;">
                    <span class="stat-label">COMBO DESCRIPTION</span>
                    <p style="font-size: 1.1rem; line-height: 1.6; color: #fff; white-space: pre-wrap;">${combo.description}</p>
                </div>

                <div class="stat-block" style="width: 100%; border: none;">
                    <span class="stat-label">PARTICIPANTS</span>
                    <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-top: 10px;">
                        ${participantsData.map(p => `
                            <span class="stat-badge" style="background:#222; border:1px solid var(--highlight);">${p.name} (${p.element})</span>
                        `).join('')}
                    </div>
                </div>
            </div>
        `;
        modal.classList.remove('hidden');
    }

    // --- Event Listeners ---

    closeBtn.addEventListener('click', () => {
        modal.classList.add('hidden');
    });

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.classList.add('hidden');
        }
    });

    searchInput.addEventListener('input', filterAndSort);
    sortSelect.addEventListener('change', filterAndSort);
    if (tribeSelect) tribeSelect.addEventListener('change', filterAndSort);

    if (showCharactersBtn && showCombosBtn) {
        showCharactersBtn.addEventListener('click', () => {
            viewMode = 'characters';
            showCharactersBtn.classList.add('active');
            showCombosBtn.classList.remove('active');
            filterAndSort();
        });

        showCombosBtn.addEventListener('click', () => {
            viewMode = 'combos';
            showCombosBtn.classList.add('active');
            showCharactersBtn.classList.remove('active');
            filterAndSort();
        });
    }

    // Initial Render
    filterAndSort();
});