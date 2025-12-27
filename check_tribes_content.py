import json

def check():
    with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    print("Checking for 'Mushroom', 'Forest', 'Sun', 'Dunes' in Tribe or Region...\n")

    for char in data.get('flare_quills', []):
        tribe = char.get('tribe', '')
        region = char.get('region', '')
        
        keywords = ['Mushroom', 'Forest', 'Sun', 'Dunes', 'Bleached', 'Scorched']
        if any(k.lower() in tribe.lower() or k.lower() in region.lower() for k in keywords):
            print(f"ID: {char.get('id')} | Name: {char.get('name')} | Tribe: {tribe} | Region: {region}")

if __name__ == "__main__":
    check()
