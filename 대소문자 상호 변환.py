Mj=input("문자열을 입력하세요:")
check=Mj
Mj2=[]
for i in range(0,len(check)):
    if check[i].isupper()==True:
        Mj2[i]=check[i].lower()

    elif check[i].isupper()==False:
        Mj2[i]=check[i].upper()

print(Mj2)