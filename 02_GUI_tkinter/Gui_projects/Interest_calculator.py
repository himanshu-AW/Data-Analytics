from tkinter import *
from PIL import ImageTk,Image

# fun to calculate simple_interest
def calculate_si():
    try:
        principal = float(E1.get())
        rate = float(E3.get())
        time = float(E2.get())
        si = (principal * rate * time) / 100
        # Clear previous result
        result_box.delete(1.0, END) 
        result_box.config(bg="lime",fg="black")
        result_box.insert(END, f"Simple Interest: {si:.2f}")
    except ValueError:
        result_box.delete(1.0, END)
        result_box.config(bg="#fb4f14",fg="white")
        result_box.insert(END, "Invalid Input!...")
   

# fun to calculate compund_interest
def calculate_ci():
    try:
        principal = float(E1.get())
        rate = float(E3.get())
        time = float(E2.get())
        ci = principal * ((1 + rate / 100 ) **  time) - principal
        # Clear previous result
        result_box.delete(1.0, END)  
        result_box.config(bg="lime",fg="black")
        result_box.insert(END, f"Compound Interest: {ci:.2f}")
    except ValueError:
        result_box.delete(1.0, END)
        result_box.config(bg="#fb4f14",fg="white")
        result_box.insert(END, "Invalid Input!...")

# Function to clear all inputs and results
def clear_all():
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    result_box.config(bg="lightgrey",fg="black")
    result_box.delete(1.0, END)

# Main Window
root = Tk()
root.title("Interest Calculator")
root.geometry("520x350")
root.minsize(520,350)
root.maxsize(520,350)

# rootackground image
img = Image.open('C:\\Users\\himan\\OneDrive\\Desktop\\Python\\GUI\\Image\\img.png')
image = ImageTk.PhotoImage(img)
img_container= Label(root, image=image)
img_container.place(x=0,y=0)


# Result box
result_box = Text(root,height=1 ,width=30, font=("aerial", 20), bg="lightgrey",bd=8,pady=5,padx=5)
result_box.grid(row=0, column=0,columnspan=2, padx=20 ,pady=(20,10))

# Entry for Principal Amount
Label(root, text="Principal Amount", font=("aerial", 20, "bold"),bd=4, fg="gray",width=14).grid(row=1, column=0)
E1 = Entry(root, font=("aerial", 20), bg="lightgrey",  bd=6, width=10)
E1.grid(row=1, column=1, pady=4)

# Entry for Time (Years)
Label(root, text="Time (Years) ", font=("aerial", 20, "bold"),bd=4, fg="gray",width=14).grid(row=2, column=0)
E2 = Entry(root, font=("aerial", 20), bg="lightgrey",  bd=6, width=10)
E2.grid(row=2, column=1, pady=4)
# Entry for Rate of Interest
Label(root, text="Rate of Interest", font=("aerial", 20, "bold"),bd=4, fg="gray",width=14).grid(row=3, column=0)
E3 = Entry(root, font=("aerial", 20), bg="lightgrey", bd=6, width=10)
E3.grid(row=3, column=1, pady=(4,20))

# Frames
F1=Frame(root,padx=5,pady=5)
F1.grid(columnspan=3)

# rootuttons for Calculation
Button(F1, text="SI", font=("aerial", 18, "bold"), bg="#4169e1", fg="white",bd=6,width=6,relief="groove", command=calculate_si).grid(row=5, column=0,)
Button(F1, text="Clear", font=("aerial", 18, "bold"), bg="#fb4f14", fg="white",bd=6,width=6,relief="groove", command=clear_all).grid(row=5, column=1,padx=5)
Button(F1, text="CI", font=("aerial", 18, "bold"), bg="#4169e1", fg="white",bd=6,width=6,relief="groove", command=calculate_ci).grid(row=5, column=2,)


root.mainloop()
