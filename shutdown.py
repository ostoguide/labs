import platform
from tkinter import *
import os
check = 0


def os_check():
	global check
	system = platform.system()
	if 'Linux' in system:
		linux_function()
	elif 'Windows' in system:
		windows_function()


def windows_function():
	if check == 1:
		os.system("shutdown /p")
	elif check == 2:
		os.system("shutdown /r")
	elif check == 3:
		os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
	elif check == 4:
		os.system("shutdown /l")


def linux_function():
	global check
	if check == 1:
		os.system("systemctl poweroff")
	elif check == 2:
		os.system("systemctl reboot")
	elif check == 3:
		os.system("systemctl suspend")
	elif check == 4:
		# os.system("logout")
		print("")

# this is the function called when the button is clicked
def btnShutdownFunction():
	global check
	check = 1
	os_check()


# this is the function called when the button is clicked
def btnSleepFunction():
	global check
	check = 3
	os_check()


# this is the function called when the button is clicked
def btnRestartFunction():
	global check
	check = 2
	return os_check()


def btnLogOutFunction():
	global check
	check = 4
	os_check()


root = Tk()

# This is the section of code which creates the main window
root.geometry('314x152')
root.configure(background='#00008B')
root.title('Shutdown prog')


# This is the section of code which creates a button
Button(root, text='Shut Down', bg='#A9A9A9', font=('arial', 13, 'normal'), command=btnShutdownFunction).place(x=4, y=10)


# This is the section of code which creates a button
Button(root, text='Sleep', bg='#A9A9A9', font=('arial', 13, 'normal'), command=btnSleepFunction).place(x=130, y=10)


# This is the section of code which creates a button
Button(root, text='Restart', bg='#A9A9A9', font=('arial', 13, 'normal'), command=btnRestartFunction).place(x=210, y=10)


# This is the section of code which creates a button
Button(root, width="27", text='Log Out', bg='#A9A9A9', font=('arial', 13, 'normal'), command=btnLogOutFunction).place(x=8, y=59)


# This is the section of code which creates a button
Button(root, text='Exit', bg='#A9A9A9', font=('arial', 13, 'normal'), command=root.destroy).place(x=250, y=107)

root.mainloop()
