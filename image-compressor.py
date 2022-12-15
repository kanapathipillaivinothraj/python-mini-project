import PIL
from PIL import Image
from tkinter.filedialog import *


file_path = askopenfilename()

img =  Image.open(file_path)
height ,width = img.size


img = img.resize((height,width), Image.ANTIALIAS)

save_path = asksaveasfilename()

img.save(save_path+ ".PNG")