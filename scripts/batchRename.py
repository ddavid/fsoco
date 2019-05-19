# -*- coding: utf-8 -*-
"""
Script used for renaming multiple files.
Takes 2 arguments and one optional argument:
	The first argument specifies the destination name, the second argument specifies the destination extension, and the optional parameter (--directory) specifies the path of the source files relative to the current working directory.

Author: Albert Seligmann - 11/04/2019
"""

import os
import glob
import argparse

def batchRename(mydir, name, extension):
    files = glob.glob(mydir + "*." + extension)
    files_sorted = sorted(files)
    num_files = str(len(files_sorted))
    print("Number of files: " + num_files)
    zeros = len(num_files)
    i = 1
    for f in files_sorted:
        title, ext = os.path.splitext(os.path.basename(f))
        num = "{1:0{0}}".format(zeros, i)
        new_filename = name + num + ext
        os.rename(f, os.path.join(mydir, new_filename))
        print(" -Renamed " + f + " to " + new_filename)
        i += 1
    files_after = glob.glob(mydir + "*.jpg")
    print("Number of files: " + str(len(files_after)))
    
        
parser = argparse.ArgumentParser()
parser.add_argument("name", help="Name that the files should be renamed to")
parser.add_argument("ext", help="Extension of files to be renamed")
parser.add_argument("--directory", help="The relative directory to the folder containing files to be renamed")

args = parser.parse_args()

cur_dir = os.getcwd() + "/"
if args.directory:
    cur_dir = cur_dir + args.directory

print("dir = " + cur_dir)
print("name = " + args.name)
batchRename(cur_dir, args.name, args.extension)
