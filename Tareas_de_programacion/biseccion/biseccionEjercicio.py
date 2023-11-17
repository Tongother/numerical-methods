
def act2():

    import tkinter as tk
    import sympy as sym
    import math

    w=0
    i=0

    xResultante=0
    n=0
    entero1=0 
    entero2=0
    fantasma1 = 0.0
    fantasma2= 0.0
    fantasmaFusion=0.0

    def fDeX(int1, xResultante):
        global w
        global i
        global entero1
        global entero2
        funcion = sym.sympify(entryFuncion.get())
        global fantasma1
        global fantasma2
        global fantasmaFusion
        decimales = 4

        fantasma1 = float(funcion.subs(x, int1))
        fantasma2 = float(funcion.subs(x, xResultante))
        LabelFantasma = tk.Label(ventana, text={f"f({math.trunc((fantasma1 * 10 ** decimales)/10**decimales)}) * f({(fantasma2 * 10 **decimales)/10 **decimales})"})
        LabelFantasma.grid(column=1, row=(w + 6))
        w = w + 1
        fantasmaFusion = fantasma1 * fantasma2

        if(fantasmaFusion > 0):
            entero1 = xResultante
            labelFantasma = LabelFantasma = tk.Label(ventana, text={f"{(fantasmaFusion * 10 ** decimales)/10 ** decimales} > 0"})
            labelFantasma.grid(column=2, row=(i + 6))
            i = i + 1
        elif (fantasmaFusion < 0):
            entero2 = xResultante
            labelFantasma = LabelFantasma = tk.Label(ventana, text={f"{(fantasmaFusion * 10 ** decimales)/10 ** decimales} < 0"})
            labelFantasma.grid(column=2, row=(i + 6))
            i = i + 1

    def biseccion():
        global xResultante
        global n
        global entero1
        global entero2

        Intervalo1 = float(entryIn1.get())
        Intervalo2 = float(entryIn2.get())
        decimales = 4
    
        entero1 = Intervalo1
        entero2 = Intervalo2

        while (round(xResultante, 4) != 1.7321):
            xResultante = (entero1 + entero2) / 2
            labelFantasma = tk.Label(ventana, text={xResultante})
            labelFantasma.grid(column=0, row=(n + 6))
            fDeX(entero1, xResultante)
            n = n + 1

    

    ventana = tk.Tk()

    x = sym.symbols("x")

    LabelBienvenida = tk.Label(ventana, text="Bienvenido al programa 'Bisección'")
    LabelBienvenida.grid(column=1, row=0)

    LabelBienvenida = tk.Label(ventana, text="Por favor, ingrese su función")
    LabelBienvenida.grid(column=0, row=1)

    entryFuncion = tk.Entry(ventana)
    entryFuncion.grid(column=2, row=1)

    LabelBienvenida = tk.Label(ventana, text="Por favor, ingrese su primer intervalor: (--> 0, 0)")
    LabelBienvenida.grid(column=0, row=2)

    entryIn1 = tk.Entry(ventana)
    entryIn1.grid(column=2, row=2)

    LabelBienvenida = tk.Label(ventana, text="Por favor, ingrese su segundo intervalo: (0, 0 <--)")
    LabelBienvenida.grid(column=0, row=3)

    entryIn2 = tk.Entry(ventana)
    entryIn2.grid(column=2, row=3)

    botonEnviar = tk.Button(ventana, text="Enviar datos", command=biseccion)
    botonEnviar.grid(column=0, row=4)

    ventana.mainloop()