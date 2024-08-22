import cv2
import numpy as np

def image_to_ascii(image, char_width=3, char_height=6):
    h, w = image.shape[:2]

    ascii_w = w // char_width
    ascii_h = h // char_height
    
    reshaped = image[:ascii_h*char_height, :ascii_w*char_width]
    reshaped = reshaped.reshape(ascii_h, char_height, ascii_w, char_width)
    avg_pixels = np.mean(reshaped, axis=(1, 3)).astype(int)

    ascii_chars = " .',:ceoxkbJCDO@"
    ascii_chars = ascii_chars[::-1]
    ascii_art = '\n'.join(''.join(ascii_chars[min(pixel // 16, len(ascii_chars) - 1)] for pixel in row) for row in avg_pixels)
    
    return ascii_art

user = input("Image file: ")
image = cv2.imread(user, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Unable to load the image.")
else:
    ascii_result = image_to_ascii(image, char_width=3, char_height=6)
    
    with open('out.txt', 'w') as f:
        f.write(ascii_result)
    
    ascii_lines = ascii_result.split('\n')
    ascii_width = len(ascii_lines[0])
    ascii_height = len(ascii_lines)
    
    print(f"ASCII art saved to 'out.txt'. Original dimensions: {image.shape[1]}x{image.shape[0]}")
    print(f"ASCII art dimensions: {ascii_width}x{ascii_height}")
