
def act1():

    import sympy as sym
    import tkinter as tk
    import math
    
    MedidasEntry, cantidadX_X, cantidadX_XPotencia = [], [], []
    sumaTotalMedidas, CantidadMedidas, sumaPotencia = 0.0, 0, 0

    def colocarTextBox():
        CantidadMedidas = int(entryMedidas.get())
        LabelPorfavor2 = tk.Label(ventana, text="Por favor, coloque las medidas que uso:")
        LabelPorfavor2.grid(column=0, row=4)
        i=0
        while (i< CantidadMedidas):
            MedidasEntry.append(tk.Entry(ventana))
            MedidasEntry[i].grid(column= 1, row=(i+4))
            i= i + 1
        botonEnviarTodo = tk.Button(ventana, text="Enviar todas las medidas", command=metodoError)
        botonEnviarTodo.grid(column=0, row=5)


    def metodoError():
        i = 0
        eInstrumento = "0."
        cantidadDecimales = 0
        numD = 0
        contador = False
        CantidadMedidas = int(entryMedidas.get())
        labelMedidas = tk.Label(ventana, text="Medidas")
        labelMedidas.grid(column=0, row=(len(MedidasEntry) + 5))
        labelMedidas = tk.Label(ventana, text="X - Xm")
        labelMedidas.grid(column=1, row=(len(MedidasEntry) + 5))
        labelMedidas = tk.Label(ventana, text="(Xm)^2")
        labelMedidas.grid(column=2, row=(len(MedidasEntry) + 5))
        sumaTotalMedidas = 0
        while (i< len(MedidasEntry)):
            sumaTotalMedidas += float(MedidasEntry[i].get())
            labelMedidas = tk.Label(ventana, text={MedidasEntry[i].get()})
            labelMedidas.grid(column=0, row=(i + len(MedidasEntry) + 6))
            i = i + 1
        Promedio = (sumaTotalMedidas/ CantidadMedidas)
        i=0
        sumaPotencia = 0
        while (i< len(MedidasEntry)):
            cantidadX_X.append((float(MedidasEntry[i].get())) - Promedio)
            labelMedidas = tk.Label(ventana, text={cantidadX_X[i]})
            labelMedidas.grid(column=1, row=(i + len(MedidasEntry) + 6))
            cantidadX_XPotencia.append((cantidadX_X[i]**2))
            sumaPotencia += cantidadX_XPotencia[i]
            labelMedidas = tk.Label(ventana, text={cantidadX_XPotencia[i]})
            labelMedidas.grid(column=2, row=(i + len(MedidasEntry) + 6))
            i = i + 1

        i=0
        while(i < len(MedidasEntry)):
            arregloCaracteres = list(str(float(MedidasEntry[i].get())))

            for c in arregloCaracteres:
                if contador:
                    numD += 1
                    if numD > cantidadDecimales:
                        cantidadDecimales = numD
                if c == '.':
                    contador = True
            i = i + 1
            numD = 0
            contador = False

        for i in range(cantidadDecimales):
            if (i+1) == cantidadDecimales:
                eInstrumento += "1"
                break
            eInstrumento += "0"

        eMedidor = round((math.sqrt((sumaPotencia/(CantidadMedidas*(CantidadMedidas-1))))), cantidadDecimales)

        labelMedidas = tk.Label(ventana, text={"e = " + round(sumaTotalMedidas, cantidadDecimales) + "+-" + eMedidor})
        labelMedidas.grid(column=1, row=(8 + len(MedidasEntry) + len(cantidadX_X)))

        labelMedidas = tk.Label(ventana, text={"eMedidor" + eMedidor})
        labelMedidas.grid(column=1, row=(8 + len(MedidasEntry) + len(cantidadX_X)))

        labelMedidas = tk.Label(ventana, text={"eInstrumento" + eInstrumento})
        labelMedidas.grid(column=1, row=(9 + len(MedidasEntry) + len(cantidadX_X)))
    




    ventana = tk.Tk()

    labelBienvenida = tk.Label(ventana, text="¡Bienvenido al programa")
    labelBienvenida.grid(column=1, row=0)

    labelBienvenida2 = tk.Label(ventana, text="'Error absoluto'!")
    labelBienvenida2.grid(column=1, row=1)

    labelPorfavor = tk.Label(ventana, text="Por favor, indique cuantas medidas uso:")
    labelPorfavor.grid(column=0, row=2)

    entryMedidas = tk.Entry(ventana)
    entryMedidas.grid(column=2, row=2)

    botonEnviarMedidas = tk.Button(ventana, text="Enviar medidas", command=colocarTextBox)
    botonEnviarMedidas.grid(column=0, row=3)

    ventana.mainloop()
