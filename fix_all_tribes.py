import json

def check_irregular_tribes():
    with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    standard_tribes = [
        "Inferno Legion", "Highborn Court", "Tideborn Covenant", 
        "Storm Vanguard", "Iron Legion", "Void Gastronomes", 
        "Crystalline Guard", "Culinary Corps", "Shadow Cabal"
    ]

    print(f"{'ID':<10} | {'Name':<20} | {'Tribe':<25} | {'Region':<25}")
    print("-" * 90)

    for char in data.get('flare_quills', []):
        tribe = char.get('tribe', 'Unknown')
        if tribe not in standard_tribes:
            print(f"{char.get('id'):<10} | {char.get('name'):<20} | {tribe:<25} | {char.get('region'):<25}")

if __name__ == "__main__":
    check_irregular_tribes()
