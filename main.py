#!/usr/bin/env
# -*- coding: utf-8 -*-
import math


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
