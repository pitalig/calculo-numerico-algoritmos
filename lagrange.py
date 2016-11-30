#!/usr/bin/env
# -*- coding: utf-8 -*-
import matplotlib.pyplot as mat


def polinomio_interp(y, x):
    l = 0
    for i in range(len(y)):
        num = 1
        den = 1
        for k in range(len(x)):
            if i != k:
                num *= x - x[k]
                den *= x[i] - x[k]
        l += y[i] * num / den
    return l

if __name__ == "__main__":
    points = [(-1, 0), (0, -1), (1, 0)]
    x_list = range(-10, 10)
    y_list = [interpolador(points, x) for x in range(-10, 10)]

    mat.plot(x_list, y_list)
    mat.grid(True)
    mat.show()