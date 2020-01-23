from lxml import etree
from io import StringIO
import os

filecount = 0
conecount = 0

directory_str = "./VOCfiles/"
directory = os.fsencode(directory_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".xml"):
        doc = etree.parse(directory_str + filename)
        objects = doc.xpath("count(//object)")
        filecount = filecount + 1
        conecount = conecount + objects

print("Files total: ", filecount)
print("Cones total: ", conecount)

