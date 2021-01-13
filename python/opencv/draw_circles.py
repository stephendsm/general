import numpy as np 
import cv2

#defining canvas
canvas = np.zeros((300,300,3), dtype = "uint8")

#Drawing Circle
#defining
green_circle = (0,255,0)
start_point_green = (100,100)
radius_green = 10
#drawing
cv2.circle(canvas,start_point_green,radius_green,green_circle)
#showing with title
cv2.imshow("This is my circle", canvas)
#showtime
cv2.waitKey(0)

#################################################

#defining canvas
canvas = np.zeros((300,300,3), dtype = "uint8")

#Drawing multiple circles/concentric
#defining
white_circle = (255,255,255)
#start_point, i.e calculating the center point of canvas
(centerX,centerY) = (canvas.shape[1]//2, canvas.shape[0]//2) #shape[1]/2 = x at center of canvas, and so do y
#drawing
for radius in range(0,175,25): #(min,max,increment)
    cv2.circle(canvas, (centerX,centerY), radius, white_circle)
#showing with title
cv2.imshow("This is my concentric circle", canvas)
#showtime
cv2.waitKey(0)

#################################################

#defining canvas
canvas = np.zeros((300,300,3), dtype = "uint8")

#Drawing 25circles ramdomly in different radius and colors
#drawing
for i in range(0,25): #(min,max)
    radius = np.random.randint(5, high = 200) # randint(min, max) i.e it can varies in between
    color = np.random.randint(0, high = 256, size=(3,)).tolist()
    centerPoint = np.random.randint(0, high=300, size=(2,)) # size(2=XandYcoor,)
    cv2.circle(canvas, tuple(centerPoint), radius, color, -1) #-1 = filled circle with color
#showing with title
cv2.imshow("This is my randomly circle with different size and color", canvas)
#showtime
cv2.waitKey(0)


