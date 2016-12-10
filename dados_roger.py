#!/usr/bin/env
# -*- coding: utf-8 -*-
import math


def y(x):  # Função y(x)
    return (x ** 4) * math.exp(x ** 2)


# Função q(x)
def q(x):
    return 4 * (x ** 2) + 18


# Função r(x)
def r(x):
    return (x ** 2) * 12 * math.exp(x ** 2)


# Extremos
a = 0
b = 1
# Solução da equação nos extremos - alfa e beta
a_ = y(a)
b_ = y(b)