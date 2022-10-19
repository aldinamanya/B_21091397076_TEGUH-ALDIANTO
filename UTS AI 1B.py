# TEGUH ALDIANTO
# 21091397076
# KECERDASAN BUATAN
# D4 MANAJEMEN INFORMATIKA

import numpy as np
inputs = [1.2, 2.3, 3.4, 2.5, 5.6, 5.7, 6.8, 7.9, 8.0, 9.0]
weights = [2.2, 3.3, -4.4, 5.0, 6.7, 7.8, 8.9, 9.0, 9.6, -1.9]
weights = [3.5, 2.6, -2.7, 2.8, 2.9, 2.8, 2.7, 3.6, 3.5, 3.4]
weights = [4.4, 3.5, 3.5, 3.6, 3.7, 3.8, 3.9, 4.1, 4.2, 4.3]
weights = [5.2, 5.2, 5.3, 5.4, 5.6, 5.7, 5.8, 5.9, 5.3, 5.4]
weights = [5.6, 5.7, 5.8, 5.9, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6]
bias = [1.0, 2.0, 3.3, 4.3, 5.1]
output = np.dot(weights, inputs) + bias
print(output)