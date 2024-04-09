import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.exp(-x) - x



def secante (x0, x1, tol, iter):
    for n in range(iter):
        fx0 = f(x0)
        fx1 = f(x1)
        if fx1 - fx0 == 0:
            print("División por cero detectada!")
            return None
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        # Grafica
        plt.figure()
        x = np.linspace(min(x0, x1) - 1, max(x0, x1) + 1, 500)
        plt.plot(x, f(x), label='f(x)', color='red')
        plt.scatter([x0, x1], [fx0, fx1], color='blue')  
        plt.scatter(x2, 0, color='green')  

        
        plt.plot([x0, x1], [fx0, fx1], 'blue', label='Secante')

        plt.title(f"Iteración {n + 1}")
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.grid(True)
        plt.axhline(0, color='black', lw=0.5)
        plt.axvline(x=x2, color='green', linestyle='--', lw=0.5, label='Raíz aproximada x_2')
        plt.legend()
        plt.show()


        if abs(f(x2)) < tol:
            print(f"La raíz encontrada es: {x2} después de {n + 1} iteraciones")
            return x2

        x0 = x1
        x1 = x2

    print("Excedió el máximo de iteraciones")
    return None


raiz = secante(0, 1, 1e-5, 15)
