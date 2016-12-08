#!/usr/bin/env
# -*- coding: utf-8 -*-
import gauss


# MÉTODO APRESENTA FUNCIONAMENTO INCORRETO
# Cria o polinômio interpolador de terceiro grau pelo método de mínimos quadrados.
# Entradas: vetor de pontos x e vetor de soluções nos respectivos pontos
# Retorno: polinômio interpolador
def polin(x, y):
    xk1 = x
    xk2 = [xi**2 for xi in x]
    xk3 = [xi**3 for xi in x]
    xk4 = sum(xi**4 for xi in x)
    xk5 = sum(xi**5 for xi in x)
    xk6 = sum(xi**6 for xi in x)
    fxk1 = sum(y)
    fxk2 = sum([a*b for a, b in zip(xk1, y)])
    fxk3 = sum([a*b for a, b in zip(xk2, y)])
    fxk4 = sum([a*b for a, b in zip(xk3, y)])
    xk1 = sum(xk1.copy())
    xk2 = sum(xk2.copy())
    xk3 = sum(xk3.copy())
    m = [[len(x), xk1, xk2, xk3], [xk1, xk2, xk3, xk4], [xk2, xk3, xk4, xk5], [xk3, xk4, xk5, xk6]]
    v = [fxk1, fxk2, fxk3, fxk4]
    return gauss.v_sol(m, v, 4)


# Cria o polinômio interpolador de grau g pelo método de mínimos quadrados, utilizando biblioteca numpy.
# Entradas: vetor de pontos, vetor de soluções nos respectivos pontos, grau desejado.
# Retorno: vetor de coeficientes do polinômio interpolador
def polin_numpy(x, y, g):
    from numpy import polyfit, array
    return polyfit(array(x), array(y), g)


# Cria o polinômio interpolador de grau g pelo método de mínimos quadrados, utilizando biblioteca numpy.
# Elimina o termo constante do polinômio.
# Entradas: vetor de pontos, vetor de soluções nos respectivos pontos, grau desejado.
# Retorno: vetor de coeficientes do polinômio interpolador
def polin_numpy_no_constant(x, y, g):
    from numpy import polyfit, array
    p = polyfit(array(x), array(y), g)
    p[len(p) - 1] = 0
    return p


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    # TESTE 1
    x = [1, 2, 3, 4, 5, 6]
    y = [1, 4, 9, 12, 25, 36]
    p = np.poly1d(polin(x, y))
    # plt.plot(x, y, "ko")
    x = np.arange(1, 10, 0.01)
    y = p(x)
    # plt.plot(x, y)
    # plt.show()

    # TESTE 2
    x = [1, 2, 4, 5, 7, 8, 10]
    y = [1, 1, 4, 4, 6, 6, 7]
    p = np.poly1d(polin(x, y))
    # plt.plot(x, y, "ko")
    x = np.arange(1, 10, 0.01)
    y = p(x)
    # plt.plot(x, y)
    # plt.show()

    # TESTE 3
    x = [1, 2, 4, 5, 7, 8, 10]
    y = [1, 1, 4, 4, 6, 6, 7]
    p = np.poly1d(polin_numpy(x, y, 5))
    # plt.plot(x, y, "ko")
    x = np.arange(1, 10, 0.01)
    y = p(x)
    # plt.plot(x, y)
    # plt.show()

    # TESTE 4
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 12, 25]
    p = np.poly1d(polin_numpy(x, y, 4))
    # plt.plot(x, y, "ko")
    x = np.arange(1, 10, 0.01)
    y = p(x)
    # plt.plot(x, y)
    # plt.show()

    # TESTE 5
    x = [1 / 1, 1 / 2, 1 / 3, 1 / 4, 1 / 5]
    y = [i ** 2 for i in x]
    plt.plot(x, y, "ko")
    p = np.poly1d(polin_numpy_no_constant(x, y, 4))
    x = np.arange(0, 5, 0.01)
    y = p(x)
    plt.plot(x, y)
    plt.show()
