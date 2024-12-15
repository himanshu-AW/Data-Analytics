from random import randint
from tkinter import *

root = Tk()
root.title("Random color generator")
root.geometry("400x400")
root.minsize(400, 400)

def random_color():
    # Ensure the first character of the hex code is not '0'
    ran_num = randint(0x100000, 0xFFFFFF)
    hex_code = "#{:06x}".format(ran_num)
    e1.delete(0, END)
    e1.insert(END, hex_code)
    root.config(bg=hex_code)
    b1.config(fg=hex_code)

e1 = Entry(root, font=("Arial", 20), bg="lightgrey", bd=8, width=8)
e1.place(relx=0.5, rely=0.46, anchor=CENTER)
b1 = Button(root, text="Generate new!", font=("Arial", 13, "bold"), padx=4, pady=4, command=random_color)
b1.place(relx=0.5, rely=0.58, anchor=CENTER)

root.mainloop()
