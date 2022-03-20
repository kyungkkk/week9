##2019038042 이도경
import turtle

##변수
swidth, sheight = 800, 500  ##너비,높이

i, k, tX, tY = [0] * 4

turtle.title('거북이구구단')
turtle.shape('turtle')  ##거북이모양
turtle.setup(width = swidth + 100, height = sheight + 100)  ##창크기
turtle.screensize(swidth, sheight)##거북이의 활동반경
turtle.penup()##움직이며 흔적남기지않게
tX, tY = -500, 250  ##
turtle.goto(tX, tY)

for i in range(1, 10) :
    for k in range(2, 10) :
        turtle.goto(tX + 90 * k, tY - 40 * i)   ##거북이가 지나가며 구구단을 그려야하니 tx,ty로부터 움직이게 만들기
        gugudan = str(k) + ' X ' + str(i) + ' = ' + str(k*i)    ##거북이가 그릴 구구단 변수
        turtle.write(gugudan, font = ('Arial', 12, 'bold')) ##gugudan을 그리며 font를 글꼴은 Arial, 크기 20, bold(궁서체)로 하겠다.

turtle.done() ##할일 다했다 가서 쉬어.