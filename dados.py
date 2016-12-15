#!/usr/bin/env
# -*- coding: utf-8 -*-
# Módulo dados: contém os dados da equação utilizada como objeto de estudo

import math


def y(x):  # Função y(x)
    return 7 * x ** 4 * math.sin(math.pi * x)


def y_2(x):  # Função y'(x)
    return (7 * x ** 3 * (4 * math.sin(math.pi * x)
                          + math.pi * x * math.cos(math.pi * x)))


def y_3(x):  # Função y"(x)
    return (- math.pi ** 2 * 7 * x ** 4 * math.sin(math.pi * x)
            + 56 * x ** 3 * math.pi * math.cos(math.pi * x)
            + 84 * x ** 2 * math.sin(math.pi * x))


def q(x):  # Função q(x)
    return (12 / x ** 2
            - math.pi ** 2)


def r(x):  # Função r(x)
    return 56 * x ** 3 * math.pi * math.cos(math.pi * x)


# Extremos
a = 0
b = 1

# Solução da equação nos extremos - alfa e beta
a_ = y(a)
b_ = y(b)
