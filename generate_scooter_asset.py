import math
from PIL import Image, ImageDraw

def create_scooter_asset():
    # 64x64 might be better for pixel art look without scaling artifacts? 
    # But game scales down based on targetSize/naturalWidth.
    # Let's stick to 128x128 but draw "chunky" pixels.
    width = 128
    height = 128
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Colors
    scooter_red = (230, 40, 40, 255)
    scooter_dark_red = (180, 20, 20, 255)
    tire_grey = (40, 40, 40, 255)
    rim_grey = (150, 150, 150, 255)
    box_white = (240, 240, 240, 255)
    box_shadow = (200, 200, 200, 255)
    seat_black = (20, 20, 20, 255)
    handlebar_silver = (200, 200, 200, 255)
    light_yellow = (255, 255, 100, 255)

    # Drawing a "Side View" scooter that is slightly angled?
    # Simple Side View facing RIGHT.
    
    # 1. Wheels (Chunky Circles)
    # Rear Wheel
    draw.rectangle([20, 80, 50, 110], fill=tire_grey) # Square-ish tire
    draw.rectangle([28, 88, 42, 102], fill=rim_grey)  # Rim
    
    # Front Wheel
    draw.rectangle([85, 80, 115, 110], fill=tire_grey)
    draw.rectangle([93, 88, 107, 102], fill=rim_grey)

    # 2. Floorboard / Chassis
    draw.rectangle([40, 95, 90, 105], fill=scooter_dark_red) # Bottom frame
    draw.rectangle([40, 85, 90, 95], fill=scooter_red)       # Floorboard

    # 3. Rear Body (Engine/Seat Base)
    draw.rectangle([25, 65, 55, 95], fill=scooter_red) 
    
    # 4. Front Body (Shield)
    draw.rectangle([85, 50, 95, 95], fill=scooter_red)
    draw.rectangle([85, 50, 95, 60], fill=scooter_dark_red) # Detail
    
    # 5. Seat
    draw.rectangle([30, 60, 55, 65], fill=seat_black)

    # 6. Handlebars
    draw.rectangle([82, 45, 98, 50], fill=scooter_red) # Head
    draw.rectangle([98, 50, 105, 58], fill=light_yellow) # Headlight
    draw.line([88, 48, 75, 40], fill=handlebar_silver, width=4) # Left bar
    draw.line([88, 48, 105, 45], fill=handlebar_silver, width=4) # Right bar looks weird in 2D, just do top bar
    draw.rectangle([75, 38, 105, 42], fill=handlebar_silver) # Horizontal bar

    # 7. Delivery Box (The Defining Feature)
    # Big white box on the back
    box_x, box_y = 15, 45
    box_w, box_h = 30, 30
    # Shadow side
    draw.rectangle([box_x, box_y, box_x + 5, box_y + box_h], fill=box_shadow)
    # Main side
    draw.rectangle([box_x + 5, box_y, box_x + box_w, box_y + box_h], fill=box_white)
    # Outline
    draw.rectangle([box_x + 5, box_y, box_x + box_w, box_y + box_h], outline=box_shadow, width=2)
    
    # Pizza Logo (Red Circle + Green Leaf)
    cx = box_x + 5 + box_w//2
    cy = box_y + box_h//2
    draw.ellipse([cx-8, cy-8, cx+8, cy+8], fill="red")
    draw.rectangle([cx-2, cy-8, cx+2, cy-2], fill="green")

    # Save
    output_path = 'assets/images/iso_scooter.png'
    img.save(output_path)
    print(f"Chunky Scooter asset saved to {output_path}")

if __name__ == "__main__":
    create_scooter_asset()
