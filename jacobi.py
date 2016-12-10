#!/usr/bin/env
# -*- coding: utf-8 -*-
import math


# MÉTODO APRESENTA FUNCIONAMENTO INCORRETO
# Calcula o vetor solução pelo método de Jacobi.
# Entradas: função q(x), malha de pontos, constante h, função y(x), tolerância, número máximo de iterações, n
# Retorno: vetor solução
def v_sol(q, x, h, y, tol, n_max, n):
    w_0 = [0] * (n - 1)
    w_new = w_0.copy()
    w_old = []
    for i in range(n - 1):
        w_old.append(w_0[i] + 2 * tol)
    norma = 2 * tol
    j = 0
    while norma > tol and j < n_max:
        j += 1
        w_old = w_new.copy()
        w_new[0] = (1 / (2 + h ** 2 * q(x[0]))) * (y(x[0]) + w_old[1])
        w_new[n - 2] = (1 / (2 + h ** 2 * q(x[n - 2]))) * (y(x[n - 2]) + w_old[n - 3])
        for i in range(1, n - 2):
            w_new[i] = (1 / (2 + h ** 2 * q(x[i]))) * (y(x[i]) + w_old[i - 1] + w_old[i + 1])
        for i in range(n - 1):
            norma += (w_new[i] - w_old[i]) ** 2
        norma = math.sqrt(norma)
    return w_new


if __name__ == "__main__":
    def y(x):  # Função y(x)
        return 1 / x


    def q(x):
        return 1 / x ** 2  # Função q(x)


    # Extremos
    a = 1
    b = 2

    # Número de passos (inserido pelo usuário)
    n = int(input("Insira o valor máximo de n: "))

    # Tamanho total do intervalo
    h = (b - a) / n

    # Malha de pontos
    x = []
    for i in range(1, n):
        x.append(a + i * h)

    print(v_sol(q, x, h, y, 0.0001, 100, n))
