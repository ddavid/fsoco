# Elbflorace VOC to Darknet-Converter

1. Put the `images` and the `image1.xml` files (one per image) into the export folder
2. Go in the folder `code_convert_label`
3. Run `python convert_label.py`
4. Now there should be a `.txt` file for every image in the export folder
5. You can now delete the XML files and use the images + .txt files to train in darknet

## TODO:

 - Right now only blue and yellow cones are converted