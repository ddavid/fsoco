import os

# directory of MM-Labels
idir = "001/"
# directory of new Darknet Labels
odir = "labels/"

# go through all files
for filename in os.listdir(idir):

    # create new label file
    lf = open(odir + filename, 'w+')

    # load label and skip first line
    f = open(idir + filename, "r")
    f.readline()

    # go through all remaining lines and get data
    line = f.readline()
    while line:
        data = line.split()
        x1,y1,x2,y2,label = int(data[0]), int(data[1]), int(data[2]), int(data[3]), data[4]

	# change this to actual size
        width, height = 1280, 1024

        # calc YOLO Coordinates
        dw = 1. / width
        dh = 1. / height
        x = (x1 + x2) / 2.0
        y = (y1 + y2) / 2.0
        w = x2 - x1
        h = y2 - y1
        x = x * dw
        w = w * dw
        y = y * dh
        h = h * dh

        # get label-number
        cone_class = -1
        if(label == "blue-cone"):
            cone_class = 0
        elif (label == "yellow-cone"):
            cone_class = 1
        elif (label == "red-cone"):
            cone_class = 2
        elif (label == "big-red-cone"):
            cone_class = 3
        if(cone_class == -1 ):
            print("NO CLASS FOUND FOR: " + filename)

        # write new label into file
        lf.write(str(cone_class) + " " + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + "\n")

        # read next line
        line = f.readline()


    f.close()
    lf.close()
