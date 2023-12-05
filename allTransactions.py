import pandas as pd
import DM as dm
import jsonOperations as json
import StudentAssignment as sa
import Analysis as ana

def generateExcel(path):
    allStudentData = dm.readFile(path)
    allStudentData = dm.dataFilter(allStudentData)
    allStudentData = dm.allStudentDataYearWise(allStudentData)

    for i in range(len(allStudentData)):
        allStudentData[i]=dm.splitByStar(allStudentData[i])

    data = json.openFileOperation()

    for i in range(len(allStudentData)):
        for j in range(len(allStudentData[i])):
            a = sa.assign(allStudentData[i][j], data)
            allStudentData[i][j]=a[0]
            data = a[1]


    allStudentData = ana.doAllAnalysis(allStudentData)
    ana.writeExcelFile(allStudentData)
    json.closeFileOperation(data)