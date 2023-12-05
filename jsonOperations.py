import json
from GetSubjectsName import resource_path

def openFileOperation():
    a = resource_path('subjects.json')
    with open(a, 'r') as file: 
        data = json.load(file)
    return data

def closeFileOperation(data):
    a = resource_path('subjects.json')
    with open(a, 'w') as file: 
        json.dump(data, file, indent=4)

def clearSubjects():
    a = resource_path('subjects.json')
    with open(a, 'w') as file:
        json.dump({}, file)