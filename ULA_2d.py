import numpy as np
import matplotlib.pyplot as plt

# Parameters
num_elements = 8  # Number of antennas in the array
d = 0.5  # Distance between elements (in wavelengths)
theta_target = 30  # Target angle in degrees
theta_range = np.linspace(-90, 90, 1000)  # Range of angles to evaluate (in degrees)
wavelength = 1  # Wavelength of the signal

# Calculate wave number (k)
k = 2 * np.pi / wavelength

# Beamforming weights for the target angle
phase_shifts = k * d * np.sin(np.radians(theta_target)) * np.arange(num_elements)
weights = np.exp(1j * phase_shifts)

# Array factor calculation
def array_factor(theta):
    theta_rad = np.radians(theta)  # Convert to radians
    steering_vector = np.exp(1j * k * d * np.sin(theta_rad)[:, None] * np.arange(num_elements))
    return np.abs(np.dot(steering_vector, weights)) / num_elements

# Compute array factor over the range of angles
array_response = array_factor(theta_range)

# Plot the array's radiation pattern
plt.figure(figsize=(10, 6))
plt.plot(theta_range, array_response, label=f"Beam steered to {theta_target}°", color='blue')
plt.title("Beamforming Radiation Pattern")
plt.xlabel("Angle (degrees)")
plt.ylabel("Normalized Amplitude")
plt.grid(True)
plt.legend()
plt.show()
