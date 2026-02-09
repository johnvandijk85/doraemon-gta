from PIL import Image
import glob
import os

def check_tiles():
    files = sorted(glob.glob('assets/images/recovered_tile_*.png'))
    for f in files:
        img = Image.open(f).convert("RGBA")
        # Get average color
        w, h = img.size
        # Sample center
        c = img.getpixel((w//2, h//2))
        print(f"{f}: Center={c}, Size={os.path.getsize(f)}")

if __name__ == "__main__":
    check_tiles()
