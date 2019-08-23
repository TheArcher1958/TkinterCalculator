import tkinter

top = tkinter.Tk()
top.geometry("200x300")
top.title("Calculator")
top.focus_force()

titleEntry = tkinter.Entry(top, width=21)
titleEntry.place(x=0, y=10)

def callInNumber(num):
    titleEntry.insert(len(titleEntry.get()), str(num))
def sum():
    theSum = eval(titleEntry.get())
    titleEntry.delete(0, len(titleEntry.get()))
    print(str(theSum))
    titleEntry.insert(0, str(theSum))
def clearEntry():
    titleEntry.delete(0, len(titleEntry.get()))
def deleteEntry():
    titleEntry.delete(len(titleEntry.get()) -1, len(titleEntry.get()))
def createButtons():
    myButton7 = tkinter.Button(top, text="7", width=5, height=3, command=lambda: callInNumber(7))
    myButton7.place(x=(0 * 50), y=(1 * 50))

    myButton4 = tkinter.Button(top, text="4", width=5, height=3, command=lambda: callInNumber(4))
    myButton4.place(x=(0 * 50), y=(2 * 50))

    myButton1 = tkinter.Button(top, text="1", width=5, height=3, command=lambda: callInNumber(1))
    myButton1.place(x=(0 * 50), y=(3 * 50))

    myButton0 = tkinter.Button(top, text="0", width=5, height=3, command=lambda: callInNumber(0))
    myButton0.place(x=(0 * 50), y=(4 * 50))

    myButton8 = tkinter.Button(top, text="8", width=5, height=3, command=lambda: callInNumber(8))
    myButton8.place(x=(1 * 50), y=(1 * 50))

    myButton5 = tkinter.Button(top, text="5", width=5, height=3, command=lambda: callInNumber(5))
    myButton5.place(x=(1 * 50), y=(2 * 50))

    myButton2 = tkinter.Button(top, text="2", width=5, height=3, command=lambda: callInNumber(2))
    myButton2.place(x=(1 * 50), y=(3 * 50))

    myButtonPer = tkinter.Button(top, text=".", width=5, height=3, command=lambda: callInNumber("."))
    myButtonPer.place(x=(1 * 50), y=(4 * 50))

    myButton9 = tkinter.Button(top, text="9", width=5, height=3, command=lambda: callInNumber(9))
    myButton9.place(x=(2 * 50), y=(1 * 50))

    myButton6 = tkinter.Button(top, text="6", width=5, height=3, command=lambda: callInNumber(6))
    myButton6.place(x=(2 * 50), y=(2 * 50))

    myButton3 = tkinter.Button(top, text="3", width=5, height=3, command=lambda: callInNumber(3))
    myButton3.place(x=(2 * 50), y=(3 * 50))

    myButtonEquals = tkinter.Button(top, text="=", width=5, height=3, command=lambda: sum())
    myButtonEquals.place(x=(2 * 50), y=(4 * 50))

    myButtonDiv = tkinter.Button(top, text="÷", width=5, height=3, command=lambda: callInNumber("/"))
    myButtonDiv.place(x=(3 * 50), y=(1 * 50))

    myButtonMult = tkinter.Button(top, text="×", width=5, height=3, command=lambda: callInNumber("*"))
    myButtonMult.place(x=(3 * 50), y=(2 * 50))

    myButtonPlus = tkinter.Button(top, text="+", width=5, height=3, command=lambda: callInNumber("+"))
    myButtonPlus.place(x=(3 * 50), y=(3 * 50))

    myButtonMinus = tkinter.Button(top, text="-", width=5, height=3, command=lambda: callInNumber("-"))
    myButtonMinus.place(x=(3 * 50), y=(4 * 50))

    myButtonClear = tkinter.Button(top, text="CLEAR", width=11, height=3, command=lambda: clearEntry())
    myButtonClear.place(x=(0 * 50), y=(5 * 50))

    myButtonDelete = tkinter.Button(top, text="< DELETE", width=11, height=3, command=lambda: deleteEntry())
    myButtonDelete.place(x=(2 * 50), y=(5 * 50))

createButtons()


top.mainloop()