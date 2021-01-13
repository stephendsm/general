import argparse #argparse to handle parsing our command line arguments
import cv2      #this is our opencv library and contains our image processing function

# fetching the arguments and save in dictionary
ap = argparse.ArgumentParser() #parse command line arguments
ap.add_argument("-i", "--image", required = True, help="Path to the image") #pass image from command line labelled as argument "-image"
args = vars(ap.parse_args()) #parse the arguments and store them in a dictionary

# loading and converting the image into numpy array
# printing the corresponding values
image = cv2.imread(args["image"])
print("width of the image in pixels is: {}".format(image.shape[1]))
print("height of the image in pixels is: {}".format(image.shape[0]))
print("channels present the image is: {}".format(image.shape[2]))

cv2.imshow("Image Title", image)    #display actual image in screen, where "Image" is the window title
cv2.waitKey(0)                      #wait key is 0, means indefinite wait, wait key 1000 means wait for 1 sec etc
cv2.imwrite("newcat.jpg", image)       #write our image to file in JPG format
