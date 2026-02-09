from PIL import Image, ImageEnhance
import os

def lighten_image(path, factor=1.4):
    if not os.path.exists(path):
        print(f"Skipping {path}: Not found")
        return

    print(f"Processing {path} with factor {factor}...")
    img = Image.open(path).convert("RGBA")
    
    # Enhancing brightness
    enhancer = ImageEnhance.Brightness(img)
    img_light = enhancer.enhance(factor)
    
    img_light.save(path)
    print(f"  Saved {path}")

if __name__ == "__main__":
    # Lighten both ground and brick for Level 4
    # lighten_image('assets/images/castle_ground.png', 1.4)
    lighten_image('assets/images/castle_brick.png', 1.2)
