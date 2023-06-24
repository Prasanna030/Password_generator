from tkinter import *
import random,string
import json

root=Tk()
root.geometry("400x280")
root.title("Password Generator")

title=StringVar()
label=Label(root,textvariable=title).pack()
title.set("Strength of Password")

def selection():
    selection=choice.get()

choice=IntVar()
R1=Radiobutton(root,text="Poor",variable=choice,value=1,command=selection).pack(anchor=CENTER)
R1=Radiobutton(root,text="Average",variable=choice,value=2,command=selection).pack(anchor=CENTER)
R1=Radiobutton(root,text="Advanced",variable=choice,value=3,command=selection).pack(anchor=CENTER)

labelchoice=Label(root)
labelchoice.pack()

lenlabel=StringVar()
lenlabel.set("password length")
lentitle=Label(root,textvariable=lenlabel).pack()

val=IntVar()
spinlength=Spinbox(root,from_=8,to_=24,textvariable=val,width=13).pack()

def callback():
    generated_password = passgen()
    Isum.config(text=generated_password)
    save_password(generated_password)
    Isum_save.config(text="Password has been saved in the JSON file.")

passgenButton=Button(root,text="Generate Password",bd=5,height=2,command=callback,pady=3)
passgenButton.pack()
password=str(callback)

Isum=Label(root,text="")
Isum.pack(side=BOTTOM)

Isum_save = Label(root, text="")
Isum_save.pack(side=BOTTOM)



#logic
poor=string.ascii_uppercase+string.ascii_lowercase
average=string.ascii_uppercase+string.ascii_lowercase+string.digits

symbols="!@#$%^&*()~`."

advance=poor+average+symbols

def passgen():
    if choice.get()==1:
        return "".join(random.sample(poor,val.get()))
    elif choice.get()==2:
        return "".join(random.sample(average,val.get()))
    elif choice.get()==3:
        return "".join(random.sample(advance,val.get()))

def save_password(password):
    data = {
        "password": password
    }
    with open("passwords.json", "a") as file:
        json.dump(data, file)
        file.write("\n")
    

root.mainloop()



