#!/usr/bin/env
# -*- coding: utf-8 -*-
import math


def jacobi(q, x, h, y, tol, n_max, n):
    w_0 = [0] * (n - 1)
    w_new = w_0
    w_old = []
    for i in range(n):
        w_old.append(w_0[i] + 2 * tol)
    norma = 2 * tol
    i = 0
    while norma > tol and i < n_max:
        i += 1
        w_old = w_new
        w_new[0] = (1 / (2 + math.pow(h, 2) * q(x[0]))) * (y(x[0]) + w_old[1])
        w_new[n - 1] = (1 / (2 + math.pow(h, 2) * q(x[n - 1]))) * (y(x[n - 1]) + w_old[n - 2])
        for i in range(1, n - 2):
            w_new[i] = (1 / (2 + math.pow(h, 2) * q(x[i]))) * (y(x[i]) + w_old[i - 1] + w_old[i + 1])
        for i in range(n):
            norma += math.pow((w_new[i] - w_old[i]), 2)
    return w_new
