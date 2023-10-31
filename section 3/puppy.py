import cv2
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

img=cv2.imread('00-puppy.jpg')
cv2.namedWindow('puppy', cv2.WINDOW_NORMAL)
while True:
    cv2.imshow('puppy',img)
    ########################   ord('q')   here is the q key on the keyboard      ###############
#     if(cv2.waitKey(1) & 0xff == ord('q')):
    if(cv2.waitKey(1) & 0xff == 27):
        break
        
cv2.destroyAllWindows()