import json
import math

file_path = 'c:/Users/sajit/OneDrive/Desktop/flame quill photos/refined/flare_quills_data.json'

heal_keywords = ['Heal', 'Restore', 'Mend', 'Revive', 'Regen', 'Cure', 'Health', 'Life']
drain_keywords = ['Drain', 'Decay', 'Rot', 'Wither', 'Leech', 'Siphon', 'Sap', 'Life Steal']

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    updated_count = 0
    for char in data['flare_quills']:
        atk_dmg = char.get('attack_damage', 30)
        powers = char.get('powers', [])
        explanations = char.get('power_explanations', ["", ""])
        current_damages = char.get('power_damages', [0, 0])
        
        heal_amounts = [0, 0]
        is_drain = [False, False]
        
        for i in range(min(2, len(powers))):
            p_name = powers[i]
            p_desc = explanations[i] if i < len(explanations) else ""
            
            # Check Heal
            is_healing = any(k.lower() in p_name.lower() or k.lower() in p_desc.lower() for k in heal_keywords)
            
            # Check Drain
            is_draining = any(k.lower() in p_name.lower() or k.lower() in p_desc.lower() for k in drain_keywords)
            
            if is_healing:
                multiplier = 2 if i == 0 else 3.5
                heal_val = math.floor(atk_dmg * multiplier)
                heal_amounts[i] = heal_val
                current_damages[i] = 0 # Remove damage if it's a pure heal
            
            if is_draining:
                is_drain[i] = True
                # Damage remains as is from previous pass
        
        char['power_heal_amounts'] = heal_amounts
        char['power_is_drain'] = is_drain
        char['power_damages'] = current_damages # Update in case we zeroed it out
        
        updated_count += 1

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    
    print(f"Successfully added Heal/Drain stats to {updated_count} characters.")

except Exception as e:
    print(f"Error updating file: {e}")
