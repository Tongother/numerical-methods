def act6():
    import matplotlib.pyplot as plt
    import numpy as np
    import tkinter as tk
    from tkinter import messagebox
    import sympy as sym

    def operacionInterpolacion():
    
        x0 = CoordenadaXCampo1.get()
        x0 = float(x0)

        x1 = CoordenadaXCampo2.get()
        x1 = float(x1)

        x2 = CoordenadaXCampo3.get()
        x2 = float(x2)

        y0 = CoordenadaYCampo1.get()
        y0 = float(y0)

        y1 = CoordenadaYCampo2.get()
        y1 = float(y1)

        y2 = CoordenadaYCampo3.get()
        y2 = float(y2)

        #---------------------------------#

        elemento1 = (y1 - y0) / (x1 - x0)

        elemento2 = (y2 - y1) / (x2 - x1)

        elemento3 = (elemento2 - elemento1) / (x2 - x0)

        #---------------------------------------------------#

        a0 = y0
        a1 = elemento1
        a2 = elemento3
        print(a0, a1, a2)

        #--------------#
    
        SYMa0, SYMa1, SYMa2, SYMx0, SYMx1, x = sym.symbols("a0 a1 a2 x0 x1 x")

        valores = {SYMa0: a0, SYMa1: a1, SYMa2: a2, SYMx0: x0, SYMx1: x1 }
        Px = sym.sympify("a0 + a1*(x-x0) + a2*(x-x0)*(x-x1)")

        Polinomio = Px.subs(valores)
        messagebox.showinfo("Polinomio", Polinomio)
        Polinomio = sym.expand(Polinomio)
        messagebox.showinfo("Polinomio", Polinomio)
        #-----------------------------------------------------------------------#

        f = sym.lambdify(x, Polinomio)

        x_valor = np.linspace(-10, 10, 400)

        y_valor = f(x_valor)

        plt.figure()
        plt.plot(x_valor, y_valor)
        plt.title('Gráfico de la función polinómica')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.show()
    #------------------------------------------------------#

    #Declaracion de ventana normal

    ventana = tk.Tk()

    campo1 = tk.Label(ventana, text="Coordenadas 1")
    campo1.grid(column=1, row=0)

    corcheteIzquierdoCampo1 = tk.Label(ventana, text="(")
    corcheteIzquierdoCampo1.grid(column=0, row=1)

    CoordenadaXCampo1 = tk.Entry(ventana)
    CoordenadaXCampo1.grid(column=1, row=1)

    CoordenadaYCampo1 = tk.Entry(ventana)
    CoordenadaYCampo1.grid(column=2, row=1)

    corcheteDerechoCampo1 = tk.Label(ventana, text=")")
    corcheteDerechoCampo1.grid(column=3, row=1)

    campo2 = tk.Label(ventana, text="Coordenadas 2")
    campo2.grid(column=6, row=0)

    corcheteIzquierdoCampo2 = tk.Label(ventana, text="(")
    corcheteIzquierdoCampo2.grid(column=5, row=1)

    CoordenadaXCampo2 = tk.Entry(ventana)
    CoordenadaXCampo2.grid(column=6, row=1)

    CoordenadaYCampo2 = tk.Entry(ventana)
    CoordenadaYCampo2.grid(column=7, row=1)

    corcheteDerechoCampo2 = tk.Label(ventana, text=")")
    corcheteDerechoCampo2.grid(column=8, row=1)

    campo3 = tk.Label(ventana, text="Coordenadas 3")
    campo3.grid(column=11, row=0)

    corcheteIzquierdoCampo3 = tk.Label(ventana, text="(")
    corcheteIzquierdoCampo3.grid(column=10, row=1)

    CoordenadaXCampo3 = tk.Entry(ventana)
    CoordenadaXCampo3.grid(column=11, row=1)

    CoordenadaYCampo3 = tk.Entry(ventana)
    CoordenadaYCampo3.grid(column=12, row=1)

    corcheteDerechoCampo3 = tk.Label(ventana, text=")")
    corcheteDerechoCampo3.grid(column=13, row=1)

    corcheteDerechoCampo3 = tk.Label(ventana, text=")")
    corcheteDerechoCampo3.grid(column=13, row=1)

    botonEnviar = tk.Button(ventana, text="Enviar coordenadas", command=operacionInterpolacion)
    botonEnviar.grid(column=1, row=3)

    #---------------------------------------------------------------------------------------------#
    
    ventana.mainloop()