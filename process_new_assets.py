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
    src_mailbox = base_artifact_path + "iso_prop_mailbox_1770667974317.png"
    src_pipes = base_artifact_path + "iso_prop_pipes_1770667986414.png"
    # New Assets
    src_suneo = base_artifact_path + "iso_suneo_house_1770668467370.png"
    src_gian = base_artifact_path + "iso_gian_house_1770668557441.png"
    src_shizuka = base_artifact_path + "iso_shizuka_house_1770668515507.png"
    src_fence = base_artifact_path + "iso_prop_fence_1770668535365.png"
    src_torii = base_artifact_path + "iso_prop_torii_1770668577326.png"

    # Destination Files
    dst_sakura = assets_path + "iso_prop_sakura.png"
    dst_vending = assets_path + "iso_prop_vending.png"
    dst_mailbox = assets_path + "iso_prop_mailbox.png"
    dst_pipes = assets_path + "iso_prop_pipes.png"
    dst_suneo = assets_path + "iso_suneo_house.png"
    dst_gian = assets_path + "iso_gian_house.png"
    dst_shizuka = assets_path + "iso_shizuka_house.png"
    dst_fence = assets_path + "iso_prop_fence.png"
    dst_torii = assets_path + "iso_prop_torii.png"

    remove_white_bg(src_sakura, dst_sakura)
    remove_white_bg(src_vending, dst_vending)
    remove_white_bg(src_mailbox, dst_mailbox)
    remove_white_bg(src_pipes, dst_pipes)
    remove_white_bg(src_suneo, dst_suneo)
    remove_white_bg(src_gian, dst_gian)
    remove_white_bg(src_shizuka, dst_shizuka)
    remove_white_bg(src_fence, dst_fence)
    remove_white_bg(src_torii, dst_torii)


if __name__ == "__main__":
    main()
