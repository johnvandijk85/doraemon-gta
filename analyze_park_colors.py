from PIL import Image
from collections import Counter
import os

img_path = '/Users/jdi/.gemini/antigravity/brain/171ccd02-8c61-4f31-a548-3cfcab6f398a/iso_park_props_1769979702818.png'

if not os.path.exists(img_path):
    print(f"Error: {img_path} not found")
    exit(1)

img = Image.open(img_path)
img = img.convert("RGBA")
datas = img.getdata()

# Count colors
colors = Counter(datas)

print("Top 20 Most Frequent Colors (R,G,B,A):")
for color, count in colors.most_common(20):
    print(f"{color}: {count}")
    
# Check corners specifically
w, h = img.size
corners = [
    (0,0), (w-1, 0), (0, h-1), (w-1, h-1),
    (10, 10), (w-10, h-10) # Inset
]
print("\nCorner/Inset Colors:")
for x,y in corners:
    try:
        c = img.getpixel((x,y))
        print(f"({x},{y}): {c}")
    except:
        pass
