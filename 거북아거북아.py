import turtle
import random

##2019038042 이도경

def  screenRightClick(x, y):
    global r, g, b, angle, dist
    tSize = random.randrange(1, 5)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color((r, g, b))
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.stamp()
    angle =  random.randrange(0,360)
    turtle.goto(x, y)
    turtle.left(angle)
    
##변수 선언 부분
pSize = 10
r, g, b = 0.0, 0.0, 0.0

##메인 코드 부분
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
