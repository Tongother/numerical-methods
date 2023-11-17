def act3():
    
    import tkinter as tk
    import sympy as sym
    from sympy.parsing.sympy_parser import parse_expr

    def n_raphson():
        x = sym.symbols("x")
        iteraciones = int(entryIteraciones.get())
        xi = float(entryCantidadInicial.get())
        result = 0.0
        resultDerivada = 0.0
        expresionX1_1 = 0.0
        expresionError = 0.0
        contador = 0
        contador2 = 6
        expresion = sym.sympify(entryFuncion.get())
        expresionDerivada = sym.diff(expresion, x)

        labelBienvenida = tk.Label(ventana, text="iteracion")
        labelBienvenida.grid(column=0, row=5)

        labelBienvenida = tk.Label(ventana, text="Funcion")
        labelBienvenida.grid(column=1, row=5)

        labelBienvenida = tk.Label(ventana, text="Funcion derivada")
        labelBienvenida.grid(column=2, row=5)

        labelBienvenida = tk.Label(ventana, text="xi + 1")
        labelBienvenida.grid(column=3, row=5)

        labelBienvenida = tk.Label(ventana, text="Error")
        labelBienvenida.grid(column=4, row=5)

        labelBienvenida = tk.Label(ventana, text="Porcentaje")
        labelBienvenida.grid(column=5, row=5)

        for i in range(iteraciones):
            contador = contador + 1
            result = expresion.subs(x, xi)
            resultDerivada = expresionDerivada.subs(x, xi)
            expresionX1_1 = xi - (result/resultDerivada)
            expresionError = (expresionX1_1 - xi) / expresionX1_1

            labelBienvenida = tk.Label(ventana, text=f"{contador}")
            labelBienvenida.grid(column=0, row=contador2)

            labelBienvenida = tk.Label(ventana, text=f"{result}")
            labelBienvenida.grid(column=1, row=contador2)

            labelBienvenida = tk.Label(ventana, text=f"{resultDerivada}")
            labelBienvenida.grid(column=2, row=contador2)

            labelBienvenida = tk.Label(ventana, text=f"{expresionX1_1}")
            labelBienvenida.grid(column=3, row=contador2)

            labelBienvenida = tk.Label(ventana, text=f"{expresionError}")
            labelBienvenida.grid(column=4, row=contador2)

            labelBienvenida = tk.Label(ventana, text=f"{(expresionError*100)}")
            labelBienvenida.grid(column=5, row=contador2)

            xi = expresionX1_1
            contador2 = contador2 + 1


    ventana = tk.Tk()

    LabelBienvenida = tk.Label(ventana, text="Bienvenido al programa 'Newton Raphson'")
    LabelBienvenida.grid(column=1, row=0)

    LabelBienvenida = tk.Label(ventana, text="Por favor, ingrese su función")
    LabelBienvenida.grid(column=0, row=1)

    entryFuncion = tk.Entry(ventana)
    entryFuncion.grid(column=2, row=1)

    LabelBienvenida = tk.Label(ventana, text="Por favor, deme la cantidad inicial")
    LabelBienvenida.grid(column=0, row=2)

    entryCantidadInicial = tk.Entry(ventana)
    entryCantidadInicial.grid(column=2, row=2)

    LabelBienvenida = tk.Label(ventana, text="Por favor, coloque el número de iteraciones:")
    LabelBienvenida.grid(column=0, row=3)

    entryIteraciones = tk.Entry(ventana)
    entryIteraciones.grid(column=2, row=3)

    botonEnviar = tk.Button(ventana, text="Enviar datos", command=n_raphson)
    botonEnviar.grid(column=0, row=4)

    ventana.mainloop()