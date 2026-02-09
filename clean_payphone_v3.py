from PIL import Image

def ultimate_clean():
    path = 'assets/images/pay_phone.png'
    try:
        img = Image.open(path).convert("RGBA")
        pixels = img.load()
        width, height = img.size
        print(f"Processing {width}x{height} image...")
        
        visited = set()
        queue = []
        
        # Start from all corners (assuming they are background)
        starts = [(0,0), (width-1, 0), (0, height-1), (width-1, height-1)]
        for s in starts:
            queue.append(s)
            visited.add(s)
            
        cleaned_count = 0
        
        while queue:
            x, y = queue.pop(0)
            
            # Get pixel color
            r, g, b, a = pixels[x, y]
            
            # HEURISTIC: Is this pixel part of the Blue Phone?
            # Blue should be dominant.
            # If B > R+20 and B > G+20, it's likely the blue paint or glass.
            # Also check for dark blue roof lines.
            
            is_blue = (b > r + 15) and (b > g + 15)
            # What if it's white highlight? (255, 255, 255)
            # The background checkerboard might be white too.
            # But the flood fill ensures we only eat white connected to the outside.
            # We must be careful not to eat white highlights INSIDE the phone if the border is open.
            # Assuming the phone has a dark outline.
            
            # Let's try a safer heuristic:
            # If it looks like GREY (r~=g~=b), it's background.
            is_grey = abs(r - g) < 20 and abs(g - b) < 20 and abs(r - b) < 20
            
            # If it's NOT Blue AND (It IS Grey OR It matches known background colors), remove it.
            
            # Actually, simply stopping at "Blue" is safest for a blue object.
            # If it's NOT Blue, we treat it as background candiate.
            # But we must stop at the object boundary.
            
            if is_blue:
                continue # Hit the object, stop spreading
            
            # If we are here, it's not Blue. Likely background (Grey/Black/White).
            # Remove it.
            pixels[x, y] = (0, 0, 0, 0)
            cleaned_count += 1
            
            # Add neighbors
            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < width and 0 <= ny < height:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        
        print(f"Cleaned {cleaned_count} pixels.")
        img.save(path)
        print(f"Saved to {path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ultimate_clean()
