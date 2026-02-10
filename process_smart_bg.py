from PIL import Image
import sys
import os

def smart_remove_bg(input_path, output_path, tolerance=30):
    print(f"Processing {input_path} -> {output_path}")
    try:
        img = Image.open(input_path).convert("RGBA")
        width, height = img.size
        pixels = img.load()
        
        # Visited set for BFS
        visited = set()
        queue = []
        
        # Start from corners (assuming white background)
        starts = [(0, 0), (width-1, 0), (0, height-1), (width-1, height-1)]
        for s in starts:
            if s not in visited:
                queue.append(s)
                visited.add(s)
        
        # Flood Fill
        while queue:
            x, y = queue.pop(0)
            
            # Get current pixel color
            r, g, b, a = pixels[x, y]
            
            # Check if it's "white enough" to be background
            if r > 255 - tolerance and g > 255 - tolerance and b > 255 - tolerance:
                # Make transparent
                pixels[x, y] = (255, 255, 255, 0)
                
                # Check neighbors
                neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
                for nx, ny in neighbors:
                    if 0 <= nx < width and 0 <= ny < height:
                        if (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
            # If not white, it's an edge/object, stop flood
    
        # Crop to content
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
            
        img.save(output_path, "PNG")
        print("Success.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Shizuka
    shizuka_src = '/Users/jdi/.gemini/antigravity/brain/57293d76-3461-4b6d-a0e5-191a7633435e/iso_shizuka_house_1770718810213.png'
    shizuka_dst = '/Users/jdi/Documents/GitHub/doraemon-presentation/assets/images/iso_shizuka_house.png'
    smart_remove_bg(shizuka_src, shizuka_dst)
