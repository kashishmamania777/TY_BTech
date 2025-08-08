import numpy as np
def binary_step(x, threshold=0):
    return 1 if x >= threshold else 0
def bipolar_step(x, threshold=0):
    return 1 if x >= threshold else -1
np.random.seed(42)
weights = np.random.uniform(-1, 1, 3)
bias=1
#bias = np.random.uniform(-1, 1)
learning_rate = 0.7

inputs = np.array([
    [0, 0, 0],
    [0, 0, 1],
    [0, 1, 0],
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 1],
    [1, 1, 0],
    [1, 1, 1]
])
expected_outputs_binary = np.array([0, 0, 0, 0, 0, 0, 0, 1])  # Binary AND
expected_outputs_bipolar = np.array([-1, -1, -1, -1, -1, -1, -1, 1])  # Bipolar AND

# Hebbian learning with binary step function
print("Hebbian Learning with Binary Step Function")
for i, input_vector in enumerate(inputs):
    net_input = np.dot(weights, input_vector) + bias
    output = binary_step(net_input, threshold=0.5)
    print(f"Input: {input_vector}, Net input: {net_input:.3f}, Output: {output}")

    weights += learning_rate * input_vector * output
    bias += learning_rate * output
    
    print(f"Updated Weights: {weights}, Updated Bias: {bias}")
    print()

weights = np.random.uniform(-1, 1, 3)
bias = np.random.uniform(-1, 1)

# Hebbian learning with bipolar step function
print("Hebbian Learning with Bipolar Step Function")
for i, input_vector in enumerate(inputs):
    net_input = np.dot(weights, input_vector) + bias
    output = bipolar_step(net_input, threshold=0)
    print(f"Input: {input_vector}, Net input: {net_input:.3f}, Output: {output}")

    weights += learning_rate * input_vector * output
    bias += learning_rate * output
    
    print(f"Updated Weights: {weights}, Updated Bias: {bias}")
    print()