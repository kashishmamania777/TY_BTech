import numpy as np
import matplotlib.pyplot as plt
def identity(x):
    return x
# Sample array of numbers from -5 to 5
x = np.linspace(-5, 5, 100)
# Applying the activation functions to the sample array
y_identity = identity(x)
# Plotting the graphs
plt.figure(figsize=(10, 6))
plt.subplot(2, 3, 1)
plt.plot(x, y_identity)
plt.title("Identity Function")
plt.tight_layout()
plt.show()