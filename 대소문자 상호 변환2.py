Mj=input("문자열을 입력하세요:")
check=Mj

for i in range(0,len(check)):
    if check[i].isupper()==True:
        print(check[i].lower())

    elif check[i].isupper()==False:
        print(check[i].upper())

