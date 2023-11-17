def act10():
    
    import sympy as sym
    import tkinter as tk

    def euler():
        ecuacion = sym.sympify(ecuacionEntry.get())
        x0 = float(entryx0.get())
        y0 = float(entryy0.get())
        xf = float(entryXf.get())
        h = entryH.get()
        n = entryN.get()
        i=0
        x= x0
        y = []
        y.append(y0)
        valoresEnFx = []
        if(h == ""):
            n = float(n)
            h = (xf-x0) / n
            while i<=n:
                print(f"Valor en x{i}:{x}")
                datos = {xS: x, yS: y[i]}
                valoresEnFx.append(ecuacion.subs(datos))
                x += h
                y.append(y[i] + (h * valoresEnFx[i]))

                print(f"Valor en y{i}:{y[i]}")
                print(f"Valor en fx{i}:{valoresEnFx[i]}")
 
                i += 1 
        elif (n == ""):
            h = float(h)
            n = (xf-x0) / h
            while i<=n:
                print(f"Valor en x{i}:{x}")
                datos = {xS: x, yS: y[i]}
                valoresEnFx.append(ecuacion.subs(datos))
                x += h
                y.append(y[i] + (h * valoresEnFx[i]))
                print(f"Valor en y{i}:{y[i]}")
                print(f"Valor en fx{i}:{valoresEnFx[i]}")
 
                i += 1 

    xS, yS = sym.symbols("x y")
    ventana = tk.Tk()
    label1 = tk.Label(ventana, text="Por favor, ingrese la funcion en formato sympy: ")
    label1.pack()
    ecuacionEntry = tk.Entry(ventana)
    ecuacionEntry.pack()
    labelX0Y0 = tk.Label(ventana, text="x0, y0: ")
    labelX0Y0.pack()
    entryx0 = tk.Entry(ventana)
    entryx0.pack()
    entryy0 = tk.Entry(ventana)
    entryy0.pack()
    labelXf = tk.Label(ventana, text="xf: ")
    labelXf.pack()
    entryXf = tk.Entry(ventana)
    entryXf.pack()
    labelN = tk.Label(ventana, text="n (si coloca h, ya no ponga ningun valor en n): ")
    labelN.pack()
    entryN = tk.Entry(ventana)
    entryN.pack()
    labelH = tk.Label(ventana, text="h (si coloca h, ya no ponga ningun valor en n): ")
    labelH.pack()
    entryH = tk.Entry(ventana)
    entryH.pack()
    boton = tk.Button(ventana, text="Calcular", command=euler)
    boton.pack()
    ventana.mainloop()