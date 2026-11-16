import cv2
import numpy as np

# Read input image
image = cv2.imread("D:\\github\\Computer-vision\\Exp36_input_img.png")

if image is None:
    print("Image not found. Keep the image in the same folder as this Python file.")
else:
    # Convert BGR image to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Green background range
    lower_green = np.array([35, 50, 50])
    upper_green = np.array([85, 255, 255])

    # Detect green background
    background_mask = cv2.inRange(hsv, lower_green, upper_green)

    # Keep everything except green background
    foreground_mask = cv2.bitwise_not(background_mask)
    result = cv2.bitwise_and(image, image, mask=foreground_mask)

    # Resize images for display while maintaining aspect ratio
    max_width = 800
    max_height = 600

    h, w = image.shape[:2]
    scale = min(max_width / w, max_height / h, 1)

    new_size = (int(w * scale), int(h * scale))

    original_display = cv2.resize(image, new_size)
    result_display = cv2.resize(result, new_size)

    # Display
    cv2.imshow("Original Image", original_display)
    cv2.imshow("Background Removed", result_display)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
