from matplotlib import pyplot as plt
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

#Split image into channels B, G and R
chans = cv2.split(image)

#initialize a tuple
colors = ("b", "g", "r")

#Plotting the graph
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of Pixels")

#Looping for each channel
for (chan, color) in zip(chans, colors):
	hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
	plt.plot(hist)
	plt.xlim([0, 256])

plt.show()
#showtime
cv2.waitKey(0)

