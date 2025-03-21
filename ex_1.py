import numpy as np

P = np.array ([[0.9,0.1], [0.2,0.8]])
print ('\n P1 =\n', P)

P2 = np.linalg.matrix_power(P, 2)
print ('\n P2 =\n', P2)

P3 = np.linalg.matrix_power(P, 3)
print ('\n P3 =\n', P3)

P10 = np.linalg.matrix_power(P, 10)
print ('\n P10 =\n', P10)

P56 = np.linalg.matrix_power(P, 56)
print ('\n P56 =\n', P56)

P100 = np.linalg.matrix_power(P, 100)
print ('\n P100=\n', P100)

V=np.array([[0.3,0.7]])

CV=V.dot(P10)
print ('\n Comportamento do Consumidor =\n', CV)

