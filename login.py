
import random
import tkinter as tk
from tkinter import *
import os
from PIL import Image, ImageTk
 
creds = 'tempfile.temp' 
 
def Signup(): 
    global pwordE
    global nameE
    global roots
    
    
    roots = Tk()
    roots.title('Register here to Login to Game')
    roots.geometry('600x500')

    my_img= ImageTk.PhotoImage(Image.open("bg.png"))
    my_Lable=Label(image=my_img)
    my_Lable.grid(row=9,column=3,columnspan = 10, rowspan = 8)
   
    intruction = Label(roots, text='Please register by Enter a new Username and Password',font="GoudyStout 16") 
    intruction.grid(row=0,column=0,columnspan = 10, rowspan = 1,padx=1,pady=10)#grid(row=0, column=0, sticky=E) 
 
    nameL = Label(roots, text='New Username: ',font="GoudyStout 12") 
    pwordL = Label(roots, text='New Password: ',font="GoudyStout 12") 
    nameL.grid(row=5, column=3, sticky=W) 
    pwordL.grid(row=6, column=3, sticky=W) 
 
    nameE = Entry(roots) 
    pwordE = Entry(roots, show='*') 
    nameE.grid(row=5, column=4)
    pwordE.grid(row=6, column=4)
 
    signupButton = Button(roots, text='Signup', command=FSSignup) 
    signupButton.grid(row=8,column=0,columnspan=10,rowspan=1)
    roots.mainloop() 
 
def FSSignup():
    with open(creds, 'w') as f: 
        f.write(nameE.get()) 
        f.write('\n')
        f.write(pwordE.get())
        f.close() 
 
    roots.destroy() 
    Login() 
 
def Login():
    global nameEL
    global pwordEL
    global rootA
 
    rootA = Tk() 
    rootA.title('Login') 
    rootA.geometry('300x300')
    intruction = Label(rootA, text='Please Login to start playing The game!\n') 
    intruction.grid(row=0,column=1,columnspan = 10, rowspan = 1)
    my_img= ImageTk.PhotoImage(Image.open("play.png"))
    my_Lable=Label(image=my_img)
    my_Lable.grid(row=9,column=1,columnspan = 10, rowspan = 8)
    
    nameL = Label(rootA, text='Username: ') 
    pwordL = Label(rootA, text='Password: ') 
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) 
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) 
    loginB.grid(column=1,columnspan=12, )
 
    rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser) 
    rmuser.grid(column=1,columnspan=12,)
    rootA.mainloop()
    

def CheckLogin():
    with open(creds) as f:
        data = f.readlines() 
        uname = data[0].rstrip()
        pword = data[1].rstrip()
      
    
 
    if nameEL.get() == uname and pwordEL.get() == pword:
       
        choice = ['rock', 'paper', 'scissors']
        r = tk.Tk()
        r.configure(bg="light blue")
        r.geometry("650x550")

        result=StringVar()
        score_com=IntVar()
        score_you=IntVar()

      
    else:
        count=1
        
        r = Tk()
        r.title('error')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()
 
def DelUser():
    os.remove(creds) 
    rootA.destroy()
    Signup() 
 
if os.path.isfile(creds):
    Login()
else: 
    Signup()




    
