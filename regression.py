#!/usr/bin/env python
# coding=utf-8
import numpy as np
import scipy as sc
import pdb
import math


def polybasisfunction(x1, x2, n):
    data = [1]
    for i in range(1, n + 1):
        for j in range(i + 1):
            data.append(math.pow(x1, j) * math.pow(x2, i - j))
    return data


def data(fileName):
    f = open(fileName, 'r')
    lines = f.readlines()
    X = []
    Y = []
    for line in lines:
        infos = line.split(',')
        #X.append(polybasisfunction(float(infos[1]), float(infos[2]), 1))
        #Y.append(float(infos[-1]))
        X.append(float(infos[1]))
        Y.append(float(infos[2]))
    f.close()
    return X, Y

def regression(X, Y):
    m = len(X)
    theta = 0
    #pdb.set_trace()   
    for times in range(10000):
        for i in range(m):
            hx = X[i]*theta
            ans = hx - Y[i]
            ans *= X[i]
            theta += 0.01*ans
    print theta
    return theta

X, Y = data('data.txt')
theta = regression(X, Y)
print theta
