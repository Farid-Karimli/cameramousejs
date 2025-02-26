# draws the imaginary box used for scaling over the camera feed
from videoProcessing.config.config import *
from videoProcessing.trackerState import trackerState

def drawScalingBox(cvObject, frame):
    templateMatchBoxLength = 11
    boundingBox = getBoundingCoordinatesOfScalingBox()
    # 2 is the width of the boxes (template matching box, scaling box) drawn
    startX = int(boundingBox["x"][0] * trackerState.FRAME_WIDTH) - 4
    endX = int(boundingBox["x"][1] * trackerState.FRAME_WIDTH) + templateMatchBoxLength + 4
    startY = int(boundingBox["y"][0] * trackerState.FRAME_HEIGHT) - 4 
    endY = int(boundingBox["y"][1] * trackerState.FRAME_HEIGHT) + templateMatchBoxLength + 4
    cvObject.rectangle(frame, (startX, startY), (endX, endY),
				(0, 255, 0 ), 2)
  
  
"""
returns  {x:[start,end] , y:[start,end] } 
if scaleFactorX = 1, returns {x:[0,1] , y:[0,1] } 
""" 
def getBoundingCoordinatesOfScalingBox():
    xBand = (0.5 * (1 / trackerState.scaleFactorX)) 
    yBand = (0.5 * (1 / trackerState.scaleFactorY)) 
    startX = 0.5 - xBand 
    endX = 0.5 +  xBand 
    startY = 0.5 - yBand
    endY = 0.5 +  yBand
    boundingBox = {"x":[startX,endX] , "y":[startY,endY] }
    return boundingBox
