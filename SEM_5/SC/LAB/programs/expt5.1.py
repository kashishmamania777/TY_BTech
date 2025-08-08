import numpy as np

# Define bipolar inputs for AND NOT function
inputs = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])  # Bipolar inputs
targets = np.array([-1, -1, 1, -1])  # Bipolar outputs for AND NOT

# Initialize weights, bias, and learning rate
weights = np.random.uniform(-1, 1, size=2)  # Random weights between -1 and 1
bias = np.random.uniform(-1, 1)  # Random bias between -1 and 1
learning_rate = 0.1  # Learning rate
epochs = 1  # Number of epochs, only 1 for this example

# Adaline training for 1 epoch
print(f"Initial weights: {weights}, Bias: {bias}\n")

for epoch in range(epochs):
    print(f"Epoch {epoch + 1}")

    for i in range(len(inputs)):
        # Set activation of input unit xi = si
        x = inputs[i]
        target = targets[i]

        # Compute net input to output unit
        net_input = np.dot(weights, x) + bias

        # Compute error
        error = target - net_input

        # Update weights and bias
        weights += learning_rate * error * x
        bias += learning_rate * error

        # Display the updated weights and bias
        print(f"Training set {i + 1}: Input: {x}, Target: {target}")
        print(f"Net Input: {net_input:.4f}, Error: {error:.4f}")
        print(f"Updated weights: {weights}, Updated Bias: {bias:.4f}\n")

    print("-" * 50)

print(f"Final weights after 1 epoch: {weights}, Final Bias: {bias}")
