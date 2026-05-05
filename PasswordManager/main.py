from tkinter import *
import pandas
from tkinter import messagebox
import pyperclip


final_password= ''

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)

    password = ""
    password = [char for char in password_list]
    final_password = "".join(password)
    password_text.insert(0,final_password)
    pyperclip.copy(final_password)

    
        
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    new_row = {
        "Website": website_text.get(),
        "Email": email_text.get(),
        "Password": password_text.get(),
    }
    
    
    
    if len(new_row["Email"]) == 0 or len(new_row["Password"]) == 0 or len(new_row["Website"]) == 0:
        messagebox.showinfo(title="error", message= "No input in either email,website, or password. \nPlease fill out all before clicking ok")
    else:
        is_ok = messagebox.askokcancel(title=website_text.get(), message=f"Confirm these are the details entered \n Email: {new_row["Email"]} \n Password: {new_row["Password"]}\n Website: {new_row["Website"]} ")
        if is_ok:
            pandas.DataFrame([new_row]).to_csv(
                "passwords.csv",
                mode="a",
                header=not pandas.io.common.file_exists("passwords.csv"),
                index=False
            )
  
            
    
    

    website_text.delete(0, END)
    password_text.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Managera")
window.config(padx=20,pady=20)


canvas = Canvas(width=200,height=200)
logo = PhotoImage(file="logo.png")

canvas.create_image(100,100,image=logo)
canvas.grid(column=1,row=0)

website = Label(text="Website: ")
website.grid(column=0,row=1)
website_text = Entry(width=35)
website_text.grid(column=1,row=1,columnspan=2)
website_text.focus()


email = Label(text="Email/Username: ")
email.grid(column=0,row=2)
email_text = Entry(width=35)
email_text.grid(column=1,row=2,columnspan=2)
email_text.insert(END,"sawyer.cawthon@gmail.com")




password = Label(text="Password: ")
password.grid(column=0,row=3)
password_text = Entry(width=21)
password_text.grid(column=1,row=3)
password_button = Button(text="Generate Password",command=generate_password)

password_button.grid(column=2,row=3)


add_button = Button(text="Add",command=save_password,width=36)
add_button.grid(column=1,row=4,columnspan=2)



window.mainloop()