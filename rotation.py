import cv2 as cv

image = cv.imread("image.png")

if image is None:
    print("error")
else:
    (h,w) = image.shape[:2]

    centre = (h //2 , w // 2)

    M = cv.getRotationMatrix2D(centre,90,1.0)
    rotated = cv.warpAffine(image,M,(h,w))
    
    cv.imshow("original image",image)
    cv.imshow("rotated image",rotated)
    
    cv.waitKey(0)
    cv.destroyAllWindows()