import os
from tkinter import *
import tkinter.ttk as ttk
import csv
root = Tk()
root.title("Cyber")
width = 1366
height = 768
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
label_0 = Label(root, text="CyberBullying", width=15, font=("bold", 10))
label_0.place(x=1, y=5)

TableMargin = Frame(root, width=0)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)

tree = ttk.Treeview(TableMargin, columns=("tweet_text"), height=400,
                    selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('tweet_text', text="tweet_text", anchor=W)




tree.column('#0', stretch=NO, minwidth=0, width=100)


tree.pack()

with open('cyberbullying_tweets.csv' ,encoding="utf8") as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        a1 = row['tweet_text']


        tree.insert("", 0, values=(a1,))


root.mainloop()
