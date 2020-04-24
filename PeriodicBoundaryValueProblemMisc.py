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
    loc_matrix = [0] * len(matrix)
    for i in range(0, len(matrix)):
        loc_matrix[i] = [0.0] * len(matrix)

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            loc_matrix[i][j] = matrix[i][j]

    solution = [0.0] * len(column)
    for i in range(0, len(column)):
        solution[i] = column[i]

    for i in range(0, len(loc_matrix) - 1):
        k = loc_matrix[i+1][i] / loc_matrix[i][i]
        for j in range(0, len(loc_matrix)):
            loc_matrix[i+1][j] = loc_matrix[i+1][j] - loc_matrix[i][j] * k

        solution[i+1] = solution[i+1] - solution[i] * k

    for i in range(len(loc_matrix) - 2, -1, -1):
        k = loc_matrix[i][i+1] / loc_matrix[i+1][i+1]
        for j in range(0, len(loc_matrix)):
            loc_matrix[i][j] = loc_matrix[i][j] - loc_matrix[i+1][j] * k

        solution[i] = solution[i] - solution[i+1] * k

    for i in range(0, len(solution)):
        solution[i] = solution[i] / loc_matrix[i][i]

    return numpy.array(solution)
