from PIL import Image
import os

files = [
    '/Users/jdi/.gemini/antigravity/brain/647e76f3-f8c9-4e7e-a0a0-be75831302c9/iso_nobita_house_1770563783778.png',
    '/Users/jdi/.gemini/antigravity/brain/647e76f3-f8c9-4e7e-a0a0-be75831302c9/iso_school_1770563806147.png',
    '/Users/jdi/.gemini/antigravity/brain/647e76f3-f8c9-4e7e-a0a0-be75831302c9/iso_shop_1770563829789.png',
    '/Users/jdi/.gemini/antigravity/brain/647e76f3-f8c9-4e7e-a0a0-be75831302c9/iso_future_house_1770563875277.png'
]

for f in files:
    try:
        img = Image.open(f).convert("RGBA")
        extrema = img.getextrema()
        alpha_extrema = extrema[3]
        if alpha_extrema[0] == 255:
            print(f"FAIL: {os.path.basename(f)} is fully opaque.")
        else:
             print(f"PASS: {os.path.basename(f)} has transparency.")
    except Exception as e:
        print(f"ERROR: {e}")
