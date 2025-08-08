import math

# Function to convert decimal octet to binary string
def decimal_to_binary(octet):
    return f'{octet:08b}'

# Function to convert binary string to decimal octet
def binary_to_decimal(binary_str):
    return int(binary_str, 2)

# Function to calculate subnet mask from binary mask
def binary_to_subnet_mask(binary_mask):
    octets = [binary_to_decimal(binary_mask[i:i+8]) for i in range(0, len(binary_mask), 8)]
    return '.'.join(map(str, octets))

# Function to convert IP address from vector form to string
def vector_to_ip(ip_vec):
    return '.'.join(map(str, ip_vec))

# Function to increment an IP address by a certain number of addresses
def increment_ip(ip, increment):
    ip_copy = ip[:]
    ip_copy[3] += increment
    if ip_copy[3] >= 256:
        ip_copy[2] += ip_copy[3] // 256
        ip_copy[3] %= 256
    if ip_copy[2] >= 256:
        ip_copy[1] += ip_copy[2] // 256
        ip_copy[2] %= 256
    if ip_copy[1] >= 256:
        ip_copy[0] += ip_copy[1] // 256
        ip_copy[1] %= 256
    return ip_copy

# Accept IP address and subnet mask from the user
IP = input("Enter IP address (e.g., 172.17.15.7): ")
subnet_mask = input("Enter subnet mask (e.g., 255.255.254.0): ")

# Convert IP address and subnet mask to vector
ip_arr = list(map(int, IP.split('.')))
subnet_mask_vec = list(map(int, subnet_mask.split('.')))

# Convert subnet mask from decimal to binary
subnet_mask_binary = ''.join(decimal_to_binary(octet) for octet in subnet_mask_vec)
print(f"Subnet mask (binary): {subnet_mask_binary}")

# Number of subnets to be created
num_subnets = int(input("Enter number of subnets to be created: "))

# Take the number of addresses per subnet from the user
addresses_per_subnet = []
for i in range(num_subnets):
    num_addresses = int(input(f"Enter number of addresses required for Subnet {i + 1}: "))
    addresses_per_subnet.append(num_addresses)

# Calculate the number of subnet bits needed
required_bits = math.ceil(math.log2(max(addresses_per_subnet)))
subnet_bits = required_bits
subnet_mask_binary_new = subnet_mask_binary[:32 - subnet_bits] + '1' * subnet_bits
subnet_mask = binary_to_subnet_mask(subnet_mask_binary_new)
print(f"Subnet mask: {subnet_mask}")

# Calculate the number of hosts per subnet
zero_bits = subnet_mask_binary_new.count('0')
hosts_per_subnet = 2 ** zero_bits - 2  # Subtracting 2 for network and broadcast addresses

print(f"Subnet Generator: {hosts_per_subnet} hosts per subnet")

# Generate subnets
current_ip = ip_arr[:]
subnet_ips = ip_arr[:]
subnet_size = 2 ** (32 - len(subnet_mask_binary_new.replace('0', '')))

for i in range(num_subnets):
    num_addresses = addresses_per_subnet[i]
    # Calculate required number of IPs for the current subnet (next power of 2)
    required_ips = 2 ** math.ceil(math.log2(num_addresses + 2))  # +2 for network and broadcast addresses

    start_ip = subnet_ips[:]
    end_ip = start_ip[:]
    
    # Calculate the end IP for the current subnet
    end_ip = increment_ip(start_ip, required_ips - 1)

    print(f"Subnet {i + 1}:")
    print(f"  First IP Address: {vector_to_ip(start_ip)}")
    print(f"  Last IP Address: {vector_to_ip(end_ip)}")
    
    # Move to the next subnet
    current_ip = increment_ip(end_ip, 1)
    subnet_ips = current_ip

# Calculate remaining addresses
total_addresses = 2 ** (32 - len(subnet_mask_binary_new.replace('0', '')))
used_addresses = sum(2 ** math.ceil(math.log2(num + 2)) for num in addresses_per_subnet)
remaining_addresses = total_addresses - used_addresses

if remaining_addresses > 0:
    remaining_start_ip = current_ip
    remaining_end_ip = increment_ip(remaining_start_ip, remaining_addresses - 1)
    print("\nRemaining Addresses:")
    print(f"  First IP Address: {vector_to_ip(remaining_start_ip)}")
    print(f"  Last IP Address: {vector_to_ip(remaining_end_ip)}")
    print(f"  Number of remaining addresses: {remaining_addresses}")
else:
    print("\nNo remaining addresses.")
