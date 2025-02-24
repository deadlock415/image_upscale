import cv2
import argparse
import os

def upscale_image(input_path, output_path, scale_factor):
    image = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
    if image is None:
        print(f"Error: Could not read the image: {input_path}")
        return
    
    new_dimensions = (int(image.shape[1] * scale_factor), int(image.shape[0] * scale_factor))
    upscaled_image = cv2.resize(image, new_dimensions, interpolation=cv2.INTER_CUBIC)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, upscaled_image)
    print(f"Upscaled image saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upscale all images in the 'image' folder by a given factor.")
    parser.add_argument("--scale", type=float, default=4.0, help="Upscale factor (default: 4)")
    args = parser.parse_args()
    
    input_folder = "image"
    output_folder = "upscale"
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        if os.path.isfile(input_path):
            upscale_image(input_path, output_path, args.scale)

