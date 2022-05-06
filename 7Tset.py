a1='Open sourece is source code that is made freely available for possible modification and redistribution'
a2='Code is released under the terms of a software license'
b1=''
b2=''

count=0
for i in range(0,len(a1)):
    b1[i]=a1[len(a1)-count]
    count+=1
print(b1)
