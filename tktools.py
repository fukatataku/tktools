# -*- coding: utf-8 -*-

def convolute(proc, iterable, start=0):
    rtn = []
    acc = start
    for value in iterable:
        result, acc = proc(value, acc)
        rtn.append(result)
    return rtn
