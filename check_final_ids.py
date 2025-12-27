import json

def check_final():
    ids = ["2.png", "19.png", "87.png", "88.png", "98.png", "99.png"]
    with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print(f"{'ID':<10} | {'Name':<25} | {'Tribe':<25} | {'Region':<25}")
    print("-" * 90)

    for char in data.get('flare_quills', []):
        if char['id'] in ids:
            print(f"{char['id']:<10} | {char['name']:<25} | {char.get('tribe'):<25} | {char.get('region'):<25}")

if __name__ == "__main__":
    check_final()
