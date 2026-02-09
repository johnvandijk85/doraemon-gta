from PIL import Image
import os

# Path to the artifact
img_path = '/Users/jdi/.gemini/antigravity/brain/171ccd02-8c61-4f31-a548-3cfcab6f398a/iso_park_props_1769979702818.png'

if not os.path.exists(img_path):
    print(f"Error: File not found at {img_path}")
    exit(1)

img = Image.open(img_path)
img = img.convert("RGBA")

datas = img.getdata()

# Sample top-left corner for background color (likely grey in checkerboard)
bg_color_1 = datas[0] # (r, g, b, a)
# Sample a pixel that might be the "white" part of checkerboard (e.g., 10px in)
bg_color_2 = (255, 255, 255, 255) # Standard white

print(f"Targeting colors: {bg_color_1} and {bg_color_2}")

newData = []
tolerance = 15 # Increased tolerance

for item in datas:
    r, g, b, a = item
    
    # Check for Dark Grey Background (approx 90-100 based on analysis)
    is_dark_grey = (85 <= r <= 110) and (85 <= g <= 110) and (85 <= b <= 110)
    
    # Check for White (Standard checkerboard) - Just in case
    is_white = (r > 240) and (g > 240) and (b > 240)

    if is_dark_grey or is_white:
        newData.append((255, 255, 255, 0)) # Transparent
    else:
        newData.append(item)

img.putdata(newData)
img.save(img_path, "PNG")
print("Successfully removed background and saved.")
