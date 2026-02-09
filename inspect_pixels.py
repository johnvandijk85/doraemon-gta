from PIL import Image

start_path = 'assets/images/doraemon_sheet.png'
print(f"Inspecting {start_path}...")
img = Image.open(start_path).convert("RGBA")
pixels = img.load()

for y in range(10):
    row = []
    for x in range(10):
        row.append(str(pixels[x, y]))
    print(f"Row {y}: " + ", ".join(row))
