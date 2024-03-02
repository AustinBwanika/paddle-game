from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
UP = 0
DOWN = 180


class PaddleB(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def move(self):
        if self.ycor() == 280:
            pass
        elif self.ycor() == -280:
            pass

    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)


    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
