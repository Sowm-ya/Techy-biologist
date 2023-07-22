#importing all the modules
import tkinter
from tkinter import *
from tkinter import messagebox

#defining a variable for the module
t=tkinter.Tk()

#Setting up the GUI window 
t.geometry("258x350") #dimensions for the display window
t.title('CALCULATOR') #title for the window
t.configure(bg='grey60') #background color for the window

#creates a entry space to display the entered values 
e=Entry(t,font=("calibri","14"),bg='turquoise2',borderwidth=2,relief="solid")
e.place(x=25,y=15)

#this function returns the value entered by the user
def num(n):
    e.insert(END,n)
    return 

#creating buttons for numbers from 1-0
b1=Button(t,text="1",font=("calibri","10"),borderwidth=2,relief="solid",padx=10,pady=10,bg='grey75',command=lambda:num(1))
b1.place(x=70,y=50)
b2=Button(t,text="2",font=("calibri","10"),borderwidth=2,relief="solid",padx=10,pady=10,bg='grey75',command=lambda:num(2))
b2.place(x=110,y=50)
b3=Button(t,text="3",font=("calibri","10"),borderwidth=2,relief="solid",padx=10,pady=10,bg='grey75',command=lambda:num(3))
b3.place(x=150,y=50)
c1=Button(t,text="4",font=("calibri","10"),borderwidth=2,relief="solid",padx=10,pady=10,bg='grey75',command=lambda:num(4))
c1.place(x=70,y=100)
c2=Button(t,text="5",font=("calibri","10"),borderwidth=2,relief="solid",padx=10,pady=10,bg='grey75',command=lambda:num(5))
c2.place(x=110,y=100)
c3=Button(t,text="6",font=("calibri","10"),borderwidth=2,relief="solid",padx=10,pady=10,bg='grey75',command=lambda:num(6))
c3.place(x=150,y=100)
d1=Button(t,text="7",font=("calibri","10"),borderwidth=2,relief="solid",padx=10,pady=10,bg='grey75',command=lambda:num(7))
d1.place(x=70,y=150)
d2=Button(t,text="8",font=("calibri","10"),borderwidth=2,relief="solid",padx=10,pady=10,bg='grey75',command=lambda:num(8))
d2.place(x=110,y=150)
d3=Button(t,text="9",font=("calibri","10"),borderwidth=2,relief="solid",padx=10,pady=10,bg='grey75',command=lambda:num(9))
d3.place(x=150,y=150)
e1=Button(t,text="0",font=("calibri","10"),borderwidth=2,relief="solid",padx=10,pady=10,bg='grey75',command=lambda:num(0))
e1.place(x=70,y=200)

#this function will get the entered values to perform the operations
def sum1(sy):
    global n1
    global s
    s=sy
    n1=int(e.get())
    e.delete(0,END)
    return

#this function will perform the operations for the recieved value 
def result():
    n2=int(e.get())
    e.delete(0,END)
    if(s=='+'):
        e.insert(0,n1+n2)
    elif(s=='-'):
        e.insert(0,n1-n2)
    elif(s=='*'):
        e.insert(0,n1*n2)
    elif(s=='/'):
        e.insert(0,n1/n2)
        return

#creating buttons for operators 
e2=Button(t,text="+",font=("calibri","10"),borderwidth=2,relief="solid",command=lambda:sum1('+'),bg='grey75',padx=10,pady=10)
e2.place(x=110,y=200)

r=Button(t,text="-",font=("calibri","10"),borderwidth=2,relief="solid",command=lambda:sum1('-'),bg='grey75',padx=10.5,pady=10)
r.place(x=150,y=200)

r1=Button(t,text="x",font=("calibri","10"),borderwidth=2,relief="solid",command=lambda:sum1('*'),bg='grey75',padx=10,pady=10)
r1.place(x=70,y=250)

r1=Button(t,text="/",font=("calibri","10"),borderwidth=2,relief="solid",command=lambda:sum1('/'),bg='grey75',padx=10,pady=10)
r1.place(x=110,y=250)

e3=Button(t,text="=",font=("calibri","10"),borderwidth=2,relief="solid",command=result,bg='DodgerBlue4',padx=10,pady=35)
e3.place(x=150,y=250)

#this function clears the entered values
def clear():
    e.delete(0,END)
    return

#creates a button for the 'clear' function
f1=Button(t,text="Clear",font=("calibri","10"),borderwidth=2,relief="solid",command=clear,bg='grey75',padx=19,pady=10)
f1.place(x=70,y=300)

#this will run the above function as long as the window is open
t.mainloop()
             
