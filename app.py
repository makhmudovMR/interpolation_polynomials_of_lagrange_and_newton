from tkinter import *


class MyApp:

    def __init__(self, master):
        self.master = master
        self.master.geometry("600x400")
        self.master.resizable(width=False, height=False)
        self.master.title("Интерполяционный многочлен Лагранжа и Ньютона (Магомед Махмудов)")
        self.init()

    def init(self):
        text_x1 = Text(self.master, height=1, width=10)
        text_x2 = Text(self.master, height=1, width=10)
        text_x3 = Text(self.master, height=1, width=10)
        text_x4 = Text(self.master, height=1, width=10)
        label_x = Label(self.master, text="X")

        label_x.grid(row=0, column=0, padx=10, pady=10)
        text_x1.grid(row=0, column=1, padx=10, pady=10)
        text_x2.grid(row=0, column=2, padx=10, pady=10)
        text_x3.grid(row=0, column=3, padx=10, pady=10)
        text_x4.grid(row=0, column=4, padx=10, pady=10)



        text_y1 = Text(self.master, height=1, width=10)
        text_y2 = Text(self.master, height=1, width=10)
        text_y3 = Text(self.master, height=1, width=10)
        text_y4 = Text(self.master, height=1, width=10)
        label_y = Label(self.master, text="Y")

        label_y.grid(row=1, column=0, padx=10, pady=10)
        text_y1.grid(row=1, column=1, padx=10, pady=10)
        text_y2.grid(row=1, column=2, padx=10, pady=10)
        text_y3.grid(row=1, column=3, padx=10, pady=10)
        text_y4.grid(row=1, column=4, padx=10, pady=10)


root = Tk()
my_app = MyApp(root)
root.mainloop()