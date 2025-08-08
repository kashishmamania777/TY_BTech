import numpy as np

# Define the initial weights and the learning rate
weights = np.array([1, -1, 0, 0.5])
learning_rate = 1  # You can set it to any value as needed

# Define the input vectors
X1 = np.array([1, -2, 1.5, 0])
X2 = np.array([1, -0.5, -2, -1.5])
X3 = np.array([0, 1, -1, 1.5])

# List of all input vectors
inputs = [X1, X2, X3]

# Hebbian learning process
print("Initial Weights:", weights)

for i, input_vector in enumerate(inputs):
    # Hebbian learning update rule: Δw = η * x * y
    # Assuming the output y = x for simplicity in Hebbian learning
    output = input_vector  # For Hebbian, output = input
    delta_w = learning_rate * output * output  # Δw = η * x * y (y = x)
    weights += delta_w
    print(f"After input X{i + 1} ({input_vector}): Updated Weights: {weights}")
print("Final Weights after Hebbian learning:", weights)
