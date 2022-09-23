import tkinter
from tkinter import *

t=Tk()
t.title("registration")
t.geometry('500x500')

Label(t,text="registration form",bg="yellow",fg="black",font=("bradely hand itc",20,"bold")).place(x=110,y=10)
Label(t,text="username",bg="blue",fg="orange",font=("time new roman",10,"bold")).place(x=50,y=100)
Label(t,text="password",bg="blue",fg="orange",font=("time new roman",10,"bold")).place(x=50,y=150)
t.mainloop()

