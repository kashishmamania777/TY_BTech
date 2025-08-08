import numpy as np

def bipolar_activation(x):
    """Bipolar activation function: returns 1 if x >= 0, -1 otherwise."""
    return 1 if x >= 0 else -1

def train_perceptron(X, Y, learning_rate, initial_weights, max_epochs):
    """Train the Perceptron network using the given learning rate, initial weights, and epochs."""
    weights = np.array(initial_weights)
    bias = 0.0
    epoch = 0
    converged = False

    while not converged and epoch < max_epochs:
        print(f"\nEpoch {epoch + 1}")
        converged = True
        total_error = 0
        
        for i in range(len(X)):
            # Step 4: Calculate the weighted sum
            weighted_sum = np.dot(X[i], weights) + bias
            
            # Step 5: Apply activation function
            prediction = bipolar_activation(weighted_sum)
            
            # Step 6: Calculate the error
            error = Y[i] - prediction
            total_error += error ** 2  # Sum of squared errors
            
            # Step 7: Update weights and bias if there is an error
            if error != 0:
                converged = False
                weights += learning_rate * error * X[i]
                bias += learning_rate * error
                print(f"Input: {X[i]}, Target: {Y[i]}, Predicted: {prediction}, Error: {error}")
                print(f"Updated Weights: {weights}")
                print(f"Updated Bias: {bias}")
        
        print(f"Total Error: {total_error}")
        
        if converged:
            print("Weights have converged.")
            break
        
        epoch += 1
    
    return weights, bias

# Bipolar Inputs and Targets for AND Function
X = np.array([[-1, -1],  # (0, 0) -> -1
              [-1,  1],  # (0, 1) -> -1
              [ 1, -1],  # (1, 0) -> -1
              [ 1,  1]]) # (1, 1) ->  1
Y = np.array([-1, -1, -1, 1])  # Bipolar targets for AND

# User inputs for learning rate and initial weights
learning_rate = float(input("Enter the learning rate (e.g., 0.1): "))
initial_weights = [float(x) for x in input("Enter initial weights separated by space (e.g., 0.0 0.0): ").split()]

# Maximum number of epochs for training
max_epochs = 1000

# Train the Perceptron
final_weights, final_bias = train_perceptron(X, Y, learning_rate, initial_weights, max_epochs)

print("\nFinal Weights:", final_weights)
print("Final Bias:", final_bias)

# Test the Perceptron with the final weights
def test_perceptron(X, weights, bias):
    """Test the Perceptron with given weights and bias."""
    print("\nTesting Perceptron with final weights:")
    for i in range(len(X)):
        weighted_sum = np.dot(X[i], weights) + bias
        prediction = bipolar_activation(weighted_sum)
        print(f"Input: {X[i]}, Predicted: {prediction}")

# Test the Perceptron
test_perceptron(X, final_weights, final_bias)