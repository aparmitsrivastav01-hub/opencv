import cv2 as cv 

image = cv.imread("IMage.jpg")
#width and height
#always save the new file

if image is None:
    print("Image Not Found")
else:
    print("Image loaded")
    
    resized = cv.resize(image,(300,300))
    
    cv.imshow("original image",image)
    cv.imshow("resized image",resized)
    
    cv.imwrite("resized_output.png",resized)
    
    cv.waitkey(0)
    cv.destroyAllWindows()