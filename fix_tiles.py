from PIL import Image

path = 'assets/images/ground_texture.png' # This is the original 1024x1024 one?
# Wait, I overwrote it or moved it. Yes, it's 1024x1024.

img = Image.open(path).convert("RGBA")
# 1. Resize down to reasonable scale. 
# 1024 is too big. Let's make it 256 wide.
scale_w = 256
scale_h = int(img.height * (scale_w / img.width))
img = img.resize((scale_w, scale_h), Image.Resampling.LANCZOS)

width, height = img.size
pixels = img.load()

# 2. Find Grass Top (first non-white row)
start_y = 0
found = False
for y in range(height):
    # Check middle pixel or scan row
    r,g,b,a = pixels[width//2, y]
    # Check if white-ish
    if r < 240 or g < 240 or b < 240:
        start_y = y
        found = True
        break

if not found:
    print("Could not find grass line, using 0")
    start_y = 0
else:
    print(f"Found grass at y={start_y}")

# 3. Crop Surface Tile (50x50)
# We want clean 50x50.
# Let's take a 50x50 chunk.
# To make it 'seem' seamless, we can't just take one random chunk if edges don't match.
# But resizing the whole seamless image to 50w would squash it.
# Let's just take a crop and hope for the best for now.
# Better: Center the crop horizontally to avoid edges.
crop_x = (width - 50) // 2

surface = img.crop((crop_x, start_y, crop_x + 50, start_y + 50))
surface.save('assets/images/ground_texture.png')

# 4. Crop Deep Dirt (50x50)
# Take from below the surface tile
deep_y = start_y + 50
if deep_y + 50 > height:
    deep_y = height - 50
    
deep = img.crop((crop_x, deep_y, crop_x + 50, deep_y + 50))
deep.save('assets/images/deep_dirt.png')

print("Saved fixed tiles.")
