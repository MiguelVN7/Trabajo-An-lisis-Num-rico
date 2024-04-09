import numpy as np
import matplotlib.pyplot as plt

def metodo_newton(xi, f, toler, n_iter, df):
    g = xi - f(xi)/df(xi)
    error = abs(xi - g)
    iter = 0
    while (iter <= n_iter) and (error >= toler):
        xi = g
        g = xi - f(xi)/df(xi)
        error = abs(xi - g)
        iter += 1
    if error < toler:
        return g
    else:
        return None

def main():
    f = lambda x: np.exp(-x) - x
    df = lambda x: -np.exp(-x) - 1
    xi = 1
    toler = 1e-5
    n_iter = 15
    raiz = metodo_newton(xi, f, toler, n_iter, df)
    if raiz is not None:
        print(f"La raiz es: {raiz}")
    else:
        print("No se encontro la raiz")

    # GRAFICA
    xi = np.linspace(0, 2, 100)  # Cambiar el rango según tus necesidades
    fi = f(xi)
    gi = df(xi)

    plt.plot(xi, fi, label='f(x)')
    plt.plot(xi, gi, label='g(x)')
    plt.axhline(0, color='k')
    plt.axvline(raiz, color='r', linestyle='--', label='Raíz')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
