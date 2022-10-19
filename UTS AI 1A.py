# TEGUH ALDIANTO
# 21091397076
# KECERDASAN BUATAN
# D4 MANAJEMEN INFORMATIKA

import numpy as np
inputs = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
weights = [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0]
bias = 2.0
outputs = np.dot(weights, inputs) + bias
print(outputs)