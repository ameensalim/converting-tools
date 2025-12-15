import os
from pillow_heif import register_heif_opener
from PIL import Image

# Enable HEIC support
register_heif_opener()

input_folder = "./images"      # HEIC folder
output_folder = "./output"     # JPG folder

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".heic"):
        heic_path = os.path.join(input_folder, filename)
        jpg_name = filename.rsplit(".", 1)[0] + ".jpg"
        jpg_path = os.path.join(output_folder, jpg_name)

        try:
            img = Image.open(heic_path)

            # Save at maximum quality
            img.save(
                jpg_path,
                "JPEG",
                quality=100,          # highest quality
                subsampling=0,        # keep 4:4:4 color (no chroma subsampling)
                optimize=True
            )

            print(f"Converted (max quality): {filename} → {jpg_name}")

        except Exception as e:
            print(f"Error converting {filename}: {e}")
