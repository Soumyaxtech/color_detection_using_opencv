import cv2

from util import color_limit

from PIL import Image

green = [0,255,0]

cap = cv2.VideoCapture(0)   

while True:
    ret,frame = cap.read()
    
    hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    low,high = color_limit(color=green)
    
    mask = cv2.inRange(hsv_img,low,high)
    
    array_mask = Image.fromarray(mask)
    
    bbox = array_mask.getbbox()
    
    if bbox is not None:
        x1,y1,x2,y2 = bbox
        
        frame =cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),5)
    
    #print(bbox)
    
    cv2.imshow('frame1',frame)
    if cv2.waitKey(1) & 0xFF == ord('p'):
        break

cap.release()

cv2.destroyAllWindows()