#!/usr/bin/env
# -*- coding: utf-8 -*-


def v_sol(y, x, n):
    v = []
    for i in range(0, n - 1):
        v.append(y(x[i]))
    return v
