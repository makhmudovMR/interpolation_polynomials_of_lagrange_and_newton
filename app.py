from tkinter import *
import scipy.interpolate
import scipy.misc
import numpy as np


class MyApp:

    def __init__(self, master):
        self.master = master
        self.master.geometry("600x400")
        self.master.resizable(width=False, height=False)
        self.master.title("Интерполяционный многочлен Лагранжа и Ньютона (Магомед Махмудов)")
        self.init()
        self.init_styles()

    def init_styles(self):
        pass

    """init widgets"""
    def init(self):

        """ Input fields"""

        # fields for x
        self.label_x = Label(self.master, text="X")
        self.text_x1 = Text(self.master, height=1, width=10)
        self.text_x2 = Text(self.master, height=1, width=10)
        self.text_x3 = Text(self.master, height=1, width=10)
        self.text_x4 = Text(self.master, height=1, width=10)

        self.label_x.grid(row=0, column=0, padx=10, pady=10)
        self.text_x1.grid(row=0, column=1, padx=10, pady=10)
        self.text_x2.grid(row=0, column=2, padx=10, pady=10)
        self.text_x3.grid(row=0, column=3, padx=10, pady=10)
        self.text_x4.grid(row=0, column=4, padx=10, pady=10)


        # fields for y
        self.label_y = Label(self.master, text="Y")
        self.text_y1 = Text(self.master, height=1, width=10)
        self.text_y2 = Text(self.master, height=1, width=10)
        self.text_y3 = Text(self.master, height=1, width=10)
        self.text_y4 = Text(self.master, height=1, width=10)

        self.label_y.grid(row=1, column=0, padx=10, pady=10)
        self.text_y1.grid(row=1, column=1, padx=10, pady=10)
        self.text_y2.grid(row=1, column=2, padx=10, pady=10)
        self.text_y3.grid(row=1, column=3, padx=10, pady=10)
        self.text_y4.grid(row=1, column=4, padx=10, pady=10)

        """ Service buttons """

        btn_load = Button(self.master, text="Загрузить данные", width=len("Загрузить данные"), command=self.load_data)
        btn_load.grid(row=0, column=5, padx=10, pady=10)

        btn_calc = Button(self.master, text="Считать", width=len("Загрузить данные"), command=self.calc)
        btn_calc.grid(row=1, column=5, padx=10, pady=10)

        btn_clear = Button(self.master, text="Очистить", width=len("Загрузить данные"), command=self.clear_fields)
        btn_clear.grid(row=2, column=5, padx=10, pady=10)


        """ RadioButtons for chose """

        # var_int = IntVar()
        # rL = Radiobutton(self.master, text="Лаграндж", variable=var_int,value=1)
        # rN = Radiobutton(self.master, text="Ньютон", variable=var_int,value=2)
        #
        # rL.grid(row=3, column=5, padx=10, pady=10)
        # rN.grid(row=4, column=5, padx=10, pady=10)

        labelframe = LabelFrame(self.master, text="Ответы")
        labelframe.grid(row=3, column=0, columnspan=5, padx=10, pady=10)

        self.label_L = StringVar()
        self.label_deriv_L = StringVar()
        self.label_N = StringVar()
        self.label_deriv_N = StringVar()
        self.label_D = StringVar()

        Label(labelframe, textvariable=self.label_L).grid(row=0, column=0, padx=10, pady=10)
        Label(labelframe, textvariable=self.label_deriv_L).grid(row=0, column=1, padx=10, pady=10)
        Label(labelframe, textvariable=self.label_N).grid(row=1, column=0, padx=10, pady=10)
        Label(labelframe, textvariable=self.label_deriv_N).grid(row=1, column=1, padx=10, pady=10)
        Label(labelframe, textvariable=self.label_D).grid(row=0, column=2, padx=10, pady=10)
        self.label_L.set("Лаградж")
        self.label_deriv_L.set("производная Лагрнаджа")
        self.label_N.set("Ньютон")
        self.label_deriv_N.set("производная Ньютона")
        self.label_D.set("D = |L'(x) - N'(x)|")

    """load data from text fields"""
    def load_data(self):
        self.text_x1.insert(END, 0)
        self.text_x2.insert(END, 0.2)
        self.text_x3.insert(END, 0.4)
        self.text_x4.insert(END, 0.6)

        self.text_y1.insert(END, 0)
        self.text_y2.insert(END, 0.564)
        self.text_y3.insert(END, 0.865)
        self.text_y4.insert(END, 0.532)

    """clear text fileds"""
    def clear_fields(self):
        self.text_x1.delete("1.0",END)
        self.text_x2.delete("1.0",END)
        self.text_x3.delete("1.0",END)
        self.text_x4.delete("1.0",END)

        self.text_y1.delete("1.0",END)
        self.text_y2.delete("1.0",END)
        self.text_y3.delete("1.0",END)
        self.text_y4.delete("1.0",END)

        self.label_L.set("Лаградж")
        self.label_deriv_L.set("производная Лагрнаджа")
        self.label_N.set("Ньютон")
        self.label_deriv_N.set("производная Ньютона")

    def calc(self):
        self.calc_L()
        self.calc_N()

    def calc_L(self):
        X = [self.text_x1.get("1.0", END), self.text_x2.get("1.0", END), self.text_x3.get("1.0", END), self.text_x4.get("1.0", END)]
        Y = [self.text_y1.get("1.0", END), self.text_y2.get("1.0", END), self.text_y3.get("1.0", END), self.text_y4.get("1.0", END)]
        X = list(map(lambda x: float(x[0:-1]), X))
        Y = list(map(lambda y: float(y[0:-1]), Y))

        X = np.array(X)
        Y = np.array(Y)

        def sub_formula(x):
            return (-7.729*(x**3))+(1.35*(x**2)) + 2.859*x

        """Lagrange formula in action"""

        result = scipy.interpolate.lagrange(X,Y)
        self.label_L.set("L(x)= " + str(result))
        self.label_deriv_L.set("L'(x) = "+str(scipy.misc.derivative(sub_formula, 0.2)))





    def calc_N(self):
        X = [self.text_x1.get("1.0", END),
             self.text_x2.get("1.0", END),
             self.text_x3.get("1.0", END),
             self.text_x4.get("1.0", END)]

        Y = [self.text_y1.get("1.0", END),
             self.text_y2.get("1.0", END),
             self.text_y3.get("1.0", END),
             self.text_y4.get("1.0", END)]

        X = list(map(lambda x: float(x[0:-1]), X))
        Y = list(map(lambda y: float(y[0:-1]), Y))

        X = np.array(X)
        Y = np.array(Y)

        # result = scipy.interpolate.newton()
        # self.label_L.set(result)





root = Tk()
my_app = MyApp(root)
root.mainloop()