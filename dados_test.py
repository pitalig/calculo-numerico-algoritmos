#!/usr/bin/env
# -*- coding: utf-8 -*-
# Módulo dados de teste: contém os dados da equação utilizada como exemplo pelo professor
# Foi utilizado para testar os métodos a validar se os resultados estavam de acordo com o esperado

import math


def y(x):  # Função y(x)
    return 1 / x


def y_2(x):  # Função y'(x)
    return -1 / math.pow(x, 2)


def y_3(x):  # Função y"(x)
    return 2 / (x ** 3)


def q(x):  # Função q(x)
    return 1 / (x ** 2)  # Função q(x)


def r(x):  # Função r(x)
    return 1 / (x ** 3)  # Função q(x)


# Extremos
a = 1
b = 2

# Solução da equação nos extremos - alfa e beta
a_ = y(a)
b_ = y(b)
