from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter.messagebox import *
import mysql.connector
import re
 
def checkk(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b' 
    if(re.fullmatch(regex, email)):
        return 1
    else:
        return 2

def login_window():
    root.destroy()
    import login


def clear():
    entryemail.delete(0, END)
    entrycontact.delete(0, END)
    entrypassword.delete(0, END)
    entryconfirmpassword.delete(0, END)
    entryfirstname.delete(0, END)
    entrylastname.delete(0, END)
    entryanswer.delete(0, END)
    comboquestion.current(0)
    check.set(0)


def register():
    if entryfirstname.get() == '' or entrylastname.get() == '' or entryemail.get() == '' or entrycontact.get() == '' or \
            entrypassword.get() == '' or entryconfirmpassword.get() == '' or comboquestion.get() == 'Select' or\
                 entryanswer.get() == '':
        showerror('Error', "All Fields Are Required", parent=root)

    elif entrycontact.get().isdecimal()==False:
        showerror('Error',"Contact must be numbers only", parent=root)

    elif checkk(entryemail.get())==2:
         showerror('Error',"invalid email", parent=root)

    elif entrypassword.get() != entryconfirmpassword.get():
        showerror('Error', "Password Mismatch", parent=root)

    elif check.get() == 0:
        showerror('Error', "Please Agree To Our Terms & Conditions", parent=root)

    else:
        try:
            con = mysql.connector.connect(host='localhost', user='root', password='root', database='doctors')
            cur = con.cursor()
            cur.execute("select * from user where email='%s'", entryemail.get())
            row = cur.fetchone()
            if row != None:
                showerror('Error', "User Already Exists", parent=root)
            else:

                cur.execute('insert into user (f_name,l_name,email,contact,question,answer,password) \
                    values(%s,%s,%s,%s,%s,%s,%s)', (entryfirstname.get(), entrylastname.get(), entryemail.get(),\
                         entrycontact.get(), comboquestion.get(), entryanswer.get(), entrypassword.get()))
                con.commit()
                con.close()
                showinfo('Success', "Registration Successful", parent=root)
                clear()
                root.destroy()
                import login


        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)


root = Tk()
img=PhotoImage(file='icon.png')
root.tk.call('wm','iconphoto',root._w,img)
root.geometry('1200x800')
root.title('DocHouse')
bgregister = PhotoImage(file='bgg.png')
bgloginLabel = Label(root, image=bgregister)
bgloginLabel.place(x=0, y=0)

registerFrame = Frame(root, bg='white', width=650, height=650)
registerFrame.place(x=540, y=10)

titleLabel = Label(registerFrame, text='Registration Form', font=('times new roman', 28, 'bold '), bg='white',
                   fg='Black' )
titleLabel.place(x=200, y=5)

firstnameLabel = Label(registerFrame, text='First Name', font=('times new roman', 18, 'bold'), bg='white', fg='gray20')
firstnameLabel.place(x=20, y=80)
entryfirstname = Entry(registerFrame, font=('times new roman', 18),bd=2)
entryfirstname.place(x=20, y=110, width=250)

lastnameLabel = Label(registerFrame, text='Last Name', font=('times new roman', 18, 'bold'), bg='white',
                      fg='gray20' )
lastnameLabel.place(x=370, y=80)
entrylastname = Entry(registerFrame, font=('times new roman', 18), bd=2)
entrylastname.place(x=370, y=110, width=250)

contactLabel = Label(registerFrame, text='Contact Number', font=('times new roman', 18, 'bold'), bg='white',
                     fg='gray20')
contactLabel.place(x=20, y=170)
entrycontact = Entry(registerFrame, font=('times new roman', 18), bd=2)
entrycontact.place(x=20, y=200, width=250)

emailLabel = Label(registerFrame, text='Email', font=('times new roman', 18, 'bold'), bg='white', fg='gray20', )
emailLabel.place(x=370, y=170)
entryemail = Entry(registerFrame, font=('times new roman', 18), bd=2)
entryemail.place(x=370, y=200, width=250)

questionLabel = Label(registerFrame, text='Security Question', font=('times new roman', 18, 'bold'), bg='white',
                      fg='gray20', )
questionLabel.place(x=20, y=250)
comboquestion = ttk.Combobox(registerFrame, font=('times new roman', 16), state='readonly', justify=CENTER)
comboquestion['values'] = ('Select', 'Your First Pet Name?', 'Your Birth Place Name?', 'Your Best Friend Name?',
                           'Your Favourite Teacher?', 'Your Favourite Hobby?')
comboquestion.place(x=20, y=280, width=250)
comboquestion.current(0)
answerLabel = Label(registerFrame, text='Answer', font=('times new roman', 18, 'bold'), bg='white',
                    fg='gray20', )
answerLabel.place(x=370, y=250)
entryanswer = Entry(registerFrame, font=('times new roman', 18), bd=2)
entryanswer.place(x=370, y=280, width=250)

passwordLabel = Label(registerFrame, text='Password', font=('times new roman', 18, 'bold'), bg='white',
                      fg='gray20', )
passwordLabel.place(x=20, y=330)
entrypassword = Entry(registerFrame, font=('times new roman', 18), bd=2,show="*")
entrypassword.place(x=20, y=360, width=250)

confirmpasswordLabel = Label(registerFrame, text='Confirm Password', font=('times new roman', 18, 'bold'),
                             bg='white',fg='gray20', )
confirmpasswordLabel.place(x=370, y=330)
entryconfirmpassword = Entry(registerFrame, font=('times new roman', 18), bd=2,show="*")
entryconfirmpassword.place(x=370, y=360, width=250)

check = IntVar()
checkButton = Checkbutton(registerFrame, text='I Agree All The Terms & Conditions', variable=check, onvalue=1,
                          offvalue=0, font=('times new roman', 14, 'bold'), bg='white')
checkButton.place(x=20, y=400)

button = PhotoImage(file='button.png')
registerbutton = Button(registerFrame, image=button, bd=1, cursor='hand2', command=register)
registerbutton.place(x=250, y=440)

haveLabel = Label(registerFrame, text='Already have an account?', font=('times new roman', 18, 'bold'),
                             bg='white',fg='gray20')
haveLabel.place(x=200, y=490)

loginbutton = Button(registerFrame, text='Login', font=('arial', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                      activebackground='gray20', activeforeground='white', command=login_window)
loginbutton.place(x=280, y=530)
root.mainloop()

