##2019038042 이도경
import turtle as t
import math
import random

##**변수**##
t1, t2, t3 = [None] * 3 ##거북이 세마리 초기화
t1X, t1Y, t2X, t2Y, t3X, t3Y = [0] * 6  ##거북이의 x축y축 
swidth, sheight = 200, 200
size = 3
#**메인 디쉬** ##

t.title('거북이 만나기')##제목
t.setup(width=swidth+200,height=sheight+200)    ##시작할 때 창크기
t.screensize(swidth,sheight)   ##자꾸 집나가는 거북이한테 가로,세로 200크기만큼만 활동범위를 제한.

##거북이 세마리를 색깔로 구분하고 똑같은속도로 움직이며 지나가며 흔적을 남기지않게
t1 = t.Turtle('turtle'); t1.color('red'); t1.speed(10); t1.penup();
t2 = t.Turtle('turtle'); t2.color('green'); t2.speed(10); t2.penup();
t3 = t.Turtle('turtle'); t3.color('blue'); t3.speed(10); t3.penup();
t1.turtlesize(size); t2.turtlesize(size); t3.turtlesize(size)
 
t1.goto(-100, -100); t2.goto(0, 0); t3.goto(100, 100) ##다른지점에서 시작해 시작부터 만나지않게
 
while True:
        ##거북이 세마리가 각각 독립적으로 방향을잡고 움직이는
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t1.left(angle); t1.forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t2.left(angle); t2.forward(dist)
        angle = random.randrange(0, 360)
        dist = random.randrange(1, 50)
        t3.left(angle); t3.forward(dist)
 
        ## xcor() : 거북이의 현재 x좌표 반환, ycor() : 거북이의 현재 y좌표 반환

        t1X = t1.xcor(); t1Y = t1.ycor()
        t2X = t2.xcor(); t2Y = t2.ycor()
        t3X = t3.xcor(); t3Y = t3.ycor()

## 거북이가 만난다-->두거북이의 중심축 x,y의거리가 30이하면 만나는걸로 정의하겠다.

##중학교 수학식:두 거북이의 거리-->(x2 -x1)의 제곱 + (y2-y1)의 제곱으로 계산

        if math.sqrt(((t1X - t2X) * (t1X - t2X)) + ((t1Y - t2Y) * (t1Y - t2Y))) <= 30 or math.sqrt(((t1X - t3X) * (t1X - t3X)) + ((t1Y - t3Y) * (t1Y - t3Y))) <= 30 or math.sqrt(((t2X - t3X) * (t2X - t3X)) + ((t2Y - t3Y) * (t2Y - t3Y))) <= 30 :
                t1.turtlesize(size*3); t2.turtlesize(size*3); t3.turtlesize(size*3)
                t.done()