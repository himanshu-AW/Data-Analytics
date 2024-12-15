# 1: Tkinter is a kind of python interface to develop graphical user intrface type application.
# 2: It contains various tools to create such type of applications.
# 3: Tkinter is  a standard GUI library for python.
# 4: When we use python and tkinter to develop GUI application it makes the task very easy.
# 5: Tkinter provides a powerful object-oriented interface to the TK GUI kit.
# 6: To use Tkinter, we have to do following steps -
    # i) import tkinter module
    # ii) create an instance of tkinter class
    # iii) create a window with title
    # iv) add 2 or more widgets(controls) to the window.
    # v) Enter the main event loop to tke action against each event triggered by the user.(start the event loop) 

# from tkinter import *
# # instance of Tk class
# root = Tk()
# # add a title
# root.title("Learning tkinter GUI ")
# # Start the event loop
# root.mainloop()


#------------------------- Tkinter Widgets -----------------------
# Button ,Label, Entry, Frame, Menu,Message, Menubutton,Lisbox,checkbutton,Canvas,Radiobutton,Scale,Text, Scrollbar,Toplevel,SpinBox,PanedWindow,LabelFramw,tkMessageBox


# There are some common attributes of all the widgets.
# Dimentions, Colors, Fonts, Anchors, Relief styles, Bitmaps, Cursors

#------------------------ Geometry Management --------------------------
# Geometry management in Tkinter determines how widgets (like Label, Button, Entry, etc.) are arranged within a parent container (like a Frame or Tk window). Tkinter provides three geometry managers:

# pack()
# grid()
# place()
# Each method offers a different level of control over widget placement and layout.

# 1. pack(): Simplicity Over Precision
# The pack() manager arranges widgets in a block-like structure (top-down, bottom-up, left-right). It's the simplest geometry manager but offers less precise control compared to grid() and place().

# Key Options:
# side: Specifies which side of the parent widget to attach (top, bottom, left, right).
# fill: Specifies whether the widget should expand to fill the allocated space ('x', 'y', 'both', or None).
# expand: Allows widgets to expand beyond their minimum size (boolean).
# padx, pady: Adds padding around the widget (horizontal and vertical).
# Example:
# from tkinter import *
# root = Tk()
# root.title("Pack Example")
# Button(root, text="Top" ).pack(side="top", fill="x")
# Button(root, text="Bottom",bg="gray").pack(side="bottom", fill="x")
# Button(root, text="Left",bg="lime").pack(side="left", fill="y")
# Button(root, text="Right",bg="yellow").pack(side="right", fill="y")
# root.mainloop()


# 2. grid(): Precise Placement Using Rows and Columns
# The grid() manager arranges widgets in a table-like structure with rows and columns. It is ideal for more complex layouts.

# Key Options:
# row and column: Specify the widget's position in the grid.
# sticky: Aligns the widget within its cell ('n', 's', 'e', 'w', or combinations like 'ne' for top-right).
# padx, pady: Adds padding inside the grid cell.
# rowspan and columnspan: Specify how many rows/columns the widget should span.
# Example:
# from tkinter import *
# root = Tk()
# root.title("Grid Example")
# Label(root,text="Row 0, Column 0").grid(row=0,column=0,padx=5,pady=5)
# Label(root,text="Row 0, Column 1").grid(row=0,column=1,padx=5,pady=5)
# Label(root,text="Row 1, Column 0").grid(row=1,column=0,padx=5,pady=5)
# Label(root,text="Row 1, Column 1").grid(row=1,column=1,padx=5,pady=5)
# root.mainloop()

# 3. place(): Absolute Positioning
# The place() manager positions widgets at specific coordinates, giving the most control but requiring manual adjustments.

# Key Options:
# x and y: Specify the absolute position of the widget in pixels.
# relx and rely: Specify the relative position (as a fraction of the parent widget's size).
# anchor: Specifies which part of the widget to align at ('n', 's', 'e', 'w', 'center', etc.).
# Example:
# from tkinter import *
# root = Tk()
# root.geometry("300x200")
# Button(root,text="Button 1").place(x=50,y=50)
# Button(root,text="Button 2").place(relx=0.5,rely=0.5,anchor="center")
# Button(root,text="Button 3").place(relx=1,rely=1,anchor="se")
# root.mainloop()
# Choosing a Geometry Manager
# Use pack() for simple, linear layouts.
# Use grid() for tabular or structured layouts.
# Use place() when absolute positioning is required.
# You can also combine these geometry managers in a single application, but only within separate containers (e.g., different Frame widgets).