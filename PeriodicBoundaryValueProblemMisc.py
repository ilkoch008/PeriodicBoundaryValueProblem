import matplotlib.pyplot as plt
import numpy
import math


def p2(x):
    return 10 + math.sin(2 * math.pi * x)


def f(x):
    return math.cos(2 * math.pi * x)


def b(n, h):
    return -(2 + math.pow(h, 2) * p2(n * h))


def solveTriMatrix(matrix, column):
    solution = [0.0] * len(column)
    for i in range(0, len(column)):
        solution[i] = column[i]

    for i in range(0, len(matrix) - 1):
        k = matrix[i+1][i] / matrix[i][i]
        for j in range(0, len(matrix)):
            matrix[i+1][j] = matrix[i+1][j] - matrix[i][j] * k

        solution[i+1] = solution[i+1] - solution[i] * k

    for i in range(len(matrix) - 2, 0):
        k = matrix[i][i+1] / matrix[i+1][i+1]
        for j in range(0, len(matrix)):
            matrix[i][j] = matrix[i][j] - matrix[i+1][j] * k

        solution[i] = solution[i] - solution[i+1] * k

    return solution
