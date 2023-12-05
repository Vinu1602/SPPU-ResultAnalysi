import pandas as pd
from tkinter import filedialog
import GetSubjectsName as gsn
import matplotlib.pyplot as plt 

def makeDictionary(student):
    newStudent = dict()
    for field in student: 
        if len(field)==6:
            sub = field[0]
            newStudent[sub+'Int']=field[1]
            newStudent[sub+'Ext'] = field[2]
            newStudent[sub+'total'] = field[3]
            newStudent[sub+'Grade'] = field[4]
            newStudent[sub+'Credits'] = field[5]
        elif(len(field)==5):
            sub = field[0]
            newStudent[sub+'Int']=field[1]
            newStudent[sub+'total'] = field[2]
            newStudent[sub+'Grade'] = field[3]
            newStudent[sub+'Credits'] = field[4]
        else: 
            newStudent[field[0]] = field[1]
    return newStudent

def makeDataFrame(allStudents):
    df = pd.DataFrame(allStudents[0], index=[1])
    for i in allStudents[1:]:
        new_row=pd.DataFrame(i, index=[0])
        df = pd.concat([df, new_row], ignore_index=True)
    df.set_index("rollno", inplace=True)
    return df   


def findAllToppers(allStudents):
    dataFrameElements = []
    dataFramesList = []
    if 'CGPA' in allStudents:
        colName = "CGPA"
        cgpaToppers = pd.DataFrame()
        allStudents[colName] = allStudents[colName].astype('float')
        toppers = pd.concat([allStudents.nlargest(10, colName)['name'],allStudents.nlargest(10, colName)[colName]], axis=1, join='inner')
        toppers.rename(columns={colName : 'Marks'}, inplace=True)
        dataFrameElements.append(colName)
        dataFramesList.append(toppers)

    semesterWise = pd.DataFrame()
    for colName in allStudents:
        if ('Sem' in colName) and len(colName)==4: 
            allStudents[colName] = allStudents[colName].astype('float')
            toppers = pd.concat([allStudents.nlargest(10, colName)['name'], allStudents.nlargest(10, colName)[colName]], axis=1, join='inner')
            toppers.rename(columns={colName : 'Marks'}, inplace=True)
            dataFrameElements.append(colName)
            dataFramesList.append(toppers)
    semesterWise = pd.concat(dataFramesList, keys=dataFrameElements)
    return semesterWise

def subjectToppers(allStudentsData):
    subjectAvailable = []
    subjectDFAvailable = []
    for colName in allStudentsData: 
        if colName[-5:]=="total":
            allStudentsData[colName] = allStudentsData[colName].replace('AB', '-1')
            allStudentsData[colName] = allStudentsData[colName].astype('float')
            subjectTop = pd.concat(
                [
                    allStudentsData[allStudentsData[colName]==max(allStudentsData[colName])]['name'],
                    allStudentsData[allStudentsData[colName]==max(allStudentsData[colName])][colName]
                ],
                axis=1, join='inner'
            )
            subjectTop.rename(columns={colName:'Marks'}, inplace=True)
            subjectAvailable.append(colName[:-5])
            subjectDFAvailable.append(subjectTop)
    
    subjectDFAvailable = pd.concat(subjectDFAvailable, keys=subjectAvailable)
    return subjectDFAvailable 

def subjectWiseCount(allStudentData):
    demoDict = dict()
    allFields = {
        0:'Marks 40 To 49',
        1:'Marks 50 To 54',
        2:'Marks 55 To 59',
        3:'Marks 60 To 65',
        4:'greater Than 66',
        5:'Fail Count',
        6:'Pass Count',
        7:'Failure Percent',
        8:'Passing Percent'
    }
    for colName in allStudentData:
        if colName[-5:]=='total':
            credit = colName[:-5]+'Credits'
            allStudentData[colName] = allStudentData[colName].astype('float')
            totalCount = allStudentData[colName].count()
            bet40to49 = allStudentData[colName][(allStudentData[colName]>=40) & (allStudentData[colName]<=49)].count()
            bet50to54 = allStudentData[colName][(allStudentData[colName]>=50) & (allStudentData[colName]<=54)].count()
            bet55to59 = allStudentData[colName][(allStudentData[colName]>=55) & (allStudentData[colName]<=59)].count()
            bet60to65 = allStudentData[colName][(allStudentData[colName]>=60) & (allStudentData[colName]<=65)].count()
            greaterThan66 = allStudentData[colName][allStudentData[colName]>=66].count()
            failCount = allStudentData[credit][allStudentData[credit]=='FF'].count()
            passCount = totalCount-failCount
            failurePercent = round((failCount*100)/totalCount,4)
            passingPercent = round((passCount*100)/totalCount,4)
            
            subjectWiseCount=[bet40to49, bet50to54, bet55to59, bet60to65, greaterThan66, failCount, passCount, failurePercent, passingPercent]
            demoDict[colName[:-5]] = subjectWiseCount
    countPassed = pd.DataFrame(demoDict)
    countPassed = countPassed.rename(index=allFields)
    return countPassed

def failStudents(allStudentsData):
    failStudents=allStudentsData[allStudentsData['Sem1']==0]['name']
    failStudentsName = pd.DataFrame(failStudents)
    return failStudentsName


def mainAnalysis(allStudentData):
    studentList = []
    studentList.append(allStudentData)
    studentList.append(findAllToppers(allStudentData))
    studentList.append(subjectToppers(allStudentData))
    studentList.append(subjectWiseCount(allStudentData))
    studentList.append(failStudents(allStudentData))
    studentList.append(getSubjectWiseStudentFail(allStudentData))
    return studentList


def semWiseStudents(allStudents):
    studentsBySemester = []
    for i in allStudents: 
        studentsBySemester.append(mainAnalysis(i))
    return studentsBySemester

def doAllAnalysis(allStudent):
    demoStudent = []
    for i in allStudent:
        newList = []
        for j in i: 
            newList.append(makeDictionary(j))
        demoStudent.append(newList)
    
    allStudentData = []
    for i in demoStudent:
        allStudentData.append(makeDataFrame(i))
    return semWiseStudents(allStudentData)


def getSubjectWiseStudentFail(allStudent):
    failedStudents = allStudent[allStudent['Sem1']==0]
    rollNo = []
    name = []
    backSub=[]
    for index,df in failedStudents.iterrows():
        rollNo.append(index)
        name.append(df['name'])
        failSubList=[]
        for k in df.items():
            if k[0][-5:]=='Grade' and k[1]=='F':
                failSubList.append(k[0][:-5])
        backSub.append(failSubList)
    fail = pd.DataFrame({
        'name':name,
        'Back_Subjects':backSub
    }, index=rollNo)
    return fail

def writeExcelFile(newList):
    # Ask the user to select a folder to save the Excel files
    folder_path = filedialog.askdirectory(title="Select Folder to Save Excel Files")

    # If the user cancels the folder selection, return without saving
    if not folder_path:
        return

    for year in newList: 
        fileName = gsn.getFileName()
        excel_file_path = f"{folder_path}/{fileName}.xlsx"

        with pd.ExcelWriter(excel_file_path) as writer: 
            year[0].to_excel(writer, sheet_name="All Student List")
            year[1].to_excel(writer, sheet_name='Toppers')
            year[2].to_excel(writer, sheet_name='Subject Toppers')
            year[3].to_excel(writer, sheet_name='SubjectWiseCount')
            year[4].to_excel(writer, sheet_name='Failed Students')
            year[5].to_excel(writer, sheet_name='Subject Wise Fail')