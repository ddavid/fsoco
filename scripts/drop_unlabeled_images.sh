#!/usr/bin/env bash

for f in Images/002/*.jpg; do
    if [[ ! -f Labels/002/$(basename "$f" .jpg).txt ]]; then
        echo "Dropping image due to missing label: $f"
        rm "$f"
    fi
done
