
from PIL import Image
import math

def get_average_color(img, x, y, w, h):
    # Crop the cell
    cell = img.crop((x, y, x + w, y + h))
    # Resize to 1x1 to get average
    cell = cell.resize((1, 1), Image.Resampling.LANCZOS)
    return cell.getpixel((0, 0))

def color_distance(c1, c2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(c1, c2)))

def identify_tribe(rgb):
    r, g, b = rgb
    # Define expected averages for tribes
    tribes = {
        "Inferno Legion": (255, 69, 0), # Red/Orange
        "Verdant Circle": (34, 139, 34), # Forest Green
        "Tideborn Covenant": (173, 216, 230), # Light Blue/Ice
        "Shadow Cabal": (75, 0, 130), # Indigo/Purple
        "Storm Vanguard": (255, 215, 0), # Gold/Yellow (Lightning) or Grey
        "Iron Legion": (169, 169, 169), # Dark Gray
        "Highborn Court": (255, 223, 0), # Golden Yellow
        "Crystalline Guard": (255, 182, 193), # Pink/Crystal
        "Void Gastronomes": (20, 20, 40), # Very Dark
        "Culinary Corps": (210, 105, 30), # Chocolate/Orange
        "Mystic Enclave": (138, 43, 226), # Blue Violet
        "Unexplored": (50, 50, 50) # Dark Grey
    }
    
    # Heuristics
    if r > 200 and g < 100: return "Inferno/Void(Crimson)", rgb
    if g > 150 and r < 150 and b < 150: return "Verdant Circle", rgb
    if b > 200 and r < 100: return "Tideborn/Mystic", rgb
    if r > 200 and g > 200 and b < 100: return "Highborn/Storm", rgb
    if r > 100 and g > 100 and b > 100 and max(r,g,b)-min(r,g,b) < 30: return "Iron/Unexplored", rgb
    
    # Closest match
    best_tribe = None
    min_dist = float('inf')
    for name, color in tribes.items():
        dist = color_distance(rgb, color)
        if dist < min_dist:
            min_dist = dist
            best_tribe = name
            
    return best_tribe, rgb

try:
    img = Image.open("world_map.png").convert("RGB")
    width, height = img.size
    cols = 3
    rows = 4
    cell_w = width // cols
    cell_h = height // rows

    print(f"Image Size: {width}x{height}")
    print("Grid Layout:")
    for r in range(rows):
        row_str = ""
        for c in range(cols):
            x = c * cell_w
            y = r * cell_h
            avg_color = get_average_color(img, x, y, cell_w, cell_h)
            tribe_guess, rgb = identify_tribe(avg_color)
            # Shorten names for table
            name = tribe_guess.split(' ')[0]
            if "Void" in tribe_guess and "Gastronomes" in tribe_guess: name = "Void"
            elif "Inferno" in tribe_guess: name = "Inferno"
            elif "Tideborn" in tribe_guess: name = "Tideborn"
            elif "Shadow" in tribe_guess: name = "Shadow"
            elif "Storm" in tribe_guess: name = "Storm"
            elif "Highborn" in tribe_guess: name = "Highborn"
            elif "Verdant" in tribe_guess: name = "Verdant"
            elif "Iron" in tribe_guess: name = "Iron"
            elif "Crystalline" in tribe_guess: name = "Crystal"
            elif "Culinary" in tribe_guess: name = "Culinary"
            elif "Mystic" in tribe_guess: name = "Mystic"
            
            row_str += f"{name:<12} "
        print(row_str)

except Exception as e:
    print(f"Error: {e}")
