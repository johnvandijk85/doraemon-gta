from PIL import Image

def remove_black_background(image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGBA")
        datas = img.getdata()

        new_data = []
        for item in datas:
            # Check if the pixel is black (or very close to it)
            # You might need to adjust the threshold
            if item[0] < 10 and item[1] < 10 and item[2] < 10:
                new_data.append((255, 255, 255, 0)) # Make it transparent
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(image_path, "PNG")
        print(f"Successfully removed black background from {image_path}")
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    remove_black_background("assets/images/iso_scooter.png")
