from tkinter import *
root=Tk()
root.title('Окно')
root.geometry('1000x500')
app=Frame(root)
app.grid()
lbl=Label(app, text='текст')
lbl.grid()
butt=Button(app, text='я ничего не делаю')
butt.grid()
butt2=Button(app)
butt2.grid()
butt2.configure(text='я тоже')
butt3=Button(app)
butt3.grid()
butt3['text']='и я'

root.mainloop()