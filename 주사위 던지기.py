##2019038042 이도경
import random

count = 0
count2 = 0
dice_sum = 0

while True:
    dice1=random.randrange(1, 6)
    dice2=random.randrange(1, 6)
    dice3=random.randrange(1, 6)
    dice4=random.randrange(1, 6)
    dice5=random.randrange(1, 6)
    dice6=random.randrange(1, 6)

    dice_sum=dice1+dice2+dice3+dice4+dice5+dice6

    if(dice1==dice2==dice3==dice4==dice5==dice6):
        print("6개의 주사위가 모두 동일한 숫자가 나옴-->",dice1,dice2,dice3,dice4,dice5,dice6)
        print("6개가 동일한 숫자가 나올 때까지 주사위를 던진 횟수-->",count2)
        print("6개가 동일한 숫자가 나올 때까지, 1~6의 연속번호가 나온 횟수-->",count)
        break

    elif(dice_sum==21 and dice1!=dice2!=dice3!=dice4!=dice5!=dice6):##연속으로 나온경우
        count += 1

    else:##주사위 던진 횟수
        count2 += 1







