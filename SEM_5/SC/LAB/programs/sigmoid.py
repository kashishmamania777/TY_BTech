import numpy as np
import matplotlib.pyplot as plt
def identity(x):
    return x
# Sample array of numbers from -5 to 5
x = np.linspace(-5, 5, 100)
# Applying the activation functions to the sample array
y_identity = identity(x)
# Plotting the graphs
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
y_sigmoid = sigmoid(x)
plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 3)
plt.plot(x, y_sigmoid)
plt.title("Sigmoid Function")
plt.tight_layout()
plt.show()