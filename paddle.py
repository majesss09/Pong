from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1,0)
        self.penup()
        self.goto(coordinates)

    def moveup(self):
        self.goto(self.xcor(),self.ycor()+35)

    def movedown(self):
        self.goto(self.xcor(),self.ycor()-35)
        
    