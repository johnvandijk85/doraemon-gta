from PIL import Image
import os

def remove_green(input_path, output_path):
    print(f"Processing {input_path} -> {output_path}...")
    try:
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()
        
        # Get the corner pixel to detect exact green color
        ref_color = img.getpixel((0, 0))
        print(f"  Reference BG color: {ref_color}")
        
        newData = []
        # Tolerance
        tol = 60
        
        r_ref, g_ref, b_ref = ref_color[:3]
        
        for item in datas:
            r, g, b = item[:3]
            if abs(r - r_ref) < tol and abs(g - g_ref) < tol and abs(b - b_ref) < tol:
               newData.append((0, 0, 0, 0))
            else:
               newData.append(item)
               
        img.putdata(newData)
        img.save(output_path, "PNG")
        print("  Done.")
    except Exception as e:
        print(f"  Error: {e}")

if __name__ == "__main__":
    if os.path.exists("car_3d_green_temp.png"):
        remove_green("car_3d_green_temp.png", 'assets/images/car_3d.png')
        
    if os.path.exists("player_3d_green_temp.png"):
        remove_green("player_3d_green_temp.png", 'assets/images/player_3d.png')
