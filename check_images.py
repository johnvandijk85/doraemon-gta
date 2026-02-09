from PIL import Image

files = ['assets/images/ground_texture.png', 'assets/images/deep_dirt.png']

for f in files:
    try:
        img = Image.open(f)
        print(f"File: {f}")
        print(f"  Size: {img.size}")
        print(f"  Mode: {img.mode}")
        # Check corners to see if they are white/transparent
        pixels = img.convert("RGBA").load()
        w, h = img.size
        print(f"  TL: {pixels[0,0]}")
        print(f"  TR: {pixels[w-1,0]}")
        print(f"  BL: {pixels[0,h-1]}")
        print(f"  BR: {pixels[w-1,h-1]}")
    except Exception as e:
        print(f"Error reading {f}: {e}")
