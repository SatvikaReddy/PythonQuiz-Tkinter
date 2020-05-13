from tkinter import *

window=Tk()
window.configure(background="lavender")
intro=Label(window,text="Welcome to our Quiz!",bg="lavender")
intro.pack()

def atw():
    try:
        import ATW.py
    except:
        pass
def ca():
    try:
        import CA.py
    except:
        pass
def faf():
    try:
        import FaF.py
    except:
        pass
def hb():
    try:
        import HumanBody.py
    except:
        pass
def sat():
    try:
     import SaT.py
    except:
        pass
def sports():
    try:
        import Sports.py
    except:
        pass
def nts():
    try:
        import NTS.py
    except:
        pass

space=Label(window,text=" ",bg='lavender')
space.pack()
questions=Label(window,text="Which quiz do you want to play?",bg='lavender')
questions.pack()

Q1=Button(window,text="Around The World",command=atw,bg='mediumorchid1',height=1,width=20)
Q1.pack()

Q2=Button(window,text="Current Affairs",command=ca,bg="mediumorchid1",height=1,width=20)
Q2.pack() 

Q3=Button(window,text="Flora and Fauna",command=faf,bg='mediumorchid1',height=1,width=20)
Q3.pack()

Q4=Button(window,text="Science and Technology",command=sat,bg='mediumorchid1',height=1,width=20)
Q4.pack()

Q5=Button(window,text="Sports",command=sports,bg='mediumorchid1',height=1,width=20)
Q5.pack()

Q6=Button(window,text="Human Body",command=hb,bg='mediumorchid1',height=1,width=20)
Q6.pack()

Q7=Button(window,text="Name the Singer",command=nts,bg='mediumorchid1',height=1,width=20)
Q7.pack()


instructions=Label(window,text="**For Each Correct Answer You Will Be Awarded 3 points and for every wrong answer 0.5 points will be deducted**",bg='lavender')
instructions.pack()

window.mainloop()