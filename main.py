#!/usr/bin/env
# -*- coding: utf-8 -*-
import math
import numpy as np
import constr_matriz
import gauss
import solve
import matplotlib.pyplot as plt


def y(x):  # Função y(x)
    return 7 * math.pow(x, 4) * math.sin(math.pi * x)


def y_2(x):
    return (7 * math.pow(x, 3) * (4 * math.sin(math.pi * x)
            + math.pi * x * math.cos(math.pi * x)))


def y_3(x):
    return (- math.pow(math.pi, 2) * 7 * math.pow(x, 4) * math.sin(math.pi * x)
            + 56 * math.pow(x, 2) * math.pi * math.cos(math.pi * x)
            + 84 * math.pow(x, 2) * math.sin(math.pi * x))


def q(x):
    return - (math.pow(math.pi, 2))  # Função q(x)


def r(x):  # Função r(x)
    return (56 * math.pow(x, 2) * math.pi * math.cos(math.pi * x)
            + 84 * math.pow(x, 2) * math.sin(math.pi * x))


# Extremos
a = 0
b = 1
# Solução da equação nos extremos - alfa e beta
a_ = y(a)
b_ = y(b)

# Número de passos (inserido pelo usuário)
n = int(input("Insira o número de passos utilizados: "))

# Tamanho total do intervalo
h = (b - a) / n

# Malha de pontos
x = []
for i in range(1, n):
    x.append(a + i*h)


# Vetor solução real
v_sol = solve.solve(y, x, n)
print("Solução real")
print(np.matrix(v_sol))

# Matriz e vetor de termos independentes
m_h = constr_matriz.constr_matriz(q, x, h, n)
v_h = constr_matriz.constr_vetor(r, x, h, n, a_, b_)

# Vetor solução pelo método de Gauss
v_gauss = gauss.gauss(m_h, v_h, n-1)
print("Solução Gauss")
print(np.matrix(v_gauss))

# Comparação entre soluções
dif = abs(np.matrix(v_sol) - np.matrix(v_gauss))
print("Diferença entre real e gauss (Erro)")
print(dif)
print("Erro máximo")
print(np.max(dif))
