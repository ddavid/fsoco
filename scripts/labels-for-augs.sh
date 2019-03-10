#!/bin/bash

declare -a prefixes=("superpixel_" "colorspace_" "grayscale_" "gaussian_blur_" "average_blur_" "median_blur_" "edge_detect_" "add_" "add_eltwise_" "invert_" "contrast_norm_" "dropout_")

file_paths=`ls *.txt`

for prefix in "${prefixes[@]}"
do
    for file in $file_paths
    do
        cp $file $prefix$file 
    done
done
