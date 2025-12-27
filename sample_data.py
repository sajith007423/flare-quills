import json

with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

ids_to_check = [f"{i}.png" for i in range(78, 84)] + [f"{i}.png" for i in range(30, 41)]

print(f"{'ID':<10} | {'Name':<20} | {'Tribe':<20} | {'Story Prefix':<30}")
print("-" * 90)

for char in data['flare_quills']:
    if char['id'] in ids_to_check:
        story = char.get('origin_story', '')[:25] + "..."
        print(f"{char['id']:<10} | {char['name']:<20} | {char['tribe']:<20} | {story:<30}")
