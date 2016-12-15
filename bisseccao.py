#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Módulo bissecção: Método da bissecção ou dicotomia para resolver equações

import math

import numpy as np


# Resolve equação pelo método da bissecção.
# Entradas: função, extremos do chute inicial, tolerancia e criticidade de parada
# Retorno: solução, número de iterações
def bissec(f, m1, m2, tol, crit_parada, prin=False):
    tab = [["iter", "m1", "m2", "alpha", "f(alpha)"]]
    itera = 1
    bool_val = True
    # Executa iterações enquanto bool_val for verdadeiro
    while bool_val:
        alpha = 0.5 * (m1 + m2)
        linha = [itera, m1, m2, alpha, f(alpha)]
        tab.append(linha)
        if f(alpha) * f(m1) < 0:
            m2 = alpha
        if f(alpha) * f(m1) > 0 or f(alpha) * f(m1) == 0:
            m1 = alpha
        itera += 1
        # Verifica os critérios de parada
        if crit_parada == 0:
            bool_val = (0.25 * abs(m1 - m2) > tol)
        elif crit_parada == 1:
            bool_val = (f(alpha - tol) * f(alpha + tol) > 0)
    if prin:
        print(np.matrix(tab))
    return alpha, itera


# ----------------teste----------------
if __name__ == "__main__":

    print("teste1")

    def f(x):
        return 3 * x ** 3 - 2 * x ** 2 + 3 * x - 2


    tol = 10 ** (-2)

    m1 = -1
    m2 = 1

    bissec(f, m1, m2, tol, 0, True)

    bissec(f, m1, m2, tol, 1, True)

    print("teste2")

    def f(x):
        return math.sin(x) - math.cos(x)


    tol = 10 ** (-10)

    m1 = 0
    m2 = math.pi / 2  # a raíz da equação no intervalo desejado é pi/4

    bissec(f, m1, m2, tol, 0, True)

    bissec(f, m1, m2, tol, 1, True)

    # definindo novos limites
    m1 = 0
    m2 = 2

    bissec(f, m1, m2, tol, 0, True)

    bissec(f, m1, m2, tol, 1, True)
