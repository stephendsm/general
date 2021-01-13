import numpy as np
import cv2

# define a canvas of size 300x300 px, with 3 channels (R,G,B) and data types as 8 bits unsigned integer
canvas = np.zeros((300,300,3), dtype = "uint8")

# Drawing Line
# defining
green_color_line = (0,255,0) 
start_point_green_line = (0,0) #at x1,x2
stop_point_green_line = (300,300) #at y1,y2
#applying
cv2.line(canvas,start_point_green_line,stop_point_green_line,green_color_line)
#showing
cv2.imshow("This is visualizing greenline", canvas)
#showtime
cv2.waitKey(0)

# defining
red_color_line = (0,0,255) 
start_point_red_line = (0,0) #at x1,x2
stop_point_red_line = (300,300) #at y1,y2
thickness_red_line = 3
#applying
cv2.line(canvas,start_point_red_line,stop_point_red_line,red_color_line,thickness_red_line)
#showing
cv2.imshow("This is visualizing redline", canvas)
#showtime
cv2.waitKey(0)

# Drawing Rectangle
# defining
green_color_rectangle = (0,255,0)
start_point_green_rectangle = (10,10)
stop_point_green_rectangle = (60,60)
#applying
cv2.rectangle(canvas,start_point_green_rectangle,stop_point_green_rectangle,green_color_rectangle)
#showing
cv2.imshow("This is the visualizing green rectangle",canvas)
#showtime
cv2.waitKey(0)

# defining
red_color_rectangle = (0,0,255)
start_point_red_rectangle = (10,10)
stop_point_red_rectangle = (60,60)
thickness_red_rectangle = 3
#applying
cv2.rectangle(canvas,start_point_red_rectangle,stop_point_red_rectangle,red_color_rectangle,thickness_red_rectangle)
#showing
cv2.imshow("This is the visualizing red rectangle",canvas)
#showtime
cv2.waitKey(0)

# defining
blue_color_rectangle = (255,0,0)
start_point_blue_rectangle = (10,10)
stop_point_blue_rectangle = (60,60)
fill_blue_rectangle = -1
#applying
cv2.rectangle(canvas,start_point_blue_rectangle,stop_point_blue_rectangle,blue_color_rectangle,fill_blue_rectangle)
#showing
cv2.imshow("This is the visualizing blue rectangle with fill coloring",canvas)
#showtime
cv2.waitKey(0)


