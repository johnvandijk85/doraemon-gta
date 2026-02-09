from PIL import Image, ImageDraw
import random

def create_noise(width, height, base_color, noise_amount=30):
    img = Image.new('RGBA', (width, height), base_color)
    pixels = img.load()
    
    r, g, b, a = base_color
    
    for y in range(height):
        for x in range(width):
            # Add random noise
            noise = random.randint(-noise_amount, noise_amount)
            nr = max(0, min(255, r + noise))
            ng = max(0, min(255, g + noise))
            nb = max(0, min(255, b + noise))
            pixels[x, y] = (nr, ng, nb, 255) # Force full Alpha
            
    return img

def create_better_cave_assets():
    # 1. Cave Ground - Rough Stone Texture
    # Base color: Dark Grey (60, 60, 70)
    img = create_noise(50, 50, (60, 60, 70, 255), noise_amount=20)
    draw = ImageDraw.Draw(img)
    
    # Add some "rocks" (lighter/darker blobs)
    for _ in range(5):
        rx = random.randint(0, 40)
        ry = random.randint(0, 40)
        size = random.randint(5, 15)
        color = (80 + random.randint(-10,10), 80 + random.randint(-10,10), 90 + random.randint(-10,10), 255)
        draw.ellipse((rx, ry, rx+size, ry+size/2), fill=color)
        
    # Add a "grass" or "moss" top layer? Cave implied maybe moss.
    # Let's add a green tint on top 5 pixels
    # draw.rectangle((0, 0, 50, 5), fill=(40, 60, 40, 100)) # Transparent overdraw? No, solid pixels needed?
    # No, keep it stone.
    
    img.save('assets/images/cave_ground.png')

    # 2. Cave Brick - Stone Bricks
    img = Image.new('RGBA', (50, 50), (40, 40, 45, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw Bricks
    colors = [(70, 70, 75), (60, 60, 65), (50, 50, 55)]
    
    # Row 1
    draw.rectangle((0, 0, 24, 24), fill=colors[0])
    draw.rectangle((26, 0, 49, 24), fill=colors[1])
    
    # Row 2 (offset)
    draw.rectangle((0, 26, 11, 49), fill=colors[1])
    draw.rectangle((13, 26, 36, 49), fill=colors[2])
    draw.rectangle((38, 26, 49, 49), fill=colors[0])
    
    # Apply some noise to existing image
    pixels = img.load()
    for y in range(50):
        for x in range(50):
            r, g, b, a = pixels[x, y]
            if a == 255: # Only noise on solid parts
                noise = random.randint(-10, 10)
                pixels[x,y] = (max(0, min(255, r+noise)), max(0, min(255, g+noise)), max(0, min(255, b+noise)), 255)

    img.save('assets/images/cave_brick.png')

    # 3. Cave Door - Stone Archway
    img = Image.new('RGBA', (60, 80), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Stones for arch
    stone_color = (90, 90, 95, 255)
    
    # Draw arch outline
    draw.ellipse((0, 0, 60, 60), fill=stone_color)
    draw.rectangle((0, 30, 60, 80), fill=stone_color)
    
    # Draw inner void (Dark)
    draw.ellipse((10, 10, 50, 60), fill=(20, 10, 10, 255))
    draw.rectangle((10, 35, 50, 80), fill=(20, 10, 10, 255))
    
    # Draw individual stones (lines)
    draw.line((30, 0, 30, 10), fill=(50, 50, 55, 255), width=2) # Keystone
    draw.arc((5, 5, 55, 55), 180, 360, fill=(50, 50, 55, 255), width=2) # Inner rim

    img.save('assets/images/cave_door_stone.png')

if __name__ == "__main__":
    create_better_cave_assets()
    print("Created improved, solid cave assets.")
