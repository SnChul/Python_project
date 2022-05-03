from tkinter import*

home = Tk()
home.title("HOME GUI")

label1 = Label(home, text="hello")
label1.pack()

photo = PhotoImage(file="photo file/pubg.png")
label2 = Label(home, image=photo)
label2.pack()

def image():
    label1.config(text="goodjob")
    photo2 = PhotoImage(file="photo file/ph1.png")
    label2.config(image=photo2)
    photo2.pack()

btn = Button(home, text="click", command=image)
btn.pack()



home.mainloop()

