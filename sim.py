import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
frequency = 28e9  # 28 GHz for 5G
wavelength = 3e8 / frequency  # wavelength (c = f * lambda)
element_spacing = wavelength / 2  # optimal spacing
num_elements = 8  # number of elements in the array

# Calculate steering vector for a given angle
def steering_vector(angle):
    angles = np.deg2rad(angle)
    phase_shifts = np.exp(-1j * 2 * np.pi * element_spacing / wavelength * np.arange(num_elements) * np.sin(angles))
    return phase_shifts

def beam_pattern(steering_angle, scan_angles):
    steering_vec = steering_vector(steering_angle)
    response = []
    for angle in scan_angles:
        scan_vec = steering_vector(angle)
        response.append(np.abs(np.dot(steering_vec.conj(), scan_vec)))
    return np.array(response)

# Visualize
scan_angles = np.linspace(-90, 90, 180)  # scanning from -90 to 90 degrees
steering_angle = 30  # target angle

response = beam_pattern(steering_angle, scan_angles)
plt.plot(scan_angles, 20 * np.log10(response / response.max()))
plt.xlabel("Angle (degrees)")
plt.ylabel("Normalized Power (dB)")
plt.title("Beamforming Pattern at 30 Degrees")
plt.show()

import matplotlib.animation as animation

user_angles = np.linspace(-30, 30, 100)  # simulate user moving from -30 to 30 degrees

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.set_xlim(-90, 90)
ax.set_ylim(-30, 0)
ax.set_xlabel("Angle (degrees)")
ax.set_ylabel("Normalized Power (dB)")
ax.set_title("Dynamic Beam Steering")

def init():
    line.set_data([], [])
    return line,

def animate(i):
    angle = user_angles[i]
    response = beam_pattern(angle, scan_angles)
    line.set_data(scan_angles, 20 * np.log10(response / response.max()))
    ax.set_title(f"Beamforming Pattern at {angle:.2f} Degrees")
    return line,

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(user_angles), interval=100, blit=True)
plt.show()

import plotly.graph_objects as go

def plot_3d_beam(steering_angle):
    scan_angles = np.linspace(-90, 90, 180)
    response = beam_pattern(steering_angle, scan_angles)
    theta = np.deg2rad(scan_angles)
    r = response / response.max()

    fig = go.Figure(data=[go.Scatterpolar(r=r, theta=scan_angles, mode='lines', line=dict(width=2))])
    fig.update_layout(title=f"3D Beam Pattern at {steering_angle} Degrees", polar=dict(radialaxis=dict(visible=True)))
    fig.show()

# Example plot
plot_3d_beam(30)

# 3D Simulation using Matplotlib
def plot_3d_beam_matplotlib(steering_angle):
    # Define scan angles and azimuth angles
    scan_angles = np.linspace(-90, 90, 180)  # Elevation angles
    azimuth_angles = np.linspace(0, 360, 360)  # Azimuth angles

    # Initialize response array
    elevation_grid, azimuth_grid = np.meshgrid(scan_angles, azimuth_angles)
    response = np.zeros_like(elevation_grid)

    # Calculate beam response for each azimuth and elevation angle
    for i, az in enumerate(azimuth_angles):
        for j, el in enumerate(scan_angles):
            response[i, j] = np.abs(
                np.dot(
                    steering_vector(steering_angle).conj(),
                    steering_vector(el)
                )
            )

    # Normalize the response
    response = response / response.max()

    # Convert polar to cartesian for 3D plotting
    r = response
    theta = np.deg2rad(azimuth_grid)  # Azimuth angle in radians
    phi = np.deg2rad(elevation_grid)  # Elevation angle in radians

    # Cartesian coordinates
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)

    # Create 3D plot
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis', edgecolor='k', alpha=0.7)

    # Add labels and title
    ax.set_title(f"3D Beam Pattern at {steering_angle} Degrees", fontsize=14)
    ax.set_xlabel("X-axis (normalized power)", fontsize=10)
    ax.set_ylabel("Y-axis (normalized power)", fontsize=10)
    ax.set_zlabel("Z-axis (normalized power)", fontsize=10)

    # Set limits and viewing angle for better visualization
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)
    ax.view_init(elev=20, azim=45)  # Elevation and azimuth angles for the view

    plt.show()

# Example usage
plot_3d_beam_matplotlib(30)
