from PIL import Image
from collections import Counter

def analyze_colors():
    try:
        img = Image.open('world_map.png')
        img = img.resize((256, 256)) # Downscale for speed
        pixels = list(img.getdata())
        
        # Count colors
        counts = Counter(pixels)
        
        print(f"Total unique colors: {len(counts)}")
        print("Top 10 most common colors:")
        for color, count in counts.most_common(10):
            print(f"Color: {color}, Count: {count}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_colors()
