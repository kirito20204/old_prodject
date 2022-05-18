from  tkinter import *
class Application(Frame):
    def __init__(self, root):
        super(Application, self,).__init__(root)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.inst_lbl=Label(self, text='чтобы узнать сикрет долголети введите пароль')
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)
        self.pw_lbl=Label(self, text='пароль: ')
        self.pw_lbl.grid(row=1, column=0, sticky=W)
        self.pw_ent=Entry(self)
        self.pw_ent.grid(row=1, column=1, sticky=W)
        self.bttn=Button(self, text='узнать секрет', command=self.reveal, width=100, height=10)
        self.bttn.grid(row=2, column=0, sticky=W)
        self.secret_text=Text(self, width=100, height=10, wrap=WORD)
        self.secret_text.grid(row=3, column=0, columnspan=2, sticky=W)
    def reveal(self):
        content=self.pw_ent.get()
        if content=='22022007' or content=='22022007':
            message='Вот секрет того, как дожить до 100: дожить до 99, а затем быть ОЧЕНЬ осторожным.'
        else:
            message='Это неправильный пароль, поэтому я не могу поделиться с вами секретом.'
        self.secret_text.delete(0.0, END)
        self.secret_text.insert(index=0.0, chars=message)
root=Tk()
root.title('долгожитель')
root.geometry('600x300')
app=Application(root)
root.mainloop()
