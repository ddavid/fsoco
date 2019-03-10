# Undistort

remap() and undistort() should be doing exactly the same thing, when getOptimalNewCameraMatrix() is not used.
This is not the case atm.
Although very similar, remap leaves zeroed out pixels at the bottom of the image, while undistort() seems to automagically zoom in to only show "valid" pixels.

Idea to test:
Use validPixROI to perform warpPerspective()
--> Probably the difference in the results
