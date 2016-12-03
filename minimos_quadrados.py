#!/usr/bin/env
# -*- coding: utf-8 -*-
import numpy as np

import gauss


def polinomio_erro(y, q, r, a, b, a_, b_):
    x = range(5, 41, 5)
    y_new = gauss.erro_n(y, q, r, a, b, a_, b_)
    return np.poly1d(np.polyfit(x, y_new, 3))
