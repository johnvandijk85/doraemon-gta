from PIL import Image
import os
import collections

def remove_white_bg(path, tolerance=30):
    if not os.path.exists(path):
        print(f"Skipping {path}: Not found")
        return

    print(f"Processing {path}...")
    img = Image.open(path).convert("RGBA")
    pixels = img.load()
    w, h = img.size
    
    # Identify background color from corners
    corners = [(0,0), (w-1,0), (0,h-1), (w-1,h-1)]
    
    start_color = pixels[0, 0]
    
    # Simple check if already transparent
    if start_color[3] == 0:
        print("  Already transparent.")
        return

    print(f"  Removing background color: {start_color}")
    
    # Flood fill algorithm
    queue = collections.deque([(0, 0), (w-1, 0), (0, h-1), (w-1, h-1)])
    visited = set(queue)
    
    def color_match(c1, c2):
        return sum(abs(a-b) for a,b in zip(c1[:3], c2[:3])) < tolerance

    while queue:
        x, y = queue.popleft()
        
        # Check bounds
        if not (0 <= x < w and 0 <= y < h): continue
        
        current = pixels[x, y]
        
        if color_match(current, start_color):
            pixels[x, y] = (0, 0, 0, 0) # Make transparent
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    img.save(path)
    print("  Done.")

if __name__ == "__main__":
    remove_white_bg('assets/images/target_enemy.png')
