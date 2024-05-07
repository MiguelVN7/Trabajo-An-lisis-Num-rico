def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def eliminacion_gaussiana(A, B):
    n = len(A)
    
    # Combinar A y B en una sola matriz aumentada
    Ab = []
    for i in range(n):
        Ab.append(A[i] + [B[i]])
    
    # Aplicar eliminación gaussiana
    for k in range(n-1):
        for i in range(k+1, n):
            factor = Ab[i][k] / Ab[k][k]
            for j in range(k, n+1):
                Ab[i][j] -= factor * Ab[k][j]
    
    # Aplicar retro-sustitución para encontrar las soluciones
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = Ab[i][n] / Ab[i][i]
        for j in range(i-1, -1, -1):
            Ab[j][n] -= Ab[j][i] * x[i]
    
    return x

# Solicitar al usuario que ingrese la matriz A
print("Ingrese la matriz A:")
A = []
filas_A = int(input("Número de filas de A: "))
columnas_A = int(input("Número de columnas de A: "))
for i in range(filas_A):
    fila = []
    for j in range(columnas_A):
        elemento = float(input(f"Ingrese el elemento A[{i+1}][{j+1}]: "))
        fila.append(elemento)
    A.append(fila)

# Solicitar al usuario que ingrese el vector B
print("Ingrese el vector B:")
B = []
for i in range(filas_A):
    elemento = float(input(f"Ingrese el elemento B[{i+1}]: "))
    B.append(elemento)

# Calcular las soluciones utilizando el método de eliminación gaussiana
soluciones = eliminacion_gaussiana(A, B)

# Mostrar las soluciones
print("Las soluciones son:")
for i, solucion in enumerate(soluciones):
    print(f"x{i+1} = {solucion}")
