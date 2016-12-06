#!/usr/bin/env
# -*- coding: utf-8 -*-


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
