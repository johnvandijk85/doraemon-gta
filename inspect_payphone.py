from PIL import Image

def inspect():
    try:
        img = Image.open('assets/images/pay_phone.png').convert('RGBA')
        pixels = img.load()
        width, height = img.size
        print(f"Size: {width}x{height}")
        
        # Check corners
        corners = [
            (0, 0),
            (width-1, 0),
            (0, height-1),
            (width-1, height-1),
            (10, 10) # offset
        ]
        
        print("Pixel Samples:")
        for x, y in corners:
            if x < width and y < height:
                print(f"({x}, {y}): {pixels[x, y]}")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect()
