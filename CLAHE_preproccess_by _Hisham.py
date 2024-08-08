import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

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

process_image_with_clahe(
    filenameInput="your path",
    filenameOutput="path to folder\\ + whatever name you want to save the photo as",
    clipLimit=5.7,
    tileSize=(8, 8),
    saveImages=True,
    showImages=False,
    channels_to_apply=['R', 'G', 'B'],
    resize_dim=
)
