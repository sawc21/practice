from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")





class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.dictionary = {}
        self.name = ""
        self.hs = 0

        self.goto(0, 265)
        self.hideturtle()
        self.penup()
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def add_dict(self):

     self.name = input("Enter Name:")
     self.hs = self.score


    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f"GAME OVER score is {self.score}:", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)





