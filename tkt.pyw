import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile, asksaveasfile
from PIL import Image, ImageTk
import pytesseract
import os

#full user path
userPath = os.getcwd()
#local tesseract path
pytesseract.pytesseract.tesseract_cmd =  userPath + r'\Tesseract-Ocr\tesseract.exe'

text = 'None'
op:Label

window = Tk()

def open_file(): 
    file = askopenfile(mode ='r', filetypes =[('image_formats', '.png')]) 
    if file is not None: 
        path = file.name
        img = Image.open(path)
        output = convertToString(img)
        printLabel(output)

def convertToString(img):
    try:
        return pytesseract.image_to_string(image=img, lang='eng')
    except Exception as e:
        printError()

def printError():
    labelError = Label(text='An error occured while converting your file. Please check if executable file and tesseract-ocr is installed in the same directory.')

def printLabel(output):
    global op
    if len(str(output)) <= 275:
        op = Label(window, text=str(output))
    else:
        op = Label(window, text=f'{str(output)[0:275]}... Save to get full output')

    global text
    
    text = str(output)
    op.pack()
    
def save():
    if text != 'None':
        files = [('Text Document', '*.txt')] 
        file = asksaveasfile(filetypes = files, defaultextension = files)
        file.write(text)

def reset():
    op.destroy()

btnChoose = Button(window, text ='Choose file', command = lambda:open_file()) 
btnSave = Button(window, text ='Save output', command = lambda:save()) 
btnChoose.pack(side = TOP, pady = 10) 
btnReset = Button(window, text='Reset', command =lambda:reset())
btnSave.pack()
btnReset.pack(side = TOP, pady = 10)
window.geometry("500x350+700+400")
window.title('Optical Character Recognition')
window.mainloop()

