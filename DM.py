import PyPDF2 

def readFile(name):
    reader = PyPDF2.PdfReader(name)
    allStudentData = ""

    for i in range(len(reader.pages)):
        page = reader.pages[i]
        allStudentData += page.extract_text()
    return allStudentData


def dataFilter(allStudentData):
    allStudentData = splitStringByLines(allStudentData)
    allStudentData=removeSpaceByString(allStudentData)
    allStudentData = stripingString(allStudentData)
    return allStudentData


def splitStringByLines(allStudentData):
    allStudentData = allStudentData.split(' ------------------------------------------------------------------------------------------------------------------------------------')
    newList = []
    for i in allStudentData:
        if 'PUNE' not in i:
            newList.append(i)

    allStudentData = newList
    newList2 = []
    for i in newList:
        if 'NAME' in i: 
            newList2.append(i.split(' ----  -------------------------------------------------- -------------------- ---   ---------- --- --- -----------------------------')[1])
        else: 
            newList2.append(i)
    return newList2[:len(newList2)-1]


def removeSpaceByString(allStudentData):
    newList = []
    for i in allStudentData:
        demo = i.split()
        for j in demo:
            j.strip()
        newList.append(demo)
    return newList


def stripingString(allStudentData):
    for i in range(len(allStudentData)):
        for j in range(len(allStudentData[i])):
            allStudentData[i][j] = allStudentData[i][j].strip('*:!$#')
            
    newList = []
    for i in allStudentData:
        demoList = []
        for j in i: 
            if j==" " or j=="" or j=="  ":
                pass
            else: 
                demoList.append(j)
        newList.append(demoList)
    return newList



def allStudentDataYearWise(allStudentData):
    i=0
    student = allStudentData[0]
    while len(student[i])>1 or not(student[i].isnumeric()):
        i+=1
    semester = int(student[i])
    allStudentDataYearWiseList = []
    studentList = []
    for student in allStudentData:
        i=0
        while len(student[i])>1 or not(student[i].isnumeric()):
            i+=1
        sem = int(student[i])
        if sem == semester: 
            studentList.append(student)
        else: 
            allStudentDataYearWiseList.append(studentList)
            studentList = []
            studentList.append(student)
            semester = sem
    allStudentDataYearWiseList.append(studentList)
    return allStudentDataYearWiseList


def splitByStar(allStudentData):
    for i in range(len(allStudentData)):
        for j in range(len(allStudentData[i])): 
            if '*' in allStudentData[i][j]: 
                l = allStudentData[i][j].split('*')
                allStudentData[i][j]=l[0]
                allStudentData[i].insert((j+1),l[1])
            elif '$' in allStudentData[i][j]:
                l = allStudentData[i][j].split('$')
                allStudentData[i][j]=l[0]
                allStudentData[i].insert((j+1),l[1])
    return allStudentData