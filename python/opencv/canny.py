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
cv2.imshow("Original image or BGR color space", image)
#showtime
cv2.waitKey(0)

#Convert image to greyscale
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Implement GAUSSIAN blurr
blurred = cv2.GaussianBlur(image, (5,5), 0)
#Showing the GAUSSIAN blurring
cv2.imshow("GAUSSIAN blurring", blurred)
#showtime
cv2.waitKey(0)

#CANNY Edge detected
canny = cv2.Canny(blurred, 30, 150)
#Showing the CANNY Edge detected image
cv2.imshow("CANNY Edge detected", canny)
#showtime
cv2.waitKey(0)
