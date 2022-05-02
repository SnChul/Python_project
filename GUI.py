from tkinter import*

home = Tk()
home.title("HOME GUI") #창 이름 
home.geometry("640x480") #가로 x 세로
home.geometry("640x480+1000+500") 
#가로 x 세로 + X좌표 +Y좌표
home.resizable(False, False) #x y 값 변경불가

button1 = Button(home, text="sign")
button1.pack()
#padx 가로 pady 세로
button2 = Button(home, padx=5, pady=10 , text="register")
button2.pack()
button3 = Button(home, fg="red", bg="yellow", width=10,height=3,text="b4")
button3.pack()
home.mainloop()