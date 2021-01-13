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

#Rectangular mask
#Create numpyarray (i.e canvas) which is filled with zeros with exact width and height of image
mask = np.zeros(image.shape[:2], dtype="uint8") #canvas filled with zero; zero i.e fill with black
(cX, cY) = (image.shape[1]//2, image.shape[0]//2) #centerpoint
cv2.rectangle(mask, (cX-50, cY-50), (cX+50, cY+50), 255, -1) # ..(mask, startingpoint(from midpoint), endingpoint(from midpoint), 255 i.ewhite color, filled)
#showing
cv2.imshow("Rectangular Masking", mask)
#showtime
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask=mask)
#showing
cv2.imshow("Rectangular Masking image now", masked)
#showtime
cv2.waitKey(0)

#Circular mask
#Create numpyarray (i.e canvas) which is filled with zeros with exact width and height of image
mask = np.zeros(image.shape[:2], dtype="uint8") #canvas filled with zero
(cX, cY) = (image.shape[1]//2, image.shape[0]//2) #centerpoint
cv2.circle(mask, (cX, cY), 50, 255, -1) # ..(mask, startingpoint(from midpoint), radius, white color, filled)
#showing
cv2.imshow("Circular Masking", mask)
#showtime
cv2.waitKey(0)

masked = cv2.bitwise_and(image, image, mask=mask)
#showing
cv2.imshow("Circular Masking image now", masked)
#showtime
cv2.waitKey(0)
