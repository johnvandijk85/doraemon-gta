from PIL import Image
import os

def clean_payphone():
    path = 'assets/images/pay_phone.png'
    try:
        img = Image.open(path)
        img = img.convert("RGBA")
        
        # 1. Auto-crop transparency
        bbox = img.getbbox()
        if bbox:
            img = img.crop(bbox)
            print(f"Cropped to {bbox}")
        
        # 2. Resize
        # Target height: ~80px (enough for a tall booth on a 64px tile)
        target_height = 80
        aspect = img.width / img.height
        new_width = int(target_height * aspect)
        
        img = img.resize((new_width, target_height), Image.Resampling.LANCZOS)
        print(f"Resized to {new_width}x{target_height}")

        img.save(path)
        print(f"Saved cleaned image to {path}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    clean_payphone()
