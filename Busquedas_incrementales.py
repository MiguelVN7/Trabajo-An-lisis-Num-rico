

#* una raiz de una funcion es un numero (x) dado que f(x) = 0

#*! Esta funcion recibe: la funcion dada, el valor inicial arbitrario, el paso y el numero de iteraciones maximo
def Busquedas_incrementales(f, x0, h, Nmax):
    x_previous = x0                         #*Inicializacion
    f_previous = f(x_previous)
    x_current = x_previous + h
    f_current = f(x_current)

    for i in range(Nmax):                   #*Recorrido en el intervalo y su condicion
        if f_previous * f_current < 0:
            break
        elif f_previous == 0:
            print("Hay una raiz exacta")
            break

        x_previous = x_current
        f_previous = f_current
        x_current = x_previous + h
        f_current = f(x_current)
        print(f"Iteration {i+1}: x = {x_current}, f(x) = {f_current}")

    a = x_previous
    b = x_current
    iteration = i + 1
    return a, b, iteration

#! funcion de ejemplo:
def Example_function(x):    
    return x**2 - 4

#! Parametros de entrada
x0 = 3        #* X inicial
h = 0.1          #* paso por iteracion
Nmax = 100       #* numero maximo de iteraciones


#? ejecucion

a, b, iteration = Busquedas_incrementales(Example_function, x0, h, Nmax)

print("Left end of the range: ", a)
print("right end of the range: ", b)
print("Number of iterations: ", iteration)
if iteration >= Nmax:
    print("Excedio el numero de iteraciones maximo")




