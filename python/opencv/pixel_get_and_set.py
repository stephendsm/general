import argparse #argparse to handle parsing our command line arguments
import cv2      #this is our opencv library and contains our image processing function

# fetchin g the arguments and save in dictionary
ap = argparse.ArgumentParser() #parse command line arguments
ap.add_argument("-i", "--image", required = True, help="Path to the image") #pass image from command line labelled as argument "-image"
args = vars(ap.parse_args()) #parse the arguments and store them in a dictionary

# loading and converting the image into numpy array
# printing the corresponding values
image = cv2.imread(args["image"])

# grab the 0,0 pixel of the image and print color values
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# change the color of the pixel at 0,0
image[0,0] = (0,0,255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# grab the region and show in cv2 window
corner = image[0:100, 0:100]
cv2.imshow("Corner just sliced", corner)
cv2.waitKey(0)

# change color of the area of image
image[0:100, 0:100] = (0,255,0)
cv2.imshow("Corner of area changed", image)
cv2.waitKey(0)


