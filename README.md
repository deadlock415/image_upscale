# Image Upscaler Script

This Python script upscales all images in the `image` folder and saves them to the `upscale` folder using OpenCV.

## Features
- Supports multiple image formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`, `.webp`.
- Automatically detects and processes images in the `image` folder.
- Upscales images using bicubic interpolation.
- Handles errors for non-image files or corrupted images.

## Requirements
Ensure you have Python installed along with the required dependency:
```bash
pip install opencv-python
```

## Usage
1. Place all images inside the **`image`** folder in the current directory.
2. Run the script with:
   ```bash
   python image_upscaler.py --scale 4
   ```
   *(Change `4` to any scale factor you prefer.)*
3. Upscaled images will be saved inside the **`upscale`** folder.

## Script Explanation
- **`upscale_image(input_path, output_path, scale_factor)`**: Reads an image, upscales it, and saves it.
- **`process_images(input_folder, output_folder, scale_factor)`**: Scans the `image` folder and processes valid image files.
- **Main script execution**: Parses arguments and calls `process_images()`.

## Example
```bash
python image_upscaler.py --scale 2
```
This will upscale all images by a factor of 2 and save them in the `upscale` folder.

## License
This project is open-source and free to use for any purpose.

---
Developed with ❤️ using OpenCV.


