from tkinter import *


class MyApp:

    def __init__(self, master):
        self.master = master
        self.master.geometry("600x400")
        self.master.resizable(width=False, height=False)
        self.master.title("Интерполяционный многочлен Лагранжа и Ньютона (Магомед Махмудов)")
        self.init()

    """init widgets"""
    def init(self):

        # fields for x
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

        self.text_x1 = text_x1
        self.text_x2 = text_x2
        self.text_x3 = text_x3
        self.text_x4 = text_x4


        # fields for y
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


        self.text_y1 = text_y1
        self.text_y2 = text_y2
        self.text_y3 = text_y3
        self.text_y4 = text_y4


        btn_load = Button(self.master, text="Загрузить данные", width=len("Загрузить данные"), command=self.load_data)
        btn_load.grid(row=0, column=5, padx=10, pady=10)

        btn_calc = Button(self.master, text="Считать", width=len("Загрузить данные"))
        btn_calc.grid(row=1, column=5, padx=10, pady=10)

        btn_clear = Button(self.master, text="Очистить", width=len("Загрузить данные"), command=self.clear_fields)
        btn_clear.grid(row=2, column=5, padx=10, pady=10)


        var_int = IntVar()
        rL = Radiobutton(self.master, text="Лаграндж", variable=var_int,value=1)
        rN = Radiobutton(self.master, text="Ньютон", variable=var_int,value=2)

        rL.grid(row=3, column=5, padx=10, pady=10)
        rN.grid(row=4, column=5, padx=10, pady=10)

        # frame1 = Frame(self.master, bg='green', bd=5)
        # btn_test = Button(frame1, text="test")
        # btn_test.pack()
        # frame1.grid(row=5, column=0)

    def load_data(self):
        self.text_x1.insert(END, 0)
        self.text_x2.insert(END, 0.2)
        self.text_x3.insert(END, 0.4)
        self.text_x4.insert(END, 0.6)

        self.text_y1.insert(END, 0)
        self.text_y2.insert(END, 0.564)
        self.text_y3.insert(END, 0.865)
        self.text_y4.insert(END, 0.532)

    def clear_fields(self):
        self.text_x1.delete("1.0",END)
        self.text_x2.delete("1.0",END)
        self.text_x3.delete("1.0",END)
        self.text_x4.delete("1.0",END)

        self.text_y1.delete("1.0",END)
        self.text_y2.delete("1.0",END)
        self.text_y3.delete("1.0",END)
        self.text_y4.delete("1.0",END)





root = Tk()
my_app = MyApp(root)
root.mainloop()