#!/usr/bin/env
# -*- coding: utf-8 -*-
import construtor
import gauss
import jacobi_numpy
import outros
import solve


def y(x):  # Função y(x)
    return x ** 4


def y_2(x):
    return 4 * x ** 3


def y_3(x):
    return 12 * x ** 2


def q(x):
    return 12 / x ** 2  # Função q(x)


def r(x):
    return 0  # Função q(x)


# Extremos
a = 1
b = 2
# Solução da equação nos extremos - alfa e beta
a_ = y(a)
b_ = y(b)

n = 100

# Calcula o passo adequado ao intervalo
h = (b - a) / n

# Cria a malha de pontos
x = []
for i in range(1, n):
    x.append(a + i * h)

v1 = gauss.v_sol_mh(q, r, x, h, n, a_, b_)

v2 = jacobi_numpy.v_sol_mh(q, r, x, h, n, a_, b_, 1000000, 0.00000001)
print('Solução Gauss')
print(v1)
print('Solução Jacobi')
print(v2)
print('Solução real')
print(solve.v_sol(y, x))
print('Resíduo')
print(outros.residuo(construtor.matriz(q, x, h, n), construtor.vetor(r, x, h, n, a_, b_), v2))
