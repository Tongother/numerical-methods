def act11():
    import tkinter as tk
    import sympy as sym

    def taylor():
        funcion = []
        x0 = float(entryX0.get())
        i = 1
        funcion.append(sym.sympify(entryEcuacion.get()))
        formulaSuprema = ""

        while funcion[-1] != 0:
 
            funcion.append(sym.diff(funcion[i-1], xS))
            derivadaLabel = tk.Label(ventana, text=f"Derivada {i}: {funcion[i-1]}")
            derivadaLabel.pack()
            derivadaSustituidaLabel = tk.Label(ventana, text=f"F({x0}): {funcion[i - 1].subs(xS, x0)}")
            derivadaSustituidaLabel.pack()
            espacio = tk.Label(ventana, text="")
            espacio.pack()
            formulaIterativa = f"*(x - {x0})**{str(i-1)}"
 
            if i == 1:
                formulaSuprema = f"{funcion[i-1].subs(xS, x0)}"

            if i == 2:
                formulaSuprema += f" + {funcion[i-1].subs(xS, x0)}"

            if i == 3:
                formulaSuprema += f" + ({funcion[i-1].subs(xS, x0)} / 2)"
                formulaSuprema += formulaIterativa

            if i>=3 and funcion[i].subs(xS, x0) != 0:
                formulaSuprema += f" + ({funcion[i].subs(xS, x0)} / {sym.factorial(i)})"
                formulaIterativa = f"*(x - {x0})**{str(i)}"
                formulaSuprema += formulaIterativa

            if i>=2 and i< 3:
                formulaSuprema += formulaIterativa
        
            labelSerie = tk.Label(ventana, text={"Serie de taylor:" + formulaSuprema})
            labelSerie.pack()
 
    xS = sym.symbols("x x0")

    ventana = tk.Tk()

    labelEcuacion = tk.Label(ventana, text="Por favor, escribe tu ecuacion en forma SYMPY:")
    labelEcuacion.pack()
    entryEcuacion = tk.Entry(ventana)
    entryEcuacion.pack()
    labelX0 = tk.Label(ventana, text="Por favor, ingresar x0:")
    labelX0.pack()
    entryX0 = tk.Entry(ventana)
    entryX0.pack()
    boton = tk.Button(ventana, text="Calcular", command=taylor)
    boton.pack()
    ventana.mainloop()