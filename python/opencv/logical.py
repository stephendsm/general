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

#create 300x300 numpy array(i.e canvas) and 250x250 white rectangle inside it
rectangle = np.zeros((300,300), dtype="uint8") #np.zeros(size,size) gives a black canvas
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1) # 255 is the 'white' color for filling
#showing
cv2.imshow("rectangle", rectangle)
cv2.waitKey(0)

#create 300x300 numpy array(i.e canvas) and 150 white radius inside it
circle = np.zeros((300,300), dtype="uint8") #np.zeros(size,size) gives a black canvas
cv2.circle(circle, (150, 150), 150, 255, -1) # (150,150) means centerPoint of canvas, and 255 is the 'white' color for filling
#showing
cv2.imshow("circle", circle)
#showtime
cv2.waitKey(0)

#Performing logical/bitwise operation
#And operation
bitwiseAnd = cv2.bitwise_and(rectangle, circle)
#showing
cv2.imshow("AND", bitwiseAnd)
#showtime
cv2.waitKey(0)

#Performing logical/bitwise operation
#OR operation
bitwiseOr = cv2.bitwise_or(rectangle, circle)
#showing
cv2.imshow("OR", bitwiseOr)
#showtime
cv2.waitKey(0)

#Performing logical/bitwise operation
#Xor operation
bitwiseXor = cv2.bitwise_xor(rectangle, circle)
#showing
cv2.imshow("XOR", bitwiseXor)
#showtime
cv2.waitKey(0)

#Performing logical/bitwise operation
#Not operation
bitwiseNot = cv2.bitwise_not(rectangle, circle)
#showing
cv2.imshow("NOT", bitwiseNot)
#showtime
cv2.waitKey(0)
