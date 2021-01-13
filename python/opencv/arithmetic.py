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

#Adding and subtracting by using opencv i.e neglect less than 0 or beyond 255
print("Max of 255 by cv2: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("Min of 0 by cv2: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

#Adding adn subtracting by using numpy i.e wrapping less than 0 or beyond 255
print("Wrap of max of 255 by numpy: {}".format(np.uint8([200]) + np.uint8([100])))
print("Wrap of min of 0 by numpy: {}".format(np.uint8([50]) - np.uint8([100])))

#Generating one array and multiplying it with 100
#adding that array to the actual image numpy array
M = np.ones(image.shape, dtype="uint8") * 100 #turns all the pixel in image into 1 and multiply with 100
added = cv2.add(image, M)
#Showing the added image
cv2.imshow("Added image", added)
#showtime
cv2.waitKey(0)

#Generating one array and multiplying it with 50
#substracting that array to the actual image numpy array
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
#Showing the subtracted image
cv2.imshow("Substracting image", subtracted)
#showtime
cv2.waitKey(0)
