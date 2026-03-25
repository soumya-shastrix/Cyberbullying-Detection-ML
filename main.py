from tkinter import *
from tkinter import messagebox


from PIL import ImageTk, Image
import sqlite3
import os
root = Tk()
root.geometry('1366x768')
root.title("Cyber")

canv = Canvas(root, width=1366, height=768, bg='white')
canv.grid(row=2, column=3)
img = Image.open('back.png')
photo = ImageTk.PhotoImage(img)
canv.create_image(1,1, anchor=NW, image=photo)
def readdataset():
    os.system('python dataset.py')
def preprocessing():
    os.system('python preprocessing.py')

def det():
        os.system('streamlit run+'
                  '* stream.py')
def clf():
        os.system('python model.py')
Button(root, text='Data Collection', width=20,height=2, bg='red', fg='white',  font=("bold", 12),command=readdataset).place(x=900, y=200)
Button(root, text='Data Preprocessing', width=20,height=2, bg='red', fg='white',  font=("bold", 12),command=preprocessing).place(x=900, y=250)
Button(root, text='Classification', width=20, height=2,bg='red', fg='white',  font=("bold", 12),command=clf).place(x=900, y=300)

Button(root, text='Streamlit Detection', height=2,width=20, bg='red', fg='white',command=det,  font=("bold", 12)).place(x=900, y=350)

root.mainloop()
    