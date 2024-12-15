# --------------- Button ------------------
# Buton: A clickable button used to perform an action.

# Attributes:---
# text: The label displayed on the button.
# command: The function to be executed when the button is clicked.
# state: Button state ("normal", "active", "disabled").
# bg/fg: Background and foreground colors.
# font: Font style of the button text.
# relief: Appearance of the button border ("flat", "raised", "sunken", etc.).

# Methods:----
# invoke(): Simulate a button click programmatically.
# config(**kwargs): Update button attributes dynamically.

# Exapmle 1:------
# import tkinter as tk
# def button_action():
#     print("Button clicked!")
# root = tk.Tk()
# button = tk.Button(root, text="Click Me", command=button_action, bg="blue", fg="white")
# button.pack()
# root.mainloop()

# Exapmle 2:-----
# from tkinter import *
# from tkinter import messagebox
# root = Tk()
# def helloCallBack():
#     messagebox.showinfo("Hello Python","Hello World!")
# B1 = Button(root,text="Hello",command=helloCallBack)
# B1.pack()
# root.mainloop()




# --------------- Label ------------------
#Label: A widget used to display text or images.

# Attributes:------
# text: Text displayed on the label.
# image: Image displayed on the label (can be used instead of text).
# bg/fg: Background and foreground colors.
# font: Font style of the label text.
# justify: Text alignment ("left", "right", "center").

# Methods:-------
# config(**kwargs): Update label attributes dynamically.

# Example 1:-----
# import tkinter as tk
# root = tk.Tk()
# label = tk.Label(root, text="Hello, World!", font=("Arial", 16), bg="yellow", fg="black")
# label.pack()
# root.mainloop()

# Example 2:-------
# from tkinter import *
# root = Tk()
# var = StringVar()
# l1 = Label(root,textvariable=var,relief=RAISED)
# var.set("Hey! I'm Karan")
# l1.pack()
# root.mainloop()




# --------------- Entry ------------------
# Entry:  A single-line text box for user input.
# Attributes:------
# textvariable: Links the entry field to a StringVar for real-time updates.
# show: Replaces entered characters with a symbol (e.g., '*' for password fields).
# state: Entry state ("normal", "readonly", "disabled").
# width: Number of characters displayed.

# Methods:----
# get(): Retrieve the current value of the entry.
# insert(index, text): Insert text at the specified index.
# delete(start, end): Delete characters between the specified indices.
# other methos--- delete(), get(), set(),icursor(),index().insert(),etc..

# Exapmle 1:-
# from tkinter import *
# def show_input():
#     print(entry.get())
# root = Tk()
# entry = Entry(root,width=20)
# entry.pack()
# btn = Button(root,text="Submit",command=show_input)
# btn.pack()
# root.mainloop()

# Exapmle 2:-
# from tkinter import *
# root = Tk()
# container = Frame(root)
# container.pack()
# name = Label(container,text="User name: ")
# name.pack(side=LEFT)
# e_name = Entry(container,bd=5)
# e_name.pack(side=LEFT)
# mobile = Label(container,text="Number: ")
# mobile.pack(side=LEFT)
# e_mobile = Entry(container,bd=5)
# e_mobile.pack(side=LEFT)
# root.mainloop()


# ---------------- Frame ------------------------
# Frame: A container used to group widgets together.
# Attributes:-------
# bg: Background color.
# height/width: Dimensions of the frame.
# relief: Border style.

# Methods:---------
# pack(), grid(), place(): Used for positioning the frame.
# config(**kwargs): Update frame attributes dynamically.

# Exapmle 1:-----
# import tkinter as tk
# root = tk.Tk()
# frame = tk.Frame(root,bg="lightblue",width=200,height=100,relief="sunken",borderwidth=2)
# frame.pack_propagate(False)# Prevent auto-resizing
# frame.pack()
# label = tk.Label(frame,text="Inside Frame")
# label.pack()
# root.mainloop()

# Exapmle 2:-----
# from tkinter import *
# root = Tk()
# frame = Frame(root)
# frame.pack()
# down_frame = Frame(root)
# down_frame.pack(side=BOTTOM)
# redBtn = Button(frame,text='Red',fg='red')
# redBtn.pack(side=LEFT)
# greenBtn = Button(frame,text='Green',fg='green')
# greenBtn.pack(side=LEFT)
# blueBtn = Button(frame,text='Blue',fg='blue')
# blueBtn.pack(side=LEFT)
# blackBTn = Button(down_frame,text='Black',fg='black')
# blackBTn.pack(side=BOTTOM)
# root.mainloop()


# --------------------------checkbutton -----------------------
# Checkbutton: A widget representing a checkbox that can be toggled on/off.
# Attributes:------------
# text: Label displayed next to the checkbox.
# variable: Links the checkbox to a BooleanVar or IntVar.
# onvalue/offvalue: Values assigned to the variable when checked/unchecked.
# state: Button state ("normal", "active", "disabled").

# Methods:----------
# select(): Check the box.
# deselect(): Uncheck the box.
# toggle(): Toggle the checkbox state.

# Exapmle 1:----
# import tkinter as tk
# def show_status():
#     print("Checked" if var.get() else "Unchecked")
# root = tk.Tk()
# var = tk.BooleanVar()
# checkbtn = tk.Checkbutton(root,text="Accept terms",variable=var, command=show_status)
# checkbtn.pack()
# root.mainloop()

# Example 2:----
# import tkinter as tk
# def show_selection():
#     print("Option 1:", var1.get(), "| Option 2:", var2.get())
# root = tk.Tk()
# var1 = tk.IntVar()
# var2 = tk.IntVar()
# cb1 = tk.Checkbutton(root, text="Option 1", variable=var1, onvalue=1, offvalue=0, command=show_selection)
# cb2 = tk.Checkbutton(root, text="Option 2", variable=var2, onvalue=1, offvalue=0, command=show_selection)
# cb1.pack()
# cb2.pack()
# root.mainloop()


# --------------------------Listbox------------------------

# A widget for displaying a list of items.

# Attributes:

# height: Number of rows visible.
# selectmode: Selection mode ("single", "browse", "multiple", "extended").
# listvariable: Links the list to a StringVar.
# Methods:

# insert(index, *items): Add items at the specified index.
# delete(start, end): Remove items between the specified indices.
# get(start, end): Retrieve items between the specified indices.
# curselection(): Get the index of the selected item(s).

# Exaple 1:----
# from tkinter import *
# def show_selected():
#     selected = listbox.curselection()
#     for i in selected:
#         print("Item selected:", listbox.get(i))
# root = Tk()
# listbox = Listbox(root,selectmode="multiple")
# listbox.pack()
# for item in ["python","java","c++","js"]:
#     listbox.insert(END,item)
# btn = Button(root,text="show selsction",command=show_selected)
# btn.pack()
# root.mainloop()

# Exapmle 2:----
# from tkinter import *
# def remove_item():
#     selected = listbox.curselection()
#     for i in reversed(selected):
#         listbox.delete(i)

# root = Tk()
# listbox = Listbox(root)
# listbox.pack()

# for item in ["Apple","Banana","Cherry","Date"]:
#     listbox.insert(END, item)

# btn = Button(root, text="Remove selected", command=remove_item)
# btn.pack()
# root.mainloop()


# ------------- Menubutton -------------------
# Menubutton: A button that, when clicked,displays a menu.

# Attributes:----
# text: Text displayed on the button.
# menu: The menu associated with the button.
# bg/fg: Background and foreground colors.
# relief: Button border style.

# Methods:-------
# config(**kwargs): Update menubutton attributes dynamically.

# Example 1: -----
# from tkinter import *
# root = Tk()
# menubtn = Menubutton(root,text="options",relief="raised")
# menu = Menu(menubtn, tearoff=0)
# menu.add_command(label="option 1")
# menu.add_command(label="option 2")
# menu.add_separator()
# menu.add_command(label="Exit",command=root.quit)
# menubtn.pack()
# root.mainloop()

# Exapmle 2: ------
# import tkinter as tk
# def option_selected(option):
#     print(option)

# root = tk.Tk()
# menubutton = tk.Menubutton(root, text="Choose Option", relief="raised")
# menu = tk.Menu(menubutton, tearoff=0)
# menubutton.config(menu=menu)

# for option in ["Option A", "Option B", "Option C"]:
#     menu.add_command(label=option, command=lambda opt=option: option_selected(opt))

# menubutton.pack()
# root.mainloop()


# 8. ------------------------ Menu ---------------------------
# A drop-down list of options or commands.

# Attributes:
# tearoff: Determines whether the menu can be detached.
# activebackground: Background color for the active item.

# Methods:
# add_command(label, command): Add a menu item with a label and action.
# add_separator(): Add a dividing line.
# add_cascade(label, menu): Add a submenu.

#example 1:----
# import tkinter as tk
# def on_menu_click():
#     print("edit menu click.")
# def open_file():
#     print("Open File clicked")

# def save_file():
#     print("Save File clicked")

# root = tk.Tk()
# menubar = tk.Menu(root)
# root.config(menu=menubar)

# file_menu = tk.Menu(menubar, tearoff=0)
# file_menu.add_command(label="Open", command=open_file)
# file_menu.add_command(label="Save", command=save_file)
# file_menu.add_separator()
# file_menu.add_command(label="Exit", command=root.quit)

# edit_menu = tk.Menu(menubar,tearoff=0)
# edit_menu.add_command(label="Copy",command=on_menu_click)
# edit_menu.add_command(label="Cut",command=on_menu_click)
# edit_menu.add_command(label="Paste",command=on_menu_click)
# edit_menu.add_separator()
# edit_menu.add_command(label="Undo",command=on_menu_click)
# edit_menu.add_command(label="Redo",command=on_menu_click)

# menubar.add_cascade(label="File", menu=file_menu)
# menubar.add_cascade(label="Edit",men=edit_menu)

# root.mainloop()



# 9.------------------ Radiobutton -----------------------
# A widget for selecting one option from a group.

# Attributes:------
# text: Label displayed next to the button.
# variable: Links the radiobutton to a StringVar or IntVar.
# value: The value assigned to the variable when selected.
# state: Button state ("normal", "active", "disabled").

# Methods:--------
# select(): Select the radiobutton.

# Example:-------
# import tkinter as tk
# def show_choice():
#     print("Selected radio button:", var.get())
# root = tk.Tk()
# var = tk.StringVar(value="None")
# options = ["Red", "Green", "BLue"]
# for opt in options:
#     rb = tk.Radiobutton(root,text=opt,variable=var,fg=opt,value=opt,command=show_choice)
#     rb.pack()
# root.mainloop()


# 10. --------------------- Text-----------------------
# A multi-line text area for user input or display.

# Attributes:-------
# height/width: Number of rows and columns displayed.
# wrap: Line wrapping style ("char", "word", "none").

# Methods:--------
# get(start, end): Retrieve text between specified indices.
# insert(index, text): Insert text at the specified index.
# delete(start, end): Delete text between specified indices.
# tag_add(name, start, end): Add a tag to a range of text.
# tag_configure(tag, **options): Configure the appearance of tagged text.

# Example:-------
# import tkinter as tk
# def get_text():
#     print(textbox.get("1.0", tk.END))
# root = tk.Tk()
# textbox = tk.Text(root, height=5, width=30)
# textbox.pack()
# button = tk.Button(root, text="Get Text", command=get_text)
# button.pack()
# root.mainloop()

# Example:--------
# import tkinter as tk
# def count_words():
#     content = textbox.get("1.0", tk.END)
#     word_count = len(content.split())
#     word_count_label.config(text=f"Word Count: {word_count}")

# root = tk.Tk()
# textbox = tk.Text(root, wrap="word", height=5, width=30)
# textbox.pack()

# word_count_label = tk.Label(root, text="Word Count: 0")
# word_count_label.pack()

# button = tk.Button(root, text="Count Words", command=count_words)
# button.pack()
# root.mainloop()


# 11. -------------- Spinbox --------------------
# A widget for selecting a value from a range.

# Attributes:-------
# from_/to: Start and end values.
# increment: Step size for value changes.
# textvariable: Links the Spinbox to a StringVar or IntVar.
# state: Spinbox state ("normal", "readonly", "disabled").

# Methods:-----------
# get(): Retrieve the current value.
# set(value): Set the Spinbox to a specific value.

# Example:-------
# import tkinter as tk
# def show_spinbox_value():
#     print("Selected Value:", spinbox.get())
# root = tk.Tk()
# spinbox = tk.Spinbox(root, from_=1, to=100, increment=5, width=10)
# spinbox.pack(pady=5)
# button = tk.Button(root, text="Show Value", command=show_spinbox_value)
# button.pack(pady=5)
# root.mainloop()

