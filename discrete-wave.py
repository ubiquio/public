# Reference: The Trojan Horse of Human Civilization – The Collapse of π and the Rise of ח
# https://www.academia.edu/127582440/The_Trojan_Horse_of_Human_Civilization_The_Collapse_of_%CF%80_and_the_Rise_of_%D7%97

import numpy as np
import matplotlib.pyplot as plt

# Pure Deterministic Perfection
# Periodicity and Oscillation without trigonometric infinite series or chaotic approximations
# The Wave From Discrete Geometry Through Geometric Necessity
# No normalization, no approximations—just perfect stepping and zero residuals.


Cycles = 3
N = 100000  # Precision level
C = Cycles * 2 * (np.sqrt(2) + np.sqrt(3)) # Geometric constant for structural recurrence
d = C / N  # Step size derived from geometric necessity

# Initialize coordinates
x = [1]  # Starting point (1,0)
y = [0]

# Pure perpendicular stepping
for _ in range(N):
    tx, ty = x[-1], y[-1]
    x.append(tx + d *-ty)
    y.append(ty + d * tx)

# Plot the emergent wave
plt.figure(figsize=(12, 4), facecolor='black')
ax = plt.gca()
ax.set_facecolor('black')

plt.plot(np.linspace(0, 20, N + 1), y, color='cyan', linewidth=1.5)
plt.axhline(0, color='white', linewidth=0.5)
plt.grid(True, color='white')
plt.title("The Wave Through Geometric Necessity", color='white')
plt.xlabel("Distance", color='white')
plt.ylabel("Amplitude", color='white')

# Styling
plt.tick_params(colors='white')
for spine in ax.spines.values():
    spine.set_color('white')

plt.show()
