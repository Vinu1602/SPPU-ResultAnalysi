import tkinter as tk
from tkinter import filedialog
import allTransactions as at
import jsonOperations as json
from GetSubjectsName import resource_path

def mainFrontEnd():
    root = tk.Tk()
    root.title('Result Analysis')
    try:
        a = resource_path('sppu.ico')
        root.iconbitmap(a)
    except: 
        pass
    root.geometry('500x500')

    def upload_file():
        file_path = filedialog.askopenfilename(title="Select a PDF File", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            # Assuming at.generateExcel is defined somewhere in your code
            at.generateExcel(file_path)
            # print(file_path)

    def clearSubjects():
        # Assuming json.clearSubjects is defined somewhere in your code
        json.clearSubjects()
        message_label.config(text='Subjects Cleared')

    # Assuming 'ResultAnalysis.png' is a valid image path
    image_path = resource_path('ResultAnalysis.png')
    image = tk.PhotoImage(file=image_path)

    image_label = tk.Label(root, image=image)
    image_label.pack(pady=20)

    upload_button = tk.Button(root, text='Upload File', command=upload_file,font=('Georgia', 16))
    upload_button.pack(pady=20)

    clear_button = tk.Button(root, text='Clear Subjects', command=clearSubjects, font=('Georgia', 16))
    clear_button.pack(padx=20)

    message_label = tk.Label(root, text='', font=('Georgia', 16))
    message_label.pack(pady=20)

    root.mainloop()

# Example usage:
mainFrontEnd()