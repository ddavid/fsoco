#!/usr/bin/python

# -*- coding: utf-8 -*-

'''
	Simple script to undistort all files in given subdirectories

	TODOs
	Create argparser to pass as arguments:
	* List of subdirectories
	* Image suffix


'''

import os
import pickle

def get_files(directory, suffix):
    '''
        Returns all files in the 'directory' with the specified suffix
        It's sorted to ensure determinism
    '''
    filenames = os.listdir(directory)
    return sorted([filename for filename in filenames if filename.endswith(suffix)])

def main():
    
    directories  = ["/100", "/102"]
    cwd          = os.getcwd()
    acc_d_height = 0.0
    acc_d_width  = 0.0 
    
    print("Starting to calculate")
    
    avgs = []
    
    for directory in directories:
        cur_dir = cwd + directory
        os.chdir(cur_dir)
        label_paths = get_files(cur_dir, "txt")
        #print(label_paths)
        counter      = 0
        acc_d_width  = 0.0
        acc_d_height = 0.0
        for label_file in label_paths:
            with open(label_file, "r") as label:
                next(label)
                #tmp_cnt = int(label.readline().strip())
                #print(counter)
                for line in label:
                    try:
                        d_width  = float(line[5])
                        d_height = float(line[6])
                        acc_d_width  += float(line[5])
                        acc_d_height += float(line[6])
                        counter += 1
                    
                    except:
                        #print("No Distance")
                        pass
                label.close()
                
        avg_d_width  = acc_d_width/float(counter)
        avg_d_height = acc_d_height/float(counter)
        #avgs.append[avg_d_width 
        #print(acc_d_width)
        #print(acc_d_height)
        print(("Distance averaged over %i Images in: \n" + cur_dir) %(counter))       
        print("Avg Width-Distance: %.2fm" %(avg_d_width))
        print("Avg Height-Distance: %.2fm" %(avg_d_height))            
                    
        

if __name__ == '__main__':
    main()
