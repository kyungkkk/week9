a=[9,15,54,369,634,1053,2954,4334,5424,9531]
b=[2,6,6,15,20,34,50,89,123,9999]
c=[0]
d=[0]
count1=0
count2=0
p=0

for i in range(0,10):
    for j in range(2,a[i]+1):
        if(a[i]%j==0 and j!=a[i]):
            c[count1]=j
            count1+=1
    for k in range(2,b[i]+1):
        if(a[i]%k==0):
            d[count2]=k
            count2+=1
    if(c[i]==d[i]):
        p=c[i]
        print[c[i]]


