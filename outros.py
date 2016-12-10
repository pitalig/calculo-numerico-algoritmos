#!/usr/bin/env
# -*- coding: utf-8 -*-
import numpy as np


# Calcula o resíduo entre um solução real e uma solução aproxixmada.
# Entradas: matriz, vetor de termos independentes, vetor solução real
# Retorno: vetor resíduo
def residuo(m, v, v_sol):
    res = (np.matrix(v) - np.dot(np.matrix(v_sol), np.matrix(m))).tolist()
    return res[0]


# Recebe o valor de n inserido pelo usuário.
# Entradas: extremos a e b
# Retorno: dicionário contendo n, h e a malha de pontos x
def set_n(a, b):
    n = int(input('Insira o valor de N desejado '))

    # Calcula o passo adequado ao intervalo
    h = (b - a) / n

    # Cria a malha de pontos
    x = []
    for i in range(1, n):
        x.append(a + i * h)
    return {'n': n, 'h': h, 'x': x}


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    b = [1, 2, 3]
    c = [3, 2, 1]
    print(residuo(a, b, c))