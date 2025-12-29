import json

json_path = "flare_quills_data.json"
js_path = "data.js"

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

js_content = f"const flareQuillsData = {json.dumps(data, indent=4)};"

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Synced data.js with flare_quills_data.json")
