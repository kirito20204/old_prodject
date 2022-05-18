from  tkinter import *
class Application(Frame):
    def __init__(self, root):
        super(Application, self,).__init__(root)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        Label(self, text='У кажите любимые жанры кино').grid(row=0, column=0, sticky=W)
        Label(self, text='Выберите все что вам по вкусу: ').grid(row=1, column=0, sticky=W)
        self.likes_comedy=BooleanVar()
        Checkbutton(self, text='Камедия', variable=self.likes_comedy, command=self.update_text).grid(row=2, column=0, sticky=W)
        self.likes_drama = BooleanVar()
        Checkbutton(self, text='Драма', variable=self.likes_drama, command=self.update_text).grid(row=3, column=0,sticky=W)
        self.likes_romance = BooleanVar()
        Checkbutton(self, text='Романтика', variable=self.likes_romance, command=self.update_text).grid(row=4, column=0,sticky=W)
        self.result_text=Text(self, width=40, height=5, wrap=WORD)
        self.result_text.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        likes = ""

        if self.likes_comedy.get():
            likes += "Тебе нравится комедия\n"

        if self.likes_drama.get():
            likes += "Ты любишь драму\n"

        if self.likes_romance.get():
            likes += "Тебе нравятся романтические фильмы"

        self.result_text.delete(0.0, END)
        self.result_text.insert(0.0, likes)
root = Tk()
root.title("Киноман")
app = Application(root)
root.mainloop()