#!/usr/bin/python

# -*- coding: utf-8 -*-

'''
	Simple script for generating image copies with drawn bounding boxes, using
	darknet format labels and the according images in the cwd.
	
'''

import cv2 as cv
import os
import argparse

def get_files(directory, suffix):
    '''
        Returns all files in the 'directory' with the specified suffix
        It's sorted to ensure determinism
    '''
    filenames = os.listdir(directory)
    return sorted([filename for filename in filenames if filename.endswith(suffix)])

#def 

def main():

    parser = argparse.ArgumentParser( description='Draw Bounding Boxes from label files to copies of according images in the cwd.')
    #parser.usage()
    parser.add_argument('-width', dest='image_width', help='Width of the images', type=int, required=True)
    parser.add_argument('-height', dest='image_height', help='Height of the images', type=int, required=True)
    parser.add_argument('-f','--format', dest='image_suffix', help='File Suffix of image files', default='jpg', required=False)

    argv = parser.parse_args()

    image_width   = argv.image_width
    image_height  = argv.image_height
    image_suffix  = argv.image_suffix
	    

    cwd         = os.getcwd()
    
    image_list  = get_files(cwd, image_suffix)
    label_paths = get_files(cwd, "txt")

    # RGB Tuple, 0-255
    # TODO adjust color according to entry index
    rectangle_color = (0, 255, 0)

    #cv_images       = []
    

    #for ( image in image_list ) :

        #cv_images.append( cv.imread( image ))

    for path in label_paths :

        label_file = open(path)
        label_lines = [line.rstrip("\n") for line in label_file.readlines()]

        rectangle_coords = []

        for line in label_lines :

            args       = line.split(' ')
            clean_args = filter(None, args)

            pixel_bb_x = (int) (float(clean_args[1]) * image_width)
            pixel_bb_y = (int) (float(clean_args[2]) * image_height)
            pixel_bb_w = (int) (float(clean_args[3]) * image_width)
            pixel_bb_h = (int) (float(clean_args[4]) * image_height)

            upper_right = ((pixel_bb_x - pixel_bb_w/2), (pixel_bb_y - pixel_bb_h/2)) 
            lower_left  = ((pixel_bb_x + pixel_bb_w/2), (pixel_bb_y + pixel_bb_h/2))

            rectangle_coords.append((upper_right, lower_left))

        prefix = path.split('.')[0]
        im     = cv.imread( prefix + "." + image_suffix)

        for coords in rectangle_coords :

            cv.rectangle( im, coords[0], coords[1], rectangle_color )
	
	boxes_image_path = "boxes_" + prefix + "." + image_suffix

	print("Drawing Boxes for image: " + prefix + "." + image_suffix + " into " + "boxes_" + prefix + "." + image_suffix)
	
        cv.imwrite( "boxes_" + prefix + "." + image_suffix, im )

if __name__ == '__main__':
    main()
