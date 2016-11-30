#!/usr/bin/env
# -*- coding: utf-8 -*-
import math


def matriz(q, x, h, n):
    b = []
    for i in range(n-1):
        l = [0] * (n-1)
        l[i] = 2 + math.pow(h, 2) * q(x[i])
        b.append(l)
    for i in range(n-2):
        b[i + 1][i] = -1
        b[i][i + 1] = -1
    return b


def vetor(r, x, h, n, a_, b_):
    z = []
    for i in range(n-1):
        z.append(- math.pow(h, 2) * r(x[i]))
    z[0] += a_
    z[n-2] += b_
    return z


# ----------------teste----------------
if __name__ == "__main__":
    def q(x):
        return 5 * x


    x = range(5)
    h = 1
    n = 5

    print(matriz(q, x, h, n))


    def r(x):
        return math.pow(x, 2)


    print(vetor(r, x, h, n, 0, 0))
