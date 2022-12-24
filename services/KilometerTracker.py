import numpy as np
import os, sys
import json


# TxtFile = '/home/edu0101/Desktop/Egetra-Annotation-App/MS-112_Eixo_LatLong_10-10m.txt'

# with open(TxtFile, 'r') as f:    
#     Json = json.load(f)


def CalculateDistanceBetween2Points(pt_1, pt_2):
    pt_1 = np.array((pt_1[0], pt_1[1]))
    pt_2 = np.array((pt_2[0], pt_2[1]))
    return np.linalg.norm(pt_1-pt_2)

def FindClosestPoint(Point, PointsDict):
    ClosestPoint = None
    ClosesPointKey = None
    Distance = 9999999

    MaxLatValue = Point[0] + 0.04
    MinLatValue = Point[0] - 0.04
    MaxLongValue = Point[1] + 0.04
    MinLongValue = Point[1] - 0.04

    for PointKey in PointsDict:
        DictPoint = PointsDict[PointKey]
        if  MinLatValue < DictPoint[0] < MaxLatValue and MinLongValue < DictPoint[1] < MaxLongValue:
            if CalculateDistanceBetween2Points(DictPoint, Point) <= Distance:
                Distance = CalculateDistanceBetween2Points(DictPoint, Point)
                ClosestPoint = DictPoint
                ClosesPointKey = PointKey

    return ClosestPoint, ClosesPointKey







# #115340,-19.72691,-51.904905
# x, Id = FindClosestPoint([-20.026288, -52.372851], Json)         
# print(Id, x)








def SaveJson(Dict, Path):
    with open(Path, 'w') as JsonPath:
        json.dump(Dict, JsonPath)

def LoadJson(JsonPath):
    with open(JsonPath, 'r') as JsonFile:    
        JsonData = json.load(JsonFile)
    return JsonData


# CoordinatesDict = {'MS-112': {}}
# RoadDict = CoordinatesDict['MS-112']
# with open(TxtFile, 'r' ) as f:
#     for el in f.readlines():
#         Km, Lat, Long = el[:-1].split(',')
#         RoadDict[Km] = [float(Lat),float(Long)]
# with open('/home/edu0101/Desktop/Egetra-Annotation-App/CoordinatesDatabase/CorrdinatesDict.json', 'w') as f:
#     json.dump(CoordinatesDict, f)

BigJson = {}
for Json in os.listdir('/mnt/0391adf6-7049-4029-ac48-e8003b7d3456/Downloads/MS-112_C_01_R0.mp4'):
    JsonData =LoadJson(os.path.join('/mnt/0391adf6-7049-4029-ac48-e8003b7d3456/Downloads/MS-112_C_01_R0.mp4', Json))
    BigJson['Json'] = JsonData

SaveJson(BigJson, 'Big112c01.json')