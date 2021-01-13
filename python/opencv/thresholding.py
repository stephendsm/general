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

#SIMPLE thresholding using NORMAL binary
(T, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY)
#Showing SIMPLE thresholding
cv2.imshow("SIMPLE thresholding", thresh)
#showtime
cv2.waitKey(0)

#SIMPLE thresholding using INV binary
(T, threshINV) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
#Showing SIMPLE INV thresholding
cv2.imshow("SIMPLE INV thresholding", threshINV)
#showtime
cv2.waitKey(0)

#MASKING(AND_bitwise) these two ( NORMAL and INV)
and_mask = cv2.bitwise_and(image, image, mask = threshINV)
#Showing MASKING(AND_bitwise)
cv2.imshow("MASKING(AND_bitwise)", and_mask)
#showtime
cv2.waitKey(0)

#ADAPTIVE thresholding using MEAN
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
#Showing ADAPTIVE thresholding using MEAN
cv2.imshow("ADAPTIVE thresholding using MEAN", thresh)
#showtime
cv2.waitKey(0)

#SIMPLE thresholding using GAUSSIAN
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
#Showing ADAPTIVE thresholding using GAUSSIAN
cv2.imshow("ADAPTIVE thresholding using GAUSSIAN", thresh)
#showtime
cv2.waitKey(0)
