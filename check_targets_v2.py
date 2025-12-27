import json

def check_irregular_details():
    try:
        with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: flare_quills_data.json not found.")
        return

    targets = ["Sun-Scorched Nomads", "Verdant Circle", "Mystic Enclave"]
    
    # Also check by region keywords just in case
    region_keywords = ["Sun-Bleached", "Mushroom", "Emerald"]

    print(f"{'ID':<10} | {'Name':<25} | {'Tribe':<25} | {'Region':<25}")
    print("-" * 90)

    for char in data.get('flare_quills', []):
        tribe = char.get('tribe', 'Unknown')
        region = char.get('region', 'Unknown')
        
        match_tribe = tribe in targets
        match_region = any(k.lower() in region.lower() for k in region_keywords)

        if match_tribe or match_region:
            print(f"{char.get('id'):<10} | {char.get('name'):<25} | {tribe:<25} | {region:<25}")

if __name__ == "__main__":
    check_irregular_details()
