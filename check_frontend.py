def check_files():
    files = ['script.js', 'style.css']
    keywords = ["Sun-Bleached", "Sun-Scorched", "Verdant", "Emerald", "Mushroom"]
    
    found = False
    for filepath in files:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                for kw in keywords:
                    if kw.lower() in content.lower():
                        print(f"Found '{kw}' in {filepath}")
                        found = True
        except FileNotFoundError:
            print(f"could not find {filepath}")

    if not found:
        print("No keywords found in frontend files.")

if __name__ == "__main__":
    check_files()
