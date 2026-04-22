from customtkinter import *
from tkinter import messagebox

set_appearance_mode("light")
set_default_color_theme("blue")

win = CTk()
win.geometry("340x380")
win.title("kilogram")

tittle_label = CTkLabel(win, text = "Login", font = CTkFont(size = 22, weight = "bold"))
tittle_label.pack(pady = (40,20))

login_entry = CTkEntry(win, placeholder_text = "name", width = 240, height = 35)
login_entry.pack(pady = 10)


host_entry = CTkEntry(win, placeholder_text = "host", width = 240, height = 35)
host_entry.pack(pady = 10)


port_entry = CTkEntry(win, placeholder_text = "port", width = 240, height = 35)
port_entry.pack(pady = 10)

def register():
	name = login_entry.get().strip()
	host = host_entry.get().strip()
	port = port_entry.get().strip()
	if not name and not host and not port:
		messagebox.showwarning("error", "enter something in the fields provided")
		return
	if not name or not host or not port:
		messagebox.showwarning("error", "make sure you filled in all the fields")
		return
	messagebox.showinfo("w","logged in")

register_btn = CTkButton(win, text = "register", command = register, width = 180, height = 35)
register_btn.pack(pady=(20,10))

win.mainloop()