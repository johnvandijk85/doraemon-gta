from PIL import Image
import os
from collections import Counter

def recover_assets():
    img_path = 'assets/images/restored_screenshot.png'
    if not os.path.exists(img_path):
        print("Screenshot not found.")
        return

    print(f"Loading {img_path}...")
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    
    # Analyze 50x50 blocks
    # We assume the game is grid aligned to some offset.
    # To find the offset, we can check where the changes happen? 
    # Or simpler: The screenshot likely starts at (0,0) of the canvas?
    # Let's try offsets 0 to 49 for x and y.
    # That's too slow.
    # Let's assume standard alignment or try to find a known pattern.
    # Actually, in the game, the canvas fills the window, but the camera moves.
    # However, tiles are 50x50.
    
    # Let's try to extract distinct 50x50 distinct blocks that appear multiple times.
    tile_counts = Counter()
    tile_images = {}
    
    # Scan with stride 10 to speed up? No, alignment issues.
    # Let's simple scan 0,0 with stride 50 first. 
    # If that fails, we can try other offsets.
    
    # Just generic distinct blocks
    tiles = []
    
    # Limiting scan for performance
    print("Scanning image...")
    # Heuristic: Start from center, scan outwards?
    # Or just scan the whole thing with a grid.
    # Let's try grid scan with a few offsets.
    
    found_tiles = []
    
    for off_y in [0, 10, 20, 25, 30, 40]: # Rough alignment check
        for off_x in [0, 10, 20, 25, 30, 40]:
             for y in range(off_y, height, 50):
                if y + 50 > height: break
                for x in range(off_x, width, 50):
                    if x + 50 > width: break
                    
                    # Get crop
                    crop = img.crop((x, y, x+50, y+50))
                    # Quick hash: use the bytes
                    h = crop.tobytes()
                    
                    if h not in tile_counts:
                         tile_images[h] = crop
                    tile_counts[h] += 1

    print(f"Found {len(tile_counts)} unique tiles.")
    
    # Filter by occurrence (must appear at least 3 times to be a tile?)
    common = tile_counts.most_common(20)
    
    print("Saving top common tiles...")
    for i, (h, count) in enumerate(common):
        print(f"Tile {i}: count={count}")
        # Save validation image
        # Don't save empty/transparent ones
        tile = tile_images[h]
        extrema = tile.getextrema()
        # extrema is list of (min, max) for R, G, B, A
        # If A is all 0, skip
        if extrema[3][1] == 0:
            print("  (Skipping fully transparent)")
            continue
            
        tile.save(f'assets/images/recovered_tile_{i}.png')

if __name__ == "__main__":
    recover_assets()
