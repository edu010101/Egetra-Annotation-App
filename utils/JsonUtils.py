import json

def SaveJson(Dict, Path):
    with open(Path, 'w') as JsonPath:
        json.dump(Dict, JsonPath)

def LoadJson(JsonPath):
    with open(JsonPath, 'r') as JsonFile:    
        JsonData = json.load(JsonFile)
    return JsonData