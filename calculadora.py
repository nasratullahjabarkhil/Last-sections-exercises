"""programa que hace una calculadora para hacer las operaciones, suma, resta, multiplicar,
potencia y la raiz cuadrada"""

import math
def calculadora():
    #los atributos con funcion lambda
    sumar = lambda a, b: a + b
    restar = lambda a, b: a - b
    dividir = lambda a, b: a / b
    multiplicar = lambda a, b: a * b
    potencia = lambda a: a**2
    raiz_cuadrada = lambda a: math.sqrt(a)

    #pedir al usuario que eliga la operacion que quiera realizar
    operacion = input("Eliga una operacion(+, -, *, /, √, ^): ")

    # la suma de los dos numeros introducidos
    if operacion == '+':
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = sumar(a,b)
        print("La suma de %s y %s es "%(a,b),resultado)

    #la resta de los dos numeros introducidos
    elif operacion == '-':
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = restar(a, b)
        print("La resta de %s - %s es "%(a,b),resultado)

    #la division de los dos numeros introducidos
    elif operacion == '/':
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = dividir(a, b)
        print("La division de %s entre %s es "%(a,b),resultado)

    #la multiplicacion de los dos numeros introducidos
    elif operacion == '*':
        a = float(input("Ingresa el primer numero: "))
        b = float(input("Ingresa el segundo numero: "))
        resultado = multiplicar(a, b)
        print("La multiplicacion de %s y %s es "%(a,b), resultado)

    #la potencia de un numero
    elif operacion == "^":
        a = float(input("ingresa el numero para calcular su potencia: "))
        resultado = potencia(a)
        print("La potencia de ", a, " es ", resultado)

    #la raiz cuadrada de un numero
    elif operacion == "√":
        a = float(input("ingresa el numero para calcular su raiz cuadrada: "))
        resultado = raiz_cuadrada(a)
        print("La raiz cuadrada de ", a, " es ", resultado)
    #el caso no valido
    else:
        print("operacion invalida")

calculadora()