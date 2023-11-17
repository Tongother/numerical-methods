def act7():
    import matplotlib.pyplot as plt
    import numpy as np
    import tkinter as tk
    from tkinter import messagebox
    import sympy as sym

    def interpolacionDeLagrange():
        x0 = CoordenadaX0.get()
        x0 = float(x0)

        x1 = CoordenadaX1.get()
        x1 = float(x1)

        x2 = CoordenadaX2.get()
        x2 = float(x2)

        x3 = CoordenadaX3.get()
        x3 = float(x3)

        y0 = CoordenadaY0.get()
        y0 = float(y0)

        y1 = CoordenadaY1.get()
        y1 = float(y1)

        y2 = CoordenadaY2.get()
        y2 = float(y2)

        y3 = CoordenadaY3.get()
        y3 = float(y3)

        SIMBOLSx0, SIMBOLSx1, SIMBOLSx2, SIMBOLSx3 = sym.symbols("x0 x1 x2 x3")
        valores = {SIMBOLSx0: x0, SIMBOLSx1: x1, SIMBOLSx2: x2, SIMBOLSx3: x3}

        L0 = sym.sympify("((x - x1)*(x - x2)*(x - x3)) / ((x0 - x1)*(x0 - x2)*(x0 - x3))")
        L1 = sym.sympify("((x - x0)*(x - x2)*(x - x3)) / ((x1 - x0)*(x1 - x2)*(x1 - x3))")
        L2 = sym.sympify("((x - x0)*(x - x1)*(x - x3)) / ((x2 - x0)*(x2 - x1)*(x2 - x3))")
        L3 = sym.sympify("((x - x0)*(x - x1)*(x - x2)) / ((x3 - x0)*(x3 - x1)*(x3 - x2))")

        PolinomioL0 = L0.subs(valores)
        PolinomioL0 = sym.expand(PolinomioL0)
        PolinomioL0 = str(PolinomioL0)
        funcionTextL0.config(text=PolinomioL0)

        PolinomioL1 = L1.subs(valores)
        PolinomioL1 = sym.expand(PolinomioL1)
        PolinomioL1 = str(PolinomioL1)
        funcionTextL1.config(text=PolinomioL1)

        PolinomioL2 = L2.subs(valores)
        PolinomioL2 = sym.expand(PolinomioL2)
        PolinomioL2 = str(PolinomioL2)
        funcionTextL2.config(text=PolinomioL2)

        PolinomioL3 = L3.subs(valores)
        PolinomioL3 = sym.expand(PolinomioL3)
        PolinomioL3 = str(PolinomioL3)
        funcionTextL3.config(text=PolinomioL3)

        SIMBOLSy0, SIMBOLSy1, SIMBOLSy2, SIMBOLSy3 = sym.symbols("y0 y1 y2 y3")

        valores2 = {SIMBOLSy0: y0, SIMBOLSy1: y1, SIMBOLSy2: y2, SIMBOLSy3: y3}

        funcionPx = sym.sympify(f"(y0 * ({PolinomioL0})) + (y1 * ({PolinomioL1})) + (y2 * ({PolinomioL2})) + (y3 * ({PolinomioL3}))")
        funcionPx = funcionPx.subs(valores2)
        funcionPx = sym.expand(funcionPx)
        print(funcionPx)
        funcionPolinomicaText.config(text=str(funcionPx))

        x = sym.symbols("x")
        fValoresEnX = sym.lambdify(x, funcionPx)

        x_valor = np.linspace(-10, 10, 100)

        y_valor = fValoresEnX(x_valor)

        plt.figure()
        plt.plot(x_valor, y_valor)
        plt.title('Gráfico de la función polinómica grado 3')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.show()

    ventana = tk.Tk()

    coordenada1 = tk.Label(ventana, text="Coordenadas 1")
    coordenada1.pack()

    CoordenadaX0 = tk.Entry(ventana)
    CoordenadaX0.pack()

    CoordenadaY0 = tk.Entry(ventana)
    CoordenadaY0.pack()

    coordenada2 = tk.Label(ventana, text="Coordenadas 2")
    coordenada2.pack()

    CoordenadaX1 = tk.Entry(ventana)
    CoordenadaX1.pack()

    CoordenadaY1 = tk.Entry(ventana)
    CoordenadaY1.pack()

    coordenada3 = tk.Label(ventana, text="Coordenadas 3")
    coordenada3.pack()

    CoordenadaX2 = tk.Entry(ventana)
    CoordenadaX2.pack()

    CoordenadaY2 = tk.Entry(ventana)
    CoordenadaY2.pack()

    coordenada4 = tk.Label(ventana, text="Coordenadas 4")
    coordenada4.pack()

    CoordenadaX3 = tk.Entry(ventana)
    CoordenadaX3.pack()

    CoordenadaY3 = tk.Entry(ventana)
    CoordenadaY3.pack()

    botonEnviar = tk.Button(ventana, text="Enviar coordenadas", command=interpolacionDeLagrange)
    botonEnviar.pack()

    funcionPolinomica = tk.Label(ventana, text="Producto resultante:")
    funcionPolinomica.pack()

    funcionPolinomicaText = tk.Label(ventana, text="")
    funcionPolinomicaText.pack()

    funcionL0 = tk.Label(ventana, text="Polinomio de L0:")
    funcionL0.pack()

    funcionTextL0 = tk.Label(ventana, text="")
    funcionTextL0.pack()

    funcionL1 = tk.Label(ventana, text="Polinomio de L1:")
    funcionL1.pack()

    funcionTextL1 = tk.Label(ventana, text="")
    funcionTextL1.pack()

    funcionL2 = tk.Label(ventana, text="Polinomio de L2:")
    funcionL2.pack()

    funcionTextL2 = tk.Label(ventana, text="")
    funcionTextL2.pack()

    funcionL3 = tk.Label(ventana, text="Polinomio de L3:")
    funcionL3.pack()

    funcionTextL3 = tk.Label(ventana, text="")
    funcionTextL3.pack()
    ventana.mainloop()