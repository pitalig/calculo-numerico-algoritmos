#!/usr/bin/env
# -*- coding: utf-8 -*-
import math
import gauss
import jacobi_numpy
import solve


def y(x):  # Função y(x)
    return 7 * math.pow(x, 4) * math.sin(math.pi * x)


def y_2(x):
    return (7 * math.pow(x, 3) * (4 * math.sin(math.pi * x)
                                  + math.pi * x * math.cos(math.pi * x)))


def y_3(x):
    return (- math.pow(math.pi, 2) * 7 * math.pow(x, 4) * math.sin(math.pi * x)
            + 56 * math.pow(x, 2) * math.pi * math.cos(math.pi * x)
            + 84 * math.pow(x, 2) * math.sin(math.pi * x))


# Função q(x)
def q(x):
    return (12 / math.pow(x, 2)
            - (math.pow(math.pi, 2)))


# Função r(x)
def r(x):
    return 56 * math.pow(x, 2) * math.pi * math.cos(math.pi * x)


# Extremos
a = 0
b = 1
# Solução da equação nos extremos - alfa e beta
a_ = y(a)
b_ = y(b)

n = 10

# Calcula o passo adequado ao intervalo
h = (b - a) / n

# Cria a malha de pontos
x = []
for i in range(1, n):
    x.append(a + i * h)

v1 = gauss.v_sol_mh(q, r, x, h, n, a_, b_)

v2 = jacobi_numpy.v_sol_mh(q, r, x, h, n, a_, b_, 100, 0.0001)
print('Solução Gauss')
print(v1)
print('Solução Jacobi')
print(v2)
print('Solução real')
print(solve.v_sol(y, x))
