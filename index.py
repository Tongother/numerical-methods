import sympy as sym
import tkinter as tk
import os
import sys
import math
from Tareas_de_programacion.Error.actError import act1
from Tareas_de_programacion.biseccion.biseccionEjercicio import act2
from Tareas_de_programacion.N_raphson.n_raphsonEjercicio import act3
from Tareas_de_programacion.jacobi.jacobiEjercicio import act4
from Tareas_de_programacion.gauss_seidel.gaussSeildel_ejercicio import act5
from Tareas_de_programacion.Interpolacion_de_newton.interpolacion import act6
from Tareas_de_programacion.Interpolacion_de_Lagrange.Lagrange import act7
from Tareas_de_programacion.trapezoide.metodoTrapezoidal import act8
from Tareas_de_programacion.Simson_un_tercio.simson import act9
from Tareas_de_programacion.euler.eulerEjercicio import act10
from Tareas_de_programacion.Taylor.serieTaylor import act11

def read_key():
    try:
        import msvcrt
        return msvcrt.getch().decode('utf-8')
    except ImportError:
        import termios
        import tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

print("¡Bienvenido al menú de Métodos númericos!")
read_key()
print("Por favor, elija una de los topicos en los que le interesa ingresar")
opcion = int(input("1. Solución númerica de ecuaciones de una variable\n"+
      "2. Sistema de ecuaciones lineales\n"+
      "3. Interpolación, derivación e integración numérica\n"+
      "4. Integración numérica método del trapecio y Simpson 1/3\n"+
      "5. Aplica solución numérica de ecuaciones y sistemas de ecuaciones\n"))

try:
    if(opcion == 1):
        print("¡Bienvenido a solución númerica de ecuaciones de una variable!")
        read_key()
        print("Por favor, elija una de los programas en los que le interesa ingresar:")
        case1 = int(input("1. Error absoluto 2. Bisección 3. Newton Raphson"))
        try:
            if(case1 == 1):
                act1()
            elif(case1 == 2):
                act2()
            elif(case1 == 3):
                act3()
            else:
                print("Error: Ingrese un número entre las opciones.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    elif(opcion == 2):
        print("¡Bienvenido a sistema de ecuaciones lineales!")
        read_key()
        print("Por favor, elija una de los programas en los que le interesa ingresar:")
        case2 = int(input("1. Jacobi 2. Gauss-seidel"))
        try:
            if(case2 == 1):
                act4()
            elif(case2 == 2):
                act5()
            else:
                print("Error: Ingrese un número entre las opciones.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    elif(opcion == 3):
        print("¡Bienvenido a interpolación, derivación e integración numérica!")
        read_key()
        print("Por favor, elija una de los programas en los que le interesa ingresar:")
        case3 = int(input("1. Interpolación de newton 2. Lagrange"))
        try:
            if(case3 == 1):
                act6()
            elif(case3 == 2):
                act7()
            else:
                print("Error: Ingrese un número entre las opciones.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    elif(opcion == 4):
        print("¡Bienvenido a integración numérica método del trapecio y Simpson 1/3!")
        read_key()
        print("Por favor, elija una de los programas en los que le interesa ingresar:")
        case4 = int(input("1. Método del trapecio 2. Simpson 1/3"))
        try:
            if(case4 == 1):
                act8()
            elif(case4 == 2):
                act9()
            else:
                print("Error: Ingrese un número entre las opciones.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    elif(opcion == 5):
        print("¡Bienvenido a aplica solución numérica de ecuaciones y sistemas de ecuaciones!")
        read_key()
        print("Por favor, elija una de los programas en los que le interesa ingresar:")
        case5= int(input("1. Euler 2. Serie de taylor"))
        try:
            if(case5 == 1):
                act10()
            elif(case5 == 2):
                act11()
            else:
                print("Error: Ingrese un número entre las opciones.")
        except ValueError:
            print("Error: Ingrese un número válido.")
except ValueError:
    print("Error: Ingrese un número válido.")