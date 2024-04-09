import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def metodo_raices_multiples(xi, f, df, ddf, toler, n_iter):
    error = 1
    iter = 0
    while (error >= toler) and (iter < n_iter):
        fxi = f(xi)
        dfxi = df(xi)
        ddfxi = ddf(xi)

        # No habra division por cero
        if dfxi ** 2 - fxi * ddfxi == 0:
            print("División por cero detectada!")
            return None

        # Nueva aproximación
        x_new = xi - (fxi * dfxi) / (dfxi ** 2 - fxi * ddfxi)
        error = abs(xi - x_new)
        xi = x_new
        iter += 1

    if error < toler:
        return xi
    else:
        print("No se encontró la raíz con la precisión deseada")
        return None


def main():
    # Funcion y derivadas
    f = lambda x: np.exp(-x) - x
    df = lambda x: -np.exp(-x) - 1
    ddf = lambda x: np.exp(-x)

    # Parámetros iniciales
    xi = 0
    toler = 1e-5
    n_iter = 15


    raiz = metodo_raices_multiples(xi, f, df, ddf, toler, n_iter)
    if raiz is not None:
        print(f"La raíz es: {raiz}")
    else:
        print("No se encontró la raíz")

    # GRAFICA
    xi = np.linspace(0, 2, 100)
    fi = f(xi)
    plt.plot(xi, fi, label='f(x)')
    plt.axhline(0, color='k')
    plt.axvline(raiz, color='r', linestyle='--', label='Raíz')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
