from  tkinter import *
class Application(Frame):
    def __init__(self, root):
        super(Application, self,).__init__(root)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        Label(self, text='У кажите любимые жанры кино').grid(row=0, column=0, sticky=W)
        Label(self, text='Выберите все что вам по вкусу: ').grid(row=1, column=0, sticky=W)
        self.favorite=StringVar()
        self.favorite.set(None)
        Radiobutton(self, text='Комедия', variable=self.favorite, command=self.update_text, value='Комедия').grid(row=2, column=0, sticky=W)

        Radiobutton(self, text='Драма', variable=self.favorite, command=self.update_text, value='Драма').grid(row=3, column=0,sticky=W)

        Radiobutton(self, text='Романтика', variable=self.favorite, command=self.update_text, value='Романтика').grid(row=4, column=0,sticky=W)
        self.result_text=Text(self, width=40, height=5, wrap=WORD)
        self.result_text.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        likes = "Ваш любимый киножанр- "
        likes+=self.favorite.get()

        self.result_text.delete(0.0, END)
        self.result_text.insert(0.0, likes)
root = Tk()
root.title("Киноман 2")
app = Application(root)
root.mainloop()