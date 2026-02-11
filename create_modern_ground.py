from PIL import Image, ImageDraw

def create_modern_ground():
    # 64x64 tile to match TILE_SIZE
    width, height = 64, 64
    img = Image.new('RGBA', (width, height), (50, 50, 55, 255)) # Dark grey pavement
    draw = ImageDraw.Draw(img)

    # 1. Subtle Paver Pattern (Square grid)
    # 16x16 blocks
    for y in range(0, height, 16):
        for x in range(0, width, 16):
            draw.rectangle((x, y, x+15, y+15), outline=(60, 60, 65, 255))

    # 2. Tactile Paving (Tenji Block) - Yellow Strip
    # A strip of 16px wide tactile paving on the left side
    strip_x = 8
    draw.rectangle((strip_x, 0, strip_x + 12, height), fill=(220, 200, 50, 255))
    
    # Tactile bumps/lines
    for y in range(0, height, 8):
        draw.rectangle((strip_x + 2, y + 2, strip_x + 10, y + 6), fill=(200, 180, 40, 255))

    # 3. Manhole Cover (Random detail) - Just one in the corner
    # draw.ellipse((40, 40, 56, 56), fill=(70, 70, 75, 255), outline=(40, 40, 45, 255))

    img.save('assets/images/iso_ground_modern.png')
    print("Created iso_ground_modern.png")

if __name__ == "__main__":
    create_modern_ground()
