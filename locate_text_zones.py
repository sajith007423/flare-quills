import cv2
import numpy as np
import json

def analyze_map():
    try:
        img = cv2.imread('world_map.png')
        if img is None:
            print("Could not read image")
            return

        h, w = img.shape[:2]
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Assuming text is somewhat bright or distinct
        # Adaptive thresholding might work well to isolate text characters
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY_INV, 11, 2)
        
        # Dilate to merge text characters into single blobs
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 5)) # Wider kernel for horizontal text
        dilated = cv2.dilate(thresh, kernel, iterations=2)
        
        # Find contours
        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        regions = []
        for cnt in contours:
            x, y, w_rect, h_rect = cv2.boundingRect(cnt)
            
            # Filter small noise and very large regions
            if w_rect > 50 and h_rect > 15 and w_rect < 400 and h_rect < 100:
                cx = x + w_rect // 2
                cy = y + h_rect // 2
                
                # Normalize to percentage
                cx_pct = round((cx / w) * 100, 1)
                cy_pct = round((cy / h) * 100, 1)
                
                regions.append({
                    "x": x, "y": y, "w": w_rect, "h": h_rect,
                    "center_pct": (cx_pct, cy_pct),
                    "area": w_rect * h_rect
                })

        # Sort by vertical position to help identify them
        regions.sort(key=lambda r: r['y'])
        
        print(f"Found {len(regions)} potential text regions:")
        for r in regions:
            print(f"Pos: {r['center_pct']}%, Rect: {r['x']},{r['y']} {r['w']}x{r['h']}")
            
    except ImportError:
        print("OpenCV (cv2) not available. Please install opencv-python.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    analyze_map()
