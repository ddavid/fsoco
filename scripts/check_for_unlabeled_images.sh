#!/bin/bash

for f in $1/*.jpg; do
    if [[ ! -f $2/$(basename "$f" .jpg).txt ]]; then
        echo "Image missing label: $f"
    fi
done
