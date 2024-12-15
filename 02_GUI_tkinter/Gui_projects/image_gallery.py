import os
from tkinter import *
from PIL import Image, ImageTk

# Define the directory path where the images are stored
img_dir = r'C:\\Users\\himan\\OneDrive\\Desktop\\Data Analitics\\02_GUI_tkinter\\Image'

# List all files in the directory
all_items = os.listdir(img_dir)

# Filter images from all files
images = [file for file in all_items if file.endswith(('.jpg', '.png', '.jpeg', '.gif'))]

root = Tk()
root.title("Image gallery")
root.geometry("400x500")

Label(root, text="Image Gallery", font=("Arial", 12)).pack(anchor='center')

# Create a frame to hold the canvas and scrollbar
frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

# Create a canvas for scrolling
canvas = Canvas(frame)
canvas.pack(side=LEFT, fill=BOTH, expand=True)

# Add a vertical scrollbar
scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configure the canvas to work with the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create another frame inside the canvas to hold the images
inner_frame = Frame(canvas)
canvas.create_window((0, 0), window=inner_frame, anchor="nw")

# Store references to PhotoImage objects to prevent garbage collection
photo_images = []

# Add images to the inner frame
for img in images:
    # Construct the full path to the image
    img_path = os.path.join(img_dir, img)

    # Open the image and convert it to a PhotoImage
    image = Image.open(img_path)
    image = image.resize((200, 150))  # Resize for uniformity
    photo = ImageTk.PhotoImage(image)

    # Store the PhotoImage object
    photo_images.append(photo)

    # Create a label widget for each image
    label = Label(inner_frame, image=photo)
    label.pack(pady=10)  # Add some spacing between images

root.mainloop()
