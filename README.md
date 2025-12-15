# Image Processing Toolkit

A collection of three powerful Python tools for image conversion, compression, and framing. Perfect for batch processing images with different requirements.

---

## 🛠️ Tools Overview

### 1. **Image Compressor** (`image-compressor.py`)

Compress images to a maximum file size while maintaining reasonable quality.

**Features:**

- Reduces images to 200KB or less
- Automatically adjusts JPEG quality and dimensions
- Converts PNG with transparency to RGB
- Optimizes and creates progressive JPEGs
- Processes all images in a folder

**Use Cases:**

- Optimize images for web
- Reduce storage space
- Prepare images for email/sharing

---

### 2. **HEIC to JPG Converter** (`convert.py`)

Convert HEIC/HEIF format images (iPhone photos) to high-quality JPG.

**Features:**

- Converts HEIC files to JPG at maximum quality
- Preserves full color information (4:4:4 subsampling)
- Batch processes entire folders
- Maintains original quality settings
- Error handling for failed conversions

**Use Cases:**

- Convert iPhone photos to universal JPG format
- Prepare photos for non-Apple devices
- Archive photos in a widely-compatible format

---

### 3. **Image Framer** (`framer.py`)

Add decorative frames to your images with intelligent cropping and centering.

**Features:**

- Applies PNG frame overlays to images
- Intelligent image scaling to fill entire frame
- Automatic center cropping if needed
- Supports multiple image formats (JPG, PNG, HEIC, WebP)
- Maintains transparency in frames

**Use Cases:**

- Add borders/frames to photos
- Create consistent styled image collections
- Prepare images for social media posts

---

## 📋 Requirements

Before running any tool, install the required Python libraries:

```bash
pip install Pillow pillow-heif
```

**Dependencies:**

- `Pillow` - Image processing library
- `pillow-heif` - Support for HEIC/HEIF format (needed for converter and framer)

---

## 📁 Folder Structure

```
convert/
├── convert.py              # HEIC to JPG converter
├── framer.py              # Image framer tool
├── image-compressor.py    # Image compressor tool
├── images/                # Input folder for convert.py
├── output/                # Output folder for convert.py & framer.py input
├── output2/               # Output folder for framer.py
├── compress_input/        # Input folder for image-compressor.py
├── compress_output/       # Output folder for image-compressor.py
├── frame.png              # Frame overlay for framer.py
└── README.md              # This file
```

---

## 🚀 How to Use Each Tool

### **Tool 1: Image Compressor**

**Setup:**

1. Create a `compress_input/` folder (already exists)
2. Add your images to the `compress_input/` folder
3. Run the script:

```bash
python image-compressor.py
```

**Output:**

- Compressed images saved to `compress_output/`
- All images reduced to ~200KB or less
- Format: JPEG with optimized quality

**Example:**

```bash
# Input: compress_input/photo1.png (5MB)
# Output: compress_output/photo1.jpg (195KB)
python image-compressor.py
```

---

### **Tool 2: HEIC to JPG Converter**

**Setup:**

1. Create an `images/` folder
2. Add your HEIC files to the `images/` folder
3. Run the script:

```bash
python convert.py
```

**Output:**

- JPG files saved to `output/` folder
- Maximum quality preserved (100 quality, no subsampling)
- Original filename maintained

**Example:**

```bash
# Input: images/photo1.heic, images/photo2.heic
# Output: output/photo1.jpg, output/photo2.jpg
python convert.py
```

---

### **Tool 3: Image Framer**

**Setup:**

1. Place your **frame image** as `frame.png` in the project root
   - Frame should be PNG with transparency
   - Example: A decorative border or overlay
2. Place your **source images** in the `output/` folder
3. Run the script:

```bash
python framer.py
```

**Output:**

- Framed images saved to `output2/` folder
- Images automatically centered and cropped to fit frame
- Transparency preserved from frame

**Frame Requirements:**

- File name: `frame.png`
- Format: PNG with RGBA (transparency support)
- Size: Any dimension (images will scale to fit)

**Example:**

```bash
# Input:
#   - frame.png (decorative border)
#   - output/photo1.jpg, output/photo2.png
# Output: output2/photo1.png, output2/photo2.png
python framer.py
```

---

## 📊 Workflow Example

Process a batch of iPhone photos with frames:

```bash
# Step 1: Convert HEIC to JPG
python convert.py
# Files now in: output/

# Step 2: Compress the JPGs (optional)
# Copy files from output/ to compress_input/
cp output/* compress_input/
python image-compressor.py
# Files now in: compress_output/

# Step 3: Add frames
# Copy files from compress_output/ to output/
cp compress_output/* output/
python framer.py
# Final framed images in: output2/
```

---

## ⚙️ Configuration

### **Image Compressor Settings**

Edit `image-compressor.py` to change:

- `MAX_SIZE_KB = 200` - Target file size
- `quality = 40` - Initial JPEG quality
- `step = 5` - Quality reduction step size

### **Converter Settings**

Edit `convert.py` to change:

- `input_folder = "./images"` - Input directory
- `output_folder = "./output"` - Output directory
- `quality=100` - JPEG quality level

### **Framer Settings**

Edit `framer.py` to change:

- `IMAGES_DIR = "output"` - Input images directory
- `FRAME_PATH = "frame.png"` - Frame file location
- `OUTPUT_DIR = "output2"` - Output directory

---

## 🔍 Troubleshooting

**"ModuleNotFoundError: No module named 'PIL'"**

```bash
pip install Pillow
```

**"HEIC support not available"**

```bash
pip install pillow-heif
```

**Framer output is all black**

- Ensure `frame.png` exists in the project root
- Check that frame.png is in PNG format with transparency

**Images not found**

- Verify folder names match the script (case-sensitive on macOS/Linux)
- Check that files are in the correct input directories

---

## 📝 Notes

- All tools support batch processing
- Original files are never modified; outputs go to separate folders
- HEIC conversion requires `pillow-heif` library
- Framer requires a PNG frame file with transparency for best results

---

## 💡 Tips

1. **Combine all tools**: Convert → Compress → Frame for optimized, styled images
2. **Test with one file** before processing entire batches
3. **Frame design**: Create custom frames in Photoshop/GIMP for unique styles
4. **Quality vs Size**: Adjust `MAX_SIZE_KB` and quality settings based on needs

---

## 📄 License

Feel free to modify and use these tools for your projects!
