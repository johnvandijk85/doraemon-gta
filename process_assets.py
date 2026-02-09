import os
from PIL import Image
from collections import deque

files = [
    'assets/images/doraemon_sheet.png',
    'assets/images/mouse_enemy.png',
    'assets/images/dorayaki.png',
    'assets/images/tileset.png',
    'assets/images/anywhere_door.png',
    'assets/images/cave_enemy_bat.png'
]

def make_transparent(path):
    if not os.path.exists(path):
        print(f"Skipping {path} (not found)")
        return

    print(f"Processing {path}...")
    img = Image.open(path).convert("RGBA")
    width, height = img.size
    pixels = img.load()
    
    # 1. Detect background colors (checkerboard)
    bg1 = pixels[0, 0]
    bg2 = bg1
    
    # Scan top-left area for a second color
    for y in range(min(50, height)):
        for x in range(min(50, width)):
            p = pixels[x, y]
            diff = sum(abs(c1 - c2) for c1, c2 in zip(p, bg1))
            if diff > 30: # tolerance
                bg2 = p
                print(f"  Found stats: BG1={bg1}, BG2={bg2}")
                break
        if bg2 != bg1: break
    
    if bg2 == bg1:
        print(f"  Single background color detected: {bg1}")

    # 2. Flood Fill Logic
    queue = deque()
    visited = set()

    def add_seed(x, y):
        if (x, y) not in visited:
            visited.add((x, y))
            queue.append((x, y))

    # Seed from all 4 borders
    for x in range(width):
        add_seed(x, 0)
        add_seed(x, height - 1)
    for y in range(height):
        add_seed(0, y)
        add_seed(width - 1, y)
    
    # Updated matching logic
    def is_grey(p):
        # Specific detection for the noisy grey background found (approx 150-160)
        # Also include the original light grey (approx 200)
        r, g, b, a = p
        if a == 0: return True # treat transparent as matching to continue fill
        
        # Check if it's grayscale-ish
        if max(abs(r-g), abs(r-b), abs(g-b)) > 20: return False
        
        # Check brightness range (found 154ish, previously 200ish)
        # Broaden range to catch all background squares
        return (130 < r < 220)

    def matches_bg(p):
        if p[3] == 0: return True # treat transparent as bg
        # Check against initial seeds (mostly for other images)
        d1 = sum(abs(c1 - c2) for c1, c2 in zip(p, bg1))
        d2 = sum(abs(c1 - c2) for c1, c2 in zip(p, bg2))
        
        if d1 < 50 or d2 < 50: return True
        return is_grey(p)

    count = 0
    while queue:
        x, y = queue.popleft()
        
        if not (0 <= x < width and 0 <= y < height):
            continue

        p = pixels[x, y]
        
        # If already transparent, continue flood fill through it
        if p[3] == 0:
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
            continue

        if matches_bg(p):
            pixels[x, y] = (0, 0, 0, 0) # Clear
            count += 1
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    print(f"  Cleared {count} pixels.")
    img.save(path)

for f in files:
    make_transparent(f)
