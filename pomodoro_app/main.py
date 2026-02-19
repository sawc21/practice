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
def start_timer(n):
    canvas.itemconfig(timer_text,text=n)
    print(n)
    if n> 0:
        window.after(1000,start_timer, n - 1)
        
def start():
    start_timer(30)
    
def reset():
    canvas.itemconfig(timer_text, text = timer)
    window.after(1000,reset,timer)
   
    
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=PINK)


canvas= Canvas(width=200,height=224,bg=PINK,highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")
timer = 30
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text=timer,fill="White",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)



# timer= Label(text="Timer", font=(FONT_NAME,35,"bold"),bg= PINK, fg=GREEN , highlightthickness=0)
# timer.grid(column=  1,row=0)

start= Button(text="Start", command=start)
start.grid(column=0,row=3)
Reset= Button(text="Reset", command=reset)
Reset.grid(column=2,row=3)

text = Label(text="✔",fg=GREEN,bg=PINK)
text.grid(column=1,row=4)
window.mainloop()