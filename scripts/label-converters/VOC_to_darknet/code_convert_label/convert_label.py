"""
@author: xi_hu_elbflorace
"""

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import glob


classes = ["ConeYellow","ConeBlue"]

#convert left top and right bottom coordinates to  x,y,w,h
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

#read in image VOC label file, convert it into YOLO-form
def convert_annotation(image_id):
    in_file = open(image_id)
    out_file = open(image_id[0:-3] + "txt", 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        if(obj.find('bndbox') != None):
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
            bb = convert((w,h), b)
        elif(obj.find('polygon') != None):
            xmlbox = obj.find('polygon')
            x_list = [ float(xmlbox.find(x).text) for x in ['x1','x2','x3','x4'] ]
            y_list = [ float(xmlbox.find(y).text) for y in ['y1','y2','y3','y4'] ]
            
            b = ( min(x_list),max(x_list),min(y_list),max(y_list) )
            bb = convert((w,h), b)
        
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    
#directory construct:
# your path--- code_convert_label / convert_label.py
#          |
#           -- export / cjr53qlsxid2w0737fxb6nrnk.png , cjr53qlsxid2w0737fxb6nrnk.xml ...
image_path = "../export/"

for xml_file in glob.glob(image_path + '*.xml'):
    print(xml_file)
    convert_annotation(xml_file)
    #converted label txt will be in the same directory: export/

