from PIL import Image

def sample_pixels(path):
    print(f"Scanning {path} for artifacts...")
    img = Image.open(path).convert("RGBA")
    pixels = img.load()
    w, h = img.size
    
    artifacts = []
    
    # Heart is roughly Red: R > G and R > B. 
    # Let's find things that are NOT red and NOT transparent.
    
    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if a == 0: continue
            
            # Simple "Red-ish" check:
            is_red = (r > g + 20) and (r > b + 20)
            
            if not is_red:
                artifacts.append(((x,y), (r,g,b,a)))
                if len(artifacts) > 10: break
    
    if artifacts:
        print(f"Found {len(artifacts)}+ non-red artifacts:")
        for pos, col in artifacts:
            print(f"  Pos: {pos}, Color: {col}")
    else:
        print("No significant non-red artifacts found. The background seems clean!")

if __name__ == "__main__":
    sample_pixels('assets/images/pickup_health.png')
