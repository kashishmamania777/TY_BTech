import numpy as np
import matplotlib.pyplot as plt

# Activation functions
def identity(x):
    return x

def binary_step(x):
    return np.where(x >= 0, 1, 0)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def bipolar_sigmoid(x):
    return (2 / (1 + np.exp(-x))) - 1

def ramp(x):
    return np.maximum(0, x)

# Input and weight vectors
input_vector = np.array(list(map(float, input("Enter the input vector (space-separated): ").split())))
weight_vector = np.array(list(map(float, input("Enter the weight vector (space-separated): ").split())))

# Ensure both vectors have the same length
if len(input_vector) != len(weight_vector):
    raise ValueError("Input and weight vectors must have the same length")

# Calculate y_n
y_n = np.dot(input_vector, weight_vector)

# Range of x values for plotting (centered around y_n for better visualization)
x = np.linspace(y_n - 10, y_n + 10, 1000)

# Plot the activation functions
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.plot(x, identity(x), label='Identity')
plt.axvline(x=y_n, color='r', linestyle='--', label=f'y_n = {y_n:.2f}')
plt.title('Identity Function')
plt.grid()
plt.legend()

plt.subplot(2, 3, 2)
plt.plot(x, binary_step(x), label='Binary Step')
plt.axvline(x=y_n, color='r', linestyle='--', label=f'y_n = {y_n:.2f}')
plt.title('Binary Step Function')
plt.grid()
plt.legend()

plt.subplot(2, 3, 3)
plt.plot(x, sigmoid(x), label='Sigmoid')
plt.axvline(x=y_n, color='r', linestyle='--', label=f'y_n = {y_n:.2f}')
plt.title('Sigmoid Function')
plt.grid()
plt.legend()

plt.subplot(2, 3, 4)
plt.plot(x, bipolar_sigmoid(x), label='Bipolar')
plt.axvline(x=y_n, color='r', linestyle='--', label=f'y_n = {y_n:.2f}')
plt.title('Bipolar Function')
plt.grid()
plt.legend()

plt.subplot(2, 3, 5)
plt.plot(x, ramp(x), label='Ramp')
plt.axvline(x=y_n, color='r', linestyle='--', label=f'y_n = {y_n:.2f}')
plt.title('Ramp Function')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# Display the calculated y_n and activation values
print(f"y_n (weighted sum): {y_n}")
print(f"Identity: {identity(y_n)}")
print(f"Binary Step: {binary_step(y_n)}")
print(f"Sigmoid: {sigmoid(y_n)}")
print(f"Bipolar: {bipolar_sigmoid(y_n)}")
print(f"Ramp: {ramp(y_n)}")