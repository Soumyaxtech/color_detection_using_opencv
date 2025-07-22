import cv2

import numpy as np


def color_limit(color):
    
    c= np.uint8([[color]])  # i/p --> 2d numpy array
    
    hsv_color = cv2.cvtColor(c,cv2.COLOR_BGR2HSV)  # bgr --> hsv
    
    
    lowerLimit = hsv_color[0][0][0] - 10,100,100    # (hue h-10 , s = 100 , v = 100)
    upperLimit = hsv_color[0][0][0] + 10,255,255    # (hue h+10 , s = 255 , v = 255)
    
    # converting values into numpy array...........inRange() func works on arrays 
    
    lowerLimit = np.array(lowerLimit,dtype=np.uint8)
    upperLimit = np.array(upperLimit,dtype=np.uint8)
    
    return lowerLimit,upperLimit
    