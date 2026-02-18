from PIL import Image

def analyze_image(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGBA")
        width, height = img.size
        print(f"Dimensions: {width}x{height}")
        
        # Check corners to guess background color
        corners = [
            (0, 0),
            (width-1, 0),
            (0, height-1),
            (width-1, height-1)
        ]
        
        print("Corner colors:")
        for x, y in corners:
            pixel = img.getpixel((x, y))
            print(f"({x}, {y}): {pixel}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_image("assets/images/iso_scooter.png")
