from PIL import Image, ImageDraw

def clean_and_resize():
    path = 'assets/images/pay_phone.png'
    try:
        img = Image.open(path).convert("RGBA")
        width, height = img.size
        
        # 1. Flood Fill Transparent from Corners
        # This handles solid backgrounds or patterns connected to the edge
        # We'll use ImageDraw.floodfill (requires PIL > 8.x) or manual BFS
        # Let's verify pixel 0,0 and see if we can just make that color transparent?
        # User mentioned "checkerboard", which implies 2 colors.
        # Safer approach: Make a mask.
        
        # Simple heuristic: The phone is in the center. The corners are definitely background.
        # We will walk from corners and erase anything that isn't clearly the blue phone.
        # Since I generated it, I know the phone is Blue.
        
        # Let's try detailed replacement:
        pixels = img.load()
        
        # Sample corners to catch checkerboard variations
        bg_colors = set()
        corners = [(0,0), (width-1, 0), (0, height-1), (width-1, height-1)]
        for x, y in corners:
            bg_colors.add(pixels[x, y])
            
        print(f"Detected potential BG colors: {bg_colors}")
        
        # Aggressive cleaning:
        # If a pixel matches ANY of the corner colors (with tolerance), clear it.
        # Note: This is risky if the phone shares the color, but the phone is Blue (#0055ff / #0033aa).
        # Background is likely black/grey/white checkerboard.
        
        new_data = []
        for y in range(height):
            for x in range(width):
                r, g, b, a = pixels[x, y]
                is_bg = False
                for bgr, bgg, bgb, bga in bg_colors:
                    # Tolerance check
                    if abs(r - bgr) < 5 and abs(g - bgg) < 5 and abs(b - bgb) < 5:
                        is_bg = True
                        break
                
                if is_bg:
                    new_data.append((0, 0, 0, 0))
                else:
                    new_data.append((r, g, b, a))
        
        img.putdata(new_data)
        
        # 2. Auto-crop
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
            print(f"Cropped to {bbox}")
            
        # 3. Resize to 40px height
        target_height = 40
        aspect = img.width / img.height
        new_width = int(target_height * aspect)
        
        img = img.resize((new_width, target_height), Image.Resampling.NEAREST) # Nearest neighbor for pixel art look
        print(f"Resized to {new_width}x{target_height}")
        
        img.save(path)
        print(f"Saved cleaned image to {path}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clean_and_resize()
