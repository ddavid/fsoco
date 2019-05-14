import os

currentPath = os.getcwd()
currentPath += '/filesToRead/'
#TO USE THIS ADD THE FILES IN A 'filesToRead' FOLDER IN THE LOCATION OF THE SCRIPT.
#EDIT THE CONE CODES TO THE NUMBER OF CLASS YOU ARE USING.
yellowConeCode = 0
blueConeCode = 1
orangeConeCode = 2
bigOrangeConeCode = 3
#EDIT THE CONE CODES TO THE NUMBER OF CLASS YOU ARE USING.


noOfYellowCones = 0
noOfBlueCones = 0
noOfOrangeCones = 0
noOfBigOrangeCones = 0
noOfFilesScanned = 0

for filename in os.listdir(currentPath):
    pathOfFile = currentPath + '/' + filename
    file = open(pathOfFile, "r")
    noOfFilesScanned += 1
    #print("FILE:" + filename)
    for line in file:
        if line[0] == str(yellowConeCode):
            noOfYellowCones += 1
        elif line[0] == str(blueConeCode):
            noOfBlueCones += 1
        elif line[0] == str(orangeConeCode):
            noOfOrangeCones += 1
        elif line[0] == str(bigOrangeConeCode):
            noOfBigOrangeCones += 1


print("No of Files Scanned: " + str(noOfFilesScanned))
print("No of Yellow Cones: " + str(noOfYellowCones))
print("No of Blue Cones: " + str(noOfBlueCones))
print("No of Orange Cones: " + str(noOfOrangeCones))
print("No of Big Orange Cones: " + str(noOfBigOrangeCones))
print("No of Cones " + str(noOfYellowCones + noOfBlueCones + noOfOrangeCones + noOfBigOrangeCones))
