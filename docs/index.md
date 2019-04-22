# FSOCO
<small>Formula Student Objects in Context</small>

## What?
Open-Source Dataset for Objects that need to be recognized during the dynamic disciplines of the Formula Student Driverless competitions.



| Team  | Data Type  | Annotation Type  | # Data | # Cones |
|---|---|---|---|---|
| municHMotorsport e.V.  | Color Images  | Darknet YOLO Format | 3745 | 18697 |
| Elbflorace e.V.  |  Color Images |  Darknet YOLO Format | 853 | 3791 |
| SCUTRacing  |  Color Images |  Darknet YOLO Format | 792 | 5896 |
| DHBW Engineering e.V.  |  Color Images |  VOC | 600 | 5794 |
| StarkStrom Augsburg e.V  | Color Images  | Darknet YOLO Format  | 1120 | 7501 |
| AMZ Racing  | Color Images | Darknet YOLO Format | 791 | 5685 |
| ITU Racing  | Color Images  | Darknet YOLO Format  | 600 | 8241 |
| Raceyard  | Color Images  | MM-Label Tool Format | 600 | 9491|
| EUFS | Color Images| Darknet YOLO Format | 1094 | 4594 |
| Dimitris Martin Arampatzis | Color Images | Darknet YOLO Format | 600 | 12333 |
|   |   |   |||

### Annotation Types

Here you'll find the definitions for all different annotation types appearing in the datasets. If you need the labels in another format, please look for the according script in the [scripts folder](https://github.com/ddavid/fsoco/tree/master/scripts) or write one and share your solution - sharing is caring ;)

#### Darknet YOLO

Darknet uses normalized image dimensions for the labels and defines the regions-of-interest (ROI) by their **class**, **mid-point**, **width** and **height**

![Darknet Bounding-Box](./img/bbox-description.png)

```bash
# darknet-label.txt

0 0.255078125 0.545833333333 0.02421875 0.0583333333333
0 0.41328125 0.613194444444 0.040625 0.081944444444
0 0.81015625 0.780555555556 0.0734375 0.15
```

[class index][mid_x][mid_y][width][height]

#### VOC

VOC is a xml based description format.
A label will be similiar to:

```xml
<object>
    <name>yellow-cone</name>
    <pose>Unspecified</pose>
    <truncated>0</truncated>
    <difficult>0</difficult>
    <polygon>
        <x1>877</x1>
        <y1>571</y1>
        <x2>897</x2>
        <y2>528</y2>
        <x3>916</x3>
        <y3>576</y3>
    </polygon>
</object>
```

VOC can be converted to Darknet YOLO by using the script provided in this repo.
DHBW Engineering used polygons for marking the cones.
An example:

![Example polygon image](./img/examplePolygone.PNG)

#### Munich Labeling Tool (https://github.com/ddavid/MM-label-tool)

[# cones]

[minX][minY][maxX][maxY][labelname][dist_from_width][dist_from_height]

The position is given in absolute pixel values, the distance is calculated in metres.

There is a converter to Darknet YOLO in Scripts.


## Who?
* [municHMotorsport e.V.](https://www.munichmotorsport.de/)  

<a href="https://www.munichmotorsport.de/"><img src="https://imgur.com/DYo8xVV.png" alt="municHMotorsport e.V." width="400" /></a>

* [Elbflorace e.V](https://www.elbflorace.de/en/)  

<a href="https://www.elbflorace.de/en/"><img src="https://www.elbflorace.de/wordpress/wp-content/themes/elbflorace/resources/logoBig.png" alt="Elbflorace e.V." width="400" /></a>
* [SCUTRacing](http://www.scutracing.com/)  


<a href="http://www.scutracing.com/"><img src="https://imgur.com/hbAelp9.png" alt="SCUTRacing" width="400" /></a>
* [DHBW Engineering e.V.](https://dhbw-engineering.de/) 

<a href="https://dhbw-engineering.de/"><img src="./img/dhbw_engineering_logo.png" alt="DHBW Engineering e.V." width="400" /></a>

* [StarkStrom Augsburg e.V.](https://starkstrom-augsburg.de/) 

<a href="https://starkstrom-augsburg.de/"><img src="./img/ssa.jpg" alt="StarkStrom Augsburg e.V." width="400" /></a>

* [AMZ Racing](http://amzracing.ch/) 

<a href="http://amzracing.ch/"><img src="./img/amz.png" alt="AMZ Racing" width="400" /></a>

* [ITU Racing](http://racing.itu.edu.tr/) 

<a href="http://racing.itu.edu.tr/"><img src="./img/itu_logo.jpg" alt="ITU Racing" height="150" width="400" /></a>

* [Raceyard](https://www.raceyard.de/) 

<a href="https://www.raceyard.de//"><img src="./img/raceyard_logo.jpg" alt="Raceyard" width="400" /></a>

* [EUFS](https://eufs.eusa.ed.ac.uk/)

<a href="https://eufs.eusa.ed.ac.uk/"><img src="./img/eufs-logo-hor.png" alt="EUFS" width="400"/></a>

*...

## Why?
Open-Source Dataset to accelerate the development of (camera-based) solutions for **Object Detection** in the context of the Formula Student Driverless competitions.
Collecting raw data and annotating it accordingly is important, but is not feesible to be done well enough by one team within the time constraints of the competition.
