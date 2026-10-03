import cv2 as cv 
image  = cv.imread("Image.png")

if image is not None:
    cropped = image[100:200,50:150]
    
    cv.imshow("Original Image ", image)
    cv.imshow("Cropped Image",cropped)
    cv.waitkey(0)
    cv.destroyAllWindows()
