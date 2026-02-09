from PIL import Image

path = 'assets/images/ground_texture.png'
print(f"Cleaning {path}...")
img = Image.open(path).convert("RGBA")
data = img.getdata()

new_data = []
for item in data:
    # Check for near-white pixels (sky background in the generated asset)
    # The user says "white coloring", so let's be aggressive on high brightness.
    # Looking at previous logs, TL pixel was (252, 255, 255).
    if item[0] > 200 and item[1] > 200 and item[2] > 200:
        new_data.append((0, 0, 0, 0)) # Make transparent
    else:
        new_data.append(item)

img.putdata(new_data)
img.save(path)
print("Saved cleaned image.")
