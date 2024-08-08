import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

def MaskingAndEnhancing(image_path, output_path):
    # Ensure the output directory exists
    output_folder = os.path.dirname(output_path)
    os.makedirs(output_folder, exist_ok=True)

    # Load the image
    image = cv2.imread(image_path)

    # Check if image is loaded successfully
    if image is None:
        print(f"Error loading image: {image_path}")
        return

    # Apply Gaussian blur to reduce noise
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Convert the blurred image to HSV color space
    hsv_image = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2HSV)

    # Define range for red color in HSV
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    # Create masks for red color
    mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    red_mask = mask1 | mask2

    # Create a copy of the original image to modify
    adjusted_image = image.copy()
    # Apply brightness adjustment only to the areas where red_mask is active
    brightened_area = cv2.convertScaleAbs(image, alpha=2.5, beta=0)
    adjusted_image[red_mask > 0] = brightened_area[red_mask > 0]

    # Save the adjusted image
    cv2.imwrite(output_path, adjusted_image)

def process_image_with_clahe(
    filenameInput='input.png',  
    filenameOutput='output.png',  
    clipLimit=2.0,  
    tileSize=(8, 8),  
    saveImages=True,  
    showImages=False,  
    channels_to_apply=['G'],  
    resize_dim=None  
):
    def apply_clahe_channels(input_image, clip_limit, tile_size, channels):
        clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_size)

        b, g, r = cv2.split(input_image)

        if 'R' in channels:
            r = clahe.apply(r)
        if 'G' in channels:
            g = clahe.apply(g)
        if 'B' in channels:
            b = clahe.apply(b)

        output_image = cv2.merge((b, g, r))

        return output_image

    input_image = cv2.imread(filenameInput, cv2.IMREAD_COLOR)
    if input_image is None:
        print(f"Error loading image: {filenameInput}")
        return
    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)

    if resize_dim is not None:
        input_image = cv2.resize(input_image, resize_dim, interpolation=cv2.INTER_AREA)

    output_image = apply_clahe_channels(input_image, clipLimit, tileSize, channels_to_apply)

    if saveImages:
        cv2.imwrite(filenameOutput, cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR))

    if showImages:
        plt.subplot(121)
        plt.imshow(input_image)
        plt.title('Input')
        plt.xticks([])
        plt.yticks([])

        plt.subplot(122)
        plt.imshow(output_image)
        plt.title('Output')
        plt.xticks([])
        plt.yticks([])

        plt.show()

def process_folder(input_folder, output_folder):
    # Ensure the output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each image in the folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            temp_output_path = os.path.join(output_folder, f"temp_{filename}")
            final_output_path = os.path.join(output_folder, filename)

            print(f"Processing {image_path}")

            # Apply CLAHE and save the result
            process_image_with_clahe(
                filenameInput=image_path,
                filenameOutput=temp_output_path,
                clipLimit=5.7,
                tileSize=(8, 8),
                saveImages=True,
                showImages=False,
                channels_to_apply=['R', 'G', 'B'],
                resize_dim=None
            )
            
            

# Example usage
input_folder = "C:\\Users\\Hrafi\\OneDrive\\Desktop\\Ungradeable - Copy"
output_folder = "C:\\Users\\Hrafi\\OneDrive\\Desktop\\Once and for all"
process_folder(input_folder, output_folder)
