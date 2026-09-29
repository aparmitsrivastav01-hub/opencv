import cv2 as c

image = c.imread("img source")

if image is not None:
    h,w,c = image.shape
    print(h , w , c )
else:
    print("Could not load image")