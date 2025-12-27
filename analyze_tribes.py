import json
from collections import Counter

def analyze():
    try:
        with open('flare_quills_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: flare_quills_data.json not found.")
        return

    tribes = Counter()
    regions = Counter()

    for char in data.get('flare_quills', []):
        tribes[char.get('tribe', 'Unknown')] += 1
        regions[char.get('region', 'Unknown')] += 1

    print("\n--- Tribes ---")
    for tribe, count in tribes.most_common():
        print(f"{tribe}: {count}")

    print("\n--- Regions ---")
    for region, count in regions.most_common():
        print(f"{region}: {count}")

if __name__ == "__main__":
    analyze()
