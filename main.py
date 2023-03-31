from tkinter import *
root = Tk()
root.iconbitmap('logo.ico')
root.title("Calculator")

# Make the window resizable false
root.resizable(False,False)
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
        e_result.insert(0,str(number_one + float(number_two)))
    elif equation == "-":
        e_result.insert(0,str(number_one - float(number_two)))
    elif equation == "*":
        e_result.insert(0,str(number_one * float(number_two)))
    elif equation == "/":
        e_result.insert(0,str(number_one / float(number_two)))

def btn_proc():
    global number_one
    number_two=float(e_result.get())
    resul=(number_one*number_two)/100
    e_result.delete(0,END)
    e_result.insert(0,str(resul))

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
btn_add = Button(root,height= 5, width=5, text="+", command=btn_add)
btn_sub = Button(root,height= 2, width=5, text="-", command=btn_sub)
btn_div = Button(root,height= 2, width=5, text="/", command=btn_div)
btn_multi = Button(root,height= 2, width=5, text="*", command=btn_multi)
btn_clear = Button(root,height= 2, width=5, text="C", command=Clear)
btn_off = Button(root,height= 2, width=5, text="OFF", command=root.quit)
btn_result = Button(root,height= 2, width=5, text="=", command=btn_result)
btn_proc = Button(root,height= 2, width=5, text="%", command=btn_proc)
btn_dot = Button(root,height= 2, width=5, text=",", command=lambda:onClick("."))

btn_ln = Button(root,height= 2, width=5, text="ln", command=root.quit)
btn_log = Button(root,height= 2, width=5, text="log", command=root.quit)
btn_tenx = Button(root,height= 2, width=5, text="10^", command=root.quit)
btn_x = Button(root,height= 2, width=5, text="x^2", command=root.quit)
btn_pi = Button(root,height= 2, width=5, text="π", command=root.quit)
btn_e = Button(root,height= 2, width=5, text="e", command=root.quit)
btn_abs = Button(root,height= 2, width=5, text="|x|", command=root.quit)
btn_n = Button(root,height= 2, width=5, text="n!", command=root.quit)
btn_xy = Button(root,height= 2, width=5, text="x^y", command=root.quit)
btn_ex = Button(root,height= 2, width=5, text="e^x", command=root.quit)

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
btn_add.grid(row=5, column=4, rowspan=2)

btn_ln.grid(row=6, column=0)
btn_0.grid(row=6, column=1)
btn_dot.grid(row=6, column=2)
btn_result.grid(row=6, column=3)


if __name__ == '__main__':
    root.mainloop()
