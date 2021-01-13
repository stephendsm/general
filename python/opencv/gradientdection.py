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

# LAPLACE gradient dection
lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap)) #convert back to 8 bit unsigned int

#Showing LAPLACE gradient dection image
cv2.imshow("LAPLACE gradient dection", lap)
#showtime
cv2.waitKey(0)

# SOBEL X and Y
sobelX = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(image, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX)) #convert back to 8 bit unsigned int
sobelY = np.uint8(np.absolute(sobelY)) #convert back to 8 bit unsigned int

sobelCombined = cv2.bitwise_or(sobelX,sobelY)

#Showing sobelX gradient dection image
cv2.imshow("sobelX gradient dection", sobelX)
#showtime
cv2.waitKey(0)

#Showing sobelY gradient dection image
cv2.imshow("sobelY gradient dection", sobelY)
#showtime
cv2.waitKey(0)

#Showing sobelCombined gradient dection image
cv2.imshow("sobelCombined gradient dection", sobelCombined)
#showtime
cv2.waitKey(0)