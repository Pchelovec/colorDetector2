import cv2
import os
import numpy as np

from supportedColor import create_mask

path = './images'
files = os.listdir(path)

def result(mask):
    #count % of white mask
    num_rows, num_cols = mask.shape
    total=num_rows*num_cols
    nonzero=np.count_nonzero(mask)
    
    if (nonzero!=0):
        div_res=nonzero/total
        if (div_res>0.15):
            print("YES", div_res)

def showSearchingMask(img, mask):
    #print(mask)
    cv2.imshow("image", img)
    cv2.imshow("Byte Mask for searching color", mask)
    print(result(mask))
    cv2.waitKey(0)

def check(file,color):
    print('check is', file, color)
    img = cv2.imread(os.path.join(path,file))
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #cv2.imshow("image",img)

    mask = create_mask(hsv, color)

    #result mask
    showSearchingMask(img,mask)


#default value is red
def method(color):
    for file in files:
        check(file,color)

