def act5():
    import sympy as sym 
    import tkinter as tk
    x, y = sym.symbols("x y")

    def gauss_seidel():

        ecuacion1 = entryFuncion1.get()
        ecuacion1_l, ecuacion1_r = ecuacion1.split("=")
        ecuacion1_l = sym.sympify(ecuacion1_l.strip())
        ecuacion1_r = sym.sympify(ecuacion1_r.strip())
        ecuacion1 = sym.Eq(ecuacion1_l, ecuacion1_r)

        ecuacion2 = entryFuncion2.get()
        ecuacion2_l, ecuacion2_r = ecuacion2.split("=")
        ecuacion2_l = sym.sympify(ecuacion2_l.strip())
        ecuacion2_r = sym.sympify(ecuacion2_r.strip())
        ecuacion2 = sym.Eq(ecuacion2_l, ecuacion2_r)
    
        valores1 = {x: 1, y: 0}
        valores2 = {y: 1, x: 0}

        print("\nEcuaciones puestas por el usuario:")
        print(ecuacion1)
        print(ecuacion2)
        if (abs(ecuacion1.lhs.subs(valores1)*ecuacion2.lhs.subs(valores2)) > abs(ecuacion2.lhs.subs(valores1)*ecuacion1.lhs.subs(valores2))):
            primero, segundo = ecuacion1, ecuacion2
        else:
            primero, segundo = ecuacion2, ecuacion1

        ecuacion1, ecuacion2 = primero, segundo
        ecuacionOriginal1, ecuacionOriginal2 = ecuacion1, ecuacion2

        print("\nEcuación encontrando la raíz:")
        print(ecuacion1)
        print(ecuacion2)

        ecuacion1 = sym.solve(ecuacion1, x)[0]
        ecuacion2 = sym.solve(ecuacion2, y)[0]

        print("\nEcuación despejada:")
        print(ecuacion1)
        print(ecuacion2)

        ec1, ec2, ec3 = 0, 0, 0
        iteracion= 1

        while (iteracion <= 4):
 
            valores1 = {y: valory}
            valorx = ecuacion1.subs(valores1)
            valores2 = {x: valorx}
            valory = ecuacion2.subs(valores2)
 
            print(f"\nIteración {iteracion}:")
            print(valorx.evalf())
            print(f"{valory.evalf()}\n")
            iteracion = iteracion + 1
 
        ec1 = (ecuacionOriginal1.rhs - ecuacionOriginal1.lhs.subs({x: valorx, y: valory})) * 100
        ec2 = (ecuacionOriginal2.rhs - ecuacionOriginal2.lhs.subs({x: valorx, y: valory})) * 100

        print("Errores finales:")
        print(f"{ec1}%")
        print(f"{ec2}%")

    ventana = tk.Tk()

    LabelBienvenida = tk.Label(ventana, text="Bienvenido al programa 'Gauss Seidel'")
    LabelBienvenida.grid(column=1, row=0)

    LabelBienvenida = tk.Label(ventana, text="Por favor, ingrese su primera ecuacion")
    LabelBienvenida.grid(column=0, row=1)

    entryFuncion1 = tk.Entry(ventana)
    entryFuncion1.grid(column=2, row=1)

    LabelBienvenida = tk.Label(ventana, text="Por favor, ingrese su segunda ecuacion")
    LabelBienvenida.grid(column=0, row=2)

    entryFuncion2 = tk.Entry(ventana)
    entryFuncion2.grid(column=2, row=2)

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

    botonEnviar = tk.Button(ventana, text="Enviar datos", command=gauss_seidel)
    botonEnviar.grid(column=0, row=6)

    ventana.mainloop()