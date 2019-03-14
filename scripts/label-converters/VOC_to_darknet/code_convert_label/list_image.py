"""
@author: xi_hu_elbflorace
"""

import glob

def main(image_path,txt_file):
    with open(txt_file, 'w') as tf:
        for jpg_file in glob.glob(image_path + '*.png'):
            tf.write(jpg_file + "\n")    
    
if __name__ == '__main__':
    main("../export/", "../train_detector/train.txt")
