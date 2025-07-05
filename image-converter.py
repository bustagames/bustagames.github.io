from PIL import Image
import os
import sys

def convert_to_webp(input_path):
    try:
        with Image.open(input_path) as img:
            output_path = os.path.splitext(input_path)[0] + ".webp"
            img.save(output_path, "WEBP")
            print(f"Converted to: {output_path}")
    except Exception as e:
        print(f"Error converting image: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python convert_to_webp.py <image_path>")
    else:
        convert_to_webp(sys.argv[1])