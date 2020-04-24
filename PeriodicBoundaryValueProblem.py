import PeriodicBoundaryValueProblemMisc as misc
import matplotlib.pyplot as plt
import numpy
import math
import datetime

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
    matrix[i][i + 1] = 1

for i in range(1, matrix.__len__()):
    matrix[i][i - 1] = 1

matrix[0][N - 1] = 1
matrix[N - 1][0] = 1

f = numpy.array(f)

matrix_np = numpy.array(matrix)
solution = numpy.linalg.solve(matrix_np, math.pow(h, 2) * f)

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
column_G[N - 2] = -1
column_F = numpy.array(column_F)
column_G = numpy.array(column_G)

my_pre_solution = [0.0] * (N - 1)
d_time = datetime.datetime.now()
y_1 = misc.solveTriMatrix(matrix_B, math.pow(h, 2) * column_F)
y_2 = misc.solveTriMatrix(matrix_B, column_G)
x_N_1 = (misc.f(1) * math.pow(h, 2) - y_1[0] - y_1[N - 2]) / (matrix[N - 1][N - 1] + y_2[N - 2] + y_2[0])

for i in range(0, N - 1):
    my_pre_solution[i] = y_1[i] + x_N_1 * y_2[i]

my_solution = [0.0] * N

for i in range(0, N - 1):
    my_solution[i] = my_pre_solution[i]

my_solution[N - 1] = x_N_1

plt.plot(t_lol, y_1)
plt.title(r'$y^{(1)}$')
plt.grid(True)
plt.minorticks_on()
plt.grid(which='minor', linestyle=':')
plt.show()

plt.plot(t_lol, y_2)
plt.title(r'$y^{(2)}$')
plt.grid(True)
plt.minorticks_on()
plt.grid(which='minor', linestyle=':')
plt.show()

plt.plot(t, my_solution)
plt.title(r'$y$')
plt.grid(True)
plt.minorticks_on()
plt.grid(which='minor', linestyle=':')
plt.show()

plt.plot(t, solution)
plt.title("solution of numpy.linalg.solve")
plt.grid(True)
plt.minorticks_on()
plt.grid(which='minor', linestyle=':')
plt.show()
