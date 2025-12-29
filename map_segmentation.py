import cv2
import numpy as np
from collections import Counter

def segment_map():
    img = cv2.imread('world_map.png')
    if img is None: return
    
    # Quantize colors to reduce noise
    data = np.float32(img).reshape((-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    # K-means with K=8 to find dominant colors
    K = 8
    # Use random state for reproducibility
    _, label, center = cv2.kmeans(data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    quantized = res.reshape((img.shape))
    
    # Convert to gray
    gray = cv2.cvtColor(quantized, cv2.COLOR_BGR2GRAY)
    
    # Assume distinct text is high freq. Use gradient.
    grad_x = cv2.Sobel(gray, cv2.CV_16S, 1, 0, ksize=3)
    grad_y = cv2.Sobel(gray, cv2.CV_16S, 0, 1, ksize=3)
    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)
    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    
    # Threshold gradient to find "busy" areas (text)
    _, thresh = cv2.threshold(grad, 40, 255, cv2.THRESH_BINARY)
    
    # Morphological closing to group text letters
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 8))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    
    contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    regions = []
    h, w = img.shape[:2]
    
    for cnt in contours:
        x, y, w_rect, h_rect = cv2.boundingRect(cnt)
        aspect_ratio = w_rect / float(h_rect)
        
        # Text is usually wider than tall, and not too huge
        if w_rect > 40 and h_rect < 60 and aspect_ratio > 2.0:
            cx = x + w_rect // 2
            cy = y + h_rect // 2
            regions.append({
                "label": "Unknown",
                "x_pct": round(cx / w * 100, 1),
                "y_pct": round(cy / h * 100, 1),
                "w": w_rect,
                "h": h_rect
            })

    # Sort top to bottom, left to right
    regions.sort(key=lambda r: (r['y_pct'], r['x_pct']))
    
    print(f"Found {len(regions)} potential labels:")
    for i, r in enumerate(regions):
        print(f"Region {i+1}: {r['x_pct']}%, {r['y_pct']}% (Size: {r['w']}x{r['h']})")

if __name__ == "__main__":
    segment_map()
