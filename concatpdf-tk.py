#import glob
import sys
import tkinter as tk
from tkinter import filedialog as fd

from fpdf import FPDF #
from PIL import Image

files = []

def openFileDialog():
    files =  fd.askopenfiles()
    imagelist = files # glob.glob('img/*.jpg')
    fileIndis = 0
    
    for image in imagelist:
        fileIndis = fileIndis + 1
        listFiles.insert(fileIndis,image.name )
    # do something

def createPdf():
    pdf = FPDF() # imagelist is the list with all image filenames
    listItems = listFiles.get(0,tk.END)
    for imageFileName in reversed(listItems):
        pdf.add_page()
        pdf.image(imageFileName, 0, 0,210)
    pdf.output("yourfile.pdf", "F")

def move_up(self, pos):
    """ Moves the item at position pos up by one """

    if pos == 0:
        return

    text = self.listFiles.get(pos)
    self.listFiles.delete(pos)
    self.listFiles.insert(pos-1, text)


root = tk.Tk()


buttonSelectFile = tk.Button(
    text="Select Files",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command= openFileDialog
)

buttonCombinePdf = tk.Button(
    text="Combine Pdf",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command= createPdf
)
buttonSelectFile.pack()
buttonCombinePdf.pack()
buttonSelectFile.place(x=0, y=0)
buttonCombinePdf.place(x=300, y=0)




listFiles = tk.Listbox( width=400)
listFiles.pack()
listFiles.place(x=0, y=100)

listFiles.bind('<ButtonPress>', lambda e: "break")
def AfterReleaseSelect(event):
    event.widget.selection_clear(0,tk.END)
    event.widget.selection_set(event.widget.nearest(event.y))
    #more stuffs here if needed...
listFiles.bind('<ButtonRelease>', AfterReleaseSelect)
root.mainloop()

