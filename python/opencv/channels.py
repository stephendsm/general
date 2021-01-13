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

#Split the image based on channels
(B,G,R) = cv2.split(image)
#Showing the split of color channels of image respectively
cv2.imshow("This is RED", R)
cv2.imshow("This is Green", G)
cv2.imshow("This is BLUE", B)
#showtime
cv2.waitKey(0)

#Merge back the channels
merged = cv2.merge([B, G, R])
#Showing the merge of channels of image
cv2.imshow("This is merging back", merged)
#showtime
cv2.waitKey(0)

#Alternate method
#zeros i.e black out the image 
zeros = np.zeros(image.shape[:2], dtype="uint8")
#splitting R and merge while others zeros, so do G and B as well
red = cv2.merge([zeros, zeros, R])
green = cv2.merge([zeros, G, zeros])
blue = cv2.merge([B, zeros, zeros])
#Showing the split and merge of channels respectively
cv2.imshow("This is RED merge", red)
cv2.imshow("This is GREEN merge", green)
cv2.imshow("This is BLUE merge", blue)
#showtime
cv2.waitKey(0)

#Merge back the channels
merged = cv2.merge([B, G, R])
#Showing the merge of channels of image
cv2.imshow("This is merging back again", merged)
#showtime
cv2.waitKey(0)
