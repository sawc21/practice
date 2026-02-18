from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height = 300)
window.config(padx=100,pady=200)

#label

my_label = Label(text="I am a label", font=("Times New Roman",24,""))


my_label["text"] = "New Text"
my_label.grid(column=0,row=0)
my_label.config(text="New Text")


#button
def button_clicked():
    my_label.config(text=input.get())

button = Button(text="Click Me",command=button_clicked )
button.grid(column=1,row=1)

button = Button(text="New Button",command=button_clicked)
button.grid(column=2,row=0)



#Entry
input = Entry(width=10)
input.grid(column=3,row=2)





window.mainloop()