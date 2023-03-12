from tkinter import *
from tkinter import messagebox


def clickButton():
    messagebox.showinfo("버튼 클릭", "버튼을 클릭했습니다.")


window = Tk()
window.geometry("200x200")

button1 = Button(window, text="여기 눌러요", fg="red", bg="yellow", command=clickButton)
button1.pack()

window.mainloop()
