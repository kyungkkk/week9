import turtle
import random
import math
from tkinter.simpledialog import*

inStr=''
swidth,sheight=500,500
tX,tY,txtSize=[0]*3
val=0
r=1

turtle.title('거북이 나선형으로 글쓰기')
turtle.shape('turtle')
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()

inStr=askstring('문자열 입력','거북이 쓸 문자열을 입력')

for ch in inStr:
    tX=r*math.cos(math.pi*(val/180))
    tY=r*math.sin(math.pi*(val/180))
    r=random.random();g=random.random();b=random.random()
    txtSize=20

    turtle.goto(tX,tY)

    turtle.pencolor((r,g,b))
    turtle.write(ch,font=('맑은고딕',txtSize,'bold'))
    val+=30
    r+=30

turtle.done()