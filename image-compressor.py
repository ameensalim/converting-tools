import os
from PIL import Image

INPUT_DIR = "compress_input"
OUTPUT_DIR = "compress_output"
MAX_SIZE_KB = 200
MAX_SIZE_BYTES = MAX_SIZE_KB * 1024

os.makedirs(OUTPUT_DIR, exist_ok=True)

def compress_image(input_path, output_path):
    img = Image.open(input_path)

    # Convert PNG with transparency to RGB
    if img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    quality = 40
    step = 5

    while quality > 5:
        img.save(
            output_path,
            format="JPEG",
            quality=quality,
            optimize=True,
            progressive=True
        )

        if os.path.getsize(output_path) <= MAX_SIZE_BYTES:
            return

        quality -= step

    # If still large, resize more aggressively
    width, height = img.size
    scale = 0.7
    while os.path.getsize(output_path) > MAX_SIZE_BYTES and scale > 0.3:
        img = Image.open(input_path)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        
        img = img.resize((int(width * scale), int(height * scale)), Image.LANCZOS)
        img.save(
            output_path,
            format="JPEG",
            quality=35,
            optimize=True,
            progressive=True
        )
        scale -= 0.1

def process_images():
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
            input_path = os.path.join(INPUT_DIR, filename)
            output_path = os.path.join(
                OUTPUT_DIR,
                os.path.splitext(filename)[0] + ".jpg"
            )

            compress_image(input_path, output_path)
            size_kb = os.path.getsize(output_path) / 1024
            print(f"{filename} → {size_kb:.1f} KB")

if __name__ == "__main__":
    process_images()
