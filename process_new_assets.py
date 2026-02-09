import os
from PIL import Image

def remove_white_bg(image_path, output_path, tolerance=30):
    print(f"Processing {image_path} -> {output_path}")
    try:
        img = Image.open(image_path).convert("RGBA")
        datas = img.getdata()

        newData = []
        for item in datas:
            # Check if pixel is white-ish
            # item is (r, g, b, a)
            if item[0] > 255 - tolerance and item[1] > 255 - tolerance and item[2] > 255 - tolerance:
                newData.append((255, 255, 255, 0)) # Transparent
            else:
                newData.append(item)

        img.putdata(newData)
        img.save(output_path, "PNG")
        print("Success.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    base_artifact_path = "/Users/jdi/.gemini/antigravity/brain/57293d76-3461-4b6d-a0e5-191a7633435e/"
    assets_path = "/Users/jdi/Documents/GitHub/doraemon-presentation/assets/images/"

    # Source Files (Generated)
    src_sakura = base_artifact_path + "iso_prop_sakura_1770667593259.png"
    src_vending = base_artifact_path + "iso_prop_vending_1770667606545.png"

    # Destination Files
    dst_sakura = assets_path + "iso_prop_sakura.png"
    dst_vending = assets_path + "iso_prop_vending.png"

    remove_white_bg(src_sakura, dst_sakura)
    remove_white_bg(src_vending, dst_vending)

if __name__ == "__main__":
    main()
