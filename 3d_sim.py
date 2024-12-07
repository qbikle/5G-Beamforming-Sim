import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
num_elements = 8  # Number of antenna elements
d = 0.5  # Distance between elements (in wavelengths)
theta_target = 30  # Target beam direction in degrees (elevation)
phi_target = 60  # Target beam direction in degrees (azimuth)
wavelength = 1  # Wavelength of the signal
k = 2 * np.pi / wavelength  # Wave number

# Define spherical coordinates
theta = np.linspace(0, np.pi, 180)  # Elevation (0 to 180 degrees)
phi = np.linspace(0, 2 * np.pi, 360)  # Azimuth (0 to 360 degrees)
theta_grid, phi_grid = np.meshgrid(theta, phi)

# Convert spherical to Cartesian for 3D plotting
x = np.sin(theta_grid) * np.cos(phi_grid)
y = np.sin(theta_grid) * np.sin(phi_grid)
z = np.cos(theta_grid)

# Beamforming weights
steering_vector = k * d * (np.sin(np.radians(theta_target)) * np.cos(np.radians(phi_target)) * np.arange(num_elements))
weights = np.exp(1j * steering_vector)

# Compute array factor
def array_factor_3d(theta, phi):
    # Expand np.arange(num_elements) to broadcast properly
    element_indices = np.arange(num_elements).reshape(1, 1, -1)  # Shape (1, 1, num_elements)

    # Expand theta and phi to 3D
    theta = theta[:, :, np.newaxis]  # Shape (360, 180, 1)
    phi = phi[:, :, np.newaxis]  # Shape (360, 180, 1)

    # Compute steering matrix
    steering = np.exp(1j * k * d * (np.sin(theta) * np.cos(phi) * element_indices))
    return np.abs(np.sum(steering, axis=2)) / num_elements  # Sum over antenna elements

# Calculate radiation pattern
radiation_pattern = array_factor_3d(theta_grid, phi_grid)

# Normalize the radiation pattern
radiation_pattern = radiation_pattern / np.max(radiation_pattern)

# 3D Plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(
    x * radiation_pattern,
    y * radiation_pattern,
    z * radiation_pattern,
    rstride=5,
    cstride=5,
    cmap="viridis",
    alpha=0.9,
)

# Set labels with more context
ax.set_title("3D Visualization of 5G Beamforming Radiation Pattern", fontsize=14)
ax.set_xlabel("Horizontal Beam Direction (Azimuth)", fontsize=12)
ax.set_ylabel("Vertical Beam Direction (Elevation)", fontsize=12)
ax.set_zlabel("Normalized Signal Strength", fontsize=12)

# Improve grid visibility
ax.grid(True)

# Show the plot
plt.show()
