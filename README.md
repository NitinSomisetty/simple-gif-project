# Python GIF Project

This project converts GIF frames into ASCII art.

## Requirements
- Python 3.x
- Packages: `imageio`, `numpy`, `Pillow`

Install dependencies:
```bash
pip install imageio numpy pillow
```


### How to Run:
Run the script with:
python main.py
Replace main.py with the actual filename of your script.
Explaning the steps: 

### Explaining the steps:

1. `import imageio.v3 as iio` <br>
   **What:** Load the imageio v3 API and alias it `iio`.<br>
   **Why:** imageio reads images/GIFs into NumPy arrays (frames). <br>
   **Tip:** `pip install imageio` if missing. <br>

2. `import os, time`<br>
   **What:** Bring in OS utilities and time functions.<br>
   **Why:** `os` clears the terminal; `time.sleep()` controls frame speed.<br>

3. `import numpy as np`<br>
   **What:** Import NumPy as `np`.<br>
   **Why:** Frames are arrays; NumPy is used for array ops and conversions.<br>

4. `from PIL import Image`
   **What:** Import Pillow’s `Image` class.<br>
   **Why:** Use Pillow to resize frames with good resampling.<br>
   **Tip:** `pip install pillow` if needed.<br>

5. `frames = iio.imread("pokemon.gif", index=None)`<br>
   **What:** Read all frames from `pokemon.gif` into a list/array.<br>
   **Result:** `frames = [frame0, frame1, ...]`; each frame usually shape `(H, W, 3)`.<br>
   **Failure:** File not found → `FileNotFoundError`. If single-frame GIF → `len(frames)==1`.<br>

6. `def frame_to_ascii(frame, new_width=60):`<br>
   **What:** Define a function converting one image-frame to an ASCII string.<br>
   **Why:** Encapsulates conversion logic; `new_width` controls character width.<br>

7. `chars = "@%#*+=-:. "`  # dark → light<br>
   **What:** Ordered ASCII palette from dense (dark) to sparse (light).<br>
   **Why:** Dark pixels map to dense characters to simulate shading.<br>

8. `gray = frame.mean(axis=2)`  # RGB → grayscale<br>
   **What:** Average R,G,B channels into a single brightness value per pixel.<br>
   **Why:** ASCII art only needs brightness, not color.<br>
   **Note:** Produces floats \~0–255.<br>

9. `h, w = gray.shape`<br>
   **What:** Get image height `h` and width `w` (in pixels).<br>
   **Why:** Needed to compute resized character-grid height preserving aspect.<br>

10. `aspect_ratio = 0.5`<br>
    **What:** Correction factor for character cell shape (height vs width).<br>
    **Why:** Terminal characters are taller; this avoids vertically squashed output.<br>
    **Tip:** Try 0.4–0.6 depending on your font/terminal.<br>

11. `new_height = int(h * new_width / w * aspect_ratio)`<br>
    **What:** Compute target character-rows to keep proportions.<br>
    **Why:** Scale width → derive height while accounting for aspect\_ratio.<br>

12. `resized = np.array(Image.fromarray(gray).resize((new_width, new_height)))`<br>
    **What:** Convert NumPy gray → Pillow image → resize → back to NumPy array.<br>
    **Why:** Pillow’s resizing gives smooth sampling and is fast.<br>

13.

```py
ascii_img = "\n".join(
    "".join(chars[int(pixel) * len(chars) // 256] for pixel in row)
    for row in resized
)
```

**What:** Map each pixel brightness (0–255) to an index in `chars`, build lines, join with `\n`.<br>
**Why:** `int(pixel) * len(chars) // 256` safely converts brightness → index `0..len(chars)-1`.<br>
**Why use `// 256` not `/255`:** integer math prevents out-of-range index for pixel==255.<br>
**Note:** `int()` avoids TypeError when using floats as indices.<br>

14. `return ascii_img`<br>
    **What:** Output the full multiline string representing the ASCII frame.<br>

15. `while True:`<br>
    **What:** Start infinite loop to replay animation continuously.<br>
    **Why:** Keeps GIF looping until you stop it.<br>
    **Stop:** Ctrl + C (KeyboardInterrupt).<br>

16. `for frame in frames:`<br>
    **What:** Iterate all frames in order for each loop pass.<br>
    **Why:** Play frames sequentially to animate.<br>

17. `ascii_art = frame_to_ascii(frame)`<br>
    **What:** Convert current frame to ASCII text.<br>

18. `os.system("cls" if os.name == "nt" else "clear")`<br>
    **What:** Clear terminal screen (Windows `cls`, Unix `clear`).<br>
    **Why:** Replace previous frame for animation effect.<br>
    **Note:** Flicker may happen; libraries like curses reduce flicker.<br>

19. `print(ascii_art)`<br>
    **What:** Display the ASCII frame in the terminal.<br>

20. `time.sleep(0.2)`<br>
    **What:** Pause \~200 ms between frames.<br>
    **Why:** Controls playback speed (\~5 FPS). Adjust for smoother/faster animation.<br>
