import mysql.connector
from mysql.connector import Error
import JsonUtils

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection


CoordinatesDict = JsonUtils.LoadJson('/home/eduardo/Desktop/Egetra-Annotation-App/CoordinatesDatabase/CorrdinatesDict.json')
Road = 'MS-112'
for Key, Content in CoordinatesDict[Road].items():
    Direction = 'C'
    Meter = str(Key)
    Latitude = str(Content[0])
    Longitude= str(Content[1])
    QueryString = "INSERT INTO Coordinate VALUES ('"+ Road +"', '"+Direction+"', "+Meter+", "+Latitude+", "+Longitude+");"
    connection = create_db_connection("localhost", "root", "xxx", 'Coordinates')
    execute_query(connection, QueryString)
    #print(QueryString)