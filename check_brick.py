from PIL import Image

path = 'assets/images/brick_texture.png'
print(f"Checking {path}...")
img = Image.open(path)
print(f"Size: {img.size}")
