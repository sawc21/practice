from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_function = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
#fg is color to foreground
        
def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN *60
    if reps % 8 == 0:
        start_timer(long_break_sec)
        timer.config(text="Break",fg=RED) 
    elif reps % 2 == 0:
            start_timer(short_break_sec)
            timer.config(text="Break",fg=RED)           
    else:
         start_timer(work_sec)
         timer.config(text="Work",fg=GREEN)  
      
    
def reset():
    window.after_cancel(timer_function)
    timer.config(text="Pomodoro",fg=GREEN)
    text.config(text="")  
    global reps
    reps = 0
    canvas.itemconfig(timer_text,text=f"25:00")
     

def start_timer(n):
    
    count_min = math.floor(n/60)
    count_sec = n % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"


        
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    
    if n> 0:
       global timer_function
       timer_function = window.after(1000,start_timer, n - 1)
    else:
        start()
        mark  = ""
        work_sessions = math.floor(reps/2)
        for _ in range (work_sessions):
             mark += "✔"
             text.config(text=mark)

    
# def reset():
#     canvas.itemconfig(timer_text, text = timer)
#     window.after(1000,reset,timer)
   
    
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=PINK)


canvas= Canvas(width=200,height=224,bg=PINK,highlightthickness=0)
tomato_img= PhotoImage(file="tomato.png")

canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text='',fill="White",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)



timer= Label(text="Pomodoro", font=(FONT_NAME,35,"bold"),bg= PINK, fg=GREEN , highlightthickness=0)
timer.grid(column=  1,row=0)

begin= Button(text="Start", command=start)
begin.grid(column=0,row=3)
Reset= Button(text="Reset", command=reset)
Reset.grid(column=2,row=3)

text = Label(text="",fg=GREEN,bg=PINK)
text.grid(column=1,row=4)
window.mainloop()