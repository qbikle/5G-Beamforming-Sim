
# 5G Beamforming Simulation

This project simulates beamforming patterns for a 5G antenna array, using Python and several libraries such as `numpy`, `matplotlib`, and `plotly`. The project consists of three primary simulation files that visualize beamforming effects in 2D and 3D, exploring different scenarios for 5G antenna arrays.

## Files Overview

### 1. `3d_sim.py`
This script simulates the 3D radiation pattern of a 5G beamforming array. The program computes the array factor based on the antenna's steering vectors and visualizes the radiation pattern in 3D using `matplotlib`.

- **Key features:**
  - Defines antenna array parameters (number of elements, element spacing, target direction).
  - Calculates the array factor in 3D.
  - Generates a 3D plot of the radiation pattern.

**How to Run:**
```bash
python 3d_sim.py
```

---

### 2. `sim.py`
This script explores beamforming patterns in both 2D and 3D, simulating dynamic beam steering for a 5G antenna array. It visualizes the beamforming response for different steering angles and allows the simulation of user movement for dynamic beamforming.

- **Key features:**
  - Computes the beamforming pattern for a given steering angle and scanning angle.
  - Visualizes the beam pattern in 2D (using `matplotlib`).
  - Simulates dynamic beam steering by animating the beam's response as a user moves.
  - 3D visualization of the beam pattern using `plotly`.

**How to Run:**
```bash
python sim.py
```

---

### 3. `ULA_2d.py`
This script calculates and plots the radiation pattern of a Uniform Linear Array (ULA) in 2D for a given target steering angle. It computes the array factor and visualizes the result over a range of angles.

- **Key features:**
  - Computes the array factor for a target angle.
  - Plots the radiation pattern in 2D.

**How to Run:**
```bash
python ULA_2d.py
```

---

## Dependencies

The following Python libraries are required to run the scripts:

- `numpy`
- `matplotlib`
- `plotly` (for 3D visualizations in `sim.py`)

You can install the required libraries using `pip`:

```bash
pip install numpy matplotlib plotly
```

## Usage

1. Run `3d_sim.py` for a 3D radiation pattern of a beamforming antenna array.
2. Run `sim.py` for a dynamic simulation that visualizes beamforming patterns in both 2D and 3D.
3. Run `ULA_2d.py` for a simple 2D radiation pattern of a Uniform Linear Array.

The project provides insight into the beamforming behavior of antenna arrays, which is a fundamental concept in 5G communications.

## Acknowledgement

We would like to express our sincere gratitude to our professor, Bhupendra Sir, for his invaluable guidance and support throughout this project. His expertise and insights have been instrumental in the successful completion of our 5G Beamforming Simulation. Thank you for your encouragement and for providing us with the knowledge and tools necessary to explore this fascinating area of study.