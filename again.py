from tkinter import Tk, Button, Frame, StringVar
from tkinter.ttk import Combobox
from tkinter import *
from tkinter import ttk
from tkinter import Tk, StringVar
import mysql.connector
from tkinter.messagebox import *
from login import mail


options = {"Cairo": ["Family medicin Dr.Maryam Montaser", "Family medicin Dr.Moatez Elshinawy", "Emergency medicine Dr.Haithm Ashour",\
        "Emergency medicine Dr.Osama Swidan","Internal medicine Dr.Ehab Elzayat","Internal medicine Dr.Mona Naser",\
            "Rheumatology Dr.Ahmed Lotfy","Rheumatology Dr.Muhammed Huseein ","Otorhinolaryngology Dr.Saad Elhussiny",\
                "Otorhinolaryngology Dr.Mark Emmanuel"],
    "Giza": ["Family medicin Dr.Fawzy Elsyaed", "Family medicin Dr.Peter Jacob", "Emergency medicine Dr.Rana Mosad",\
        "Emergency medicine Dr. Mostafa Hafez","Internal medicine Dr.Ahmed Mansour","Internal medicine Dr.Emam Elmorsy",\
            "Rheumatology Dr.Mahmoud Tantawi","Rheumatology Dr.Mai Mohab","Otorhinolaryngology Dr.Aya Mostafa",\
                "Otorhinolaryngology Dr.mayada Nasr"],
    "Alexandria": ["Family medicin Dr.Amira elsayed","Family medicin Dr.Radwan Al Rifai","Emergency medicine Dr.Eslam Muzffar",\
        "Emergency medicine Dr.Eyad Hassan","Internal medicine Dr.Nada Ramadan","Internal medicine Dr.Muhammed abdelrahman",\
            "Rheumatology Dr.Abdelrahman Ashraf","Rheumatology Dr.Alaa Elsofany","Otorhinolaryngology Dr.Daniel Raphael"\
                ,"Otorhinolaryngology Dr.Akram Montaer"],
    "Gharbiya":["Family medicin Dr.Ramzy Ramadan","Family medicin Dr.Shaima Mabrouk","Emergency medicine Dr.Zeyad Sultan"\
        ,"Emergency medicine Dr.Diana Selim","Internal medicine Dr.Tasneem Ashraf","Internal medicine Dr.Nour Gomaa"\
            ,"Rheumatology Dr.Ibrahim Al Gendy","Rheumatology Dr.Mark Allam","Otorhinolaryngology Dr.Diab El Shazly"\
                ,"Otorhinolaryngology Dr.Ahmed Tawfik"],
    "Dakahlia":["Family medicin Dr.Gamal Tawfik","Family medicin Dr.Basel Muhammed","Emergency medicine Dr.Hossam Khalil"\
        ,"Emergency medicine Dr. Hamza Hammad","Internal medicine Dr.Sameh Baha","Internal medicine Dr.Mary Isaac"\
            ,"Rheumatology Dr.Ebrahim Fawaz","Rheumatology Dr.Hassan Elshazily","Otorhinolaryngology Dr.Esraa Madbouly"\
                ,"Otorhinolaryngology Dr.Muhammed Abo zaid"]}


def get_var_1(event):
    value = cb1_var.get()
    cb2_var.set(options[value][0])
    cb2.config(values=options[value])


def get_info():
    print(cb1_var.get(), cb2_var.get())


root = Tk()
img=PhotoImage(file='icon.png')
root.tk.call('wm','iconphoto',root._w,img)
root.title('DocHouse')  
root.geometry('1200x800')
bglogin = PhotoImage(file='bgg.png')
bgloginLabel = Label(root, image=bglogin)
bgloginLabel.place(x=0, y=0)
frame = Frame(root, bg='white', width=1200, height=50)
frame.place(x=0, y=0)
mailLabel = Label(frame, text='DocHouse', font=('times new roman', 22, 'bold'), bg='white', fg='black')
mailLabel.place(x=10, y=11)
frame = Frame(root, bg='white', width=700, height=450)
frame.place(x=240, y=140)
print(mail)

# cb_frame = Frame(root)
# cb_frame.pack(side='left')

cb1_values = list(options.keys())

cb1_var = StringVar()
cb1_var.set(cb1_values[0])
cb1 = Combobox(frame, values=list(options.keys()), textvariable=cb1_var,state='readonly')
cb1.place(x=20,y=30, width=220)
cb1.bind('<<ComboboxSelected>>', get_var_1)


cb2_var = StringVar()
cb2_var.set(options[cb1_values[0]][0])
cb2 = Combobox(frame, values=options[cb1_values[0]], textvariable=cb2_var,state='readonly')
cb2.place(x=20,y=150, width=200)


# btn_frame = Frame(root)
# btn_frame.pack(side='right')
# Button(btn_frame, text='Confirm', command=get_info).pack()

def old():
    window.destroy()
    import database


def submit():
       if enter1.get() == '' or var.get() == '' or combo4.get() == 'Select' or combo5.get() == 'Select' \
           or combo2.get() == 'Select':
               showerror('Error', "All Fields Are Required", parent=root)
       else: 
           try:
               con = mysql.connector.connect(host='localhost', user='root', password='root', database='doctors')
               cur = con.cursor()
               cur.execute('insert into userschoice(governorate,specialization,address,gender,day,cost,age,email) \
                           values(%s,%s,%s,%s,%s,%s,%s,%s)', (cb1_var.get(), cb2_var.get(),enter1.get(), var.get(),combo4.get(),\
                                combo5.get(), combo2.get(),mail[4]))
               con.commit()
               con.close()
            #    l=Label(Frame1,text="In "+cb2_var.get()+" will be there in time",font=("times new roman",16,'bold')\
            #        ,bg='white')
            #    l.place(x=490,y=180)
            #    showinfo('Success', "Your order has been submitted, The doctor will be their on time", parent=root)
               root.destroy()
           except Exception as e:
               showerror('Error', f"Error due to: {e}", parent=root)   


dochello=PhotoImage(file='doc.png')
lable2=Label(frame,image=dochello,bg='white')
lable2.place(x=370,y=0)
label3=Label(frame,text="Governorate",font=("times new roman",16,'bold'),bg='white') 
label3.place(x=20,y=0) 
label4=Label(frame,text='The address in details',font=("times new roman",16,'bold'),bg='white') 
label4.place(x=20,y=60)  
enter1=Entry(frame,font=('times new roman',14),bd=2) 
enter1.place(x=20,y=90,width=200) 
label5=Label(frame,text="Specification",font=("times new roman",16,'bold'),bg='white') 
label5.place(x=20,y=120) 
var=IntVar() 
r1=ttk,Radiobutton(frame,text='male',font=("times new roman",14,'bold'),variable=var,value=1,bg='white').place(x=20,y=180) 
r1=ttk,Radiobutton(frame,text='female',font=("times new roman",14,'bold'),variable=var,value=2,bg='white').place(x=100,y=180) 
 
label6=Label(frame,text='Patient age',font=("times new roman",16,'bold'),bg='white').place(x=20,y=210) 
combo2= ttk.Combobox(frame, font=('times new roman', 14), state='readonly', justify=CENTER)
combo2['values'] = ('Select',1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,\
    33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70\
        ,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100)
combo2.current(0)
combo2.place(x=20,y=240, width=200)
label8=Label(frame,text='Day of the visit',font=("times new roman",16,'bold'),bg='white').place(x=20,y=270) 
combo4=ttk.Combobox(frame, font=('times new roman', 14), state='readonly', justify=CENTER)
combo4['values'] = ('Select','Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday')
combo4.current(0)
combo4.place(x=20,y=300, width=200) 
 
 
label9=Label(frame,text='Cost of the visit',font=("times new roman",16,'bold'),bg='white').place(x=20,y=330) 
combo5=ttk.Combobox(frame, font=('times new roman', 14), state='readonly', justify=CENTER)
combo5['values'] = ('Select',70,100,150,200,300,500,800,1000)
combo5.current(0)
combo5.place(x=20,y=360, width=200) 
 

submitb = PhotoImage(file='submit1.png')
button = Button(frame, image=submitb, cursor='hand2',bg='white',command=submit)
button.place(x=490, y=380)


root.mainloop()

window=Tk()
img=PhotoImage(file='icon.png')
window.tk.call('wm','iconphoto',window._w,img)
window.title('DocHouse')  
window.geometry('1200x800')
bglogin = PhotoImage(file='bgg.png')
bgloginLabel = Label(window, image=bglogin)
bgloginLabel.place(x=0, y=0)
Frame1 = Frame(window, bg='white', width=1200, height=200)
Frame1.place(x=0, y=300)
l=Label(Frame1,text="In "+cb2_var.get()+" will be there in time",font=("times new roman",25,'bold')\
       ,bg='white')
l.place(x=170,y=40)
b2 = Label(Frame1, text='Thank you for using DocHouse',font=('times new roman', 25, 'bold'), bg='white', fg='black')
b2.place(x=350, y=90)
be=Button(Frame1, text='Details', font=('times new roman', 18, 'bold'), fg='white', bg='gray20', cursor='hand2',
                      activebackground='gray20', activeforeground='white', command=old)
be.place(x=550,y=150)
window.mainloop()