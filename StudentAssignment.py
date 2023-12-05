import GetSubjectsName as fe


#get CGPA from student 
def getCGPA(student):
    if 'CGPA' in student: 
        return student[student.index('CGPA')+1]
    return 0

def getSGPA(student, sem):
    semesterMarks = []
    if 'SGPA' in student: 
        index = student.index('SGPA')+2
        i = 0
        while i<sem: 
            semesterMarks.append(['Sem'+str(i+1),student[index][0:5]])
            i+=1
            index+=1
        try:
            semesterMarks.append(['TotalCredit',student[student.index('CREDITS')+1]])
            semesterMarks.append(['GradePoints',student[student.index('POINTS')+1]])
        except: 
            semesterMarks.append(['TotalCredit',0])
            semesterMarks.append(['GradePoints',0])
    else: 
        i=0
        while i<sem: 
            semesterMarks.append(['Sem'+str(i+1),0])
            i+=1
        semesterMarks.append(['TotalCredit',0])
        semesterMarks.append(['GradePoints',0])
    return semesterMarks

def ifIsSubject(value):
    if ((len(value)==5 or len(value)==6) and value.isnumeric()) or (len(value)==7 and value[0:6].isnumeric()):
        return True
    return False

def getLastSubject(subjects):
    for i in subjects: 
        if ((len(i)==5 or len(i)==6) and i.isnumeric()) or (len(i)==7 and i[0:6].isnumeric()):
            lastSubject = i
    return lastSubject

def getSubjectsViseMarks(subjectMarks, lastSubject):
    i=0
    newList = []
    while(subjectMarks[i]!=lastSubject):
        subjectList = []
        while not(ifIsSubject(subjectMarks[i+1])):
            if len(subjectMarks[i])==7:
                subjectList.append(subjectMarks[i][:6])
            else:
                subjectList.append(subjectMarks[i])
            i+=1
        subjectList.append(subjectMarks[i])
        i+=1
        newList.append(subjectList)
    if (subjectMarks[i+1].isnumeric() or subjectMarks[i+1]=='AB') and subjectMarks[i+2].isnumeric():
        subjectList=[]
        subjectList.append(subjectMarks[i])
        subjectList.append(subjectMarks[i+1])
        subjectList.append(subjectMarks[i+2])
        subjectList.append(subjectMarks[i+3])
        subjectList.append(subjectMarks[i+4])
        newList.append(subjectList)
    return newList

def removeGradeSubject(subjectList):
    newList=[]
    for i in subjectList: 
        if 'GRADE' in i: 
            pass
        else: 
            newList.append(i)
    return newList

def assignSubjectsNames(subjectList, subjects):
    for i in subjectList:
        sub = i[0]
        try: 
            i[0] = subjects[i[0]]
        except: 
            subName = fe.getSubjectName("Enter the SubName for "+i[0])
            subjects[i[0]] = subName
            i[0] = subName
    return [subjectList, subjects]



def assign(student, subjects):
    newStudent = []
    #in new List student name, rollno, mothername, gender, PRN and semester is added 
    newStudent.append(['rollno', student[0]])
    name = ['name']
    nameIndex = 1
    n = ""
    while(len(student[nameIndex])!=1 or  not(student[nameIndex]=='M' or student[nameIndex]=='F')): 
        nameIndex = nameIndex+1
        if not(student[nameIndex-2].isnumeric()):
            n = n + " " +student[nameIndex-2]
    name.append(n)
    newStudent.append(name)
    newStudent.append(['Mother_Name', student[nameIndex-1]])
    newStudent.append(['Gender', student[nameIndex]])
    newStudent.append(['PRN', student[nameIndex+1]])
    newStudent.append(['Semester', int(student[nameIndex+2])])
    newStudent.append(['CGPA',getCGPA(student)])
    l = getSGPA(student,int(student[nameIndex+2]))
    for i in l: 
        newStudent.append(i)
    while not(ifIsSubject(student[nameIndex])):
        nameIndex+=1
    lastSubject = getLastSubject(student[nameIndex:])
    marksVise = getSubjectsViseMarks(student[nameIndex:], lastSubject)

    marksVise = removeGradeSubject(marksVise)

    marksVise = assignSubjectsNames(marksVise, subjects)
    subjects = marksVise[-1]
    marksVise = marksVise[0]
    for i in marksVise: 
        newStudent.append(i)
    return [newStudent, subjects]