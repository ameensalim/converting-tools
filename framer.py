from PIL import Image
import os

IMAGES_DIR = "output"
FRAME_PATH = "frame.png"
OUTPUT_DIR = "output2"

def main():
    # create output folder if not exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # load the frame
    frame = Image.open(FRAME_PATH).convert("RGBA")
    frame_w, frame_h = frame.size

    for filename in os.listdir(IMAGES_DIR):
        if not filename.lower().endswith(("jpg", "jpeg", "png", "heic", "webp")):
            continue

        img_path = os.path.join(IMAGES_DIR, filename)

        # open the source image
        img = Image.open(img_path).convert("RGBA")

        # resize the image to COVER the frame (fill entire frame, crop if needed)
        img_ratio = img.width / img.height
        frame_ratio = frame_w / frame_h

        if img_ratio > frame_ratio:
            # image is wider — match height and crop width
            new_h = frame_h
            new_w = int(frame_h * img_ratio)
        else:
            # image is taller — match width and crop height
            new_w = frame_w
            new_h = int(frame_w / img_ratio)

        img = img.resize((new_w, new_h), Image.LANCZOS)

        # create blank background same size as frame
        final_img = Image.new("RGBA", (frame_w, frame_h), (0, 0, 0, 0))

        # center the resized image (and crop overflow)
        x = (frame_w - new_w) // 2
        y = (frame_h - new_h) // 2
        final_img.paste(img, (x, y))

        # paste the frame on top
        final_img = Image.alpha_composite(final_img, frame)

        # save output
        output_path = os.path.join(OUTPUT_DIR, filename)
        
        # Convert to RGB if saving as JPEG (JPEG doesn't support transparency)
        if filename.lower().endswith(("jpg", "jpeg")):
            # Create white background and paste the RGBA image on it
            rgb_img = Image.new("RGB", final_img.size, (255, 255, 255))
            rgb_img.paste(final_img, mask=final_img.split()[3])  # Use alpha channel as mask
            rgb_img.save(output_path, quality=95)
        else:
            final_img.save(output_path)

        print(f"Saved: {output_path}")

    print("Done! All images processed.")


if __name__ == "__main__":
    main()
