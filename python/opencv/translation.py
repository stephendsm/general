import numpy as np 
import cv2
import imutils
import argparse

#This is parsing the image 
# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser() #parse command line arguments
ap.add_argument("-i", "--image", required = True, help="Path to the image") #pass image from command line labelled as argument "-image"
args = vars(ap.parse_args()) #parse the arguments and store them in a dictionary

# loading and converting the image into numpy array
# printing the corresponding values
image = cv2.imread(args["image"])

#Shifting the image now
#shifted down
shifted = imutils.translate(image, 0, 100) #translate(image,x,y=100 i.e + values in y shifted down)
#showing
cv2.imshow("This is shifted down image", shifted)
#showtime
cv2.waitKey(0)

#Shifting the image now
#shifted up
shifted = imutils.translate(image, 0, -100) #translate(image,x,y=-100 i.e - values in y shifted up)
#showing
cv2.imshow("This is shifted up image", shifted)
#showtime
cv2.waitKey(0)

#Shifting the image now
#shifted left
shifted = imutils.translate(image, -100, 0) #translate(image,x=-100,y=0 i.e - values in x shifted left)
#showing
cv2.imshow("This is shifted left image", shifted)
#showtime
cv2.waitKey(0)

#Shifting the image now
#shifted right
shifted = imutils.translate(image, 100, 0) #translate(image,x=100,y=0 i.e + values in x shifted right)
#showing
cv2.imshow("This is shifted right image", shifted)
#showtime
cv2.waitKey(0)

#Shifting the image now
#shifted combine
shifted = imutils.translate(image, 100, 50) #translate(image,x=100,y=50)
#showing
cv2.imshow("This is shifted combine image", shifted)
#showtime
cv2.waitKey(0)