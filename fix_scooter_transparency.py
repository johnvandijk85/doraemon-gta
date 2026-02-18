from PIL import Image

def remove_background(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGBA")
        datas = img.getdata()

        new_data = []
        # Target Grey from analysis: (83, 85, 82)
        target_r, target_g, target_b = 83, 85, 82
        tolerance = 30 

        for item in datas:
            # Check for Black (previous issue)
            is_black = item[0] < 40 and item[1] < 40 and item[2] < 40
            
            # Check for the Grey background
            is_grey = (abs(item[0] - target_r) < tolerance and 
                       abs(item[1] - target_g) < tolerance and 
                       abs(item[2] - target_b) < tolerance)

            # Check for White (sometimes used as bg)
            is_white = item[0] > 240 and item[1] > 240 and item[2] > 240

            # If it matches background criteria, make it transparent
            if is_black or is_grey or is_white:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(image_path, "PNG")
        print(f"Successfully processed {image_path}")
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    remove_background("assets/images/iso_scooter.png")
