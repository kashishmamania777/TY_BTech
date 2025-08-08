import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 100)


mu_A = np.maximum(0, np.minimum((x-2)/2, 1, (6-x)/2))  
mu_B = np.maximum(0, np.minimum((x-5)/2, 1, (9-x)/2))

# 1. Max Membership Method (Height Method)
def max_membership_method(mu):
    return x[np.argmax(mu)]

# 2. Center of Gravity (Centroid Method)
def center_of_gravity(mu):
    return np.sum(mu * x) / np.sum(mu)

# 3. Center of Sums (For simplicity, we'll take the sum of two sets)
def center_of_sums(mu_A, mu_B):
    combined_mu = mu_A + mu_B
    return np.sum(combined_mu * x) / np.sum(combined_mu)

# 4. Mean of Maximum Method
def mean_of_maximum(mu):
    max_val = np.max(mu)
    max_positions = x[mu == max_val]
    return np.mean(max_positions)

# 5. Weighted Average Method
def weighted_average_method(mu):
    max_val = np.max(mu)
    return np.sum(max_val * x) / np.sum(max_val)

# 6. Center of Largest Area (Assuming non-overlapping sets for simplicity)
def center_of_largest_area(mu_A, mu_B):
    area_A = np.sum(mu_A)
    area_B = np.sum(mu_B)
    if area_A > area_B:
        return np.sum(mu_A * x) / np.sum(mu_A)
    else:
        return np.sum(mu_B * x) / np.sum(mu_B)

# Calculate defuzzified values
z_max_membership = max_membership_method(mu_A)
z_center_gravity = center_of_gravity(mu_A)
z_center_sums = center_of_sums(mu_A, mu_B)
z_mean_max = mean_of_maximum(mu_A)
z_weighted_avg = weighted_average_method(mu_A)
z_largest_area = center_of_largest_area(mu_A, mu_B)

# Plotting
plt.figure(figsize=(10, 8))

# Plot fuzzy set A
plt.subplot(2, 2, 1)
plt.plot(x, mu_A, label="Set A", color="blue")
plt.axvline(z_max_membership, color="red", linestyle="--", label="Max Membership")
plt.axvline(z_center_gravity, color="green", linestyle="--", label="Centroid")
plt.axvline(z_mean_max, color="purple", linestyle="--", label="Mean of Max")
plt.title("Fuzzy Set A with Defuzzified Values")
plt.legend()

# Plot fuzzy set B
plt.subplot(2, 2, 2)
plt.plot(x, mu_B, label="Set B", color="orange")
plt.axvline(z_center_sums, color="red", linestyle="--", label="Center of Sums")
plt.axvline(z_largest_area, color="green", linestyle="--", label="Center of Largest Area")
plt.title("Fuzzy Set B with Defuzzified Values")
plt.legend()

# Union of A and B
plt.subplot(2, 2, 3)
combined_mu = mu_A + mu_B
plt.plot(x, combined_mu, label="Union of A and B", color="purple")
plt.title("Union of Fuzzy Sets A and B")
plt.legend()

# Weighted Average
plt.subplot(2, 2, 4)
plt.plot(x, mu_A, label="Set A", color="blue")
plt.axvline(z_weighted_avg, color="orange", linestyle="--", label="Weighted Average")
plt.title("Weighted Average Method")
plt.legend()

plt.tight_layout()
plt.show()
