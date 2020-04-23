import PeriodicBoundaryValueProblemMisc as misc
import matplotlib.pyplot as plt
import numpy
import math


h = 0.005
N = int(1 / h)

solution = [0.0] * N
t = [0.0] * N
t_lol = [0.0] * (N - 1)
f = [0.0] * N
matrix = [0] * N

for i in range(0, t.__len__()):
    t[i] = i * h

for i in range(0, t_lol.__len__()):
    t_lol[i] = i * h

for i in range(0, f.__len__()):
    f[i] = misc.f(i * h)

for i in range(0, matrix.__len__()):
    matrix[i] = [0.0] * matrix.__len__()

for i in range(0, matrix.__len__()):
    matrix[i][i] = misc.b(i, h)

for i in range(0, matrix.__len__() - 1):
    matrix[i][i+1] = 1

for i in range(1, matrix.__len__()):
    matrix[i][i-1] = 1

matrix[0][N-1] = 1
matrix[N-1][0] = 1

matrix_np = numpy.array(matrix)
solution = numpy.linalg.solve(matrix_np, f)

matrix_B = [0.0] * (N - 1)
for i in range(0, matrix_B.__len__()):
    matrix_B[i] = [0.0] * (N - 1)

for i in range(0, N - 1):
    for j in range(0, N - 1):
        matrix_B[i][j] = matrix[i][j]

column_F = [0.0] * (N - 1)
for i in range(0, N - 1):
    column_F[i] = f[i]

column_G = [0.0] * (N - 1)
column_G[0] = -1
column_G[N-2] = -1

x_1 = misc.solveTriMatrix(matrix_B, column_F)
x_2 = misc.solveTriMatrix(matrix_B, column_G)

plt.plot(t_lol, x_2)
plt.show()
