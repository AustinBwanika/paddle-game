from turtle import Screen, Turtle


class Background(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.right(90)
        self.outline()

    def outline(self):
        while self.ycor() != -300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
