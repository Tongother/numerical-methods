def act8():
    import sympy as sym;
    import tkinter as tk;
    import matplotlib.pyplot as plt
    import numpy as np
    from numpy.polynomial.polynomial import Polynomial

    def crearGrafica(ecuacion, Valora, Valorb):
        Polinomio = sym.Poly(ecuacion)
        constantes = Polinomio.all_coeffs()
        constantes.reverse()
        valoresEnCoeficientes = Polynomial(coef = constantes)

        xGrafica = np.linspace(start=Valorb-1, stop=Valora+1, num=600)
        y = valoresEnCoeficientes(xGrafica)

        plt.plot(xGrafica, valoresEnCoeficientes(xGrafica), "red")

        xs = [Valora, Valora, Valorb, Valorb]
        ys = [0, valoresEnCoeficientes(Valora), valoresEnCoeficientes(Valorb), 0]

        plt.fill(xs, ys, 'grey', edgecolor='black', linewidth=2.0, alpha=0.5)

        plt.axhline(0, color='black', linewidth=2.0)
        plt.axvline(0, color='black', linewidth=2.0)

        plt.title('Gráfico de la función polinómica grado 3')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.show()

    def metodoTrapezoidal():

        #-----------------------------------#

        Valora = float(coordenadaX.get())
        Valorb = float(coordenadaY.get())
        ecuacion = funcion.get()
        ecuacion = sym.sympify(ecuacion)

        #-----------------------------------#

        pruebaLinealidad = sym.diff(sym.diff(ecuacion, x), x)

        #----------------------------------------------------------#

        if pruebaLinealidad != 0:
        
            E = Valorb - Valora
            segundaDerivada = pruebaLinealidad.subs(x, E)

            #-----------------#

            terminoFinal_Ex = (-1/12) * (segundaDerivada) * ((E)**3)

            print(f"Termino E: {E} \nResultado derivada'': {segundaDerivada} \nTermino Ex: {terminoFinal_Ex}")
            crearGrafica(ecuacion, Valora, Valorb)

        else:


            EvaluarA = ecuacion.subs(x, Valora)
            EvaluarB = ecuacion.subs(x, Valorb)
            B_A = (Valorb - Valora) / 2

            puntoIntegrado = B_A*((EvaluarA + EvaluarB))

            print(f"Evaluacion en A: {EvaluarA} \nEvaluacion en B: {EvaluarB} \nB_A: {B_A}\nPunto Integrado: {puntoIntegrado}")
            crearGrafica(ecuacion, Valora, Valorb)
            #-----------------------------------#




    x = sym.symbols('x')

    ventana = tk.Tk()

    LabelFuncion = tk.Label(ventana, text="Coloque la funcion en formato SYMPY (Potencia = **, variables = *x)")
    LabelFuncion.grid(column=1, row=0)

    funcion = tk.Entry(ventana)
    funcion.grid(column=1, row=1)

    LabelCoordenadas = tk.Label(ventana, text="Coordenadas (x - up, y - down)")
    LabelCoordenadas.grid(column=1, row=2)

    coordenadaX = tk.Entry(ventana)
    coordenadaX.grid(column=1, row=3)

    coordenadaY = tk.Entry(ventana)
    coordenadaY.grid(column=1, row=4)

    botonCalcular = tk.Button(ventana, text="Calcular area", command=metodoTrapezoidal)
    botonCalcular.grid(column=1, row=5)

    ventana.mainloop()