from tkinter import*

def submit():
    z=open("RegistrationFormDetails2.txt","a")
    a=e3.get()
    b=e4.get()
    c=e5.get()
    d=e6.get()
    e=e7.get()
    f=e8.get()
    z.write(a+","+b+","+c+","+d+","+e+","+f+"\n")
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    z.close()


def access():
    z=open("RegistrationFormDetails2.txt","r+")
    
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    for i in z:
        a=i.split(',')
        if(a[0]==str(e3.get())):
            e4.insert(0,a[1])
            e5.insert(0,a[2])
            e6.insert(0,a[3])
            e7.insert(0,a[4])
            e8.insert(0,a[5])
            
       
    z.close()
def close():
    root.destroy()
    
    
root=Tk()
root.geometry('300x300')
root.resizable(0,0)
root.title("REGISTRATION FORM")

f1=Frame(root,bg='cyan')
f1.pack(side=TOP,expand=TRUE,fill=BOTH)
l1=Label(f1,text='REGISTRATION FORM by ANISH GAUTAM',fg='blue',bg='yellow')
l1.pack(side=TOP)

#f2=Frame(root)
#f2.pack(side=TOP,expand=TRUE,fill=BOTH)
#l2=Label(f2,text='File name',fg='red')
#l2.pack(side=LEFT)
#e2=Entry(f2,bg='white')
#e2.pack(side=RIGHT)

f3=Frame(root,bg='cyan')
f3.pack(side=TOP,expand=TRUE,fill=BOTH)
l3=Label(f3,text='Name',fg='red',bg='cyan')
l3.pack(side=LEFT,padx=20)
e3=Entry(f3,bg='white')
e3.pack(side=RIGHT,padx=20)


f4=Frame(root,bg='cyan')
f4.pack(side=TOP,expand=TRUE,fill=BOTH)
l4=Label(f4,text='College name',fg='red',bg='cyan')
l4.pack(side=LEFT,padx=20)
e4=Entry(f4,bg='white')
e4.pack(side=RIGHT,padx=20)


f5=Frame(root,bg='cyan')
f5.pack(side=TOP,expand=TRUE,fill=BOTH)
l5=Label(f5,text='School name',fg='red',bg='cyan')
l5.pack(side=LEFT,padx=20)
e5=Entry(f5,bg='white')
e5.pack(side=RIGHT,padx=20)

f6=Frame(root,bg='cyan')
f6.pack(side=TOP,expand=TRUE,fill=BOTH)
l6=Label(f6,text='Mobile no.',fg='red',bg='cyan')
l6.pack(side=LEFT,padx=20)
e6=Entry(f6,bg='white')
e6.pack(side=RIGHT,padx=20)

f7=Frame(root,bg='cyan')
f7.pack(side=TOP,expand=TRUE,fill=BOTH)
l7=Label(f7,text='Address',fg='red',bg='cyan')
l7.pack(side=LEFT,padx=20)
e7=Entry(f7,bg='white')
e7.pack(side=RIGHT,padx=20)

f8=Frame(root,bg='cyan')
f8.pack(side=TOP,expand=TRUE,fill=BOTH)
l8=Label(f8,text='Roll no.',fg='red',bg='cyan')
l8.pack(side=LEFT,padx=20)
e8=Entry(f8,bg='white')
e8.pack(side=RIGHT,padx=20)

f9=Frame(root)
f9.pack(side=TOP)
b1=Button(f9,text="SUBMIT",fg="green",command=submit)
b1.pack(side=LEFT,padx=10)
b2=Button(f9,text="ACCESS",fg="green",command=access)
b2.pack(side=LEFT,padx=10)
b3=Button(f9,text="CLOSE",fg="green",command=close)
b3.pack(side=LEFT,padx=10)


