import numpy as np
import os, sys
import json

def CalculateDistanceBetween2Points(pt_1, pt_2):
    pt_1 = np.array((pt_1[0], pt_1[1]))
    pt_2 = np.array((pt_2[0], pt_2[1]))
    return np.linalg.norm(pt_1-pt_2)

def FindClosestPoint(Point, PointsDict, Radius=0.04):
    ClosestPoint = None
    ClosestPointKey = None
    Distance = 9999999

    MaxLatValue = Point[0] + Radius
    MinLatValue = Point[0] - Radius
    MaxLongValue = Point[1] + Radius
    MinLongValue = Point[1] - Radius

    for PointKey in PointsDict:
        DictPoint = PointsDict[PointKey]
        
        if  MinLatValue < DictPoint[0] < MaxLatValue and MinLongValue < DictPoint[1] < MaxLongValue:
            if CalculateDistanceBetween2Points(DictPoint, Point) <= Distance:
                Distance = CalculateDistanceBetween2Points(DictPoint, Point)
                ClosestPoint = DictPoint
                ClosestPointKey = PointKey

    return ClosestPoint, ClosestPointKey