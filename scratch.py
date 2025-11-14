# import numpy as np

# P = np.array([[0.5, 0.5],
#               [0.33, 0.66],
#               ])

# A = P.T - np.eye(2)
# A = np.vstack([A, np.ones(2)])
# b = np.array([0, 0, 1])

# # Solve using least squares
# pi, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
# print("Stationary distribution:", pi)

a,b = 256, 256

c,d = 10000, 10000
print(a is b, c is d)