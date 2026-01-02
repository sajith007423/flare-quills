
import json
import math

JSON_PATH = 'c:/Users/sajit/OneDrive/Desktop/flame quill photos/refined/flare_quills_data.json'
JS_PATH = 'c:/Users/sajit/OneDrive/Desktop/flame quill photos/refined/data.js'

def calculate_power_score(quill):
    hp = quill.get('hitpoints', 0)
    ad = quill.get('attack_damage', 0)
    p_dmgs = quill.get('power_damages', [])
    avg_pd = sum(p_dmgs) / len(p_dmgs) if p_dmgs else 0
    return hp + ad + avg_pd

def get_growth_multiplier(level):
    # 5% compound growth per level
    # Base is Level 1 (multiplier 1.0)
    return 1.05 ** (level - 1)

def get_upgrade_cost(rarity, level):
    # Returns (Gold, Cards)
    # Level 1 has 0 cost to reach (you start there)
    # This cost is to UPGRADE TO this level. e.g. Cost for Lvl 2.
    
    if level == 1:
        return 0, 0

    l = level 
    
    if rarity == 'Community': # Fallback if error, treat as Common
        rarity = 'Common'

    if rarity == 'Common':
        # Low Gold, High Cards
        # Gold: Base 5, growing * 1.15
        gold = int(5 * (1.15 ** (l - 2))) * 10 
        # Cards: Base 20, growing * 1.1
        cards = int(20 * (1.10 ** (l - 2)))
        
    elif rarity == 'Rare':
        # Med Gold, Med Cards
        # Gold: Base 50, growing * 1.13
        gold = int(50 * (1.13 ** (l - 2))) * 10
        # Cards: Base 10, growing * 1.08
        cards = int(10 * (1.08 ** (l - 2)))

    elif rarity == 'Epic':
        # High Gold, Low Cards
        # Gold: Base 200, growing * 1.11
        gold = int(200 * (1.11 ** (l - 2))) * 10
        # Cards: Base 2, growing * 1.06
        cards = int(2 * (1.06 ** (l - 2)))

    elif rarity == 'Legendary':
        # Very High Gold, Very Low Cards
        # Gold: Base 1000, growing * 1.09
        gold = int(1000 * (1.09 ** (l - 2))) * 10
        # Cards: 1 every level? Or varying. 
        # Let's make it 1 card every level to start, then 2, etc.
        # Base 1, growing * 1.04
        cards = int(1 * (1.04 ** (l - 2)))
        if cards < 1: cards = 1

    # Cap/floor adjustments
    if gold < 0: gold = 0
    if cards < 1: cards = 1
    
    return gold, cards

def main():
    with open(JSON_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    quills = data['flare_quills']
    
    # 1. Calculate Power Scores
    for q in quills:
        q['power_score'] = int(calculate_power_score(q))
    
    # 2. Sort by Power Score Descending
    quills.sort(key=lambda x: x['power_score'], reverse=True)
    
    # 3. Assign Rarity
    # Top 10 = Legendary
    # Next 20 = Epic
    # Next 30 = Rare
    # Rest = Common
    total = len(quills)
    
    for i, q in enumerate(quills):
        if i < 10:
            q['rarity'] = 'Legendary'
        elif i < 30:
            q['rarity'] = 'Epic'
        elif i < 60:
            q['rarity'] = 'Rare'
        else:
            q['rarity'] = 'Common'
            
    # 4. Generate Upgrade Charts
    for q in quills:
        base_hp = q['hitpoints']
        base_ad = q['attack_damage']
        base_p_dmgs = q['power_damages']
        
        upgrade_chart = []
        
        for lvl in range(1, 100):
            mult = get_growth_multiplier(lvl)
            
            # Stats
            hp = int(base_hp * mult)
            ad = int(base_ad * mult)
            p_dmg = [int(p * mult) for p in base_p_dmgs]
            
            # Cost to reach this level (from prev)
            cost_gold, cost_cards = get_upgrade_cost(q['rarity'], lvl)
            
            upgrade_chart.append({
                'level': lvl,
                'hitpoints': hp,
                'attack_damage': ad,
                'power_damages': p_dmg,
                'cost_gold': cost_gold,
                'cost_cards': cost_cards
            })
            
        q['upgrade_chart'] = upgrade_chart

    # Save JSON
    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    print("Updated flare_quills_data.json with Rarity and Upgrade Charts.")

    # Update JS
    js_content = f"const flareQuillsData = {json.dumps(data, indent=4)};"
    with open(JS_PATH, 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    print("Updated data.js")

if __name__ == '__main__':
    main()
