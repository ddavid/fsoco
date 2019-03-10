#!/usr/bin/python

# -*- coding: utf-8 -*-

'''
    Simple Script for augmenting our images.
        - Takes *.JPG images and applies image augmentations with imgaug
        - Takes all *.JPG images in the cwd
        - Manipulates them with imgaug augmenters
        - Saves augmented images in the cwd with the augmentation prefixed to its original file name

    Requirements:
        * See requirements.txt in https://github.com/aleju/imgaug
        * opencv (conda) or python-opencv (pip)
        * imgaug

    Suggested setup:
        * Create new conda environment
        * Get requirements.txt from above source -> cat requirements.txt | xargs -i conda [install|add] {}
        * Install opencv in env
        * Install imgaug from git:
            - /env_path/bin/pip install git+https://github.com/aleju/imgaug

    
    How to use:
        * Copy this script into directory with training images
        * (Source) Activate environment
        * Run script

'''

import cv2
import os
from imgaug import augmenters as iaa

def get_files(postfix):
    '''
        Returns all files in the current working directory with the specified postfix
        It's sorted to ensure determinism
    '''
    filenames = os.listdir(os.getcwd())
    return sorted([filename for filename in filenames if filename.endswith(postfix)])
    
def save_augmented_images(prefix, aug_images, paths):
    '''
    aug_images - list of numpy.ndarray's 
    
    '''
    for i in range(len(paths)):
        cv2.imwrite(prefix + "_" + paths[i], aug_images[i])
     
def get_images(paths):
    '''
    Images of shape := (height, width, channels = 3) in BGR Format 

    paths - [str]
    '''
    images = []
    
    for path in paths:
        images.append(cv2.imread(path))
    
    return images

def main():
    '''
	Dirty image augmentation to get better recognition for systems presentation.

    '''
    augs = ["superpixel","colorspace","grayscale","gaussian_blur", "average_blur","median_blur","edge_detect","add","add_eltwise","invert","contrast_norm","dropout"]
            
    superpixel    = iaa.Superpixels(p_replace=(0.4, 0.6), n_segments=(16, 64))
    #colorspace    = iaa.Sequential([iaa.ChangeColorspace(from_colorspace="BGR",  to_colorspace="HSV"), iaa.WithChannels(0, iaa.Add(-50, 50), iaa.ChangeColorspace(from_colorspace="BGR", to_colorspace="BGR")])
    grayscale     = iaa.Grayscale(alpha = (0.0, 1.0))
    gaussian_blur = iaa.GaussianBlur(sigma = (0.0, 3.0))
    average_blur  = iaa.AverageBlur(k = (2, 10))
    median_blur   = iaa.MedianBlur(k = (5, 11))
    edge_detect   = iaa.EdgeDetect(alpha = (0.0 , 1.0))
    add           = iaa.Add((-50, 50), per_channel = 0.5)
    add_eltwise   = iaa.AddElementwise((-50, 50), per_channel = 0.5)
    invert        = iaa.Invert(0.25, per_channel = 0.5)
    contrast_norm = iaa.ContrastNormalization((0.5, 1.5), per_channel = 0.5)
    dropout       = iaa.Dropout(p = (0, 0.3), per_channel = 0.5)
         
    image_paths   = get_files("JPG")
    cv_images     = get_images(image_paths)
    
    for augmentation in augs:
        if augmentation == "superpixel":
            aug_images = superpixel.augment_images(cv_images)
            save_augmented_images("superpixel", aug_images, image_paths)
            
        #elif augmentation == "colorspace":
        #   aug_images = colorspace.augment_images(cv_images)
        #    save_augmented_images("colorspace", aug_images, image_paths)
            
        elif augmentation == "grayscale":
            aug_images = grayscale.augment_images(cv_images)
            save_augmented_images("grayscale", aug_images, image_paths)
            
        elif augmentation == "gaussian_blur":
            aug_images = gaussian_blur.augment_images(cv_images)
            save_augmented_images("gaussian_blur", aug_images, image_paths)
          
        elif augmentation == "average_blur":
            aug_images = average_blur.augment_images(cv_images)
            save_augmented_images("average_blur", aug_images, image_paths)
            
        elif augmentation == "edge_detect":
            aug_images = edge_detect.augment_images(cv_images)
            save_augmented_images("edge_detect", aug_images, image_paths) 
       
        elif augmentation == "add":
            aug_images = add.augment_images(cv_images)
            save_augmented_images("add", aug_images, image_paths)
            
        elif augmentation == "add_eltwise":
            aug_images = add_eltwise.augment_images(cv_images)
            save_augmented_images("add_eltwise", aug_images, image_paths)
            
        elif augmentation == "invert":
            aug_images = invert.augment_images(cv_images)
            save_augmented_images("invert", aug_images, image_paths)
            
        elif augmentation == "contrast_norm":
            aug_images = contrast_norm.augment_images(cv_images)
            save_augmented_images("contrast_norm", aug_images, image_paths)
            
        elif augmentation == "dropout":
            aug_images = dropout.augment_images(cv_images)
            save_augmented_images("dropout", aug_images, image_paths)

if __name__ == '__main__':
    main()
    
    
    
