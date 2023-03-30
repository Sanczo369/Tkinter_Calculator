from tkinter import *
root = Tk()
root.iconbitmap('logo.ico')
root.title("Calculator")
def onClick():
    pass


# Define Element
label_result = Label(root, text="      ")
btn_1 = Button(root, text="1", command=onClick)
btn_2 = Button(root, text="2", command=onClick)
btn_3 = Button(root, text="3", command=onClick)
btn_4 = Button(root, text="4", command=onClick)
btn_5 = Button(root, text="5", command=onClick)
btn_6 = Button(root, text="6", command=onClick)
btn_7 = Button(root, text="7", command=onClick)
btn_8 = Button(root, text="8", command=onClick)
btn_9 = Button(root, text="9", command=onClick)
btn_0 = Button(root, text="0", command=onClick)
btn_add = Button(root, text="+", command=onClick)
btn_sub = Button(root, text="-", command=onClick)
btn_div = Button(root, text="/", command=onClick)
btn_multi = Button(root, text="*", command=onClick)
btn_clear = Button(root, text="C", command=onClick)
btn_off = Button(root, text="OFF", command=onClick)
btn_result = Button(root, text="=", command=onClick)
btn_proc = Button(root, text="%", command=onClick)
btn_dot = Button(root, text=",", command=onClick)

# Element Position
label_result.grid(row=0, column=0)

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
btn_add.grid(row=4, column=3)

btn_0.grid(row=5, column=0)
btn_dot.grid(row=5, column=1)
btn_result.grid(row=5, column=2)


if __name__ == '__main__':
    root.mainloop()
