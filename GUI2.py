from tkinter import  *
class Application(Frame):
    def __init__(self, root):
        super(Application, self).__init__(root)
        self.grid()
        self.butt_clicks=0
        self.create_widgets()
    def create_widgets(self):
        self.butt = Button(self, text='количество щелчков: 0')
        self.butt['command']=self.update_count
        self.butt.grid()
    def update_count(self):
        self.butt_clicks+=1
        self.butt['text']='количество щелчков: '+str(self.butt_clicks)
root=Tk()
root.title('Окно')
root.geometry('1000x500')
app=Application(root)
root.mainloop()
