import json

json_path = 'c:/Users/sajit/OneDrive/Desktop/flame quill photos/refined/flare_quills_data.json'
js_path = 'c:/Users/sajit/OneDrive/Desktop/flame quill photos/refined/data.js'

try:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    js_content = f"const flareQuillsData = {json.dumps(data, indent=4)};"

    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    print("Successfully updated data.js with content from flare_quills_data.json")

except Exception as e:
    print(f"Error: {e}")
