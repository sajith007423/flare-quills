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
                <img src="${quill.id}" alt="${quill.name}" class="card-image" onerror="this.src='https://via.placeholder.com/200?text=No+Image'">
            </div>
            <div class="card-content">
                <div class="card-header">
                    <h2 class="card-name">${quill.name}</h2>
                    <span class="ember-cost">${quill.ember_cost} <span class="ember-icon">🔥</span></span>
                </div>
                <p class="card-occupation">${quill.occupation}</p>
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
 
 / /   - - -   P o p u l a t e   T e x t   Z o n e s   - - -  
 c o n s t   z o n e s L i s t   =   d o c u m e n t . g e t E l e m e n t B y I d ( ' z o n e s L i s t ' ) ;  
 i f   ( z o n e s L i s t )   {  
         c o n s t   z o n e M a p   =   { } ;  
  
         / /   1 .   G r o u p   T r i b e s   b y   R e g i o n  
         a l l C a r d s . f o r E a c h ( c a r d   = >   {  
                 c o n s t   r e g i o n   =   c a r d . r e g i o n   | |   ' U n k n o w n   R e g i o n ' ;  
                 c o n s t   t r i b e   =   c a r d . t r i b e   | |   ' M e r c e n a r i e s ' ;  
  
                 i f   ( ! z o n e M a p [ r e g i o n ] )   {  
                         z o n e M a p [ r e g i o n ]   =   n e w   S e t ( ) ;  
                 }  
                 z o n e M a p [ r e g i o n ] . a d d ( t r i b e ) ;  
         } ) ;  
  
         / /   2 .   R e n d e r  
         O b j e c t . k e y s ( z o n e M a p ) . s o r t ( ) . f o r E a c h ( r e g i o n   = >   {  
                 c o n s t   t r i b e s   =   A r r a y . f r o m ( z o n e M a p [ r e g i o n ] ) . j o i n ( ' ,   ' ) ;  
  
                 c o n s t   z o n e I t e m   =   d o c u m e n t . c r e a t e E l e m e n t ( ' d i v ' ) ;  
                 z o n e I t e m . c l a s s N a m e   =   ' z o n e - i t e m ' ;  
                 z o n e I t e m . o n c l i c k   =   ( )   = >   {  
                         / /   D e t e r m i n e   w h i c h   t r i b e   t o   f i l t e r   b y .    
                         / /   I f   m u l t i p l e   t r i b e s ,   m a y b e   f i l t e r   b y   R e g i o n ?    
                         / /   C u r r e n t   f i l t e r   l o g i c   i s   T r i b e - b a s e d .    
                         / /   L e t ' s   p i c k   t h e   f i r s t   t r i b e   f o r   n o w   o r   i m p l e m e n t   r e g i o n   f i l t e r i n g .  
                         / /   T h e   u s e r   r e q u e s t e d   " r e g i o n s "   o n   t h e   m a p ,   u s u a l l y   l i n k e d   t o   1   t r i b e .  
                         c o n s t   p r i m a r y T r i b e   =   A r r a y . f r o m ( z o n e M a p [ r e g i o n ] ) [ 0 ] ;  
                         w i n d o w . f i l t e r B y T r i b e ( p r i m a r y T r i b e ) ;  
                 } ;  
  
                 z o n e I t e m . i n n e r H T M L   =   `  
                                 < d i v   c l a s s = " z o n e - n a m e " > $ { r e g i o n . t o U p p e r C a s e ( ) } < / d i v >  
                                 < d i v   c l a s s = " t r i b e - n a m e " > $ { t r i b e s } < / d i v >  
                         ` ;  
                 z o n e s L i s t . a p p e n d C h i l d ( z o n e I t e m ) ;  
         } ) ;  
 }  
 