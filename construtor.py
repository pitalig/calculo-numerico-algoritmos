#!/usr/bin/env
# -*- coding: utf-8 -*-
# Módulo construtor: contém os métodos de construção da matriz do sistema e do vetor de termos independentes


# Constroi a matriz do sistema
# Entradas: função q(x), malha de pontos, contante h, número de pontos
# Retorno: matriz do sistema
def matriz(q, x, h, n):
    b = []
    for i in range(n-1):
        l = [0] * (n-1)
        l[i] = 2 + h ** 2 * q(x[i])
        b.append(l)
    for i in range(n-2):
        b[i + 1][i] = -1
        b[i][i + 1] = -1
    return b


# Constroi o vetor de termos independentes
# Entradas: função r(x), malha de pontos, contante h, número de pontos, soluções nos extremos da malha
# Retorno: vetor de termos independentes
def vetor(r, x, h, n, a_, b_):
    z = []
    for i in range(n-1):
        z.append(- h ** 2 * r(x[i]))
    z[0] += a_
    z[n-2] += b_
    return z


# ----------------teste----------------
if __name__ == "__main__":
    def q(x):
        return 5 * x


    x = range(5)
    h = 1
    n = 5

    print(matriz(q, x, h, n))


    def r(x):
        return x ** 2


    print(vetor(r, x, h, n, 0, 0))
