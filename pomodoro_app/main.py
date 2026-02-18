from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
#fg is color to foreground
text = "✔"
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=PINK)

canvas= Canvas(width=200,height=224,bg=PINK,highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas.create_text(100,130,text="00:00",fill="White",font=(FONT_NAME,35,"bold"))
canvas.grid(column=3,row=3)

timer= Label(text="Timer", font=(FONT_NAME,35,""),bg= PINK, fg=GREEN , highlightthickness=0)
timer.grid(column=  3,row=1)



window.mainloop()