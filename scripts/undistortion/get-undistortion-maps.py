#!/usr/bin/python

# -*- coding: UTF-8 -*-

'''
    Simple script for getting the undistortion maps for point projection from distorted images
    to undistorted images.
    
    Writes calculated maps out to pickle.
'''

import pickle
import cv2 as cv
import numpy as np

def main():

  basler_undistorted = pickle.load(open("basler_pickle.p", "rb"))

  #objects = []
  #with (open("./basler_pickle.p", "rb")) as openfile:
  #    while True:
  #        try:
  #            basler_undistorted.append(pickle.load(openfile))
  #        except EOFError:
  #            break
    
  image_width  = 1280
  image_height = 1024

  #print(basler_undistorted)

  cam_mtx = basler_undistorted["mtx"]
  cam_dist = basler_undistorted["dist"]
  rvecs = basler_undistorted["rvecs"]
  tvecs = basler_undistorted["tvecs"]
  #imageSize = image_height * image_width
  imageSize = ( image_height, image_width )
  
  #getOptimal...Mtx(cameraMatrix, distCoeffs, imageSize, alpha[, newImgSize[, centerPrincipalPoint]]) -> retval, validPixROI
  # Doesn't take Rect of validPixROI, contrary to the cpp method
  new_cam_mtx, valid_roi = cv.getOptimalNewCameraMatrix(cam_mtx, cam_dist, imageSize, 1, imageSize, 1) 
  
  # getOptimalNewCameraMatrix() possibly not working like in cpp
  #map1, map2 = cv.initUndistortRectifyMap(cam_mtx, cam_dist, np.eye(3), new_cam_mtx, imageSize, cv.CV_16SC2);
  map1, map2 = cv.initUndistortRectifyMap(cam_mtx, cam_dist, np.eye(3), cam_mtx, imageSize, cv.CV_16SC2);
  
  # map1 and map2 can be used together with cv.remap() for efficient real-time undistortion
  # Only need to be calculated once.
  maps = { "map1": map1, "map2": map2 }
  pickle.dump( maps, open("maps.p", "wb"))

if __name__ == '__main__':
    main()
