#!/usr/bin/env
# -*- coding: utf-8 -*-
# Módulo mínimos: Método dos mínimos quadrados para ajuste de valores

import numpy as np

import gauss


# Cria o polinômio interpolador de terceiro grau pelo método de mínimos quadrados.
# Polinomio no formato: k1/x + k2/x**2 + k3/X**3
# Entradas: vetor de pontos x e vetor de soluções nos respectivos pontos
# Retorno: polinômio interpolador e um vetor com os coeficientes do polinômio
def polin(x, y):
    m = len(x)

    def g_1(x):
        return 1 / x

    def g_2(x):
        return 1 / x ** 2

    def g_3(x):
        return 1 / x ** 3

    aux = np.zeros((m, 3))
    for i in range(m):
        aux[i][0] = g_1(x[i])
        aux[i][1] = g_2(x[i])
        aux[i][2] = g_3(x[i])

    matriz = np.zeros((3, 3))
    vetor = np.zeros(3)

    for i in range(3):
        for j in range(3):
            for k in range(m):
                matriz[i][j] += aux[k][i] * aux[k][j]
        for k in range(m):
            vetor[i] += aux[k][i] * y[k]

    p = gauss.v_sol(matriz, vetor, 3)

    def sol(x):
        return (p[0] / x) + (p[1] / x ** 2) + (p[2] / x ** 3)

    return sol, p


# Cria o polinômio interpolador de grau g pelo método de mínimos quadrados, utilizando biblioteca numpy.
# Entradas: vetor de pontos, vetor de soluções nos respectivos pontos, grau desejado.
# Retorno: vetor de coeficientes do polinômio interpolador e o polinômio
def polin_numpy(x, y, g):
    from numpy import polyfit, array, poly1d
    v = polyfit(array(x), array(y), g)
    return poly1d(v), v


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # TESTE 1
    x = [1, 2, 3, 4, 5, 6]


    def func(x):
        return 3 + 1/x - 5/x**2 + x**3
    y = [func(i) for i in x]
    p = polin(x, y)
    # plt.plot(x, y, "ko")
    x = np.arange(1, 10, 0.01)
    y = p(x)
    # plt.plot(x, y)
    # plt.show()

    # TESTE 2
    x = [1, 2, 3]
    y = [9, 4, 1]
    p = polin(x, y)
    plt.plot(x, y, "ko")
    x = np.arange(1, 10, 0.01)
    y = p(x)
    plt.plot(x, y)
    plt.show()

    # TESTE 3
    x = [1, 2, 4, 5, 7, 8, 10]
    y = [1, 1, 4, 4, 6, 6, 7]
    p = polin_numpy(x, y, 5)[0]
    # plt.plot(x, y, "ko")
    x = np.arange(1, 10, 0.01)
    y = p(x)
    # plt.plot(x, y)
    # plt.show()

    # TESTE 4
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 12, 25]
    p = polin_numpy(x, y, 4)[0]
    # plt.plot(x, y, "ko")
    x = np.arange(1, 10, 0.01)
    y = p(x)
    # plt.plot(x, y)
    # plt.show()
