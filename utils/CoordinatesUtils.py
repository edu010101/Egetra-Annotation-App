import numpy as np

def CalculateDistanceBetween2Points(Point1, Point2):
    Point1 = np.array((Point1[0], Point1[1]))
    Point2 = np.array((Point2[0], Point2[1]))
    return np.linalg.norm(Point1-Point2)

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