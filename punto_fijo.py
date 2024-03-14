
#! Entre mas alto sea el k mas se demora en converger el punto fijo 

def Punto_fijo(x0, g, tol, Niter):
    g = g(x0)
    E = abs(x0 - g)
    iter = 0

    while (iter <= Niter and E >= tol):
        x0 = g
        g = g(x0)
        E = abs(x0 - g)
        iter += 1
    if E < tol:
        print("g es raiz con tolerancia optimista")

    else:
        print("maximo numero de iteraciones alcanzado")
    
    error = E
    iteration = iter
    x = x0

    return error, iteration, x

x0 = 1
tol = 0.0001
Niter = 100

#! Funcion de ejemplo
def Example_function(x):
    return (x-1) * (x-2)

#? Ejecucion

error, iteration ,x = Punto_fijo(x0, Example_function, tol, Niter)

print("Solucion: ", x) 
print("numero de iteraciones: ", iteration)
print("Error: ", error)

