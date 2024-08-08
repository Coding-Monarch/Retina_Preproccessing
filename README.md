# Retina Preproccessing
Retina Preprocessing with CLAHE

### Project Description
>This project focuses on enhancing images using CLAHE (Contrast Limited Adaptive Histogram Equalization) to improve contrast and clarity. The preprocessing technique is especially useful for medical imaging, >where clear visibility of features such as blood vessels or hemorrhages is crucial. CLAHE is applied to specified color channels to enhance features while maintaining image quality.

### What Problem Does It Solve?
>CLAHE preprocessing addresses the problem of insufficient contrast in images. This is particularly important for applications where detail and feature visibility are critical. By enhancing contrast adaptively, >CLAHE helps in better feature extraction and analysis.

## Features
>Apply CLAHE to specific color channels (Red, Green, Blue).

>Resize images if needed.

>Save processed images to specified directories.

>CLAHE clip limit input. (Note: I have found 5.7-5.5 most successful)

>CLAHE tile grid size input. (Note: I have found 8,8 most successful)

>display the input and output images if wanted.

## Dependencies
>OpenCV: For image processing and applying CLAHE.

>NumPy: For numerical operations.

>Matplotlib: For visualizing results.
>Features

## Install instructions
>Just download the file it's stand alone
>
But:
>You need to install these libraries:
```
pip install opencv-python
```
```
python -m pip install -U matplotlib
```
```
pip install numpy
```

## Use instructions

>param filenameInput: Path to the input image file.
>
>param filenameOutput: Path to save the output image.
>
>param clipLimit: CLAHE clip limit. Float or int (Note: I have found 5.7-5.5 most successful)
>
>param tileSize: CLAHE tile grid size. (Note: I have found 8,8 most successful)
>
>param saveImages: Whether to save the output image. bool: True or False
>
>param showImages: Whether to display the input and output images. bool: True or False
>
>param channels_to_apply: List of channels to apply CLAHE ('R', 'G', 'B'). #any combination is possible as well as only one
>(Note: I have found RBG most successful but you can choose whichever you prefer)
>
>param resize_dim: New dimensions for resizing the image (width, height). (Note: you can also put None if unneeded)
## For example:
```
process_image_with_clahe(
    filenameInput="file path",
    filenameOutput="folder you want it in path\\ name of output",
    clipLimit=5.7,
    tileSize=(8, 8),
    saveImages=True,
    showImages=False,
    channels_to_apply=['R', 'G', 'B'],
    resize_dim= None
)
```

