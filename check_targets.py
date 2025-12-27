import json

def check_irregular_details():
    with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    targets = ["Sun-Scorched Nomads", "Verdant Circle", "Mystic Enclave"]

    print(f"{'ID':<10} | {'Name':<20} | {'Tribe':<25} | {'Region':<25} | {'Origin':<50}")
    print("-" * 140)

    for char in data.get('flare_quills', []):
        tribe = char.get('tribe', 'Unknown')
        if tribe in targets:
            print(f"{char.get('id'):<10} | {char.get('name'):<20} | {tribe:<25} | {char.get('region'):<25} | {char.get('origin_story', '')[:50]}")

if __name__ == "__main__":
    check_irregular_details()
