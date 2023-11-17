def act4():
    import sympy as sym
    import tkinter as tk

    x1,x2,x3 = sym.symbols('x1 x2 x3')
    def jacobi():
    
        ecuacion1_str = entryFuncion1.get()
        lhs_str, rhs_str = ecuacion1_str.split('=')
        ecuacion1 = sym.Eq(sym.sympify(lhs_str), sym.sympify(rhs_str))

        ecuacion2_str = entryFuncion2.get()
        lhs_str, rhs_str = ecuacion2_str.split('=')
        ecuacion2 = sym.Eq(sym.sympify(lhs_str), sym.sympify(rhs_str))

        ecuacion3_str = entryFuncion3.get()
        lhs_str, rhs_str = ecuacion3_str.split('=')
        ecuacion3 = sym.Eq(sym.sympify(lhs_str), sym.sympify(rhs_str))

        print(f"\n{ecuacion1}")
        print(ecuacion2)
        print(ecuacion3)
        ecuacionOriginal1, ecuacionOriginal2, ecuacionOriginal3 = ecuacion1, ecuacion2, ecuacion3
        valores1 = {x1: 1, x2: 0, x3:0}
        valores2 = {x2: 1, x3: 0, x1:0}
        valores3 = {x3: 1, x2: 0, x1:0}
        if (ecuacion1.lhs.subs(valores1) > ecuacion2.lhs.subs(valores1)) and (ecuacion1.lhs.subs(valores1) > ecuacion3.lhs.subs(valores1)):
            primero = ecuacion1
        elif (ecuacion2.lhs.subs(valores1) > ecuacion1.lhs.subs(valores1)) and (ecuacion2.lhs.subs(valores1) > ecuacion3.lhs.subs(valores1)):
            primero = ecuacion2
        else:
            primero = ecuacion3
 
        if (ecuacion1.lhs.subs(valores2) > ecuacion2.lhs.subs(valores2)) and (ecuacion1.lhs.subs(valores2) > ecuacion2.lhs.subs(valores2)):
            segundo = ecuacion1
        elif (ecuacion2.lhs.subs(valores2) > ecuacion1.lhs.subs(valores2)) and (ecuacion2.lhs.subs(valores2) > ecuacion3.lhs.subs(valores2)):
            primero = ecuacion2
        else:
            segundo = ecuacion3
 
        if (ecuacion1.lhs.subs(valores3) > ecuacion2.lhs.subs(valores3)) and (ecuacion1.lhs.subs(valores3) > ecuacion2.lhs.subs(valores3)):
            tercero = ecuacion1
        elif (ecuacion2.lhs.subs(valores3) > ecuacion1.lhs.subs(valores3)) and (ecuacion2.lhs.subs(valores3) > ecuacion3.lhs.subs(valores3)):
            tercero = ecuacion2
        else:
            tercero = ecuacion3
 
        ecuacion1 = primero
        ecuacion2 = segundo
        ecuacion3 = tercero

        print("\nEcuación encontrando la raíz:")
        print(f"\n{ecuacion1}")
        print(ecuacion2)
        print(ecuacion3)

        ecuacion1 = sym.solve(ecuacion1, x1)[0]
        ecuacion2 = sym.solve(ecuacion2, x2)[0]
        ecuacion3 = sym.solve(ecuacion3, x3)[0]

        valorx1, valorx2, valorx3 = 0, 0, 0
        ec1, ec2, ec3 = 10, 10, 10
        inicio = True
        iteracion= 1
        while (abs(ec1) > 5) or (abs(ec2) > 5) or (abs(ec3) > 5):
            if inicio:
                ec1, ec2, ec3 = valorInicialx1, valorInicialx2, valorInicialx3
                inicio = False
            valores1 = {x2: valorx2, x3: valorx3}
            valores2 = {x1: valorx1, x3: valorx3}
            valores3 = {x1: valorx1, x2: valorx2}
            valorx1 = ecuacion1.subs(valores1)
            valorx2 = ecuacion2.subs(valores2)
            valorx3 = ecuacion3.subs(valores3)
 
            print(f"\nIteración {iteracion}:")
            print(valorx1.evalf())
            print(valorx2.evalf())
            print(f"{valorx3.evalf()}\n")
            iteracion = iteracion + 1
            ec1 = (ecuacionOriginal1.rhs - ecuacionOriginal1.lhs.subs({x1: valorx1, x2: valorx2, x3: valorx3})) * 100
            ec2 = (ecuacionOriginal2.rhs - ecuacionOriginal2.lhs.subs({x1: valorx1, x2: valorx2, x3: valorx3})) * 100
            ec3 = (ecuacionOriginal3.rhs- ecuacionOriginal3.lhs.subs({x1: valorx1, x2: valorx2, x3: valorx3})) * 100
 
        print("\nPorcentajes del error final")
        print(f"{ec1.evalf()}%")
        print(f"{ec2.evalf()}%")
        print(f"{ec3.evalf()}%")

    ventana = tk.Tk()

    LabelBienvenida = tk.Label(ventana, text="Bienvenido al programa 'Jacobi'")
    LabelBienvenida.grid(column=1, row=0)

    LabelBienvenida = tk.Label(ventana, text="Por favor, ingrese su primera ecuacion")
    LabelBienvenida.grid(column=0, row=1)

    entryFuncion1 = tk.Entry(ventana)
    entryFuncion1.grid(column=2, row=1)

    LabelBienvenida = tk.Label(ventana, text="Por favor, ingrese su segunda ecuacion")
    LabelBienvenida.grid(column=0, row=2)

    entryFuncion2 = tk.Entry(ventana)
    entryFuncion2.grid(column=2, row=2)

    LabelBienvenida = tk.Label(ventana, text="Por favor, ingrese su tercera ecuacion")
    LabelBienvenida.grid(column=0, row=3)

    entryFuncion3 = tk.Entry(ventana)
    entryFuncion3.grid(column=2, row=3)

    LabelBienvenida = tk.Label(ventana, text="Por favor, coloque el valor de x1")
    LabelBienvenida.grid(column=0, row=4)

    entryX1 = tk.Entry(ventana)
    entryX1.grid(column=2, row=4)

    LabelBienvenida = tk.Label(ventana, text="Por favor, coloque el valor de x2")
    LabelBienvenida.grid(column=0, row=5)

    entryX2 = tk.Entry(ventana)
    entryX2.grid(column=2, row=5)

    LabelBienvenida = tk.Label(ventana, text="Por favor, coloque el valor de x3")
    LabelBienvenida.grid(column=0, row=6)

    entryX3 = tk.Entry(ventana)
    entryX3.grid(column=2, row=6)

    botonEnviar = tk.Button(ventana, text="Enviar datos", command=jacobi)
    botonEnviar.grid(column=0, row=7)

    ventana.mainloop()