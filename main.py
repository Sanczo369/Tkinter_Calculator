from tkinter import *
import math
root = Tk()
root.iconbitmap('logo.ico')
root.title("Calculator")

# Make the window resizable false
root.resizable(False,False)

#Menu
mainMenu=Menu()
root.config(menu=mainMenu)
fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="File",menu=fileMenu)
editMenu=Menu(mainMenu)
mainMenu.add_cascade(label="Edit",menu=editMenu)
viewMenu=Menu(mainMenu)
mainMenu.add_cascade(label="View",menu=viewMenu)
def onClick(number):
    current=e_result.get()
    e_result.delete(0,END)
    e_result.insert(0,current+str(number))
def Clear():
    e_result.delete(0, END)
def btn_add():
    global equation
    global number_one
    equation="+"
    number_one=float(e_result.get())
    e_result.delete(0,END)
def btn_sub():
    global equation
    global number_one
    equation="-"
    number_one=float(e_result.get())
    e_result.delete(0,END)
def btn_div():
    global equation
    global number_one
    equation="/"
    number_one=float(e_result.get())
    e_result.delete(0,END)
def btn_multi():
    global equation
    global number_one
    equation="*"
    number_one=float(e_result.get())
    e_result.delete(0,END)
def btn_result():
    global number_one
    number_two=e_result.get()
    e_result.delete(0,END)
    if equation == "+":
        e_result.insert(0,str(round(number_one + float(number_two), 13)))
    elif equation == "-":
        e_result.insert(0,str(round(number_one - float(number_two), 13)))
    elif equation == "*":
        e_result.insert(0,str(round(number_one * float(number_two), 13)))
    elif equation == "/":
        e_result.insert(0,str(round(number_one / float(number_two), 13)))
    elif equation == "xy":
        e_result.insert(0,str(round(number_one ** float(number_two), 13)))
def btn_proc():
    global number_one
    number_two=float(e_result.get())
    resul=(number_one*number_two)/100
    e_result.delete(0,END)
    e_result.insert(0,str(resul))
def btn_pi():
    e_result.delete(0,END)
    e_result.insert(0,str(round(math.pi, 13)))
def btn_e():
    e_result.delete(0,END)
    e_result.insert(0,str(round(math.e, 13)))
def btn_abs():
    current = float(e_result.get())
    e_result.delete(0,END)
    e_result.insert(0,str(round(abs(current), 13)))
def btn_n():
    current=int(e_result.get())
    e_result.delete(0,END)
    result=1
    for i in range(1,current+1):
        result*=i
    e_result.insert(0,str(result))
def btn_ln():
    current = int(e_result.get())
    e_result.delete(0,END)
    e_result.insert(0,str(round(math.log(current), 13)))
def btn_log():
    current = int(e_result.get())
    e_result.delete(0,END)
    e_result.insert(0,str(round(math.log10(current), 13)))
def btn_tenx():
    current=int(e_result.get())
    e_result.delete(0,END)
    result=1
    for i in range(current):
        result*=10
    e_result.insert(0,str(result))
def btn_x():
    current=int(e_result.get())
    e_result.delete(0,END)
    e_result.insert(0,str(round(current**2, 13)))
def btn_xy():
    global equation
    global number_one
    equation="xy"
    number_one=float(e_result.get())
    e_result.delete(0,END)
def btn_ex():
    current=int(e_result.get())
    e_result.delete(0,END)
    e_result.insert(0,str(round(math.e**current, 13)))
def btn_sin():
    current = float(e_result.get())
    e_result.delete(0,END)
    e_result.insert(0,str(round(math.sin(current), 13)))
def btn_cos():
    current = float(e_result.get())
    e_result.delete(0,END)
    e_result.insert(0,str(round(math.cos(current), 13)))
def btn_tg():
    current = float(e_result.get())
    e_result.delete(0,END)
    e_result.insert(0,str(round(math.tan(current), 13)))
def btn_ctg():
    current = float(e_result.get())
    e_result.delete(0,END)
    e_result.insert(0,str(round(1/math.tan(current), 13)))
def btn_sqrt():
    current = float(e_result.get())
    e_result.delete(0,END)
    e_result.insert(0,str(round(math.sqrt(current), 13)))


def btn_length():
    tab=[39.37008,3.28084,1.093613,0.000621,0.00054]
    current = float(e_length.get())
    l_cale = Label(frameLength, height=2, width=12, text="Cale ="+str(round(tab[0]*current,4)))
    l_stopy = Label(frameLength, height=2, width=12, text="Stopy ="+str(round(tab[1]*current,4)))
    l_jardy = Label(frameLength, height=2, width=12, text="Jardy ="+str(round(tab[2]*current,4)))
    l_mile = Label(frameLength, height=2, width=12, text="Mile ="+str(round(tab[3]*current,4)))
    l_mileM = Label(frameLength, height=2, width=12, text="Mile Morskie ="+str(round(tab[4]*current,4)))
    l_cale.grid(row=2, columnspan=2)
    l_stopy.grid(row=3, columnspan=2)
    l_jardy.grid(row=4, columnspan=2)
    l_mile.grid(row=5, columnspan=2)
    l_mileM.grid(row=6, columnspan=2)

# Define Element
e_result = Entry(root, bg="#FFF", width=5, font=("Arial",20))
btn_1 = Button(root,height= 2, width=5, text="1", command=lambda:onClick(1))
btn_2 = Button(root,height= 2, width=5, text="2", command=lambda:onClick(2))
btn_3 = Button(root,height= 2, width=5, text="3", command=lambda:onClick(3))
btn_4 = Button(root,height= 2, width=5, text="4", command=lambda:onClick(4))
btn_5 = Button(root,height= 2, width=5, text="5", command=lambda:onClick(5))
btn_6 = Button(root,height= 2, width=5, text="6", command=lambda:onClick(6))
btn_7 = Button(root,height= 2, width=5, text="7", command=lambda:onClick(7))
btn_8 = Button(root,height= 2, width=5, text="8", command=lambda:onClick(8))
btn_9 = Button(root,height= 2, width=5,text="9", command=lambda:onClick(9))
btn_0 = Button(root,height= 2, width=5, text="0", command=lambda:onClick(0))
btn_00 = Button(root,height= 2, width=5, text="00", command=lambda:onClick("00"))
btn_add = Button(root,height= 2, width=5, text="+", command=btn_add)
btn_sub = Button(root,height= 2, width=5, text="-", command=btn_sub)
btn_div = Button(root,height= 2, width=5, text="/", command=btn_div)
btn_multi = Button(root,height= 2, width=5, text="*", command=btn_multi)
btn_clear = Button(root,height= 2, width=5, text="C", command=Clear)
btn_off = Button(root,height= 2, width=5, text="OFF", command=root.quit)
btn_result = Button(root,height= 2, width=5, text="=", command=btn_result)
btn_proc = Button(root,height= 2, width=5, text="%", command=btn_proc)
btn_dot = Button(root,height= 2, width=5, text=",", command=lambda:onClick("."))
btn_ln = Button(root,height= 2, width=5, text="ln", command=btn_ln)
btn_log = Button(root,height= 2, width=5, text="log", command=btn_log)
btn_tenx = Button(root,height= 2, width=5, text="10^", command=btn_tenx)
btn_x = Button(root,height= 2, width=5, text="x^2", command=btn_x)
btn_pi = Button(root,height= 2, width=5, text="π", command=btn_pi)
btn_e = Button(root,height= 2, width=5, text="e", command=btn_e)
btn_abs = Button(root,height= 2, width=5, text="|x|", command=btn_abs)
btn_n = Button(root,height= 2, width=5, text="n!", command=btn_n)
btn_xy = Button(root,height= 2, width=5, text="x^y", command=btn_xy)
btn_ex = Button(root,height= 2, width=5, text="e^x", command=btn_ex)

# LabelFrame "Trigonometric Functions"
frameTrino=LabelFrame(root,text="Trigonometric Functions",padx=5, pady=5)
btn_sin = Button(frameTrino,height= 2, width=5, text="sin()", command=btn_sin)
btn_cos = Button(frameTrino,height= 2, width=5, text="cos()", command=btn_cos)
btn_tg = Button(frameTrino,height= 2, width=5, text="tg()", command=btn_tg)
btn_ctg = Button(frameTrino,height= 2, width=5, text="ctg()", command=btn_ctg)
# btn_sqrt = Button(root,height= 2, width=5, text="√x", command=btn_sqrt)


# LabelFrame "Length Conversion"
frameLength=LabelFrame(root,text="Length Conversion",padx=5, pady=5)
l_length = Label(frameLength,height= 2, width=5, text="Metry= ")
e_length = Entry(frameLength, bg="#FFF", width=5, font=("Arial",10))
btn_length = Button(frameLength,height= 1, width=12, text="Convert", command=btn_length)

# LabelFrame "Weight Conversion"
frameWeight=LabelFrame(root,text="Weight Conversion",padx=5, pady=5)
l_weight = Label(frameWeight,height= 2, width=5, text="Kg= ")
e_weight = Entry(frameWeight, bg="#FFF", width=5, font=("Arial",10))
btn_weight = Button(frameWeight,height= 1, width=12, text="Convert")



# Element Position
e_result.grid(row=0, column=0,columnspan=5, sticky=W+E)

btn_abs.grid(row=1, column=0)
btn_n.grid(row=1, column=1)
btn_pi.grid(row=1, column=2)
btn_e.grid(row=1, column=3)
btn_ex.grid(row=1, column=4)

btn_x.grid(row=2, column=0)
btn_off.grid(row=2, column=1)
btn_clear.grid(row=2, column=2)
btn_proc.grid(row=2, column=3)
btn_div.grid(row=2, column=4)

btn_xy.grid(row=3, column=0)
btn_7.grid(row=3, column=1)
btn_8.grid(row=3, column=2)
btn_9.grid(row=3, column=3)
btn_multi.grid(row=3, column=4)

btn_tenx.grid(row=4, column=0)
btn_4.grid(row=4, column=1)
btn_5.grid(row=4, column=2)
btn_6.grid(row=4, column=3)
btn_sub.grid(row=4, column=4)

btn_log.grid(row=5, column=0)
btn_1.grid(row=5, column=1)
btn_2.grid(row=5, column=2)
btn_3.grid(row=5, column=3)
btn_add.grid(row=5, column=4)

btn_ln.grid(row=6, column=0)
btn_0.grid(row=6, column=1)
btn_00.grid(row=6, column=2)
btn_dot.grid(row=6, column=3)
btn_result.grid(row=6, column=4)

frameTrino.grid(row=7, columnspan=5)
btn_sin.grid(row=0, column=0)
btn_cos.grid(row=0, column=1)
btn_tg.grid(row=0, column=2)
btn_ctg.grid(row=0, column=3)
# btn_sqrt.grid(row=7, column=4)

frameLength.grid(row=8, column=0)
l_length.grid(row=0, column=0)
e_length.grid(row=0, column=1, sticky=W+E)
btn_length.grid(row=1, columnspan=2)

frameWeight.grid(row=8, column=1)
l_weight.grid(row=0, column=0)
e_weight.grid(row=0, column=1, sticky=W+E)
btn_weight.grid(row=1, columnspan=2)

if __name__ == '__main__':
    root.mainloop()
