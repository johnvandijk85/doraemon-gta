from PIL import Image
import os

def check_and_fix_door():
    path = 'assets/images/cave_door_stone.png'
    if not os.path.exists(path):
        print("Door not found.")
        return

    img = Image.open(path).convert("RGBA")
    pixels = img.load()
    w, h = img.size
    
    # Check corners
    corners = [(0,0), (w-1, 0), (0, h-1), (w-1, h-1)]
    transparent_corners = 0
    bg_color = None
    
    for x, y in corners:
        if pixels[x, y][3] == 0:
            transparent_corners += 1
        else:
            bg_color = pixels[x, y]
            
    if transparent_corners == 4:
        print("Door is already transparent.")
        return

    print(f"Door has background {bg_color}. Fixing...")
    
    # Simple Flood Fill from corners
    from collections import deque
    queue = deque(corners)
    visited = set(corners)
    
    # Tolerance
    tol = 30
    
    start_color = bg_color
    
    def matches(c1, c2):
        return sum(abs(a-b) for a,b in zip(c1, c2)) < tol

    while queue:
        x, y = queue.popleft()
        if not (0 <= x < w and 0 <= y < h): continue
        
        current = pixels[x, y]
        if matches(current, start_color):
            pixels[x, y] = (0, 0, 0, 0)
            
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    img.save(path)
    print("Door background removed.")

if __name__ == "__main__":
    check_and_fix_door()
