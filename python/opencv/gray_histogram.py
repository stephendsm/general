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

#Convert the original image to Gray scale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#Showing the original image
cv2.imshow("Gray scale image", gray)
#showtime
cv2.waitKey(0)

#Create the histogram of the Gray scale image
hist = cv2.calcHist([gray], [0], None, [256], [0, 256]) #[0]i.e Gray channel has 0, 
                                                        #None i.e we dont have mask in this case, 
                                                        #256 i.e bin size, [0, 256] i.e values range in btw

#Plotting the graph
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
#showtime
cv2.waitKey(0)

