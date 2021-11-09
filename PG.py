from tkinter import *
from tkinter import messagebox
import pyperclip
import random


#frame
window = Tk()
window.title("Password Generator")
window.geometry("500x300")

my_password = ""

def password():
	global my_password
	
	password_length = int(box.get())


	letters_lower = 'abcdefghijklmnopqrstuwxyz'
	letters_upper = 'ABCDEFGHIJKLMNOPQRSTUWXYZ'
	numbers = '1234567890'
	signs = '!@#$%^&*()_-+=|<>;:'

	my_password = ""

	for i in range(password_length):
		my_password += (random.choice(letters_lower + letters_upper + numbers + signs))
	
	box.insert(0, my_password)
	box.delete(password_length)

def copy_password():
	global my_password
	pyperclip.copy(my_password)
	messagebox.showinfo(" ", "Password has been copied.")
	

#Label frame
Lframe = LabelFrame(window, text = "How many characters do you want?")
Lframe.pack(pady = 20)


#Box asking how many characters 
box = Entry(Lframe, font = ("Helvetica", 24))
box.pack(pady = 20, padx = 20)


#Button frame
Bf = Frame(window)
Bf.pack(pady = 20)

#Button generating password
B = Button(Bf, text = "Generate password", command = password)
B.grid(row = 0, column = 0, padx = 10)

#Copy button
Cb = Button(Bf, text = "Copy password", command = copy_password)
Cb.grid(row = 0, column = 1, padx = 10)




window.mainloop()