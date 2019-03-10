#!/bin/bash


prefix="augmented_training/"
file_paths=`ls *.JPG`

for file in $file_paths
do
    echo $prefix$file >> ../augmented_training.list 
done
