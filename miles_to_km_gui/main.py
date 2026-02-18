from tkinter import *

window = Tk()
window.title("Mile To Km Converter")
window.minsize(width=75,height=100)
window.config(padx=50,pady=50)

input = Entry(width=10)
input.grid(column=1,row=2)
Miles = Label(text="Miles", font=("Arial",12,""))
Miles.grid(column=2,row=2)


km = 0
km_covert = Label(text=km, font=("Arial",12,""))
km_covert.config(padx=50,pady=10)
km_covert.grid(column=1,row=4)
equal = Label(text="is equal to", font=("Arial",12,""))
equal.grid(column=0,row=4)
km_label = Label(text="Km", font=("Arial",12,""))
km_label.grid(column=2,row=4)


def calc_miles_to_km():
    
    km_covert.config(text=float(input.get()) * 1.609344, font=("Arial",12,""))

  
calc = Button(text="Calculate", command= calc_miles_to_km)
calc.grid(column=1,row=5)
window.mainloop()