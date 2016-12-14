#!/usr/bin/env python
# encoding: utf-8
import math

import numpy as np


def newton(f, deriv_f, x_0, n_max, precisao, prin=False):
    itera = [("NumIter", "itera", "new itera", "f(new itera)", "controle")]
    i = 1
    x_k = x_0
    while f(x_k - precisao) * f(x_k + precisao) > 0 and i < n_max:
        temp = x_k - f(x_k) / deriv_f(x_k)
        linha = (i, x_k, temp, f(temp), f(x_k - precisao) * f(x_k + precisao))
        x_k = temp
        itera.append(linha)
        i += 1
    temp = x_k - f(x_k) / deriv_f(x_k)
    linha = (i, x_k, temp, f(temp), f(x_k - precisao) * f(x_k + precisao))
    itera.append(linha)
    if prin:
        print(np.matriz(itera))
    return temp, i


########################################################################################

if __name__ == "__main__":
    # Exemplo 1

    def func(x):
        return 3 * x ** 3 - 2 * x ** 2 + 3 * x - 2


    def derivf(x):
        return 9 * x ** 2 - 4 * x + 3


    prec = 10 ** -8
    n_max = 1000
    m = -1
    M = 1
    x_0 = M
    x_1 = M + 5
    print(newton(func, derivf, M, n_max, prec))


    # Exemplo 2

    def func(x):
        return math.sin(x) + 2 * math.cos(x)


    def derivf(x):
        return math.cos(x) - 2 * math.sin(x)


    prec = 10 ** -13
    n_max = 1000
    m = 2
    M = 3
    x_0 = M
    x_1 = M + 0.1
    print(newton(func, derivf, M, n_max, prec))
