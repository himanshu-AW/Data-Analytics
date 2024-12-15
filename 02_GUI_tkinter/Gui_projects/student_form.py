from tkinter import *
from tkcalendar import Calendar


# adding more features like student address by using Text,Highest-degree by menu(select opetion one), adding Links, uploading photos/signature, adding seperator-line by using canvas


root = Tk()
root.title("Registration form")
root.geometry("400x500")

# get the selected date when the user close the calender window
def get_selected_date(event):
    global cal,date_window
    date_window = Toplevel()
    date_window.grab_set()
    date_window.title("Choose Date of Birth")
    date_window.geometry("250x220+100+100")
    cal = Calendar(date_window, selectmode='day', date_pattern="mm/dd/yyyy")
    cal.place(x=0,y=0)

    submit_btn = Button(date_window,text="Submit DOB",command=grab_date)
    submit_btn.place(x=80,y=190)

def grab_date():
    dob_entry.delete(0,END)
    dob_entry.insert(END, cal.get_date())
    date_window.destroy()
    dob_entry.config(fg="#222")


# Create a frame for the registration form
frame = Frame(root)
frame.pack(padx=20,pady=20)

# creating variables for the registration form
name_var = StringVar()
dob_var = StringVar()
email_var = StringVar()
mobileNo_var = StringVar()
gender_var = StringVar(value="None")
pass_var = StringVar()
terms_var = BooleanVar()

# Headings for registration
Label(frame, text="Registration Form", font=("Helvetica", 14,"bold")).grid(row=0,columnspan=2,pady=(0,20),padx=20)

# Create labels and entry for name
Label(frame, text="Full name : ",font=("Helvetica", 10,"bold")).grid(row=1,column=0)
name_entry = Entry(frame,font=("Helvetica", 10),fg="#222",textvariable=name_var)
name_entry.grid(row=1, column=1,padx=10,pady=4)

# create labels and entry for Date of Birth
Label(frame, text="Date of Birth : ",font=("Helvetica", 10,"bold")).grid(row=2,column=0)
dob_entry = Entry(frame,font=("Arial", 10),fg="#777",textvariable=dob_var)
dob_entry.grid(row=2, column=1,padx=10,pady=4)
dob_entry.insert(0,"DD/MM/YYYY")
dob_entry.bind("<1>",get_selected_date)

# Create labels and radio buttons for gender selection
Label(frame, text="Gender :",font=("Helvetica", 10,"bold")).grid(row=3,column=0)
gender_frame = Frame(frame)
gender_frame.grid(row=3,column=1,padx=10,pady=4)
# Adding gender radiobutton options
gender_options = ["Male", "Female", "Other"]
for opt in gender_options:
    rb = Radiobutton(gender_frame,text=opt,font=("Helvetica", 10),variable=gender_var,value=opt)
    rb.pack(side=LEFT)

# Create labels and entry for email
Label(frame, text="E-mail : ",font=("Helvetica", 10,"bold")).grid(row=4,column=0)
email_entry = Entry(frame,font=("Helvetica", 10),fg="#222",textvariable=email_var)
email_entry.grid(row=4, column=1,padx=10,pady=4)

# Create labels and entry for mobile number
Label(frame, text="Mobile No. : ",font=("Helvetica", 10,"bold")).grid(row=5,column=0)
mobileNo_entry = Entry(frame,font=("Helvetica", 10),fg="#222",textvariable=mobileNo_var)
mobileNo_entry.grid(row=5, column=1,padx=10,pady=4)

# Create labels and entry for password
Label(frame, text="Password : ",font=("Helvetica", 10,"bold")).grid(row=6,column=0)
pass_entry = Entry(frame,font=("Helvetica", 10,"bold"),fg="#222", show="*",textvariable=pass_var)
pass_entry.grid(row=6, column=1,padx=10,pady=4)

# Create checkboxes for terms and conditions
terms_check = Checkbutton(frame, text="I agree with the terms and conditions", font=("Arial", 10), variable=terms_var)
terms_check.grid(row=7, columnspan=2, pady=5)

# Create submit button
submit_btn = Button(frame, text="Submit", font=("Helvetica", 10,"bold"),padx=10,pady=5)
submit_btn.grid(row=8, column=0, pady=10)

# Create reset button
reset_btn = Button(frame, text="Reset", font=("Helvetica", 10,"bold"),padx=10,pady=5)
reset_btn.grid(row=8, column=1, pady=10)


root.mainloop()
