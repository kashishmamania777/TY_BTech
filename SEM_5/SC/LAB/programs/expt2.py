def mcculloch_pitts_nand_3input(input1, input2, input3):
    # Weights for the inputs
    w1 = -1
    w2 = -1
    w3 = -1
    
    # Threshold
    theta = -2.5
    
    # Calculate the weighted sum
    weighted_sum = w1 * input1 + w2 * input2 + w3 * input3
    
    # Apply the threshold function
    if weighted_sum > theta:
        return 1
    else:
        return 0

# Function to get binary input from user
def get_binary_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1]:
                return value
            else:
                print("Please enter 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter 0 or 1.")

# Get user inputs for the three inputs
input1 = get_binary_input("Enter the first input (0 or 1): ")
input2 = get_binary_input("Enter the second input (0 or 1): ")
input3 = get_binary_input("Enter the third input (0 or 1): ")

# Get the output of the three-input NAND gate
output = mcculloch_pitts_nand_3input(input1, input2, input3)

# Display the result
print(f"Three-Input NAND Gate Output for inputs ({input1}, {input2}, {input3}): {output}")