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

#Rotating the image
rotated = imutils.rotate(image, 180)
#showing
cv2.imshow("This is rotating 180deg the image", rotated)
#showtime
cv2.waitKey(0)