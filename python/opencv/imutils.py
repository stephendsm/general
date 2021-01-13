import numpy as np 
import cv2

def translate(image, x, y):
    Matrix = np.float32([[1,0,x],[0,1,y]])
    shifted = cv2.warpAffine(image, Matrix, (image.shape[1], image.shape[0]))
    return shifted

def rotate(image, theta, center=None, scale=1.0): #scale 1.0 gives the original image
    (h, w) = image.shape[:2] #taking the height=h and width=w of the image

    if center is None: #calculating the center of the image
    	center = (w//2, h//2)

    Matrix = cv2.getRotationMatrix2D(center, theta, scale) #creating our own design image as a matrix with a specific value as we like
    rotated = cv2.warpAffine(image, Matrix, (w,h)) #nothing but exactly the same as bove shifted(translate)
    return rotated

def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
	dim = None
	(h, w) = image.shape[:2] #parsing the image and getting h=height and w=width

	if width is None and height is None: #there is not user defined width and height
		return image

	if width is None: #user defined height (i.e needs to adjust(makes ratio) width by the given height)
		r = height/float(h)
		dim = (int(w*r), height)

	else: #user defined width (i.e needs to adjust(makes ratio) height by the given width)
		r = width/float(w)
		dim = (width, int(h*r))

	resized = cv2.resize(image, dim, interpolation=inter)
	return resized