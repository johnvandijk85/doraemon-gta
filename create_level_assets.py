from PIL import Image, ImageDraw

def create_sky_assets():
    # 1. Sky Background (50x50 tileable or just a large gradient)
    # Let's make a 800x600 gradient for simplicity, or a seamless 50x50 blue tile.
    # Platformer uses 100% width/height. Let's make a seamless 50x50 blue tile.
    img = Image.new('RGBA', (50, 50), (135, 206, 235, 255)) # Sky Blue
    # Add some white fluff for clouds
    draw = ImageDraw.Draw(img)
    draw.ellipse((10, 10, 40, 40), fill=(255, 255, 255, 100))
    img.save('assets/images/sky_bg.png')

    # 2. Sky Ground (Cloud) - 50x50
    img = Image.new('RGBA', (50, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Fluffy white circles
    draw.ellipse((0, 10, 30, 40), fill=(255, 255, 255, 255))
    draw.ellipse((20, 10, 50, 40), fill=(255, 255, 255, 255))
    draw.ellipse((10, 0, 40, 30), fill=(255, 255, 255, 255))
    draw.rectangle((0, 25, 50, 50), fill=(255, 255, 255, 255)) # Solid bottom for seamlessness
    img.save('assets/images/sky_ground.png')

    # 3. Sky Brick (Compressed Cloud/Rainbow?) - 50x50
    img = Image.new('RGBA', (50, 50), (200, 200, 255, 255)) # Darker cloud
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 49, 49), outline=(100, 100, 200, 255), width=2)
    # Rainbow stripe
    draw.rectangle((5, 20, 45, 25), fill=(255, 0, 0, 255))
    draw.rectangle((5, 25, 45, 30), fill=(255, 255, 0, 255))
    draw.rectangle((5, 30, 45, 35), fill=(0, 0, 255, 255))
    img.save('assets/images/sky_brick.png')

    # 4. Sky Enemy (Bird) - 50x50
    img = Image.new('RGBA', (50, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Yellow Bird body
    draw.ellipse((10, 15, 40, 45), fill=(255, 215, 0, 255))
    # Wing
    draw.ellipse((25, 25, 45, 35), fill=(255, 165, 0, 255))
    # Eye
    draw.ellipse((15, 20, 20, 25), fill=(0, 0, 0, 255))
    # Beak
    draw.polygon([(10, 25), (0, 30), (10, 35)], fill=(255, 100, 0, 255))
    img.save('assets/images/sky_enemy.png')
    
    # 5. Sky Door (Cloud Gate) - 60x80
    img = Image.new('RGBA', (60, 80), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Arch
    draw.ellipse((0, 0, 60, 60), fill=(255, 255, 255, 255))
    draw.rectangle((0, 30, 60, 80), fill=(255, 255, 255, 255))
    # Inner opening (Dark blue)
    draw.ellipse((10, 10, 50, 60), fill=(0, 191, 255, 255))
    draw.rectangle((10, 35, 50, 80), fill=(0, 191, 255, 255))
    img.save('assets/images/sky_door.png')

def create_castle_assets():
    # 1. Castle BG - Dark Grey Pattern
    img = Image.new('RGBA', (50, 50), (50, 50, 60, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 49, 49), outline=(30, 30, 40, 255))
    img.save('assets/images/castle_bg.png')

    # 2. Castle Ground - Stone Blocks
    img = Image.new('RGBA', (50, 50), (100, 100, 100, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 49, 49), outline=(50, 50, 50, 255), width=3)
    # Inner bevel
    draw.line((2, 2, 47, 2), fill=(150, 150, 150, 255))
    draw.line((2, 2, 2, 47), fill=(150, 150, 150, 255))
    img.save('assets/images/castle_ground.png')

    # 3. Castle Brick - Cracked Stone
    img = Image.new('RGBA', (50, 50), (80, 80, 80, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 49, 49), outline=(30, 30, 30, 255), width=2)
    # Crack
    draw.line((10, 10, 25, 25), fill=(0, 0, 0, 255), width=2)
    draw.line((25, 25, 20, 40), fill=(0, 0, 0, 255), width=2)
    img.save('assets/images/castle_brick.png')

    # 4. Castle Enemy (Ghost)
    img = Image.new('RGBA', (50, 50), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    # Ghost body shape
    draw.ellipse((10, 5, 40, 45), fill=(255, 255, 255, 200))
    draw.rectangle((10, 25, 40, 45), fill=(255, 255, 255, 200))
    # Eyes
    draw.ellipse((15, 15, 20, 20), fill=(0, 0, 0, 255))
    draw.ellipse((30, 15, 35, 20), fill=(0, 0, 0, 255))
    img.save('assets/images/castle_enemy.png')
    
    # 5. Castle Door (Iron Gate)
    img = Image.new('RGBA', (60, 80), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 0, 60, 80), fill=(60, 60, 60, 255), outline=(30,30,30,255), width=3)
    # Bars
    for x in range(10, 60, 10):
        draw.line((x, 5, x, 75), fill=(30, 30, 30, 255), width=2)
    img.save('assets/images/castle_door.png')

def create_cave_assets():
    # 1. Cave Ground - Grey Stone (Solid)
    img = Image.new('RGBA', (50, 50), (80, 80, 85, 255))
    draw = ImageDraw.Draw(img)
    # irregular stone pattern
    draw.rectangle((0,0,49,49), outline=(50,50,55,255), width=2)
    draw.line((10,10, 40,40), fill=(60,60,65,255), width=2)
    draw.line((40,10, 10,40), fill=(60,60,65,255), width=2)
    img.save('assets/images/cave_ground.png')

    # 2. Cave Brick - Darker Bricks (Solid)
    img = Image.new('RGBA', (50, 50), (60, 60, 65, 255))
    draw = ImageDraw.Draw(img)
    draw.rectangle((0,0,49,24), outline=(40,40,45,255))
    draw.rectangle((0,25,49,49), outline=(40,40,45,255))
    draw.line((25,0,25,24), fill=(40,40,45,255))
    draw.line((12,25,12,49), fill=(40,40,45,255))
    draw.line((37,25,37,49), fill=(40,40,45,255))
    img.save('assets/images/cave_brick.png')
    
    # 3. Cave Door (Stone Arch)
    img = Image.new('RGBA', (60, 80), (0, 0, 0, 0)) # Transparent BG
    draw = ImageDraw.Draw(img)
    # Arch shape
    draw.ellipse((0, 0, 60, 60), fill=(100, 100, 105, 255))
    draw.rectangle((0, 30, 60, 80), fill=(100, 100, 105, 255))
    # Inner black void
    draw.ellipse((10, 10, 50, 60), fill=(20, 10, 10, 255))
    draw.rectangle((10, 35, 50, 80), fill=(20, 10, 10, 255))
    img.save('assets/images/cave_door_stone.png')

if __name__ == "__main__":
    create_sky_assets()
    create_castle_assets()
    create_cave_assets()
    print("Created Level 3, 4, and Cave assets.")
