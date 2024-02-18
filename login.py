from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import mysql.connector
mail={}
ee=""
def getinto():
    def order():
       roott.destroy()
       import again

    def old():
        roott.destroy()
        import database
    
    root.destroy()
    roott = Tk()
    img=PhotoImage(file='icon.png')
    roott.tk.call('wm','iconphoto',roott._w,img)
    roott.geometry('1200x800')
    roott.title('DocHouse')
    bgregister = PhotoImage(file='bgg.png')
    bgloginLabel = Label(roott, image=bgregister)
    bgloginLabel.place(x=0, y=0)
    frame = Frame(roott, bg='white', width=600, height=320)
    frame.place(x=320, y=240)
    l = Label(frame, text="Your name: ", font=('times new roman', 18, 'bold'), bg='white',fg='#009973' )
    l.place(x=130,y=50)
    n=Label(frame, text=mail[1]+" "+mail[2] , font=('times new roman', 18, 'bold'), bg='white',fg='gray20' )
    n.place(x=300,y=50)
    l2 = Label(frame, text="Your contact: ", font=('times new roman', 18, 'bold'), bg='white',fg='#009973' )
    l2.place(x=130,y=100)
    n2=Label(frame, text=mail[3] , font=('times new roman', 18, 'bold'), bg='white',fg='gray20' )
    n2.place(x=300,y=100)
    l3 = Label(frame, text="Your Email: ", font=('times new roman', 18, 'bold'), bg='white',fg='#009973' )
    l3.place(x=130,y=150)
    n3 = Label(frame, text=mail[4] , font=('times new roman', 18, 'bold'), bg='white',fg='gray20' )
    n3.place(x=300,y=150)
    butto = Button(frame, text='Make an reservation', font=('times new roman', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                      activebackground='gray20', activeforeground='white', command=order)
    butto.place(x=30,y=220)
    butt = Button(frame, text='Old reservation', font=('times new roman', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                       activebackground='gray20', activeforeground='white', command=old)
    butt.place(x=345,y=220)  
    roott.mainloop()
    roott.destroy()



def forget_password():
    def reset():
        securityquescombo.current(0)
        newpassEntry.delete(0, END)
        answerforgetEntry.delete(0, END)
        mailentry.delete(0, END)
        passentry.delete(0, END)

    def reset_password():
        if securityquescombo.get() == 'Select' or answerforgetEntry.get() == '' or newpassEntry.get() == '':
            showerror('Error', 'All Fields Are Required', parent=root2)
        else:
            try:
                con = mysql.connector.connect(host='localhost', user='root', password='root', database='doctors')
                cur = con.cursor()
                cur.execute('select * from user where email=%s and question=%s and answer=%s',
                            (mailentry.get(), securityquescombo.get(), answerforgetEntry.get()))
                row = cur.fetchone()
                if row == None:
                    showerror('Error', 'Security Question or Answer is Incorrect\n\n\tPlease Try Again ', parent=root2)

                else:
                    cur.execute('update user set password=%s where email=%s', (newpassEntry.get(), mailentry.get()))
                    con.commit()
                    con.close()
                    showinfo('Success', 'Password is reset, please login with new password', parent=root2)
                    reset()
                    root2.destroy()


            except Exception as e:
                showerror('Error', f"Error due to: {e}", parent=root)

    if mailentry.get() == '':
        showerror('Error', 'Please enter the email address to reset your password', parent=root)
    else:
        try:
            con = mysql.connector.connect(host='localhost', user='root', password='root', database='doctors')
            cur = con.cursor()
            cur.execute("select * from user where email='%s'", mailentry.get())
            print(mailentry.get())
            row = cur.fetchall()
            if row == None:
                showerror('Error', 'Please enter the valid email address', parent=root)

            else:
                con.close()
                root2 = Toplevel()
                root2.title('Forget Password')
                root2.geometry('470x560+400+60')
                root2.config(bg='white')
                root2.focus_force()
                root2.grab_set()
                forgetLabel = Label(root2, text='Forget', font=('times new roman', 22, 'bold'), fg='black', bg='white')
                forgetLabel.place(x=128, y=10)
                forgetpassLabel = Label(root2, text='Password', font=('times new roman', 22, 'bold'), fg='#009973',
                                        bg='white')
                forgetpassLabel.place(x=225, y=10)

                passwordimage = PhotoImage(file='pass.png')
                forgetimageLabel = Label(root2, image=passwordimage, bg='white')
                forgetimageLabel.place(x=170, y=70)

                securityquesLabel = Label(root2, text='Security Questions', font=('times new roman', 19, 'bold'),
                                          fg='black', bg='white')
                securityquesLabel.place(x=60, y=220)
                securityquescombo = ttk.Combobox(root2, font=('times new roman', 19), state='readonly', justify=CENTER,
                                                 width=28)
                securityquescombo['values'] = (
                    'Select', 'Your First Pet Name?', 'Your Birth Place Name?', 'Your Best Friend Name?',
                    'Your Favourite Teacher?', 'Your Favourite Hobby?')
                securityquescombo.place(x=60, y=260)
                securityquescombo.current(0)

                answerforgetLabel = Label(root2, text='Answer', font=('times new roman', 19, 'bold'), fg='black',
                                          bg='white')
                answerforgetLabel.place(x=60, y=310)
                answerforgetEntry = Entry(root2, font=('times new roman', 19,), fg='black', width=30,
                                          bg='white')
                answerforgetEntry.place(x=60, y=350)

                newpassLabel = Label(root2, text='New Password', font=('times new roman', 19, 'bold'), fg='black',
                                     bg='white')
                newpassLabel.place(x=60, y=400)
                newpassEntry = Entry(root2, font=('times new roman', 19,), fg='black', width=30,show="*",
                                     bg='white')
                newpassEntry.place(x=60, y=440)

                changepassbutton = Button(root2, text='Change Password', font=('arial', 17, 'bold'), bg='#009973',
                                          fg='white', cursor='hand2', activebackground='#009973',
                                          activeforeground='white', command=reset_password)
                changepassbutton.place(x=130, y=500)

                root2.mainloop()

        except Exception as e:
            showerror('Error', f"Error due to: {e}", parent=root)


def register_window():
    root.destroy()
    import register


def signin():
    if mailentry.get() == '' or passentry.get() == '':
        showerror('Error', 'All Fields Are Required')

    else:
        try:
            con = mysql.connector.connect(host='localhost', user='root', password='root', database='doctors')
            cur = con.cursor()
            cur.execute('select * from user where email=%s and password=%s', (mailentry.get(), passentry.get()))
            row = cur.fetchone()
            if row == None:
                showerror('error', 'Invalid Email or Password')
            else:
                #showinfo('Success', 'Welcome to DocHouse')
                global mail
                global ee
                mail=row
                ee=mailentry.get()
                getinto()
                


            con.close()
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

frame = Frame(root, bg='white', width=560, height=320)
frame.place(x=320, y=140)

userimage = PhotoImage(file='user.png')
userimageLabel = Label(frame, image=userimage, bg='white')
userimageLabel.place(x=10, y=50)
mailLabel = Label(frame, text='Email', font=('arial', 22, 'bold'), bg='white', fg='black')
mailLabel.place(x=220, y=32)
mailentry = Entry(frame, font=('arial', 22,), bg='white', fg='black')
mailentry.place(x=220, y=70)

passLabel = Label(frame, text='Password', font=('arial', 22, 'bold'), bg='white', fg='black')
passLabel.place(x=220, y=120)
passentry = Entry(frame, font=('arial', 22,), bg='white', fg='black',show="*")
passentry.place(x=220, y=160)
regbutton = Button(frame, text='Register New Account?', font=('arial', 12,), bd=0, fg='gray20', bg='white',
                   cursor='hand2', command=register_window,
                   activebackground='white', activeforeground='gray20')
regbutton.place(x=220, y=200)

forgetbutton = Button(frame, text='Forget Password?', font=('arial', 12,), bd=0, fg='#009973', bg='white',
                      cursor='hand2', command=forget_password,
                      activebackground='white', activeforeground='gray20')
forgetbutton.place(x=410, y=200)

loginbutton2 = Button(frame, text='Login', font=('arial', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                      activebackground='gray20', activeforeground='white', command=signin)
loginbutton2.place(x=450, y=240)
root.mainloop()


