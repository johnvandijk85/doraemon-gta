from PIL import Image
import collections

def diagnose(path):
    print(f"Diagnosing {path}...")
    try:
        img = Image.open(path).convert("RGBA")
    except Exception as e:
        print(e)
        return

    pixels = img.load()
    w, h = img.size
    
    # Sample top-left 50x50 block (should be background)
    colors = collections.Counter()
    
    for y in range(50):
        for x in range(50):
            if x < w and y < h:
                colors[pixels[x,y]] += 1
                
    print("Most common corner colors:")
    for c, count in colors.most_common(10):
        print(f"  {c}: {count}")

if __name__ == "__main__":
    diagnose('assets/images/car_blue.png')
    diagnose('assets/images/car_green.png')
