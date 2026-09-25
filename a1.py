import cv2 
print("Welcome to the world of Computer Vision where we make colorful images to grayscale!")
input_image = input("Please give the relative path of your image...\n")
image = cv2.imread(input_image)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
print("Do you want to see the image of save the image?")
press = input("Write 'see' to see the image and Write 'save' to save it\n")
if press=='save':
    output_name = input("What name do you want to save your image as?\n")  
    cv2.imwrite(output_name,gray)
    print('Image saved successfully')
elif press =='see':
    cv2.imshow("Grayscaled",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()