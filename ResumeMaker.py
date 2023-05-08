# Resume Maker

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

main = Tk()
main.geometry('1080x800')
main.title('Resume Maker')
main.config(background='#B7DDFB')

java = IntVar()
python = IntVar()
c = IntVar()
javaStatus = StringVar()
pythonStatus = StringVar()
cStatus = StringVar()

def submit():
    global main
    fn = nameEntry.get()
    ln = lastName.get()
    pn = phoneEntry.get()
    obj = summaryEntry.get(1.0,END)
    exp = expEntry.get(1.0,END)
    deg = degreeEntry.get()
    year = yearEntry.get()
    cert = certificate.get(1.0,END)
    jv = java.get()
    js = javaStatus.get()
    py = python.get()
    pys = pythonStatus.get()
    cl = c.get()
    cs = cStatus.get()
    email = mailEntry.get()
    addre = city.get()

    ll = [fn,ln,pn,obj,exp,deg,year,cert,jv,js,py,pys,cl,email,addre]
    for a  in ll:
        if a=="" or a==None:
            mes = messagebox.showerror('Error',"Fill all the Fields")
            break
            
    else:
        try:
            decl = "I hereby declare that all the information provided above is accurate to the best of my knowledge."
            fileName = 'C:\\Users\\admin\\Desktop\\{fname} {lname} Resume.doc'.format(fname=fn,lname=ln)
            file = open(fileName,'w')
            file.write("RESUME\n\n")
            file.write("OBJECTIVE : \n\n")
            file.write("\t"+obj)
            file.write("\n\nEXPERIENCE : \n\n")
            file.write("\t"+exp)
            file.write("\n\nEDUCATION : \n\n")
            file.write("\tDEGREE          :   "+deg)
            file.write("\n\tYEAR OF PASSING :   "+year)
            file.write("\n\nCERTIFICATIONS : \n\n")
            file.write("\t"+cert)
            file.write("\n\nSKILLS : \n\n")
            skills = ""
            if jv==1:
                level = js
                skills+=level+" Level of Knowledge in Java Programming\n\t"
            if py==1:
                level = pys
                skills+=level+" Level of Knowledge in Python Programming\n\t"
            if cl==1:
                level = cs
                skills+=level+" Level of Knowledge in C Programming\n\n\t"
            file.write("\t"+skills)
            file.write("\n\nPERSONAL DETAILS : \n\n")
            file.write("\n\tFirst Name         :       "+fn)
            file.write("\n\tLast Name          :       "+ln)
            file.write("\n\tMail Id            :       "+email)
            file.write("\n\tMobile Number      :       "+pn)
            file.write("\n\tAddress            :       "+addre)
            file.write("\n\nDECLARATION : \n\n")
            file.write("\t"+decl)
            file.write("\n\n\nDate    : ")
            file.write("\nPlace    : ")
            file.close()
            
            m = messagebox.showinfo('Success',"Successfully Created a Resume! Check in Your Desktop")
            main.destroy()
        except:
            m = messagebox.showwarning("OOPS!","Something Went Wrong! Please Try again Later!")
        

titleLabel = Label(main,text='Resume Maker',bg='#F984A2',font=('normal',15,'bold')).place(x=0,y=10,width=1080,height=50)

personalLabel = Label(main,text='Personal Details',font=('normal',14,'bold')).place(x=10,y=70,width=520,height=30)
nameLabel = Label(main,text='Name : ',bg='#B7DDFB',anchor='w',font=('normal',13,'bold')).place(x=20,y=150,width=200,height=30)
nameEntry = Entry(main,font=('normal',13,''))
nameEntry.place(x=220,y=150,width=300,height=30)

mailLabel = Label(main,text='Mail Id : ',anchor='w',bg='#B7DDFB',font=('normal',13,'bold')).place(x=20,y=200,width=200,height=30)
mailEntry = Entry(main,font=('normal',13,''))
mailEntry.place(x=220,y=200,width=300,height=30)

phoneLabel = Label(main,text='Phone Number : ',anchor='w',bg='#B7DDFB',font=('normal',13,'bold')).place(x=20,y=250,width=200,height=30)
phoneEntry = Entry(main,font=('normal',13,''),)
phoneEntry.place(x=220,y=250,width=300,height=30)

lastnameLabel = Label(main,text='Last Name : ',anchor='w',bg='#B7DDFB',font=('normal',13,'bold')).place(x=20,y=300,width=250,height=30)
lastName = Entry(main,font=('normal',13,''),)
lastName.place(x=220,y=300,width=300,height=30)
                 
summaryLabel= Label(main,text='Profile Summary : ',anchor='w',bg='#B7DDFB',font=('normal',13,'bold')).place(x=20,y=350,width=300,height=30)
summaryEntry = Text(main,font=('normal',13,''),)
summaryEntry.place(x=220,y=350,width=300,height=100)

skillLabel = Label(main,text='Skills : ',anchor='w',bg='#B7DDFB',font=('normal',13,'bold')).place(x=20,y=500,width=200,height=30)
javaBox = Checkbutton(main,bg='#B7DDFB',text='Java',font=('normal',13,''),anchor='w',onvalue=1,variable=java)
javaBox.place(x=220,y=500,width=100,height=30)
javaStatus1 = Radiobutton(main,bg='#B7DDFB',text='Beginner',variable=javaStatus,font=('normal',13,''),anchor='w',value='Beginner').place(x=320,y=500,width=100,height=30)
javaStatus2 = Radiobutton(main,bg='#B7DDFB',text='Advanced',variable=javaStatus,font=('normal',13,''),anchor='w',value='Advanced').place(x=420,y=500,width=100,height=30)

pythonBox = Checkbutton(main,bg='#B7DDFB',text='Python',font=('normal',13,''),anchor='w',onvalue=1,variable=python)
pythonBox.place(x=220,y=550,width=100,height=30)
pythonStatus1 = Radiobutton(main,bg='#B7DDFB',text='Beginner',variable=pythonStatus,font=('normal',13,''),anchor='w',value='Beginner').place(x=320,y=550,width=100,height=30)
pythonStatus2 = Radiobutton(main,bg='#B7DDFB',text='Advanced',variable=pythonStatus,font=('normal',13,''),anchor='w',value='Advanced').place(x=420,y=550,width=100,height=30)

cBox = Checkbutton(main,bg='#B7DDFB',text='C',font=('normal',13,''),anchor='w',onvalue=1,variable=c)
cBox.place(x=220,y=600,width=100,height=30)
cStatus1 = Radiobutton(main,bg='#B7DDFB',text='Beginner',variable=cStatus,font=('normal',13,''),anchor='w',value='Beginner').place(x=320,y=600,width=100,height=30)
cStatus2 = Radiobutton(main,bg='#B7DDFB',text='Advanced',variable=cStatus,font=('normal',13,''),anchor='w',value='Advanced').place(x=420,y=600,width=100,height=30)

otherDetails = Label(main,text='Educational & Experience Details',font=('normal',14,'bold')).place(x=550,y=70,width=520,height=30)

experienceLabel = Label(main,text='Experience (if any) : ',anchor='w',bg='#B7DDFB',font=('normal',13,'bold')).place(x=560,y=150,width=200,height=30)
expEntry = Text(main,font=('normal',13,''),)
expEntry.place(x=760,y=150,width=300,height=100)

degreeLabel = Label(main,text='Name of the Degree : ',anchor='w',bg='#B7DDFB',font=('normal',13,'bold')).place(x=560,y=300,width=200,height=30)
degreeEntry = ttk.Combobox(main,values=['B.Sc','B.E','M.Sc','BBA','MBA'],font=('normal',13,''))
degreeEntry.place(x=760,y=300,width=300,height=30)

YearLabel = Label(main,text='Year of Passing : ',anchor='w',bg='#B7DDFB',font=('normal',13,'bold')).place(x=560,y=350,width=150,height=30)
yearEntry = ttk.Combobox(main,values=['2018','2019','2020','2021','2022'],font=('normal',13,''))
yearEntry.place(x=760,y=350,width=300,height=30)

certiLabel = Label(main,text='Certificates (if any) : ',anchor='w',bg='#B7DDFB',font=('normal',13,'bold')).place(x=560,y=400,width=200,height=30)
certificate = Text(main,font=('normal',13,''),)
certificate.place(x=760,y=400,width=300,height=70)

cityLable = Label(main,text='City : ',anchor='w',bg='#B7DDFB',font=('normal',13,'bold')).place(x=560,y=500,width=200,height=30)
city = Entry(main,font=('normal',13,''),)
city.place(x=760,y=500,width=300,height=30)

submit = Button(main,text='Submit',font=('normal',13,'bold'),command=submit).place(x=260,y=700,width=540,height=40)
