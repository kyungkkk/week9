#if문에서 n을 확인
#n이 =0인지 확인
#0이 아니면 n/k(2,8,16)을 리턴하고 나머지는 저장
#0이면 다나눴다는 의미이므로 저장해놨던 나머지를 역순출력

two_dater=[]


def two_jinsu(n1):
    if n1//2==0:
        return str(n1%2)
    return two_jinsu(n1//2)+str(n1%2)
        
def eight_jinsu(n1):
    if n1//8==0:
        return str(n1%8)
    return two_jinsu(n1//8)+str(n1%8)

def sixteen_jinsu(n1):
    if n1//16==0:
        return str(n1%16)
    return two_jinsu(n1//16)+str(n1%16)

if __name__=="__main__":
    n=int(input("변환할 10진수 입력"))
    print("0b",two_jinsu(n))
    print("0o",eight_jinsu(n))
    print("0x",sixteen_jinsu(n))
    print(bin(n))
    print(oct(n))
    print(hex(n))

