import numpy as np
import matplotlib.pyplot as plt
def identity(x):
    return x
# Sample array of numbers from -5 to 5
x = np.linspace(-5, 5, 100)
# Applying the activation functions to the sample array
y_identity = identity(x)
# Plotting the graphs
def ramp(x):
    return max(0, x)
y_ramp = np.array([ramp(xi) for xi in x])
plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 5)
plt.plot(x, y_ramp)
plt.title("Ramp Function")
plt.tight_layout()
plt.show()