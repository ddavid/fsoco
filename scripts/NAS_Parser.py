import csv
import json
import torch
import os

list_path = os.path.expanduser('~/Desktop/MitDut_NASlabels.csv') #Path to csv file
img_path = os.path.expanduser('~/Desktop/MitDut_Images/') #Path to folder containing images

img_files = []
label_files = []
box_count = 0
img_count = 0
with open(list_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    for i, row in enumerate(csv_reader):
        if i == 0:
            continue
        img_boxes = []
        for img_box_str in row[2:]:
            if not img_box_str == "":
                img_boxes.append(json.loads(img_box_str))

        img_boxes = torch.tensor(img_boxes, dtype=torch.float)
        if os.path.exists(os.path.join(img_path, row[0])):
            img_files.append(row[1])
            label_files.append(img_boxes)
            img_count += 1
            box_count += len(img_boxes)
        else:
            print('File Missing: ' + row[0])
print('Total images: ' + str(img_count))
print('Total boxes: ' + str(box_count))