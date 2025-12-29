import cv2
import numpy as np

def analyze_map_v2():
    try:
        img = cv2.imread('world_map.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Use Canny edge detection
        edges = cv2.Canny(gray, 100, 200)
        
        # Dilate to connect edges of text
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 5))
        dilated = cv2.dilate(edges, kernel, iterations=3)
        
        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        regions = []
        h, w = img.shape[:2]
        
        for cnt in contours:
            x, y, w_rect, h_rect = cv2.boundingRect(cnt)
            # Relaxed size constraints
            if w_rect > 40 and h_rect > 10:
                cx = x + w_rect // 2
                cy = y + h_rect // 2
                
                cx_pct = round((cx / w) * 100, 1)
                cy_pct = round((cy / h) * 100, 1)
                
                regions.append({
                    "center_pct": (cx_pct, cy_pct),
                    "rect": (x, y, w_rect, h_rect),
                    "area": w_rect * h_rect
                })

        # Sort by Y then X to roughly order them top-down, left-right
        regions.sort(key=lambda r: (r['center_pct'][1], r['center_pct'][0]))
        
        print(f"Found {len(regions)} regions:")
        for r in regions:
            print(f"Pos: {r['center_pct']}%, Area: {r['area']}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_map_v2()
