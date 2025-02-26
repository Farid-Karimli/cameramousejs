#Record tracking state 
from collections import deque
from videoProcessing.config import config

class TrackerState:
    def __init__(self):
        self.totalReq = 0
        self.trackedReq = 0
        self.trackedProb = 0
        self.trackedPositions = deque() # tracks past N positions to help determine jover to click gesture
        self.scaleFactorX = config.SCALE_FACTOR_X
        self.scaleFactorY = config.SCALE_FACTOR_Y
        self.FRAME_WIDTH = 300
        self.FRAME_HEIGHT = 168

    def updateTracked(confidence):
        trackedReq += 1
        trackedProb += confidence
        
    def addTrackedPosition(self, position):
        if len(self.trackedPositions) >  config.HOVER_TO_CLICK_MIN_POINTS:
            self.trackedPositions.popleft()
        self.trackedPositions.append(position)

    def setScaleFactorValues(self, newScaleFactorXValue, newScaleFactorYValue):
        self.scaleFactorX = newScaleFactorXValue
        self.scaleFactorY = newScaleFactorYValue

    def setWebcamFrameSize(self, width, height):
        self.FRAME_WIDTH = width
        self.FRAME_HEIGHT = height



trackerState = TrackerState()