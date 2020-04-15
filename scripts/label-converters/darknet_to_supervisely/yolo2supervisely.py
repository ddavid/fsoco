#!/usr/bin/env python
# coding: utf-8

"""
    Simple script for converting Darknet YOLO labels to Supervisely format.
    https://docs.supervise.ly/ann_format/
    
    As always, you'll need a classes.txt file for the dataset.
    `#classes.txt
    0 fst-class
    1 snd-class 
    2 third-class
    . ...
    .
    .
    `
    
    You can also input the path to a colors.txt file with HEX color codes for the color of the labels in Supervisely.
    The index of the classes will be matched to the index of the HEX color code, they need to be of the same length, even if you repeat a color.
    If no colors.txt file is given, we try to infer the color from the class name, be aware that this can fail.
    Your directory structure should look like this. Sample files are in the `config` directory.

    Input:
    cwd
    ├── img_x.txt
    ├── img_y.txt
    ├── img_z.txt
    ...
    ├── img_x.jpeg
    ├── img_y.jpeg
    └── img_z.jpeg

    Output:
    cwd
    ├── img_x.txt
    ├── img_y.txt
    ├── img_z.txt
    ├── project_name
        ├── meta.json
        ├── dataset_name
            ├── ann
            │   ├── img_x.json
            │   ├── img_y.json
            │   └── img_z.json
            └── img
                ├── img_x.jpeg
                ├── img_y.jpeg
                └── img_z.jpeg

    Simply Drag and Drop the project_name folder in Supervisely to create a new project with the converted dataset contained in it.
"""

import json
import os
import sys
import argparse
from tqdm import tqdm
from pathlib import Path


# TODO Replace OpenCV with PIL since only the image dimensions are required
import cv2 as cv

colors = {'yellow': "#FFFF00",
          'blue': "#0000ff",
          'red': "#ff0000",
          # For daltonics
          'orange': "#ffa500",
          'green': "#008000",
          'pink': "#ffc0cb"}
          
SLY_META_FILE_NAME = 'meta.json'

def get_args():
    parser = argparse.ArgumentParser(description='Convert Darknet YOLO annotations to Supervisely format.')
    parser.add_argument('classes_file', help='path to classes txt file', type=str)
    parser.add_argument('dataset_name', help='Name of dataset on Supervisely', type=str)
    parser.add_argument('project_name', help='Name of project on Supervisely', type=str)
    parser.add_argument('--format', default='jpg',
                        help='Image format', type=str, required=True)
    parser.add_argument('--colors_file', default='',
                        help='path to txt file with HEX colors for labels in the same order as classes file', type=str, required=False)
    return parser.parse_args()


def get_files(directory, suffix):
    '''
        Returns all files in the 'directory' with the specified suffix
        It's sorted to ensure determinism
    '''
    filenames = os.listdir(directory)
    return sorted([filename for filename in filenames if filename.endswith(suffix)])


def get_class_list(file_path):
    '''
        Generates a list of class names based on classes txt file
    :param file_path:
    :return: List of string class_names
    '''

    class_list = []
    with open(file_path) as classes_file:
        for idx, line in enumerate(classes_file.readlines()):
            class_name = line.strip()
            class_list.append(class_name)

    return class_list


def get_class_color(cone_class):
    '''
        Returns the RGB HEX string for the class's color
    :param class_idx: Int : Class ID from labels
    :param class_list: List of class names
    :return:
    '''
    class_color = None
    #cone_class = class_list[class_idx]
    for color, hex_code in colors.items():
        if color in cone_class.lower():
            class_color = hex_code
    if class_color is None:
        class_color = colors['pink']
    return class_color


def create_meta_file(classes, colors):
    """
    Generate meta.json file contents for the project to be uploaded to Supervisely
    :returns: JSON object
    """
    meta_data = {'tags': [], 'classes': []}
    assert (len(classes) is len(colors))
    for ix, color in enumerate(colors):
        meta_data['classes'].append({'title': classes[ix],
                                     'shape': 'rectangle',
                                     'color': color})
    try:
        with open(SLY_META_FILE_NAME, 'w', encoding='utf-8') as f:
            json.dump(meta_data, f, ensure_ascii=False, indent=4)
    except:
        return False
    return True


def create_img_json_file(name, size, objects):
    """
        Generate .json file contents for one single image label
        :returns: JSON object
        """
    img_data = {'description': "This is an empty description as Darknet YOLO labels don't have one.", 'name': name}
    size_obj = {'width': size[0], 'height': size[1]}
    img_data['size'] = size_obj
    img_data['objects'] = objects

    try:
        with open(name + '.json', 'w', encoding='utf-8') as f:
            json.dump(img_data, f, ensure_ascii=False, indent=4)
    except:
        return False
    return True


def create_object_list(rectangles, class_list):
    object_list = []

    for (upper_left, lower_right), class_ix in rectangles:
        rectangle = {'description': '', 'tags': [], 'bitmap': None}
        class_title = class_list[class_ix]
        rectangle['classTitle'] = class_title
        rectangle['points'] = {'exterior': [upper_left, lower_right], 'interior': []}
        object_list.append(rectangle)

    return object_list


def convert_labels(label_paths, class_list, image_suffix):
    failed_conversions = []
    for path in tqdm(label_paths, total=len(label_paths), dynamic_ncols=True, desc="Converting labels from cwd"):

        im = None

        with open(path) as label_file:

            label_lines = [line.rstrip("\n") for line in label_file.readlines()]

            rectangles = []

            prefix = path.split('.')[0]
            im = cv.imread(prefix + '.' + image_suffix)

            image_height = im.shape[0]
            image_width = im.shape[1]
            size = image_width, image_height

            for line in label_lines:
                args = line.split(' ')
                # args = filter(None, args)

                cone_class = (int)(args[0])
                pixel_bb_x = (int)(float(args[1]) * image_width)
                pixel_bb_y = (int)(float(args[2]) * image_height)
                pixel_bb_w = (int)(float(args[3]) * image_width)
                pixel_bb_h = (int)(float(args[4]) * image_height)

                upper_left = [(pixel_bb_x + pixel_bb_w / 2), (pixel_bb_y - pixel_bb_h / 2)]
                # upper_right = ((pixel_bb_x - pixel_bb_w / 2), (pixel_bb_y - pixel_bb_h / 2))
                lower_right = [(pixel_bb_x - pixel_bb_w / 2), (pixel_bb_y + pixel_bb_h / 2)]
                # lower_left = ((pixel_bb_x + pixel_bb_w / 2), (pixel_bb_y + pixel_bb_h / 2))

                rectangles.append(((upper_left, lower_right), cone_class))
            object_list = create_object_list(rectangles, class_list)
            success = create_img_json_file(prefix, size, object_list)
            if not success:
                failed_conversions.append(path)
                print("Failed to convert label for image: ", path)
    return True


def main():
    argv = get_args()

    class_list = get_class_list(argv.classes_file)
    image_suffix = argv.format
    
    colors_list = []
    if argv.colors_file is '':
        for cone_class in class_list:
            colors_list.append(get_class_color(cone_class))
    else:
        colors_list = get_class_list(argv.colors_file)

    cwd = os.getcwd()
    Path(argv.project_name).mkdir(exist_ok=True)
    os.chdir(argv.project_name)
    Path(argv.dataset_name).mkdir(parents=True, exist_ok=True)
    Path(argv.dataset_name + "/ann").mkdir(parents=True, exist_ok=True)
    Path(argv.dataset_name + "/img").mkdir(parents=True, exist_ok=True)
    os.chdir("..")
    label_paths = get_files(cwd, "txt")
    img_paths = get_files(cwd, image_suffix)

    success_labels = convert_labels(label_paths, class_list, image_suffix)
    success_meta = create_meta_file(class_list, colors_list)

    if success_labels and success_meta:
        print("Successfully converted labels.")
        # Move meta.json file to root of new supervisely project
        os.rename(SLY_META_FILE_NAME, argv.project_name + '/'+ SLY_META_FILE_NAME)
        # Only annotation json files left
        converted_label_paths = get_files(cwd, "json")       
        # Move labels
        for converted_label_path in converted_label_paths:
            os.rename(converted_label_path, argv.project_name + '/' + argv.dataset_name + "/ann/" + converted_label_path)
        # Move images
        for img_path in img_paths:
            os.rename(img_path, argv.project_name + '/' + argv.dataset_name + "/img/" + img_path)
        return True
    else:
        print("Failed to convert labels.")
        return False


if __name__ == '__main__':
    main()
