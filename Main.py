
from tkinter import*
from tkinter import ttk
from Functions import encode
from Functions import decode

het = 400
wih = 600

def Encall(mes,key):
    text = encode(mes,key)
    lab['text'] = 'Encrypted Cipher text: '+text

def Dcrcall(mes,key):
    text = decode(mes,key)
    lab['text'] = 'Decrypted Message: '+text

root = Tk()

root.title("Playfair_Cipher")
C = Canvas(root,height=het,width=wih)
C.pack()


fra = Frame(root,background='red',bd=5)
fra.place(relx=0.01, rely=0.05,relheight=1,relwidth=1)

l11 = Label(fra, text='Message:')
l11.place(relx=0.0001,rely = 0.1,relheight=0.8)

BI = PhotoImage(file='Cypher.png')
BL = Label(root,image=BI)
BL.place(relheight=1,relwidth=1)



fram = Frame(root,bd=5)
fram.place(relx=0.01, rely=0.1,relheight=0.1,relwidth=0.9755)

l1 = Label(fram, text='Message:')
l1.place(relx=0.0001,rely = 0.1,relheight=0.8)

Tex = Entry(fram)
Tex.place(relx = 0.115,rely = 0.1, relwidth=0.4,relheight=0.8)

l2 = Label(fram, text='Key:')
l2.place(relx=0.52,rely = 0.1,relheight=0.8)

Ke = Entry(fram)
Ke.place(relx = 0.57,rely = 0.1, relwidth=0.2,relheight=0.8)

B = Button(fram,text='Encrypt',command=lambda:Encall(Tex.get(),Ke.get()))
B.place(relx= 0.79,rely=0.1,relwidth=0.2,relheight=0.9)




fram1 = Frame(root,bd=5)
fram1.place(relx=0.01, rely=0.3,relheight=0.1,relwidth=0.9755)

l11 = Label(fram1, text='Cipher:')
l11.place(relx=0.0001,rely = 0.1,relheight=0.8)

Tex1 = Entry(fram1)
Tex1.place(relx = 0.115,rely = 0.1, relwidth=0.4,relheight=0.8)

l21 = Label(fram1, text='Key:')
l21.place(relx=0.52,rely = 0.1,relheight=0.8)

Ke1 = Entry(fram1)
Ke1.place(relx = 0.57,rely = 0.1, relwidth=0.2,relheight=0.8)

B1 = Button(fram1,text='Decrypt',command=lambda:Dcrcall(Tex1.get(),Ke1.get()))
B1.place(relx= 0.79,rely=0.1,relwidth=0.2,relheight=0.9)



out = Frame(root,bd=10)
out.place(relx=0.01,rely=0.5,relheight=0.4,relwidth=0.9755)

lab = Label(out,text='Your output will apprear here',bg='white',font=40)
lab.place(relwidth=1,relheight=1)

 
root.mainloop()

