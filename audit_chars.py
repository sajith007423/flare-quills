import json

with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

ids_to_check = ["1.png", "10.png", "19.png", "20.png", "32.png", "55.png", "84.png"]

print(f"{'ID':<10} | {'Name':<20} | {'Tribe':<20} | {'Region':<20}")
print("-" * 80)

for char in data['flare_quills']:
    if char['id'] in ids_to_check:
        print(f"{char['id']:<10} | {char['name']:<20} | {char['tribe']:<20} | {char['region']:<20}")
