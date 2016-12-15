#!/usr/bin/env
# -*- coding: utf-8 -*-
# Módulo Largange: Métodos para criação do polinômio interpolador de lagrange

import matplotlib.pyplot as mat
from numpy import arange


# Cria o polinômio interpolador, baseado em um conjunto resultados já conhecidos.
# Entradas: lista de pontos de x já conhecidos, solução y correspondente aos pontos x já conhecidos,
# intervalo de pontos de x para onde se deseja obter a solução.
# Retorno: a função com o polinômio interpolador
def pol_interpola(x, y):
    # Define a função pol_lagrange
    def pol_lagrange(x_i):
        pol = 0
        # Calcula o polinômio interpolador
        for i in range(len(y)):
            num = 1
            den = 1
            for k in range(len(x)):
                if i != k:
                    num *= x_i - x[k]
                    den *= x[i] - x[k]
            if den != 0:
                pol += y[i] * num / den
        return pol

    return pol_lagrange


# Calcula o vetor solução (y), para um intervalo de pontos de x, baseado em um conjunto resultados já conhecidos.
# Entradas: lista de pontos de x já conhecidos, solução y correspondente aos pontos x já conhecidos,
# intervalo de pontos de x para onde se deseja obter a solução.
# Retorno: vetor solução para o intervalo escolhido
def interpola_vetor(x, y, x_new):
    p = pol_interpola(x, y)
    y_new = []
    for x_i in x_new:
        y_new.append(p(x_i))
    return y_new

if __name__ == "__main__":
    # Teste 1
    points_x = [-1, 0, 1]
    points_y = [0, -1, 0]
    x_list = arange(-10, 10, 0.1)
    y_list = interpola_vetor(points_x, points_y, x_list)

    mat.plot(x_list, y_list)
    mat.grid(True)
    mat.show()
