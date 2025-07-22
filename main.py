import cv2

from util import color_limit

from PIL import Image

green = [0,255,0]   # defineing green color in bgr format

cap = cv2.VideoCapture(0)       # initialized video capture using webcam

while True:
    ret,frame = cap.read()      # reading frames
    
    hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # each frame from bgr to hsv
    
    low,high = color_limit(color=green)     # getting lower and upper hsv value for green color
    
    mask = cv2.inRange(hsv_img,low,high)    # creat mask for green color
    
    
    array_mask = Image.fromarray(mask)      # convert numpy array ---> PIL image 
    
    bbox = array_mask.getbbox()     # creat boundary box for green color image
    
    if bbox is not None:
        x1,y1,x2,y2 = bbox
        
        frame =cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),5)
    
    #print(bbox)p
    
    cv2.imshow('frame1',frame)
    if cv2.waitKey(1) & 0xFF == ord('p'):
        break

cap.release()

cv2.destroyAllWindows()