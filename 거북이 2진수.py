import turtle

##2019038042 이도경

num =int(input("값 입력 : "))
n = bin(num)    ##2진수로 변경
a = len(n)      ##2진수의 길이구하기

turtle.shape('turtle')
turtle.setheading(90)
##왜 if문이 작동을 안하는건가:1이 숫자1이 아니라 문자열이네
for i in range(2, a) :##0b제외
    if(n[i]=='1'):
        turtle.fillcolor('red') ##빨간거북이
        turtle.shapesize(2) ##거북이 크기 2
        turtle.penup()  ##움직이면서 선안그려지게
        turtle.stamp()  ##움직인위치에 도장찍기
        turtle.goto(i*20,0) ##움직여
        
    elif(n[i]=='0'):
        turtle.fillcolor('blue')
        turtle.shapesize(1)
        turtle.penup()
        turtle.stamp()
        turtle.goto(i*20,0)

turtle.done()