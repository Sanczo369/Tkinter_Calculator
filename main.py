from tkinter import *
root = Tk()
root.iconbitmap('logo.ico')
root.title("Calculator")

# Make the window resizable false
root.resizable(False,False)
def onClick(number):
    global number_one
    number_one=e_result.get()+str(number)
    e_result.delete(0,END)
    e_result.insert(0,number_one)

def Clear():
    e_result.delete(0, END)

def btn_add():
    pass
def btn_sub():
    pass
def btn_div():
    pass
def btn_multi():
    pass
def btn_result():
    pass
def btn_proc():
    pass


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
btn_dot = Button(root,height= 2, width=5, text=",", command=lambda:onClick(","))

# Element Position
e_result.grid(row=0, column=0,columnspan=4, sticky=W+E)

btn_off.grid(row=1, column=0)
btn_clear.grid(row=1, column=1)
btn_proc.grid(row=1, column=2)
btn_div.grid(row=1, column=3)

btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_multi.grid(row=2, column=3)

btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_sub.grid(row=3, column=3)

btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_add.grid(row=4, column=3, rowspan=2)

btn_0.grid(row=5, column=0)
btn_dot.grid(row=5, column=1)
btn_result.grid(row=5, column=2)


if __name__ == '__main__':
    root.mainloop()
