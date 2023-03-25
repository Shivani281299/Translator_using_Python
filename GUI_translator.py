from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import googletrans
from googletrans import Translator

root=Tk()
root.title("Google Translator ")
root.geometry("1200x500")
root.resizable(False,False)
root.configure(background ="#f0f0f0")

def label_change():
    c =combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)

def translate_now():
    text_ =text1.get(1.0,END)
    t1 =Translator()
    trans_text=t1.translate(text_,src=combo1.get(),dest=combo2.get())
    trans_text=trans_text.text

    text2.delete(1.0,END)
    text2.insert(END,trans_text)


#icon
image_icon = PhotoImage(file ="google.png")
root.iconphoto(False,image_icon)


#arrow
arrow_image =PhotoImage(file="arrow.png")
# resized_arrow=arrow_image.resize((300,200))
# new_arrow=ImageTk.PhotoImage(resized_arrow)
image_label =Label(root,image=arrow_image,width=530,height=250)
image_label.place(x=320,y=100)

language = googletrans.LANGUAGES
languageV =list(language.values())
lang1=language.keys()

#first combobox
combo1 =ttk.Combobox(root,values =languageV,font="Roboto 14",state="r")
combo1.place(x=80,y=20)
combo1.set("ENGLISH")

label1=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)


#second combobox
combo2 =ttk.Combobox(root,values =languageV,font="Roboto 14",state="r")
combo2.place(x=850,y=20)
combo2.set("Select Language")

label2=Label(root,text="ENGLISH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=700,y=50)

#first frame
f = Frame(root,bg="black",bd=5)
f.place(x=10,y=118,width=440,height=210)

text1=Text(f,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


#second frame
f1 = Frame(root,bg="black",bd=5)
f1.place(x=700,y=118,width=440,height=210)

text2=Text(f1,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#translate button

translate =Button(root,text="Translate",font=("Roboto",15),activebackground="white",cursor="hand2",
                  bd=1,width=10,height=2,bg="black",fg="white",command=translate_now)
translate.place(x=510,y=250)



label_change()
root.mainloop()