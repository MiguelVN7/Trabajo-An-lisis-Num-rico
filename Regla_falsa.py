def Regla_falsa(f, a, b, tolerance, Nmax):
    f_a = f(a)
    f_b = f(b)
    midpoint = (f_b * a - f_a * b) / (f_b - f_a)
    f_midpoint = f(midpoint)
    E = 1000
    count = 0

    while E > tolerance and count < Nmax:
        if f_a * f_midpoint < 0:
            b = midpoint
        else:
            a = midpoint

        previous_midpoint = midpoint
        midpoint = (f(b) * a - f(a) * b) / (f(b) - f(a))
        f_midpoint = f(midpoint)
        E = abs(midpoint - previous_midpoint)
        count +=1 
        print(f"Iteration {count}: x = {midpoint}, f(x) = {f_midpoint}, a = {a}, b = {b}")
    
    x = midpoint
    iteration = count
    error = E
    return x, iteration, error

#! Funcion de ejemplo:
def Example_function(x):
    return x**2 - 4

#! Parametros de entrada:
a = 0                   #* Extremo izquierdo del intervalo inicial
b = 3                   #* Extremo derecho del intervalo inicial
tolerance = 0.0001      #* Tolerancia
Nmax = 100              #* Numero de iteraciones maximo

#? Ejecucion

x, iteration, error = Regla_falsa(Example_function, a, b, tolerance, Nmax)
print("Solucion: ", x) 
print("numero de iteraciones: ", iteration)
print("Error: ", error)


