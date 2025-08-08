import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def ramp(x):
    return np.where(x <= 0, 0,
                    np.where(x < 1, x,
                             1))

def binary_step(x):
    return np.where(x > 0, 1, 0)

def identity(x):
    return x

def bipolar_sigmoid(x):
    return (2 / (1 + np.exp(-x))) - 1

def relu(x):
    return np.maximum(0, x)


x = np.linspace(-15, 15, 100)


y_sigmoid = sigmoid(x)
y_ramp = ramp(x)
y_binary_step = binary_step(x)
y_identity = identity(x)
y_bipolar_sigmoid = bipolar_sigmoid(x)
y_relu = relu(x)


plt.figure(figsize=(15, 10))

plt.subplot(2, 3, 1)
plt.plot(x, y_sigmoid, label="Sigmoid Function", color='blue')
plt.title("Sigmoid Function")
plt.xlabel("x")
plt.ylabel("Sigmoid(x)")
plt.legend()

plt.subplot(2, 3, 2)
plt.plot(x, y_ramp, label="Ramp Function", color='green')
plt.title("Ramp Function")
plt.xlabel("x")
plt.ylabel("Ramp(x)")
plt.legend()

plt.subplot(2, 3, 3)
plt.plot(x, y_binary_step, label="Binary Step Function", color='red')
plt.title("Binary Step Function")
plt.xlabel("x")
plt.ylabel("Binary Step(x)")
plt.legend()

plt.subplot(2, 3, 4)
plt.plot(x, y_identity, label="Identity Function", color='purple')
plt.title("Identity Function")
plt.xlabel("x")
plt.ylabel("Identity(x)")
plt.legend()

plt.subplot(2, 3, 5)
plt.plot(x, y_bipolar_sigmoid, label="Bipolar Sigmoid Function", color='orange')
plt.title("Bipolar Sigmoid Function")
plt.xlabel("x")
plt.ylabel("Bipolar Sigmoid(x)")
plt.legend()

plt.subplot(2, 3, 6)
plt.plot(x, y_relu, label="ReLU Function", color='cyan')
plt.title("ReLU Function")
plt.xlabel("x")
plt.ylabel("ReLU(x)")
plt.legend()

plt.tight_layout()
plt.show()
