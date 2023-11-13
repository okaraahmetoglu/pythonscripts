#import glob
import sys
from tkinter import filedialog as fd
from fpdf import FPDF #
from PIL import Image
files = fd.askopenfiles()
imagelist = files # glob.glob('img/*.jpg')

pdf = FPDF()
# imagelist is the list with all image filenames
for image in imagelist:
    
    pdf.add_page()
    pdf.image(image.name, 0, 0,210)

pdf.output("yourfile.pdf", "F")