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
                <img src="${quill.id}" alt="${quill.name}" class="card-image" onerror="this.src='https://via.placeholder.com/200?text=No+Image'">
            </div>
            <div class="card-content">
                <div class="card-header">
                    <h2 class="card-name">${quill.name}</h2>
                    <span class="ember-cost">${quill.ember_cost} <span class="ember-icon">🔥</span></span>
                </div>
                <p class="card-occupation">${quill.occupation}</p>
                <div class="card-stats">
                    <span class="stat-badge">${quill.element}</span>
                </div>
                <p class="card-attack"><strong>⚔️ Action:</strong> ${quill.attack_action}</p>
            </div>
        `;

        // Add click event to open modal
        card.addEventListener('click', () => openModal(quill));

        return card;
    }

    // --- Core Logic ---

    // Function to render cards with sectioning
    function renderCards(cardsToRender, isSortedOrFiltered = false) {
        cardGrid.innerHTML = ''; // Clear existing cards

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

    function openModal(card) {
        modalBody.innerHTML = `
            <h2 style="margin-bottom: 20px; color: var(--highlight); text-align: center;">${card.name}</h2>
            <div class="modal-details">
                <div class="modal-img-container">
                    <img src="${card.id}" alt="${card.name}" style="width: 100%; image-rendering: pixelated; display: block; border: 4px solid var(--border-color);">
                </div>
                <div class="modal-info">
                    <div class="stat-block">
                        <span class="stat-label">ORIGIN STORY</span>
                        <p>${card.origin_story}</p>
                    </div>
                    
                    <div class="stat-block">
                        <span class="stat-label">ATTACK ACTION</span>
                        <p>${card.attack_action}</p>
                    </div>

                    <div class="stat-block">
                        <span class="stat-label">STATS</span>
                        <p><strong>OCCUPATION:</strong> ${card.occupation}</p>
                        <p><strong>ELEMENT:</strong> ${card.element}</p>
                        <p><strong>EMBER COST:</strong> ${card.ember_cost} 🔥</p>
                        <p><strong>TRIBE:</strong> ${card.tribe}</p>
                    </div>

                    <div class="stat-block">
                        <span class="stat-label">POWERS</span>
                        <ul style="list-style-type: square; padding-left: 20px;">
                            ${card.powers.map(p => `<li>${p}</li>`).join('')}
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

    // Initial Render
    filterAndSort();
});
