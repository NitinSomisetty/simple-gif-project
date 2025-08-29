import imageio.v3 as iio
import numpy as np

img = iio.imread("20230929.jpg") #IMPORTANT

# Make it grayscale (average R,G,B)
gray = img.mean(axis=2).astype(np.uint8) #.astype(np.uint8) converts floats back to valid pixel values (e.g., 149.3 → 149).

# Save the modified image
iio.imwrite("out.png", gray)

# To invert colours
inverted = 255 - img  
iio.imwrite("out_inverted.png", inverted)

#Crop
cropped = img[0:200, 0:200]   # [rows, columns]
iio.imwrite("out_cropped.png", cropped)

#rotate
rotated = np.rot90(img)  
iio.imwrite("out_rotated.png", rotated)

#darken and brighten
darker = (img * 0.5).astype(np.uint8)
brighter = np.clip(img * 1.5, 0, 255).astype(np.uint8)

