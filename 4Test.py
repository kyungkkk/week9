k=0
count=0
for k in range (2,1001):
    for i in range(1,k+1):
        if(k%i==0):
            count+=1
    if (count==2):
        print(k)
    count=0