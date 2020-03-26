#!/bin/bash
#send directory file as argument and the script will add line breaks at the end of every .txt on the directory
var=$(find $1 -name '*.txt')
for i in $var
do
echo "" >> $i
done
