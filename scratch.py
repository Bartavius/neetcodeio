# import numpy as np
# import matplotlib.pyplot as plt

# w = np.array([4, -5])
# b = -2

# origin = np.array([0,0])


# plt.figure(figsize=(8, 8))

# # w vector
# plt.quiver(
#     origin[0], origin[1],
#     w[0], w[1],
#     angles='xy', scale_units='xy', scale=1,
#     color='black', label='Weight Vector w'
# )

# # orthog line
# orth = np.array([5, 4])
# t = np.linspace(-5, 5, 10)
# orth_x = t * orth[0]
# orth_y = t * orth[1]
# plt.plot(orth_x, orth_y, label="orthogonal to w line")

# # boundary
# x_vals = np.linspace(-10, 10, 10)
# y_vals = (w[0] * x_vals + b) / -w[1]

# plt.plot(x_vals, y_vals, label='Decision Boundary')

# plt.xlim(-10, 10)
# plt.ylim(-10, 10)
# plt.axhline(0, color='gray', linewidth=0.5)
# plt.axvline(0, color='gray', linewidth=0.5)
# plt.gca().set_aspect('equal', adjustable='box')

# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Weight Vector, Orthogonal Line, and Decision Boundary")
# plt.legend()
# plt.grid(True)
# plt.show()

from scipy.special import expit
import numpy as np

def cross_ent_loss(x):

    # weight vectors
    w1 = np.array([0, 4, -4, 5, 4])
    w2 = np.array([2, 2, -4, 3, 0])
    v1 = np.array([1, -2])
    v2 = np.array([2, 3])
    v3 = np.array([1, 2])

    # biases
    w1_b = 1
    w2_b = 1
    v1_b = -1
    v2_b = 0
    v3_b = 2

    # 0, 1, or 2 class
    one_shot = [0, 1, 0] # '1' is true class

    # layer 1 ReLU
    z = np.array([
        np.maximum(np.dot(x, w1) + w1_b, 0),
        np.maximum(np.dot(x, w2) + w2_b, 0)
        ])
    
    # layer 2 sigmoid
    z = np.array([
        expit(np.dot(z, v1) + v1_b),
        expit(np.dot(z, v2) + v2_b),
        expit(np.dot(z, v3) + v3_b),
    ])

    softmax = np.exp(z) / np.sum(np.exp(z))

    # cross ent loss fn
    L = -np.sum(one_shot * np.log(softmax))
    return L

x = [6,4,7,2,1]
res = cross_ent_loss(x)
print(res)
