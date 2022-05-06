from tkinter import*

btnList=[None]*9
fnameList=["froyo.gif","gingerbread.gif","icecream.gif","jellybean.gif","kitkat.gif","lolloipop.gif","mashmallow.gif","nougat.gif"]
photoList=[None]*9
i,k=0,0
xPos,yPos=0,0
num=0

window=Tk()
window.geometry("210x210")

for i in range(0,9):
    photoList[i]=PhotoImage(file="gif/"+ fnameList[i])#리스트에 이미지를 넣어줌
    btnList[i]=Button(window,image=photoList[i])#

for i in range(0,3):
    for k in range(0,3):
        btnList[num.plack(x=xPos,y=yPos)]
        num+=1
        xPos+=70
    xPos=0
    yPos+=70

window.mainloop()