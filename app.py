"""
This is bad code
Предупреждаю говнокод!
"""

from tkinter import *
import scipy.interpolate
import scipy.misc
import numpy as np
import newton

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




        self.label_L_y1 = StringVar()
        self.label_L_y2 = StringVar()
        self.label_L_y3 = StringVar()
        self.label_L_y4 = StringVar()

        self.label_deriv_L = StringVar()

        self.label_N_y1 = StringVar()
        self.label_N_y2 = StringVar()
        self.label_N_y3 = StringVar()
        self.label_N_y4 = StringVar()

        self.label_deriv_N = StringVar()

        self.label_D = StringVar()

        self.label_L = Label(labelframe,text="L(x):").grid(row=0, column=0, padx=10, pady=10)
        Label(labelframe, textvariable=self.label_L_y1).grid(row=0, column=1, padx=10, pady=10)
        Label(labelframe, textvariable=self.label_L_y2).grid(row=0, column=2, padx=10, pady=10)
        Label(labelframe, textvariable=self.label_L_y3).grid(row=0, column=3, padx=10, pady=10)
        Label(labelframe, textvariable=self.label_L_y4).grid(row=0, column=4, padx=10, pady=10)

        Label(labelframe, textvariable=self.label_deriv_L).grid(row=0, column=5, padx=10, pady=10)

        self.label_N = Label(labelframe, text="N(x):").grid(row=1, column=0, padx=10, pady=10)

        Label(labelframe, textvariable=self.label_N_y1).grid(row=1, column=1, padx=10, pady=10)
        Label(labelframe, textvariable=self.label_N_y2).grid(row=1, column=2, padx=10, pady=10)
        Label(labelframe, textvariable=self.label_N_y3).grid(row=1, column=3, padx=10, pady=10)
        Label(labelframe, textvariable=self.label_N_y4).grid(row=1, column=4, padx=10, pady=10)

        Label(labelframe, textvariable=self.label_deriv_N).grid(row=1, column=5, padx=10, pady=10)

        Label(labelframe, textvariable=self.label_D).grid(row=0, column=6, padx=10, pady=10)

        self.label_deriv_L.set("L'(x): ")
        self.label_deriv_N.set("N'(x): ")
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

        self.label_deriv_L.set("L'(x): ")
        self.label_deriv_N.set("N'(x): ")

        self.label_L_y1.set("")
        self.label_L_y2.set("")
        self.label_L_y3.set("")
        self.label_L_y4.set("")

        self.label_N_y1.set("")
        self.label_N_y2.set("")
        self.label_N_y3.set("")
        self.label_N_y4.set("")

        self.label_D.set("d:")


    """Calculations"""

    def calc(self):
        self.calc_L()
        self.calc_N()
        self.calc_D()

    def calc_D(self):
        d = abs(self.deriv_L - self.deriv_N)
        self.label_D.set("d: " + str(d))

    def calc_L(self):
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

        def sub_formula(x):
            return (-7.729*(x**3))+(1.35*(x**2)) + 2.859*x

        """Lagrange formula in action"""

        lagrange_func = scipy.interpolate.lagrange(X,Y)

        L_y = [round(lagrange_func(x), 4) for x in X]

        self.deriv_L = round(scipy.misc.derivative(lagrange_func, 0.2), 4)
        self.label_deriv_L.set("L'(x): " + str(self.deriv_L))
        self.label_L_y1.set(L_y[0])
        self.label_L_y2.set(L_y[1])
        self.label_L_y3.set(L_y[2])
        self.label_L_y4.set(L_y[3])


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

        points = list(zip(X,Y))

        p_func, p_string = newton.interpolation_polynomial(points, get_string=True)

        self.deriv_N = round(scipy.misc.derivative(p_func, 0.2), 4)
        N_y = [p_func(x) for x in X]

        self.label_deriv_N.set("N'(x): " + str(self.deriv_N))
        self.label_N_y1.set(N_y[0])
        self.label_N_y2.set(N_y[1])
        self.label_N_y3.set(N_y[2])
        self.label_N_y4.set(N_y[3])

        # result = scipy.interpolate.newton()
        # self.label_L.set(result)


root = Tk()
my_app = MyApp(root)
root.mainloop()