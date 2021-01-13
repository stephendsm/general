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

#AVERAGE blurring
blurred = np.hstack([
	cv2.blur(image, (3,3)),
	cv2.blur(image, (5,5)),
	cv2.blur(image, (7,7))])
#Showing the AVERAGE blurring
cv2.imshow("AVERAGE blurring", blurred)
#showtime
cv2.waitKey(0)

#GAUSSIAN blurring
blurred = np.hstack([
	cv2.GaussianBlur(image, (3,3), 0),
	cv2.GaussianBlur(image, (5,5), 0),
	cv2.GaussianBlur(image, (7,7), 0)])
#Showing the GAUSSIAN blurring
cv2.imshow("GAUSSIAN blurring", blurred)
#showtime
cv2.waitKey(0)

#MEDIAN blurring
blurred = np.hstack([
	cv2.medianBlur(image, 3),
	cv2.medianBlur(image, 5),
	cv2.medianBlur(image, 7)])
#Showing the MEDIAN blurring
cv2.imshow("MEDIAN blurring", blurred)
#showtime
cv2.waitKey(0)

#BILATERAL blurring
blurred = np.hstack([
	cv2.bilateralFilter(image, 3, 21, 21),
	cv2.bilateralFilter(image, 5, 32, 32),
	cv2.bilateralFilter(image, 7, 42, 42)])
#Showing the BILATERAL blurring
cv2.imshow("BILATERAL blurring", blurred)
#showtime
cv2.waitKey(0)