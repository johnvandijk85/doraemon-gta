from PIL import Image

path = 'assets/images/ground_texture.png'
out_path = 'assets/images/deep_dirt.png'

print(f"Processing {path}...")
img = Image.open(path).convert("RGBA")
width, height = img.size

# Assume top 1/3 is grass, bottom 2/3 is dirt.
# Let's crop the bottom half to be safe and use it as deep dirt.
# Or better, crop a middle section of dirt and tile it?
# Let's just take the bottom 50%
crop_y = int(height * 0.4) 
# Actually, if we want it to match the top tile's bottom edge, we should precise match.
# But for now, let's just take the bottom square. 
# If height is large, we might need to resize.
# Game uses 50x50 tiles. 
# If image is e.g. 512x512, we want a 512x512 deep dirt that tiles?
# Or we just want a 50x50 dirt block?
# Let's try to just take the bottom part.

dirt_img = img.crop((0, crop_y, width, height))
dirt_img.save(out_path)
print(f"Saved {out_path}")
