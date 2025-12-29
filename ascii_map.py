import cv2
import numpy as np

def ascii_map():
    img = cv2.imread('world_map.png')
    if img is None: return
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Resize to small grid
    h, w = gray.shape
    grid_h, grid_w = 32, 64
    small = cv2.resize(gray, (grid_w, grid_h))
    
    # Calculate gradients on the original image first? 
    # Better: resize original, calculate variance?
    # Simple edge detection on original, then resize
    edges = cv2.Canny(gray, 100, 200)
    
    # Resize edges to grid, summing up edges
    # We want to know density of edges in each cell
    cell_h = h // grid_h
    cell_w = w // grid_w
    
    print(f"ASCII Map ({grid_w}x{grid_h}):")
    print("+" + "-"*grid_w + "+")
    
    for r in range(grid_h):
        line = "|"
        for c in range(grid_w):
            y1, x1 = r * cell_h, c * cell_w
            y2, x2 = y1 + cell_h, x1 + cell_w
            chunk = edges[y1:y2, x1:x2]
            
            # If significant edges, mark it
            density = np.sum(chunk) / 255
            if density > (cell_h * cell_w * 0.1): # >10% are edges
                line += "#"
            elif density > (cell_h * cell_w * 0.05):
                line += ":"
            else:
                line += " "
        line += "|"
        print(line)
    print("+" + "-"*grid_w + "+")

if __name__ == "__main__":
    ascii_map()
