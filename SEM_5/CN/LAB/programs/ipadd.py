import math

def ip_to_vector(ip):
    return list(map(int, ip.split('.')))

def vector_to_ip(ip_vec):
    return '.'.join(map(str, ip_vec))

def bitwise_and(ip1, ip2):
    return [a & b for a, b in zip(ip1, ip2)]

def bitwise_or(ip1, ip2):
    return [a | b for a, b in zip(ip1, ip2)]

def increment_ip(ip_vec, increment):
    ip_vec = ip_vec[:]
    for i in range(3, -1, -1):
        ip_vec[i] += increment
        if ip_vec[i] < 256:
            break
        ip_vec[i] = 0
    return ip_vec

def subnet_mask_to_cidr(mask):
    return sum(bin(octet).count('1') for octet in mask)

def cidr_to_subnet_mask(cidr):
    mask = [0, 0, 0, 0]
    for i in range(cidr):
        mask[i//8] += (1 << (7 - i % 8))
    return mask

def next_power_of_two(n):
    return 2**math.ceil(math.log2(n))

def main():
    ip = input("Enter IP Address (e.g., 172.17.15.7): ")
    subnet_mask = input("Enter Subnet Mask (e.g., 255.255.254.0): ")
    num_subnets = int(input("Enter the number of subnets required: "))

    ip_vec = ip_to_vector(ip)
    mask_vec = ip_to_vector(subnet_mask)

    base_cidr = subnet_mask_to_cidr(mask_vec)
    total_addresses = 2**(32 - base_cidr)

    start_ip_vec = ip_vec

    print("\nEnter the number of addresses required for each subnet:")
    addresses_per_subnet_list = []
    for i in range(num_subnets):
        required_addresses = int(input(f"No. of addresses for subnet {i + 1}: "))
        addresses_per_subnet = next_power_of_two(required_addresses)  # Ensure power of 2 allocation
        addresses_per_subnet_list.append(addresses_per_subnet)

    subnet_start_ip = ip_vec
    subnet_end_ip = None
    for subnet_num, addresses_per_subnet in enumerate(addresses_per_subnet_list):
        required_cidr = 32 - (addresses_per_subnet - 1).bit_length()
        subnet_mask = cidr_to_subnet_mask(required_cidr)

        network_address = bitwise_and(subnet_start_ip, subnet_mask)
        broadcast_address = increment_ip(network_address, addresses_per_subnet - 1)

        print(f"\nSubnet {subnet_num + 1}:")
        print("  First IP Address:", vector_to_ip(network_address))
        print("  Last IP Address:", vector_to_ip(broadcast_address))
        print("  Subnet Mask:", vector_to_ip(subnet_mask))

        # Set the start of the next subnet
        subnet_start_ip = increment_ip(broadcast_address, 1)

    # Calculate remaining addresses
    total_subnet_addresses = sum(addresses_per_subnet_list)
    remaining_addresses = total_addresses - total_subnet_addresses

    if remaining_addresses > 0:
        remaining_end_ip = increment_ip(subnet_start_ip, remaining_addresses - 1)
        print("\nRemaining Addresses:")
        print("  First IP Address:", vector_to_ip(subnet_start_ip))
        print("  Last IP Address:", vector_to_ip(remaining_end_ip))
        print(f"  Number of remaining addresses: {remaining_addresses}")
    else:
        print("\nNo remaining addresses.")

if __name__ == "__main__":
    main()
