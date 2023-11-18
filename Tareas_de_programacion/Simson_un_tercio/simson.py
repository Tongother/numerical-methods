def act9():
    import sympy as sym
    import math
    import numpy as np
    import TKinterModernThemes as TKMT
    from tkinter import ttk
    from PIL import Image, ImageTk
    import tkinter as tk

    xS, yS = sym.symbols('x y')

    def buttonCMD():
        print("Button clicked!")



    class App(TKMT.ThemedTKinterFrame):
        def __init__(self, theme, mode, usecommandlineargs=True, usethemeconfigfile=True):
            super().__init__("¡ Simpson 1/3 !", theme, mode, usecommandlineargs, usethemeconfigfile)

            placeholder = "4*x**3 + 2*x**2 + x - 10" + "+ y"

            def on_entry_focus_in(event):
                if funcion_var.get() == placeholder:
                    entryFuncion.delete(0, tk.END)

            def on_entry_focus_out(event):
                if funcion_var.get() == "":
                    entryFuncion.insert(0, placeholder)
                    entryFuncion.config(foreground="gray")

            def on_button_hover(event):
                    button.config(cursor="hand2")
        
            def create_table(root, rows, x, y):
                    windowTable = tk.Toplevel(self.master)
                    windowTable.title("Tabla de resultados")
                    # Encabezados de columna
                    label1 = ttk.Label(windowTable, text=f'I')
                    label1.grid(row=0, column=0)

                    label2 = ttk.Label(windowTable, text=f'X')
                    label2.grid(row=0, column=1)

                    label3 = ttk.Label(windowTable, text=f'Y')
                    label3.grid(row=0, column=2)

                    # Celdas de datos
                    for i in range(0, rows + 1):
                            labelI = ttk.Label(windowTable, text=str(i+1))
                            labelI.grid(row=i, column=0)
                        
                            labelX = ttk.Label(windowTable, text=str(x[i]))
                            labelX.grid(row=i, column=1)

                            labelY = ttk.Label(windowTable, text=str(y[i])) 
                            labelY.grid(row=i, column=2)

        

            def simpson():
                labelEscondido.config(text=funcion_var.get())

                x1 = float(limite_inferior_var.get())
                xf = float(limite_superior_var.get())
                n = int(numeroIntervalos_var.get())

                h = (xf - x1) / n
                x1_Array = []
                y1_Array = []
                x1_Array.append(x1)
                funcion = sym.sympify(funcion_var.get() + "+ y")
                funcion_numpy = np.vectorize(sym.lambdify((xS, yS), funcion, 'numpy'))

                x = np.linspace(start= -5-1,stop= xf+1, num=200)  # Valores de x
                y = np.linspace(start= -5-1,stop= xf+1, num=200)  # Valores de y
                Xm, Ym = np.meshgrid(x, y)  # Malla de puntos

                Zm = funcion_numpy(Xm, Ym) # Evaluar la función en la malla

                self.ax2.clear()  # Limpiar la gráfica anterior
                self.ax2.plot_surface(Xm, Ym, Zm, cmap='viridis')  # Graficar la superficie
                self.canvas2.draw()

                for i in range(0, n+1):
                    x1_Array.append((x1_Array[i] + h))
                    y1_Array.append((funcion.subs(xS, x1_Array[i])))

                    if i == 12:
                        x1_Array[i] = math.ceil(x1_Array[i])
                        create_table(self.grafica_frame.master, n, x1_Array, y1_Array)
                        return
            #--------------------------------------------------#

            funcion_var = tk.StringVar()
            limite_superior_var = tk.StringVar()
            limite_inferior_var = tk.StringVar()
            numeroIntervalos_var = tk.StringVar()

            self.frame = self.addLabelFrame("Interfaz", colspan=3, rowspan=3)
            self.frame

            image = Image.open("C:/Users/nette/OneDrive/Imágenes/Saved Pictures/integral.png")
            image_tk = ImageTk.PhotoImage(image)

            imagenIntegral = ttk.Label(self.frame.master, image=image_tk)
            imagenIntegral.place(x=60, y=180, width=200, height=300)

            LabelSimpy = ttk.Label(self.frame.master, text="Función SYMPY: ")
            LabelSimpy.place(x=150, y=150, width=200, height=20)
            LabelSimpy.config(font=("Monospace", 14, "bold"))

            entryFuncion = ttk.Entry(self.frame.master, textvariable=funcion_var)
            entryFuncion.place(x=150, y=180, width=165, height=35)
            entryFuncion.insert(0, placeholder)
            entryFuncion.bind("<FocusIn>", on_entry_focus_in)
            entryFuncion.bind("<FocusOut>", on_entry_focus_out)

            ttk.Entry(self.frame.master, textvariable=limite_superior_var).place(x=260, y=240, width=40, height=35)

            ttk.Entry(self.frame.master, textvariable=limite_inferior_var).place(x=220, y=385, width=40, height=35)

            labelNumero = ttk.Label(self.frame.master, text="N: ")
            labelNumero.place(x=180, y=450, width=30, height=35)

            labelEscondido = ttk.Label(self.frame.master, text="")
            labelEscondido.place(x=230, y=320, width=210, height=40)
            labelEscondido.config(font=("Monospace",  14, "bold"))

            ttk.Entry(self.frame.master, textvariable=numeroIntervalos_var).place(x=200, y=450, width=40, height=35)

        
            button = ttk.Button(self.frame.master, text="Calcular área", command=simpson)
            button.place(x=165, y=500, width=100, height=35)
            button.bind("<Enter>", on_button_hover)

            self.nextCol()
            self.nextCol()

            self.graphframe = self.addLabelFrame("3D Graph")
            self.canvas2, fig2, self.ax2, _, _ = self.graphframe.matplotlibFrame("Graph 3D", projection='3d')

            self.run()

    App("sun-valley", "dark")