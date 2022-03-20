##2019038042 이도경

a,b,HeartNum=0,0,0
NumStr,ch,HeartStr="","",""

NumStr=input("숫자를 여러개 입력하세요:")
print("")

a=0
ch=NumStr[a]    ##문자열로 변경해서 입력받은 숫자를 쪼개기

while True:
    HeartNum=int(ch)    ##a번째 자리의 숫자
    HeartStr="" ##하트를 넣을 변수

    for b in range(0,HeartNum):
        HeartStr += "\u2665"    ##HeartNum의 숫자만큼 하트를 넣어줌
        b+=1
    print(HeartStr)

    a+=1##무한루프를 막기위한 조건식을 위한 변수

    if(a>len(NumStr)-1):    ##a가 입력받은숫자의 자릿자릿수보다 커지면 무한루프 탈출
        break;

    ch=NumStr[a]    ##첫째자리의 하트를 출력하고 다음자리로 넘어가기




