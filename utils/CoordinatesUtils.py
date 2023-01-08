import numpy as np
import mysql
from mysql.connector import Error


import time

class CoordinatesManager():
    def __init__(self, RoadName, Direction):
        self.StartCoordinatesDatabaseConnection()
        self.RoadName = RoadName
        self.Direction = Direction

    def FindClosestPoint(self, Point, Radius=0.03):
        ClosestPoint = None
        ClosestRoadMeter = None
        Distance = 9999999

        MaxLatValue = str(Point[0] + Radius)
        MinLatValue = str(Point[0] - Radius)
        MaxLongValue = str(Point[1] + Radius)
        MinLongValue = str(Point[1] - Radius)

        QueryString="SELECT * FROM Coordinate WHERE road= '"+self.RoadName+"' and direction='"+self.Direction+"' and latitude<"+MaxLatValue+" and latitude>"+MinLatValue+" and longitude<"+MaxLongValue+" and longitude>"+MinLongValue+";"
        #print(QueryString)

        
        QueryResults = self.SearchQuery(QueryString)
        
        #print(len(QueryResults))

        for PointTuple in QueryResults:
            PointCoordinates = [PointTuple[3], PointTuple[4]]
            CurrentDistance = self.CalculateDistanceBetween2Points(PointCoordinates, Point)
            
            if CurrentDistance < Distance:
                Distance = CurrentDistance
                ClosestPoint = PointCoordinates
                ClosestRoadMeter = PointTuple[2]
                

        return ClosestPoint, ClosestRoadMeter
    
    def CalculateDistanceBetween2Points(self, Point1, Point2):
        Point1 = np.array((Point1[0], Point1[1]))
        Point2 = np.array((Point2[0], Point2[1]))
        return np.linalg.norm(Point1-Point2)

    def SearchQuery(self, query):
        QueryResult = None
        try:
            self.Cursor.execute(query)
            QueryResult = self.Cursor.fetchall()
            return QueryResult

        except Error as err:
            print(f"Error: '{err}'")
    
    def StartCoordinatesDatabaseConnection(self):
        #Connection = create_db_connection("localhost", "root", "xxx", 'Coordinates')
        self.Connection = None
        try:
            self.Connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="xxx",
                database='Coordinates'
            )
            print("MySQL Database connection successful")
        except Error as err:
            print(f"Error: '{err}'")
        self.Cursor = self.Connection.cursor()


# q1 = """SELECT * FROM Coordinate WHERE road= 'MS-112' and direction='C' and latitude<-20.225501351999995 and latitude>-20.245501351999998 and longitude<-51.816022511999996 and longitude>-51.83602251199999;
# """
# x = CoordinatesManager('MS-112', 'C')
# start = time.time()
# results = x.SearchQuery(q1)        
# end = time.time()
# print(end - start)
# #connection = create_db_connection("localhost", "root", 'xxx', 'Coordinates')
