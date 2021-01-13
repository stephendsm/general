import numpy as np 
import cv2
import argparse

#This is parsing the image 
# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser() #parse command line arguments
ap.add_argument("-i", "--image", required = True, help="Path to the image") #pass image from command line labelled as argument "-image"
args = vars(ap.parse_args()) #parse the arguments and store them in a dictionary

# loading and converting the image into numpy array
# printing the corresponding values
image = cv2.imread(args["image"])

#Showing the original image
cv2.imshow("This is original of the image", image)
#showtime
cv2.waitKey(0)

#Cropping the image
#crop 
cropped = image[16:140, 57:217] #image[y_start:y_stop, x_start:x_stop] (we are getting those values from the original image as you like)
#showing
cv2.imshow("This is the cropped of the image", cropped)
#showtime
cv2.waitKey(0)