
import cv2

# Read input image
image = cv2.imread(r"D:\github\Computer-vision\Exp31_input_img.png")

if image is None:
    print("Image not found. Check the image path.")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply threshold segmentation
    ret, segmented = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Resize images for display only
    original_display = cv2.resize(image, (800, 500))
    segmented_display = cv2.resize(segmented, (800, 500))

    # Display output
    cv2.imshow("Original Image", original_display)
    cv2.imshow("Segmented Image", segmented_display)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
