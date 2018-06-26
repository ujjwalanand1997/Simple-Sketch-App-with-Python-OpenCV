#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:05:56 2018

@author: ujjwal
"""

import cv2
import numpy as np

def sketch(video):
        grey_video = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(grey_video,(5,5),0)
        canny_video = cv2.Canny(blur,20,40)
        return canny_video
        
        
cap = cv2.VideoCapture(0)

while True:
        ret,frame = cap.read()
        cv2.imshow("video",sketch(frame))
        if cv2.waitKey(1)==ord('q'):
                break

cap.release()
cv2.destroyAllWindows()