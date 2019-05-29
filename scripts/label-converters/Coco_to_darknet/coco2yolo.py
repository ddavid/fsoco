#!/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import json
import os
import sys
import argparse
import numpy as np

from shutil import copyfile
from pycocotools.coco import COCO

def parse_args():
    parser = argparse.ArgumentParser(description='Coco Dataset 2 Yolo Dataset')
    parser.add_argument(
        'coco_file',
        help='path to coco json file',
        type=str
    )

    if len(sys.argv) < 1:
        print("Error: Only coco-file or yolo-file can be specified")
        parser.print_help()
        sys.exit(1)

    args, unknown = parser.parse_known_args()
    return args

def normalize_annos(coco_dataset):
    image_infos = coco_dataset['images']
    annos = coco_dataset['annotations']
    image_annos = [[] for _ in range(len(annos))]
    for anno in annos:
        print(anno)
        img_id = anno['image_id']
        h = image_infos[img_id]['height']
        w = image_infos[img_id]['width']
        bbox = anno['bbox']
        area = anno['area']
        class_id = anno['category_id']
        bbox_norm = np.array(bbox, dtype=np.float32) 
        bbox_norm[[0,1]] += bbox_norm[[2,3]] / 2
        bbox_norm[[0, 2]] /= w
        bbox_norm[[1,3]] /= h
        
        image_annos[img_id].append((class_id, bbox_norm))
    return image_annos

def coco2yolo_image_paths(coco_dataset): 
    """ Converts coco images to yolo annotations """
    filenames = [im['file_name'] for im in coco_dataset['images']]
    for f in filenames:
        path, basename = os.path.split(f)
        new_image_path = '{}_darknet/JPEGImages'.format(path)
        if not os.path.exists(new_image_path):
            os.makedirs(new_image_path)

        print("Saving image to", os.path.join(new_image_path, basename))
        copyfile(os.path.join(path, basename), 
                 os.path.join(new_image_path, basename))
        
def coco2yolo_annos(coco_dataset):    
    """ Converts coco annotations to yolo annotations """    
    normalized_annos = normalize_annos(coco_dataset)
    filenames = [im['file_name'] for im in coco_dataset['images']]
    for f, image_anno in zip(filenames, normalized_annos):
        path, basename = os.path.split(f)
        new_anno_dir = os.path.join('{}_darknet'.format(path), 'labels')
        if not os.path.exists(new_anno_dir):
            os.makedirs(new_anno_dir)
        
        new_name = os.path.splitext(basename)[0]
        anno_filename = os.path.join(new_anno_dir, new_name + '.txt')
        print("Saving annotations to", anno_filename)

        class_ids = [str(ann[0]) for ann in image_anno]
        bboxes = [['{:.8f}'.format(p) for p in ann[1]] for ann in image_anno]
        lines = [' '.join([c] + b) + '\n' for c, b in zip(class_ids, bboxes)]
        with open(anno_filename, 'w') as fp:
            fp.writelines(lines)
            
def coco2yolo(coco_dataset):
    coco2yolo_image_paths(coco_dataset)
    coco2yolo_annos(coco_dataset)    


if __name__ == "__main__":
    args = parse_args()
    coco = COCO(args.coco_file)
    coco2yolo(coco.dataset)
    print("Conversion done!")