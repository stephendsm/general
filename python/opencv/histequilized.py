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

#Convert the original image to Gray scale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Showing the original image
cv2.imshow("Gray scale image", gray)
#showtime
cv2.waitKey(0)

eq = cv2.equalizeHist(gray)
#Showing the equilize image
cv2.imshow("Equilize image", np.hstack([gray, eq]))
#showtime
cv2.waitKey(0)