#!/usr/bin/env
# -*- coding: utf-8 -*-
import matplotlib.pyplot as mat
from numpy import arange


# Calcula o vetor solução (y), para um intervalo de pontos de x, baseado em um conjunto resultados já conhecidos.
# Entradas: lista de pontos de x já conhecidos, solução y correspondente aos pontos x já conhecidos,
# intervalo de pontos de x para onde se deseja obter a solução.
# Retorno: vetor solução para o intervalo escolhido
def interpola(x, y, x_new):
    y_new = []
    # Itera por todos os elementos do vetor x desejado
    for x_i in x_new:
        # Calcula o polinômio interpolador e sua solução
        l = 0
        for i in range(len(y)):
            num = 1
            den = 1
            for k in range(len(x)):
                if i != k:
                    num *= x_i - x[k]
                    den *= x[i] - x[k]
            if den != 0:
                l += y[i] * num / den
        y_new.append(l)
    return y_new

if __name__ == "__main__":
    # Teste 1
    points_x = [-1, 0, 1]
    points_y = [0, -1, 0]
    x_list = arange(-10, 10, 0.1)
    y_list = interpola(points_x, points_y, x_list)

    mat.plot(x_list, y_list)
    mat.grid(True)
    mat.show()