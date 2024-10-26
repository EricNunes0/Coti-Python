import random
from turtle import *

class Draw:
    def __init__(self, turtle):
        self.turtle = turtle
        self.x = 0
        self.y = 0
        self.angle = 90

        self.turtle.screen.title('Desenho')
        self.turtle.screen.bgcolor("#000")
        self.turtle.color("#FFF")

        self.items = []

        self.spawnKnife(random.randint(0, 5) * 20, random.randint(0, 5) * 20)

        listen()
        onkey(self.moveUp, "Up")
        onkey(self.moveDown, "Down")
        onkey(self.moveLeft, "Left")
        onkey(self.moveRight, "Right")
        mainloop()

    # 0
    def moveUp(self):
        if self.angle == 0:
            self.turtle.left(0)
        elif self.angle == 90:
            self.turtle.left(90)
        elif self.angle == 180:
            self.turtle.left(180)
        elif self.angle == 270:
            self.turtle.left(-90)
        self.setAngle(0)
        self.y += 20
        self.moveForward()

    # 90
    def moveRight(self):
        if self.angle == 0:
            self.turtle.left(-90)
        elif self.angle == 90:
            self.turtle.left(0)
        elif self.angle == 180:
            self.turtle.left(90)
        elif self.angle == 270:
            self.turtle.left(-180)
        self.setAngle(90)
        self.x += 20
        self.moveForward()

    # 180
    def moveDown(self):
        if self.angle == 0:
            self.turtle.left(180)
        elif self.angle == 90:
            self.turtle.left(-90)
        elif self.angle == 180:
            self.turtle.left(0)
        elif self.angle == 270:
            self.turtle.left(90)
        self.setAngle(180)
        self.y -= 20
        self.moveForward()

    # 270
    def moveLeft(self):
        if self.angle == 0:
            self.turtle.left(90)
        elif self.angle == 90:
            self.turtle.left(180)
        elif self.angle == 180:
            self.turtle.left(-90)
        elif self.angle == 270:
            self.turtle.left(0)
        self.setAngle(270)
        self.x -= 20
        self.moveForward()

    def moveForward(self):
        self.turtle.forward(20)
        self.checkCollision()

    def setAngle(self, newAngle):
        #print(self.angle, " -> ", newAngle)
        self.angle = newAngle

    def checkCollision(self):
        playerX = self.x
        playerY = self.y
        for item in self.items:
            print(item['x'], item['y'], "\n", playerX, playerY)
            if item['x'] == playerX and item['y'] == playerY:
                if item['type'] == 0: # Adaga
                    self.turtle.color("#F60")

    def spawnKnife(self, x=0, y=0):
        knifeTurtle = Turtle()
        knifeTurtle.color("#F60")
        knifeTurtle.goto(x, y)
        knifeTurtle.clear()
        self.items.append({
            "type": 0,
            "x": x,
            "y": y
        })

    def changeColor(self, color):
        self.turtle.color(color)

if __name__ == '__main__':
    Draw(Turtle())
    pass