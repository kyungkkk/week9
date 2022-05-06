from tkinter import*
import PIL

window=Tk()
window.title("윈도창 연습")

photo=PhotoImage(file="cat.gif")
label1=Label(window,image=photo)

label1.pack()

window.mainloop()
