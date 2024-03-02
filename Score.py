from turtle import Turtle


class ScoreB(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.goto(0, 280)
        self.score = -1
        self.hideturtle()

    def set_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"{self.score}", align="center", move=False, font=('Courier', 16, 'normal'))

    def game_over(self):
        self.write("Game over", align="center", move = False, font=('Courier', 16, 'normal'))