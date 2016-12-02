#!/usr/bin/env
# -*- coding: utf-8 -*-


def v_sol(y, x):
    v = []
    for i in x:
        v.append(y(i))
    return v

