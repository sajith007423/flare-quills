import json
import os

# Load JSON data
try:
    with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    existing_ids = {item['id'] for item in data.get('flare_quills', [])}
except (FileNotFoundError, json.JSONDecodeError):
    existing_ids = set()

# Check for missing IDs from 1.png to 100.png
missing_ids = []
for i in range(1, 101):
    image_id = f"{i}.png"
    if image_id not in existing_ids:
        missing_ids.append(image_id)

print(f"Total existing characters: {len(existing_ids)}")
print(f"Missing IDs count: {len(missing_ids)}")
if missing_ids:
    print(f"Missing IDs: {missing_ids}")
else:
    print("No missing data for images 1-100.")
