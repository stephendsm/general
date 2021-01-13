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

#Resizing the image
#not user defined i.e original
resized = imutils.resize(image)
#showing
cv2.imshow("This is not Resizing or original of the image", resized)
#showtime
cv2.waitKey(0)

#Resizing the image
#user defined width
resized = imutils.resize(image,width=100)
#showing
cv2.imshow("This is Resizing by giving width of the image", resized)
#showtime
cv2.waitKey(0)

#Resizing the image
#user defined height
resized = imutils.resize(image,height=200)
#showing
cv2.imshow("This is Resizing by giving height of the image", resized)
#showtime
cv2.waitKey(0)

#Resizing the image
#user defined width and height
resized = imutils.resize(image, width=100, height=200)
#showing
cv2.imshow("This is Resizing by giving width and height of the image", resized)
#showtime
cv2.waitKey(0)