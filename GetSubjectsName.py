import tkinter as tk
import os 
import sys

def resource_path(relative_path):
    try: 
        base_path = sys._MEIPASS
    except Exception: 
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def getSubjectName(subjectCode):
    subjectCodeRoot = tk.Tk()
    subjectCodeRoot.title('Enter Subject Name')
    try:
        a = resource_path('sppu.ico')
        subjectCodeRoot.iconbitmap(a)
    except: 
        pass
    subjectCodeRoot.geometry('500x500')
    
    global subName
    subName = ""

    def submitSubject():
        demo = subjectCodeEntry.get().strip()
        if len(demo) == 0:
            pass
        else: 
            global subName 
            subName = demo
            subjectCodeRoot.destroy()
    
    subjectCodeLabel = tk.Label(subjectCodeRoot, text=subjectCode, font=('Georgia', 16))
    subjectCodeEntry = tk.Entry(subjectCodeRoot, font=('Georgia', 16))
    subjectCodeButton = tk.Button(subjectCodeRoot, text='Submit', command=submitSubject, font=('Georgia', 16))
    
    subjectCodeLabel.pack(pady=20)
    subjectCodeEntry.pack(pady=20)
    subjectCodeButton.pack(pady=20)
    
    subjectCodeRoot.mainloop()
    
    return subName

def getFileName():
    fileNameRoot = tk.Tk()
    fileNameRoot.title('File Name')
    try:
        fileNameRoot.iconbitmap(r'/sppu.ico')
    except: 
        pass
    fileNameRoot.geometry('500x500')
    
    global finalName
    finalName = ""
    
    def submitFileName():
        fileName = fileText.get().strip()
        if len(fileName) == 0:
            pass
        else: 
            global finalName
            finalName = fileName
            fileNameRoot.destroy()
                
    myLabel = tk.Label(fileNameRoot, text='Enter the File Name', font=('Georgia', 16))
    fileText = tk.Entry(fileNameRoot, font=('Georgia', 16))
    fileSubmit = tk.Button(fileNameRoot, text='Submit', command=submitFileName, font=('Georgia', 16))

    myLabel.pack(pady=20)
    fileText.pack(pady=20)
    fileSubmit.pack(pady=20)
    
    fileNameRoot.mainloop()
    return finalName