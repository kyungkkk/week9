inFp=None
inList,inStr=[],""

inFp=open("data1.txt","r")

inList=inFp.readlines()

for inStr in inList:
    print(inStr,end="")

inFp.close()