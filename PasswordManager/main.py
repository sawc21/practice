from tkinter import *



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Managera")
window.config(padx=20,pady=20)
canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")

canvas.create_image(100,112,image=logo)
canvas.grid(column=1,row=0)

window.mainloop()