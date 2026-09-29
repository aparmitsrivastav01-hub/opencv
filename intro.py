import cv2 as cv
img = cv.imread("path/to/image")


if img is not None:
    success = cv.imwrite("name",img)
    if success:
        print("Image Saved successfully")
    else:
        print("Failed to save an image")
else:
    print("Error image not loaded")