import numpy as np
import os, sys
import json

def CalculateDistanceBetween2Points(pt_1, pt_2):
    pt_1 = np.array((pt_1[0], pt_1[1]))
    pt_2 = np.array((pt_2[0], pt_2[1]))
    return np.linalg.norm(pt_1-pt_2)

def FindClosestPoint(Point, PointsDict, Radius=0.04):
    ClosestPoint = None
    ClosesPointKey = None
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
                ClosesPointKey = PointKey

    return ClosestPoint, ClosesPointKey

def SaveJson(Dict, Path):
    with open(Path, 'w') as JsonPath:
        json.dump(Dict, JsonPath)

def LoadJson(JsonPath):
    with open(JsonPath, 'r') as JsonFile:    
        JsonData = json.load(JsonFile)
    return JsonData


def LabelmeToEgetra(LabelmeDict):
    EgetraDict = {'Latitude': LabelmeDict['latitude'], 'Longitude': LabelmeDict['longitude'], 'Data': LabelmeDict['tempo'], 'Shapes': LabelmeDict['shapes']}    
    return EgetraDict

# CoordinatesDict = {'MS-112': {}}
# RoadDict = CoordinatesDict['MS-112']
# with open(TxtFile, 'r' ) as f:
#     for el in f.readlines():
#         Km, Lat, Long = el[:-1].split(',')
#         RoadDict[Km] = [float(Lat),float(Long)]
# with open('/home/edu0101/Desktop/Egetra-Annotation-App/CoordinatesDatabase/CorrdinatesDict.json', 'w') as f:
#     json.dump(CoordinatesDict, f)

BigJson = {}
for Json in os.listdir('/home/eduardo/labelme/labelme/videos_processados/MS-112_C_01_R0.mp4'):
    JsonData =LoadJson(os.path.join('/home/eduardo/labelme/labelme/videos_processados/MS-112_C_01_R0.mp4', Json))
    JsonData = LabelmeToEgetra(JsonData)
    BigJson[int(Json.split('_')[-2])] = JsonData

SaveJson(BigJson, '/home/eduardo/Downloads/MS-112_C_01_R0.mp4.json')

x = LoadJson('/home/eduardo/Downloads/MS-112_C_01_R0.mp4.json')
print(x['173399'])