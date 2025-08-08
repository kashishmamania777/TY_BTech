import numpy as np

# OR function with bipolar inputs and outputs
inputs = np.array([[-1, -1], [-1, 1], [1, -1], [1, 1]])  # Bipolar inputs
targets = np.array([-1, 1, 1, 1])  # OR function outputs in bipolar form

# Initialize weights as equal and same, bias as 1, and learning rate
initial_weight_value = 0.5  # Initial weight value (equal and same for both weights)
weights = np.array([initial_weight_value, initial_weight_value])  # Equal weights
bias = 1.0  # Bias initialized to 1
learning_rate = 0.1  # Learning rate
max_epochs = 1000  # Maximum number of epochs to allow for convergence check
convergence_threshold = 1e-5  # Threshold for convergence (error tolerance)

# Adaline training
print(f"Initial weights: {weights}, Bias: {bias}\n")

epoch = 0
previous_total_error = float('inf')  # Set initial total error to infinity

while epoch < max_epochs:
    print(f"Epoch {epoch + 1}")
    total_error = 0  # Reset total error for the current epoch

    for i in range(len(inputs)):
        # Step 4: Set activation of input unit xi = si
        x = inputs[i]
        target = targets[i]

        # Step 5: Compute net input to output unit
        net_input = np.dot(weights, x) + bias

        # Step 6: Calculate squared error
        error = (target - net_input)  # Error term
        squared_error = error ** 2  # Squared error

        # Update weights and bias
        weights += learning_rate * error * x
        bias += learning_rate * error

        # Accumulate total error
        total_error += squared_error

        # Display the updated weights and bias
        print(f"Training set {i + 1}: Input: {x}, Target: {target}")
        print(f"Net Input: {net_input:.4f}, Error: {error:.4f}, Squared Error: {squared_error:.4f}")
        print(f"Updated weights: {weights}, Updated Bias: {bias:.4f}\n")

    # Check for convergence
    if abs(previous_total_error - total_error) < convergence_threshold:
        print("Convergence reached!")
        break

    # Update for the next epoch
    previous_total_error = total_error
    epoch += 1
    print(f"Total Error after Epoch {epoch}: {total_error:.6f}")
    print("-" * 50)

# Print final results
print(f"Final weights: {weights}, Final Bias: {bias}")
print(f"Training completed in {epoch + 1} epochs.")
