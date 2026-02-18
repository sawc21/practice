
#########improvements#######
# 1) animate words
# 2) make words fit correctly
# 3) add 3 strikes and your out
# 4) add a time option
# 5) add a click instead of type option
#6) add a main menu to choose a timer or if you want to guess with clicking or typing
#7) on click add if you make it green
###########################



import turtle
import tkinter
import pandas
t = turtle.Turtle()
screen = turtle.Screen()
screen.title("U.S States Quiz")
image = "blank_states_img.gif"
screen.addshape("broken_heart.gif")
screen.addshape(image)
turtle.shape(image)




data = pandas.read_csv("50_states.csv")
states = data.state.values


running = True
def on_close():
    global running
    running = False
    try:
        screen.bye()
    except:
        pass

screen._root.protocol("WM_DELETE_WINDOW", on_close)

lives = 3
correct_guess = 0
correct_guesses = []
x_cor = 0
y_cor = 0


def create_heart_from_image(image_path):
    """
    Creates and returns a turtle using a GIF image.
    image_path must be a .gif file.
    """
    screen = turtle.Screen()

    # Register the image as a shape (only needs to happen once)
    if image_path not in screen.getshapes():
        screen.addshape(image_path)

    t = turtle.Turtle()
    t.shape(image_path)
    t.penup()
    t.speed(0)

    return t


def add_lives(lives, start_x, y=-300, spacing=40):
    hearts = []

    for i in range(lives):
        h = create_heart_from_image("heart.gif")
        h.goto(start_x + i * spacing, y)
        hearts.append(h)

    return hearts

def break_heart(hearts):
    if hearts:
        hearts[lives].shape("broken_heart.gif")


def write_states (text, x,y, font_size = 16, font_type = "Arial", align = "center"):
    t.penup()
    t.goto(x,y)
    t.write(text, align = align, font = (font_type, font_size, "normal"))
    t.pendown()

def numbered_list(items,words_per_line=10):
    numbered_text = " ".join(f"{i}.{str(items)}" for i,items in enumerate(items,start = 1))

    words = numbered_text.split()

    lines = [
         "     ".join(words [i:i + words_per_line]) 
         for i in range(0,len(words),words_per_line)    
            ]
    return "\n\n".join(lines)
states_list = numbered_list(states)    
write_states(states_list,-350,250,font_size=8, align= "left")


hearts = add_lives(lives,start_x= 200)
try:
    
    while running and correct_guess < 50 and lives > 0:
        answer_state = screen.textinput(
            title=f"{correct_guess}/50 States Correct",
            prompt="Whats another state's name?"
        )
        answer_state = answer_state.strip().title()
        if not running or answer_state == "Exit":
            incorrect_guesses = [state for state in states if state not in correct_guesses]
            new_data = pandas.DataFrame(incorrect_guesses)
            new_data.to_csv("states_not_guessed.csv")
            break
        if answer_state in states:
            correct_guess += 1
            correct_guesses.append(answer_state)
            # correct_state1 = data.state == answer_state
            # print(correct_state1)
            
            correct_state = data[data.state == answer_state]
            print(correct_state)
            x_cor = int(correct_state["x"].iloc[0])
            y_cor = int(correct_state["y"].iloc[0])
            print(x_cor)
            write_states(answer_state, x_cor, y_cor, font_size=8, align= "left")
        else:
            
            lives -= 1
            
            break_heart(hearts)
            
           

except (turtle.Terminator, tkinter.TclError):
    pass













