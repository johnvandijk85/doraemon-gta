from PIL import Image

path = 'assets/images/doraemon_sheet.png'
print(f"Analyzing {path}...")
img = Image.open(path).convert("RGBA")
width, height = img.size
pixels = img.load()

colors = {}

def add_color(p):
    if p[3] == 0: return # ignore transparent
    if p not in colors: colors[p] = 0
    colors[p] += 1

# Scan top 50 rows
for y in range(50):
    for x in range(width):
        add_color(pixels[x, y])

# Scan left 50 cols
for x in range(50):
    for y in range(height):
        add_color(pixels[x, y])

print("Unique border colors (count > 100):")
sorted_colors = sorted(colors.items(), key=lambda x: x[1], reverse=True)
for c, count in sorted_colors:
    if count > 100:
        print(f"Color: {c}, Count: {count}")
