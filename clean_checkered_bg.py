from PIL import Image
import os
from collections import deque

def remove_bg_global_safe(path):
    # For Cars: Protects white tires (>235)
    if not os.path.exists(path):
        print(f"Skipping {path}: Not found")
        return

    print(f"Processing Car {path} (Global Safe)...")
    try:
        img = Image.open(path).convert("RGBA")
    except Exception as e:
        print(f"Failed to open {path}: {e}")
        return

    pixels = img.load()
    w, h = img.size
    
    changes = 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if a == 0: continue
            
            # Check for Neutral/Grey
            is_neutral = abs(r-g) < 30 and abs(g-b) < 30 and abs(r-b) < 30
            
            # Safe Range (Protects White Tires > 235)
            if 80 < r < 235 and 80 < g < 235 and 80 < b < 235 and is_neutral:
                pixels[x, y] = (0, 0, 0, 0)
                changes += 1
                
    img.save(path)
    print(f"  Done. Removed {changes} pixels.")

def remove_bg_pickup(path):
    # For Pickups: Aggressive Global Removal of Neutral Colors (Greys/Whites)
    if not os.path.exists(path): return

    print(f"Processing Pickup {path} (Global Neutral Removal)...")
    img = Image.open(path).convert("RGBA")
    pixels = img.load()
    w, h = img.size
    
    changes = 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if a == 0: continue
            
            # Check for Neutrality (Low Saturation)
            is_neutral = abs(r-g) < 40 and abs(g-b) < 40 and abs(r-b) < 40
            
            # Target Brightness: lowered to > 5 to catch EVERYTHING not pitch black
            # Protect only pitch blacks (outlines < 5)
            # Most outlines are 0,0,0 or very dark. 55 is definitely trash.
            is_bright_enough = r > 5 and g > 5 and b > 5
            
            if is_neutral and is_bright_enough:
                pixels[x, y] = (0, 0, 0, 0)
                changes += 1
    
    # Save as v3 to bust cache
    new_path = path.replace('.png', '_v3.png')
    img.save(new_path)
    print(f"  Done. Removed {changes} pixels. Saved to {new_path}")

if __name__ == "__main__":
    cars = [
        # Cars are fine, skip them to save time or just run safe mode
        # 'assets/images/car_blue.png',
        # 'assets/images/car_green.png',
        # 'assets/images/car_yellow.png' 
    ]
    pickups = [
        'assets/images/pickup_health.png',
        'assets/images/pickup_armor.png'
    ]
    
    # for c in cars:
    #     remove_bg_global_safe(c)
        
    for p in pickups:
        remove_bg_pickup(p)
