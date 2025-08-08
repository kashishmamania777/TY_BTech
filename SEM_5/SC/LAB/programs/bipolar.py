import numpy as np
import matplotlib.pyplot as plt
def identity(x):
    return x
# Sample array of numbers from -5 to 5
x = np.linspace(-5, 5, 100)
# Applying the activation functions to the sample array
y_identity = identity(x)
# Plotting the graphs
def bipolar_sigmoid(x):
    return (2 / (1 + np.exp(-x))) - 1
y_bipolar_sigmoid = bipolar_sigmoid(x)
plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 4)
plt.plot(x, y_bipolar_sigmoid)
plt.title("Bipolar Sigmoid Function")


plt.tight_layout()
plt.show()
