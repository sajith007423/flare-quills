
import json
import random

def calculate_hp(char):
    ember_cost = char.get("ember_cost", 1)
    occupation = char.get("occupation", "").lower()
    
    # Base formula: 50 + (Cost * 20)
    base_hp = 50 + (ember_cost * 20)
    
    # Variance ±10%
    variance = base_hp * 0.1
    hp = base_hp + random.uniform(-variance, variance)
    
    # Occupational modifiers
    if any(word in occupation for word in ["knight", "soldier", "sentinel", "warden", "defender"]):
        hp *= 1.15  # Tanky
    elif any(word in occupation for word in ["mage", "wizard", "warlock", "seer", "scholar"]):
        hp *= 0.90  # Glass Cannon
        
    return int(hp)

def update_data():
    json_path = "flare_quills_data.json"
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if "flare_quills" in data:
            for char in data["flare_quills"]:
                char["hitpoints"] = calculate_hp(char)
        else:
            print("Error: 'flare_quills' key not found.")
            return
            
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
        print(f"Successfully updated {len(data['flare_quills'])} characters with hitpoints.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_data()
