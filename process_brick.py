from PIL import Image

path = 'assets/images/brick_texture.png'
print(f"Resizing {path}...")
img = Image.open(path)
# Resize to 50x50 using Lanczos for quality
# Since it's seamless, this small tile will also be seamless.
img_small = img.resize((50, 50), Image.Resampling.LANCZOS)
img_small.save(path)
print("Saved resized brick texture.")
