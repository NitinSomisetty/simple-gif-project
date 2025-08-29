import imageio.v3 as iio
import os, time
import numpy as np
from PIL import Image

# Load all frames from gif
frames = iio.imread("pokemon.gif", index=None)

# Convert one frame to ASCII
def frame_to_ascii(frame, new_width=60):
    chars = "@%#*+=-:. "   # dark → light
    gray = frame.mean(axis=2)  # RGB → grayscale
    h, w = gray.shape
    aspect_ratio = 0.5
    new_height = int(h * new_width / w * aspect_ratio)
    resized = np.array(Image.fromarray(gray).resize((new_width, new_height)))

    ascii_img = "\n".join(
        "".join(chars[int(pixel) * len(chars) // 256] for pixel in row)  # <-- int()
        for row in resized
    )
    return ascii_img

while True:
    for frame in frames:
        ascii_art = frame_to_ascii(frame)
        os.system("cls" if os.name == "nt" else "clear")
        print(ascii_art)
        time.sleep(0.2)

