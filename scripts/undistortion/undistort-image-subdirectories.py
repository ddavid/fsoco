#!/usr/bin/python

# -*- coding: utf-8 -*-

'''
	Simple script to undistort all files in given - still hardcoded - subdirectories

	TODOs
	Create argparser to pass as arguments:
	* List of subdirectories
	* Image suffix


'''

import os
import pickle
import cv2 as cv
import numpy as np

def get_files(directory, suffix):
    '''
        Returns all files in the 'directory' with the specified suffix
        It's sorted to ensure determinism
    '''
    filenames = os.listdir(directory)
    return sorted([filename for filename in filenames if filename.endswith(suffix)])

def undistorted_dir(directory):
    '''
        Checks if images in directory have already been undistorted with this script.
    '''
    files = get_files(directory, "dist")
    return (files != [])

def main():

  directories = ["/100 (copy)"]#, "/101", "/102", "/103"]
  undistortion_maps = {}
  
  try:
    undistortion_maps = pickle.load(open("maps.p", "rb"))
    distortion_coeff  = pickle.load(open("basler_pickle.p", "rb"))
    
  except:
    print("No pickle file found for undistortion maps")
    return
  
  cam_mtx  = distortion_coeff["mtx"]
  cam_dist = distortion_coeff["dist"]
   
  map1 = undistortion_maps["map1"]
  map2 = undistortion_maps["map2"]
  cwd  = os.getcwd()
  
  print("Starting to undistort!")
  for directory in directories:
    cur_dir = cwd + directory
    os.chdir(cur_dir)
    if not undistorted_dir(cur_dir):
      print("Undistorting files in subdirectory: %s" %(directory))
      img_height = 1024
      img_width  = 1280

                
      image_files = get_files(cur_dir, "JPG")
      for img_path in image_files:
        img    = cv.imread(img_path)
        #undist = cv.remap(img, map1, map2, cv.INTER_LINEAR) 
        undist = cv.undistort(img, cam_mtx, cam_dist, None, cam_mtx)
        cv.imwrite(img_path, undist)
      # Create undistorted flag-file
      tmp = open("un.dist", "w")

    else:
      print("All images in " + cur_dir + " have already been undistorted")
  
  print("Finished undistorting")

if __name__ == '__main__':
    main()
