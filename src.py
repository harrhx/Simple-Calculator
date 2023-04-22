from tkinter import *
root = Tk()
click = 0
procedure = ""
root.title("Simple Calculator")
root.geometry("272x315")
root.maxsize(272,315)
root.minsize(272,315)
root.configure(bg="#FFFFFF")
root.iconbitmap(r'C:\Users\Harshit Ranjan\Desktop\1st Year\tkinter\calculator.ico')

e = Entry(root, width=18,borderwidth=1,font=('Arial',20))
e.grid(row=0, column=0, columnspan=4)

def button_click(number):
    first = e.get()
    e.delete(0, END)
    e.insert(0, str(first) + str(number))
    

def button_add():
    first_num = e.get()
    
    global f_num
    global procedure
    procedure = "add"
    f_num = first_num
    e.delete(0, END)

def button_substract():
    first_num = e.get()
    global f_num
    global procedure
    procedure = "substract"
    f_num = float(first_num)
    e.delete(0, END)

def button_divide():
    first_num = e.get()
    global f_num
    global procedure
    procedure = "divide"
    f_num = float(first_num)
    e.delete(0, END)

def button_multiply():
    first_num = e.get()
    global f_num
    global procedure
    procedure = "multiply"
    f_num = float(first_num)
    e.delete(0, END)
 
def button_clear():
    e.delete(0, END)

def button_equal():
    global click
    click = click + 1
    second_num = e.get()
    global s_num
    e.delete(0, END)
    if procedure == "add":
        s_num = float(second_num)
        e.insert(0, float(f_num) + s_num)
        click = 0
    elif procedure == "substract":
        s_num = float(second_num)
        e.insert(0, float(f_num) - s_num)
        click = 0
    elif procedure == "divide":
        s_num = float(second_num)
        e.insert(0, (float(f_num))/(s_num))
        click = 0
    elif procedure == "multiply":
        s_num = float(second_num)
        e.insert(0, float(f_num) * s_num)
        click = 0
    elif procedure == "":
        pass
    
    else:
        e.delete()
    
label1 = Label(root, text="1",foreground="white")



mybutton0 = Button(root, text="0",padx=59, pady=15,command=lambda: button_click("0"),bg="White",fg="Black")
mybutton1 = Button(root, text="1",padx=25, pady=15,command=lambda: button_click('1'),bg="White",fg="Black")
mybutton2 = Button(root, text="2",padx=25, pady=15,command=lambda: button_click('2'),bg="White",fg="Black")
mybutton3 = Button(root, text="3",padx=25, pady=15,command=lambda: button_click('3'),bg="White",fg="Black")
mybutton4 = Button(root, text="4",padx=25, pady=15,command=lambda: button_click('4'),bg="White",fg="Black")
mybutton5 = Button(root, text="5",padx=25, pady=15,command=lambda: button_click('5'),bg="White",fg="Black")
mybutton6 = Button(root, text="6",padx=25, pady=15,command=lambda: button_click('6'),bg="White",fg="Black")
mybutton7 = Button(root, text="7",padx=25, pady=15,command=lambda: button_click('7'),bg="White",fg="Black")
mybutton8 = Button(root, text="8",padx=25, pady=15,command=lambda: button_click('8'),bg="White",fg="Black")
mybutton9 = Button(root, text="9",padx=25, pady=15,command=lambda: button_click('9'),bg="White",fg="Black")
mybutton_add = Button(root, text="+",font = ('Arial',15),padx=20, pady=37,command=button_add,bg="#F1C1F8",fg="#D902F9")
mybutton_substract = Button(root, text="-",font = ('Arial',15),padx=22, pady=9,command=button_substract,bg="#F1C1F8",fg="#D902F9")
mybutton_divide = Button(root, text="÷",font = ('Arial',15),padx=20, pady=9,command=button_divide,bg="#F1C1F8",fg="#D902F9")
mybutton_multiply = Button(root, text="×",font = ('Arial',15),padx=20, pady=9,command=button_multiply,bg="#F1C1F8",fg="#D902F9")
mybutton_decimal = Button(root, text=".",font=('Arial',15),padx=22, pady=8,command=lambda: button_click("."),bg="#F1C1F8",fg="#D902F9")
mybutton_equal = Button(root, text="=",font = ('Arial',15),padx=54, pady=8,command=button_equal,bg="#66F9B1",fg="Black")
mybutton_clear = Button(root, text="C",padx=25, pady=15,command=button_clear,bg="#FDC167",fg="Red")

mybutton7.grid(row=1,column=0,columnspan=1)
mybutton8.grid(row=1,column=1)
mybutton9.grid(row=1,column=2)
mybutton_divide.grid(row=1,column=3) 

mybutton4.grid(row=2,column=0)
mybutton5.grid(row=2,column=1)
mybutton6.grid(row=2,column=2)
mybutton_multiply.grid(row=2,column=3)

mybutton1.grid(row=3,column=0)
mybutton2.grid(row=3,column=1)
mybutton3.grid(row=3,column=2)
mybutton_add.grid(row=4,column=3,rowspan=2)

mybutton0.grid(row=4,column=0,columnspan=2)
mybutton_decimal.grid(row=4,column=2)
mybutton_substract.grid(row=3,column=3)

mybutton_equal.grid(row=5,column=1,columnspan=2)
mybutton_clear.grid(row=5,column=0)

root.mainloop()














