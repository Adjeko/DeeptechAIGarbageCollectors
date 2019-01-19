# -*- coding: utf-8 -*-
"""ImageCruncher.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fxySyUfuCnV_g28cdScuWwL9WYCzzSTf
"""

import numpy as np
import cv2
import os

def readImage(filename):
  return cv2.imread(filename, 0)

def resizeImage(img):
  return cv2.resize(img, (48, 84)) # 9:16

def writeImage(filename, resizedImg):
  cv2.imwrite(filename,resizedImg)
  
def convertAllImages(rootdir, convertedFileName):
  for root, dirs, files in os.walk(rootdir):
    for file in files:
      imgPath = os.path.join(root, file)
      img = readImage(imgPath)
      img = resizeImage(img)
      writeImage(root + "\\" + convertedFileName, img)

import os

#rootdir = 'C:\\Users\\Julian\\Nextcloud\\DeeptechAI\\screenshots'
rootdir = 'C:\\Jupyter\\Websites'

convertAllImages(rootdir, "ganzeBild.jpg")