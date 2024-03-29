import numpy as np
import cv2
import math
import os
import time

def img_resize_and_paddig(img, size=(224, 244), color=(255, 255, 255), show=False, save=False, path=RF"{os. getcwd()}"):

    h_new,w_new=size
    h,w, channels = img.shape
    padded_img=np.full((h_new, w_new, 3), color, np.uint8)
    aspectRatio= h/w
    if aspectRatio==1:
        pass
    elif aspectRatio>1:
        k=w_new/h
        wCal= math.ceil(k*w)
        imgResize=cv2.resize(img,(wCal,h_new))
        wGap = math.ceil((w_new-wCal)/2)
        padded_img[ : , wGap:wCal+wGap ]= imgResize
    else:
        k=h_new/w
        hCal= math.ceil(k*h)
        imgResize=cv2.resize(img,(w_new,hCal))
        hGap = math.ceil((h_new-hCal)/2)
        padded_img[ hGap:hCal+hGap: , : ]= imgResize
    if save:
        cv2.imwrite(RF"{path}\padded{time.time()}.jpg",padded_img)
        print("\n"+RF'File saved at "{path}\padded{time.time()}.jpg"'+"\n")
    if show:
        t_end = time.time() + 5
        while time.time() < t_end:
            cv2.imshow(rf"padded_image",padded_img)
            if cv2.waitKey(2) & 0xFF == 27: #press ESC for exit
                break
            
        cv2.destroyAllWindows() 
        
    return padded_img


