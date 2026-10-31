# Import necessary libraries
from tkinter import *
from datetime import date

# Create Window
root= Tk()
root.title("getting started with widgets")
root.geometry('400x300')
lbl= Label(text="Hey There!",fg="white",bg="#072f54", height=2,width=300)
name_lbl= Label(text="full name",bg="#232B5C",fg="#13644B")
name_entry=Entry()

# Function to display a Message
def display():
	# Read input given by user
	name = name_entry.get()
	# Declaring a global variable 
	# to make it accessible anywhere in the program
	global message
	message = "Welcome to the Application! \nToday's date is: "
	greet = "Hello "+name+"\n"
	# Display details in a text box
	# Specify where to add the details inside the text box
	text_box.insert(END, greet)
	text_box.insert(END, message)
	text_box.insert(END, date.today())

# Add a Text Widget to display information/messages
text_box = Text(height=3)

# Add button and give value of command as name of the function
# Press button, display function will be called automatically
btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')

# Organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

# Start the GUI event loop
root.mainloop()