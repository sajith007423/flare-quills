import json

with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# IDs 84 to 100
ids_to_check = [f"{i}.png" for i in range(84, 101)]

print(f"{'ID':<10} | {'Name':<20} | {'Occupation':<15} | {'Origin Story':<30}")
print("-" * 80)

for char in data['flare_quills']:
    if char['id'] in ids_to_check:
        story = char.get('origin_story', '')[:25] + "..."
        print(f"{char['id']:<10} | {char['name']:<20} | {char['occupation']:<15} | {story:<30}")
