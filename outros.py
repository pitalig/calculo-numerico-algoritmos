#!/usr/bin/env
# -*- coding: utf-8 -*-
import numpy as np


# Calcula o resíduo entre um solução real e uma solução aproxixmada.
# Entradas: matriz, vetor de termos independentes, vetor solução real
# Retorno: vetor resíduo
def residuo(m, v, v_sol):
    res = (np.matrix(v) - np.dot(np.matrix(v_sol), np.matrix(m))).tolist()
    return res[0]


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [1, 2, 3]
    c = [3, 2, 1]
    print(residuo(a, b, c))