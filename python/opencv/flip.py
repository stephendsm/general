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

#Flipping the image
#None flip i.e original
#showing
cv2.imshow("This is original of the image", image)
#showtime
cv2.waitKey(0)

#Flipping the image
#flip vertically i.e around x-axis
flipped = cv2.flip(image, 0) #0 flip vertically i.e around x-axis
#showing
cv2.imshow("This is Flipping vertically of the image", flipped)
#showtime
cv2.waitKey(0)

#Flipping the image
#flip horizontally i.e around y-axis
flipped = cv2.flip(image, 1) #1 flip horizontally i.e around y-axis
#showing
cv2.imshow("This is Flipping horizontally of the image", flipped)
#showtime
cv2.waitKey(0)

#Flipping the image
#flip both side i.e around x-axis and y-axis
flipped = cv2.flip(image, -1) #-1 flip vertically i.e around x-axis and y-axis
#showing
cv2.imshow("This is Flipping both sides of the image", flipped)
#showtime
cv2.waitKey(0)