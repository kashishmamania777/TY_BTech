import numpy as np
import matplotlib.pyplot as plt
def identity(x):
    return x
# Sample array of numbers from -5 to 5
x = np.linspace(-5, 5, 100)
# Applying the activation functions to the sample array
y_identity = identity(x)
# Plotting the graphs
def binary_step(x):
    return 1 if x >= 0 else 0
y_binary_step = np.array([binary_step(xi) for xi in x])
plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 2)
plt.plot(x, y_binary_step)
plt.title("Binary Step Function")
plt.tight_layout()
plt.show()