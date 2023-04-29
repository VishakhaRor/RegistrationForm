# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 14:33:28 2022

@author: riyam
"""

#Registration Form for Admission :--------------------------------------------
from tkinter import*
from tkcalendar import DateEntry
import sqlite3 as s

root = Tk()
root.geometry("1600x1600")
root.title("MyForm")
def dis():
       # a=e2.get()
       # b=e3.get()
       # c=e4.get()
       # d=e5.get()
       # e=e6.get()
       # f=e7.get()
       # g=e8.get()
       # h=e9.get()
       # print(a)
       # print(b)
       # print(c)
       # print(d)
       # print(e)
       # print(f)
       
#Another way to get/fetch values -------   
        a=e2.get()
        b=e3.get()
        c=e4.get()
        d=e5.get()
        e=e6.get()
        f=e7.get()
        g=e8.get()
        h=e9.get()
        i=var_rd.get()
        j=var_c1.get() or var_c2.get() or var_c3.get() or var_c4.get() or var_c5.get() or var_c6.get()
        k=var_c7.get()
        l=var_cal.get()
        m=lm.get()
        lst=[a,b,c,d,e,f,i,j,m,l,g,h]
        
 #show error message on empty fields------------------------------
        if a=="" or b=="" or c=="" or d=="" or e=="" or f=="" or g=="" or h=="" or i=="" or j=="" or k=="" or l=="" or m=="":
           messagebox.showerror("error","All fields are mandatory",parent=root)
        elif g!=h:
           messagebox.showerror("error","Password and Confirm Password must be same",parent=root)
        elif k==0:
           messagebox.showerror("error","Please Agree our Terms and Conditions",parent=root)
        else:
           messagebox.showinfo("Success","Registration is done",parent=root)
        
 # database connection----------------------------------   
        conn=s.connect('MyForm.db')
        with conn:
           cursor=conn.cursor()
        o = s.connect('MyForm.db')
        if o:
           print("DataBase is created and connected")
        cur = o.cursor()
        cur.execute("create table if not exists RegisterEntry(Name text,Father_Name text,Mothers_Name text,Email text,Mobile_Number integer,Address text,\
                    Gender text,Language text,State text,DOB int,Password integer,Confirm_Password integer)")
        cur.execute("insert into RegisterEntry Values(?,?,?,?,?,?,?,?,?,?,?,?)",lst)
            
        o.commit()
        o.close()           
             

       
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(g)
        print(h)
        print(i)
        print(j)
        print(l)
        print(m)
       
#variable define------------------------------------
e2=StringVar()
e3=StringVar()
e4=StringVar()
e5=StringVar()
e6=StringVar()
e7=StringVar()
e8=StringVar()
e9=StringVar()
var_rd=StringVar()
var_c1=StringVar()
var_c2=StringVar()
var_c3=StringVar()
var_c4=StringVar()
var_c5=StringVar()
var_c6=StringVar()
lm=StringVar()
var_cal=DateEntry()
var_c7=IntVar() 


l1=Label(root,text="REGISTRATION FORM FOR ADMISSION",bg="yellow",fg="black",
         font=('MV BOLI',22,'bold'),width=90,height=2)
l1.place(x=0,y=0)

l2=Label(root,text="Name",bg="yellow",fg="black",
        font=('MV BOLI',12,'bold'),width=30,height=1 )
l2.place(x=10,y=100)

e2=Entry(root,font=('MV BOLI',12,'bold'),width=50,text=e2)
e2.place(x=500,y=100)

l3=Label(root,text="Father Name",bg="yellow",fg="black",
        font=('MV BOLI',12,'bold'),width=30,height=1 )
l3.place(x=10,y=150)

e3=Entry(root,font=('MV BOLI',12,'bold'),width=50,text=e3)
e3.place(x=500,y=150)

l4=Label(root,text="Mothers Name",bg="yellow",fg="black",
        font=('MV BOLI',12,'bold'),width=30,height=1 )
l4.place(x=10,y=200)

e4=Entry(root,font=('MV BOLI',12,'bold'),width=50,text=e4)
e4.place(x=500,y=200)

l5=Label(root,text="Email",bg="yellow",fg="black",
        font=('MV BOLI',12,'bold'),width=30,height=1 )
l5.place(x=10,y=250)

e5=Entry(root,font=('MV BOLI',12,'bold'),width=50,text=e5)
e5.place(x=500,y=250)

l6=Label(root,text="Mobile Number",bg="yellow",fg="black",
        font=('MV BOLI',12,'bold'),width=30,height=1 )
l6.place(x=10,y=300)

e6=Entry(root,font=('MV BOLI',12,'bold'),width=50,text=e6)
e6.place(x=500,y=300)

l7=Label(root,text="Address",bg="yellow",fg="black",
        font=('MV BOLI',12,'bold'),width=30,height=1 )
l7.place(x=10,y=350)

e7=Entry(root,font=('MV BOLI',12,'bold'),width=50,text=e7)
e7.place(x=500,y=350)

l8=Label(root,text="Gender",bg="yellow",fg="black",
        font=('MV BOLI',12,'bold'),width=30,height=1 )
l8.place(x=10,y=400)

rd1=Radiobutton(root,text="Male",variable=var_rd,value='Male')           # or it can also be value=0
rd2=Radiobutton(root,text="Female",variable=var_rd,value='Female')       # or it can also be value=1
rd3=Radiobutton(root,text="Others",variable=var_rd,value='Others')       # or it can also be value=2
rd1.place(x=500,y=400)
rd2.place(x=600,y=400)
rd3.place(x=700,y=400)

l9=Label(root,text="Language",bg="yellow",fg="black",
        font=('MV BOLI',12,'bold'),width=30,height=1 )
l9.place(x=10,y=450)

c1=Checkbutton(root,text="Hindi",variable=var_c1,onvalue='Hindi',offvalue="")              # or it can also be onvalue=1,offvalue=0
c2=Checkbutton(root,text="English",variable=var_c2,onvalue='English',offvalue="")
c3=Checkbutton(root,text="Punjabi",variable=var_c3,onvalue='Punjabi',offvalue="")
c4=Checkbutton(root,text="Marathi",variable=var_c4,onvalue='Marathi',offvalue="")
c5=Checkbutton(root,text="Telegu",variable=var_c5,onvalue='Telegu',offvalue="")
c6=Checkbutton(root,text="Tamil",variable=var_c6,onvalue='Tamil',offvalue="")
c1.place(x=500,y=450)
c2.place(x=600,y=450)
c3.place(x=700,y=450)
c4.place(x=800,y=450)
c5.place(x=900,y=450)
c6.place(x=1000,y=450)

l10=Label(root,text="State",bg="yellow",fg="black",
        font=('MV BOLI',12,'bold'),width=30,height=1 )
l10.place(x=10,y=500)

l=['Select Your State','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh',
   'Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka',
   'Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha',
   'Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh',
   'Uttrakhand','West Bengal']
lm.set(l[0])
om=OptionMenu(root,lm,*l)
om.place(x=500,y=500)

l11=Label(root,text="DOB",bg="yellow",fg="black",
        font=('MV BOLI',12,'bold'),width=30,height=1 )
l11.place(x=10,y=550)

cal=DateEntry(root,width=38,variable=var_cal,background='darkblue',foreground='white',borderwidth=2)
cal.place(x=500,y=550)

l12=Label(root,text="Password",bg="yellow",fg="black",
        font=('MV BOLI',12,'bold'),width=30,height=1 )
l12.place(x=10,y=600)

e8=Entry(root,font=('MV BOLI',12,'bold'),width=50,text=e8)
e8.place(x=500,y=600)

l13=Label(root,text="Confirm Password",bg="yellow",fg="black",
        font=('MV BOLI',12,'bold'),width=30,height=1 )
l13.place(x=10,y=650)

e9=Entry(root,font=('MV BOLI',12,'bold'),width=50,text=e9)
e9.place(x=500,y=650)

                     #put before onvalue=1,variable=var_c7
c7=Checkbutton(root,text="I Agree with the Terms and Conditions",variable=var_c7,onvalue=1,offvalue=0,
               bg="yellow",font=("MV BOLI",12,'bold'),activebackground="red")
c7.place(x=550,y=695)

b1=Button(root,text="Successful",bg="cyan",fg="blue",cursor="hand2",
      font=('MV BOLI',16,'bold'),width=15,height=1,activebackground='lawn green',
        command=dis)
b1.place(x=650,y=740)

root.mainloop()


