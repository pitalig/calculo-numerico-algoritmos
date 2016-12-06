#!/usr/bin/env python
# encoding: utf-8
# Método da falsa posição
import numpy as np


# Resolve equação pelo método da falsa posição.
# Entradas: função, extremos do chute inicial, tolerancia
# Retorno: solução
def falsaposicao(f, m1, m2, tol):
    tab = [['i', 'm1', 'm2', 'alpha', 'f(alpha)']]
    alpha = 0.5 * (m1 + m2)
    i = 0
    while (f(alpha - tol) * f(alpha + tol)) > 0:
        alpha = (m1 * f(m2) - m2 * f(m1)) / (f(m2) - f(m1))
        i += 1

        linha = [i, m1, m2, alpha, f(alpha)]

        if f(alpha) * f(m1) < 0:
            m2 = alpha
        if f(alpha) * f(m1) > 0:
            m1 = alpha

        tab.append(linha)

    return tab


# ----------------teste----------------
if __name__ == "__main__":
    def f(x):
        return 3 * x ** 3 - 2 * x ** 2 + 3 * x - 2


    print('teste1')

    tol = 10 ** (-6)
    m1 = 0.6
    m2 = 1

    print(np.matrix(falsaposicao(f, m1, m2, tol)))

    # TESTE 5

    print('teste2')

    tol = 10 ** (-6)
    m1 = -7
    m2 = 5

    print(np.matrix(falsaposicao(f, m1, m2, tol)))

    # TESTE 6

    print('teste3')

    tol = 10 ** (-6)
    m1 = 0
    m2 = 2

    print(np.matrix(falsaposicao(f, m1, m2, tol)))
