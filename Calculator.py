import customtkinter as ctk
import tkinter
from sys import platform

mode='dark'
ctk.set_appearance_mode(mode)
global boxstate
boxstate='normal'
eqstate=False
operatorstate=False

wind=ctk.CTk()
wind.geometry("400x570")
wind.title("Calculator")
wind.iconbitmap("Graphics\calculator.ico")


global counter
counter=0.0
fontset=ctk.CTkFont('Sans Serif',30)
global modecount
modecount=1




frame=ctk.CTkFrame(master=wind,width=390,height=560,corner_radius=10,)
frame.pack(expand=True,padx=10, pady=10, side='top')
frame.place(x=5, y=1)



def butt1():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='1'
    global boxstate
    boxstate='normal'
    counter=counter+1.0
    output.insert(counter,text)


def butt2():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='2'
    counter=counter+1.0
    output.insert(counter,text)

def butt3():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='3'
    counter=counter+1.0
    output.insert(counter,text)

def butt4():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='4'
    counter=counter+1.0
    output.insert(counter,text)


def butt5():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='5'
    counter=counter+1.0
    output.insert(counter,text)


def butt6():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='6'
    counter=counter+1.0
    output.insert(counter,text)


def butt7():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='7'
    counter=counter+1.0
    output.insert(counter,text)


def butt8():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='8'
    counter=counter+1.0
    output.insert(counter,text)



def butt9():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='9'
    counter=counter+1.0
    output.insert(counter,text)



def butt0():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='0'
    counter=counter+1.0
    output.insert(counter,text)


def buttdiv():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='/'
    counter=counter+1.0
    output.insert(counter,text)


def buttmulti():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='*'
    counter=counter+1.0
    output.insert(counter,text)


def buttadd():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='+'
    counter=counter+1.0
    output.insert(counter,text)

def buttminus():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='-'
    counter=counter+1.0
    output.insert(counter,text)

def butteq():
    text='='
    global counter

    while True:
     try:
          
          calculate=eval((output.get('0.0',"end-1c")))
          counter=counter+1.0
          output.insert(counter,text)
          break
     except SyntaxError:
         print('syntax error')
         output.delete(0.0, tkinter.END)
         output.insert(0.0,'Syntax Error: \nInvalid Expression')
         break
    global eqstate
    eqstate=True
    counter=counter+1.0
    output.insert(counter,calculate)

def ac():
    global counter
    output.delete(0.0,counter)
    counter=0
    eqstate=False

def buttopen():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text='('
    counter=counter+1.0
    output.insert(counter,text)



def buttclose():
    global counter
    global eqstate
    if (counter!=0)and(eqstate==True):
        output.delete(0.0, tkinter.END)
        counter=0
        eqstate=False
    text=')'
    
    counter=counter+1.0
    output.insert(counter,text)

def buttmode():
    global modecount
    modecount=modecount+1
    global mode
    if (modecount%2==0):
        mode='light'
        ctk.set_appearance_mode(mode)
    else:
        mode='dark'
        ctk.set_appearance_mode(mode)

def sc():
    global operatorstate
    if (operatorstate==False):
      global toplevel
      toplevel = ctk.CTkToplevel()
      toplevel.title('Scientific Operator')
      toplevel.geometry ('300x300')
      toplevel.iconbitmap("Graphics\calculator.ico")
      operatorstate=True
      if platform.startswith("win"):
          toplevel.after(200, lambda: toplevel.iconbitmap("Graphics\calculator.ico"))
      tframe=ctk.CTkFrame(master=toplevel, width=280, height=280, corner_radius=10)
      tframe.pack(padx=10, pady=10)
      
      buttonabs=ctk.CTkButton(master=tframe, width=80, height=50, fg_color="grey",text="Abs(x)" ,hover_color="blue" ,)
      buttonabs.place(relx=0.06, rely=0.03)
      buttonexp=ctk.CTkButton(master=tframe, width=80, height=50, fg_color="grey",text="Exp(x) " ,hover_color="blue" ,)
      buttonexp.place(relx=0.36, rely=0.03)
      buttonpow=ctk.CTkButton(master=tframe, width=80, height=50, fg_color="grey",text="Pow(x,y) " ,hover_color="blue" ,)
      buttonpow.place(relx=0.66, rely=0.03)
      buttonsqrt=ctk.CTkButton(master=tframe, width=80, height=50, fg_color="grey",text="Sqrt(x)" ,hover_color="blue" ,)
      buttonsqrt.place(relx=0.06, rely=0.22)
      buttoncos=ctk.CTkButton(master=tframe, width=80, height=50, fg_color="grey",text="Cos(rad) " ,hover_color="blue" ,)
      buttoncos.place(relx=0.36, rely=0.22)
      buttonsin=ctk.CTkButton(master=tframe, width=80, height=50, fg_color="grey",text="Sin(rad)" ,hover_color="blue" ,)
      buttonsin.place(relx=0.66, rely=0.22)
      buttontan=ctk.CTkButton(master=tframe, width=80, height=50, fg_color="grey",text="Tan(rad)" ,hover_color="blue" ,)
      buttontan.place(relx=0.06, rely=0.41)
      buttondeg2rad=ctk.CTkButton(master=tframe, width=80, height=50, fg_color="grey",text="Rad(deg)" ,hover_color="blue" ,)
      buttondeg2rad.place(relx=0.36, rely=0.41)


      toplevel.protocol("WM_DELETE_WINDOW", closeoperator)


def closeoperator():
    global operatorstate
    operatorstate=False
    toplevel.destroy()





button1=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text="1" ,hover_color="blue", command=butt1 )

button1.place(relx=0.01, rely=0.28)
button1. bind(("<Return>") ,lambda event:butt1().focus())

button2=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text="2" ,hover_color="blue", command=butt2 )
button2.pack(fill="both", expand=True)
button2.place(relx=0.26, rely=0.28)

button3=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text="3" ,hover_color="blue" , command=butt3 )
button3.pack(fill="both", expand=True)
button3.place(relx=0.51, rely=0.28)

buttonminus=ctk.CTkButton(master=frame, width=90, height=70, fg_color="orange",text="-" ,hover_color="blue", font=fontset, command=buttminus  )
buttonminus.pack(fill="both", expand=True)
buttonminus.place(relx=0.76, rely=0.28)

button4=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text="4" ,hover_color="blue" , command=butt4 )
button4.pack(fill="both", expand=True)
button4.place(relx=0.01, rely=0.415)

button5=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text="5" ,hover_color="blue", command=butt5  )
button5.pack(fill="both", expand=True)
button5.place(relx=0.26, rely=0.415)

button6=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text="6" ,hover_color="blue", command=butt6  )
button6.pack(fill="both", expand=True)
button6.place(relx=0.51, rely=0.415)

buttonadd=ctk.CTkButton(master=frame, width=90, height=70, fg_color="orange",text="+" ,hover_color="blue", font=fontset, command=buttadd )
buttonadd.pack(fill="both", expand=True)
buttonadd.place(relx=0.76, rely=0.415)

buttondiv=ctk.CTkButton(master=frame, width=90, height=70, fg_color="orange",text="/" ,hover_color="blue", font=fontset, command=buttdiv )
buttondiv.pack(fill="both", expand=True)
buttondiv.place(relx=0.76, rely=0.5525)

button8=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text="8" ,hover_color="blue", command=butt8  )
button8.pack(fill="both", expand=True)
button8.place(relx=0.51, rely=0.5525)

button9=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text="9" ,hover_color="blue", command=butt9  )
button9.pack(fill="both", expand=True)
button9.place(relx=0.26, rely=0.5525)

button7=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text="7" ,hover_color="blue" , command=butt7 )
button7.pack(fill="both", expand=True)
button7.place(relx=0.01, rely=0.5525)

button0=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text="0" ,hover_color="blue", command=butt0  )
button0.pack(fill="both", expand=True)
button0.place(relx=0.51, rely=0.69)

buttoneq=ctk.CTkButton(master=frame, width=90, height=70, fg_color="orange",text="=" ,hover_color="blue",font=fontset , command=butteq )
buttoneq.pack(fill="both", expand=True)
buttoneq.place(relx=0.76, rely=0.825)

buttonac=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text="AC" ,hover_color="blue" ,command=ac )
buttonac.pack(fill="both", expand=True)
buttonac.place(relx=0.26, rely=0.69)

buttonmulti=ctk.CTkButton(master=frame, width=90, height=70, fg_color="orange",text="*" ,hover_color="blue",font=fontset, command=buttmulti  )
buttonmulti.pack(fill="both", expand=True)
buttonmulti.place(relx=0.76, rely=0.69)

buttonmode=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text="Dark/Light" ,hover_color="blue", command=buttmode  )
buttonmode.pack(fill="both", expand=True)
buttonmode.place(relx=0.01, rely=0.69)

buttonopenbrac=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text="(" ,hover_color="blue" ,command=buttopen )
buttonopenbrac.pack(fill="both", expand=True)
buttonopenbrac.place(relx=0.26, rely=0.825)

buttonclosebrac=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text=")" ,hover_color="blue" ,command=buttclose )
buttonclosebrac.pack(fill="both", expand=True)
buttonclosebrac.place(relx=0.51, rely=0.825)

buttonsc=ctk.CTkButton(master=frame, width=90, height=70, fg_color="grey",text="Scientific" ,hover_color="blue" ,command=sc)
buttonsc.place(relx=0.01, rely=0.825)








print(boxstate)
output=ctk.CTkTextbox(master=frame, width=380, height=150, fg_color="grey", font=fontset, state=boxstate)
output.place(relx=0.01, rely=0.005)

wind.update()


wind.mainloop()

