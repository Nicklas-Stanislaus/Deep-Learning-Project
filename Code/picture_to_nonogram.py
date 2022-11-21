# import numpy as np
# from PIL import Image
# import matplotlib.pyplot as plt
# import os

def convert_nonogram_image_to_nparray(path): 
    """Convert a nonogram picture stored at a given path to np array"""
    img = Image.open(path)
    return np.array(img).astype(int)

def show_nonogram_image(path): 
    """Plot a nonogram picture stored at a given path"""
    img = Image.open(path)
    plt.imshow(img)
    plt.show()

def convert_to_fixed_size_nonogram(directory, size = 50):
    """Convert the images in a given directory to correct nonogram picture format.
    Deletes original image. 
    
    Parameters: 
        directory (string): path to the directory where images are stored.
        size (int): the target size of nonograms (default: 50).
    """
    
    for picture in os.listdir(directory):
        img = Image.open(directory + picture)
        nonogram = img.convert('L').point(lambda x: 0 if x < 128 else 255, '1').resize((size, size))
        nonogram.save(directory + picture, "PNG")


