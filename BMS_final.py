from tkinter import *
from tkinter.messagebox import *
import sqlite3


def login_user(username,password):
    con=sqlite3.connect("createuser.db")
    cur=con.cursor()
    cur.execute("select * from user")
    row=cur.fetchall()
    for i in row:
        if(i[0]==username and i[3]==password):
            showinfo("Login","You have been successfully logged in")
            available_books()
            break
        else:
            showinfo("Login","Invalid Details")
            break


def create_user(name,gender,email,password):
    con=sqlite3.connect("createuser.db")
    cur=con.cursor()
    if(name=='' or gender=='' or email=='' or password==''):
        showinfo("New User","Fill all the details")
        new_user()


    else:
        cur.execute("create table if not exists user(name varchar(20),gender number(2),email varchar(20),password varchar(20))")
        if(gender==1):
            cur.execute("insert into user values(?,?,?,?)",(name,"Male",email,password))
        else:
            cur.execute("insert into user values(?,?,?,?)",(name,"Female",email,password))
        con.commit()
        con.close()
        showinfo("New User","Registration Successful")



def rbook(username,bookname,price):
    if(username=='' or bookname=='' or price==''):
        showinfo("Request Book","Please fill all the details")
    else:
        con=sqlite3.connect("createuser.db")
        cur=con.cursor()
        cur.execute("select * from user")
        row=cur.fetchall()
        for i in row:
            if(i[0]==username):
                cur.execute("create table if not exists request(username varchar(20),bookname varchar(20),price number(10))")
                cur.execute("insert into request values(?,?,?)",(username,bookname,price))
                con.commit()
                con.close()
                showinfo("Request Book","Pay the money and Collect the book from counter")
                break
            else:
                showinfo("Request Book","User doesn't exist")
                break
   
    
def sbook(username,bookname,price):
    if(username=='' or bookname=='' or price==''):
        showinfo("Submit Book","Please fill all the details")
    else:
        con=sqlite3.connect("createuser.db")
        cur=con.cursor()
        cur.execute("select * from request")
        row=cur.fetchall()
        for i in row:
            if(i[0]==username and i[1]==bookname):
                cur.execute("delete from request where username=?",(username,))
                con.commit()
                con.close()
                showinfo("Submit Book","Submit the book and Collect the money from counter")
                break
            elif(i[0]=='' or i[1]==''):
                showinfo("Submit Book","No Records found")
                break
            else:
                showinfo("Request Book","No book records exists on your username")
                break



def login():
    frame = Frame(window)
    Frame.tkraise(frame)
    frame=Toplevel()
    frame.geometry("500x400")
    #Frame.title("Login")
    d = Canvas(frame, height=190, width=460, bg="green")
    username=StringVar()
    l1=Label(frame,text="Username",bg="brown")
    l1.place(x=150,y=150)
    e1=Entry(frame,bd=5,textvariable=username)
    e1.place(x=230,y=150)
    password=StringVar()
    l2=Label(frame,text="Password",bg="brown")
    l2.place(x=150,y=200)
    e2=Entry(frame,bd=5,textvariable=password,show='*')
    e2.place(x=230,y=200)

    b4=Button(frame,text="Login",bg="Skyblue",command=lambda:login_user(username.get(),password.get()))
    b4.place(x=150,y=250,height=40,width=70)

    b5=Button(frame,text="New User",bg="Skyblue",command=new_user)
    b5.place(x=250,y=250,height=40,width=70)
    d.pack(side="top",fill="both",expand=True)



def new_user():
    frame = Frame(window)
    Frame.tkraise(frame)
    frame=Toplevel()
    frame.geometry("450x350")
    e = Canvas(frame, height=190, width=460, bg="Yellow")

    e3_value=StringVar()
    l3=Label(frame,text="Name",bg="Yellow")
    l3.place(x=100,y=100)
    e3=Entry(frame,bd=4,textvariable=e3_value)
    e3.place(x=170,y=100)

    c1_value=IntVar()

    l4=Label(frame,text="Gender",bg="Yellow")
    l4.place(x=100,y=140)
    c1=Radiobutton(frame,text="Male",value=1,variable=c1_value,bg="Yellow")
    c1.place(x=170,y=140)
    c2=Radiobutton(frame,text="Female",value=2,variable=c1_value,bg="Yellow")
    c2.place(x=240,y=140)

    e5_value=StringVar()
    l5=Label(frame,text="Email",bg="Yellow")
    l5.place(x=100,y=180)
    e5=Entry(frame,bd=4,textvariable=e5_value)
    e5.place(x=170,y=180)

    e6_value=StringVar()
    l6=Label(frame,text="Password",bg="Yellow")
    l6.place(x=100,y=220)
    e6=Entry(frame,bd=4,textvariable=e6_value,show='*')
    e6.place(x=170,y=220)

    b6=Button(frame,text="Submit",bg="Skyblue",command=lambda:create_user(e3_value.get(),c1_value.get(),e5_value.get(),e6_value.get()))
    b6.place(x=150,y=260,height=40,width=70)
    e.pack(side="top",fill="both",expand=True)

def submit_book():
    frame = Frame(window)
    Frame.tkraise(frame)
    frame=Toplevel()
    frame.geometry("450x350")
    e = Canvas(frame, height=190, width=460, bg="Violet")

    e7_value=StringVar()
    l7=Label(frame,bg="Violet",text="Username")
    l7.place(x=150,y=130)
    e7=Entry(frame,bd=5,textvariable=e7_value)
    e7.place(x=230,y=130)

    e8_value=StringVar()
    l8=Label(frame,bg="Violet",text="Bookname")
    l8.place(x=150,y=180)
    e8=Entry(frame,bd=5,textvariable=e8_value)
    e8.place(x=230,y=180)

    e9_value=StringVar()
    l9=Label(frame,bg="Violet",text="Price")
    l9.place(x=150,y=230)
    e9=Entry(frame,bd=5,textvariable=e9_value)
    e9.place(x=230,y=230)

    b6=Button(frame,text="Submit",bg="Skyblue",command=lambda:sbook(e7_value.get(),e8_value.get(),e9_value.get()))
    b6.place(x=195,y=260,height=40,width=70)
    e.pack(side="top",fill="both",expand=True)

def request_book():
    frame = Frame(window)
    Frame.tkraise(frame)
    frame=Toplevel()
    frame.geometry("450x350")
    e = Canvas(frame, height=190, width=460, bg="Orange")
    e10_value=StringVar()
    l10=Label(frame,bg="Orange",text="Username")
    l10.place(x=100,y=100)
    e10=Entry(frame,bd=4,textvariable=e10_value)
    e10.place(x=170,y=100)

    c3_value=StringVar()
    l11=Label(frame,bg="Orange",text="Bookname")
    l11.place(x=100,y=140)
    c3=Entry(frame,textvariable=c3_value,bd=4)
    c3.place(x=170,y=140)

    e12_value=StringVar()
    l12=Label(frame,bg="Orange",text="Price")
    l12.place(x=100,y=180)
    e12=Entry(frame,bd=4,textvariable=e12_value)
    e12.place(x=170,y=180)

    b7=Button(frame,text="Submit",bg="Skyblue",command=lambda:rbook(e10_value.get(),c3_value.get(),e12_value.get()))
    b7.place(x=195,y=220,height=40,width=70)
    e.pack(side="top",fill="both",expand=True)

def available_books():
    frame = Frame(window)
    Frame.tkraise(frame)
    frame=Toplevel()
    frame.geometry("470x350")
    e = Canvas(frame, height=190, width=460, bg="Red")

    a1=Label(frame,text="Available Books",bg="Red")
    a1.place(x=200,y=4)

    b8=Button(frame,text="Request Book",command=request_book,bg="Skyblue")
    b8.place(x=100,y=40,height=40,width=90)

    b9=Button(frame,text="Submit Book",command=submit_book,bg="Skyblue")
    b9.place(x=300,y=40,height=40,width=90)
    e.pack(side="top",fill="both",expand=True)


#window.geometry("500x200")
window=Tk()
window.title("BMS")
C = Canvas(window, height=190, width=460, bg="light green")
C.pack(side="top",fill="both",expand=True)

b1=Button(window,text="Login",bg="green",command=login)
b1.place(x=70,y=70,height=40,width=70)
b2=Button(window,text="Sign Up",bg="green",command=new_user)
b2.place(x=180,y=70,height=40,width=80)
b3=Button(window,text="Available Books",bg="green",command=available_books)
b3.place(x=300,y=70,height=40,width=95)



window.mainloop()
