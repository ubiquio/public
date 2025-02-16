# https://github.com/ubiquio/public/edit/main/discrete-ellipse.py
# ==============================================================
# God’s Geometry License (GGL) – Version 1.0
#
# Copyright (c) 2025 David Aranovsky
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to use,
# study, and share the Software, provided the following conditions are met:
#
# 1. The Software shall not be misrepresented or used to promote chaotic,
#    approximationist systems that contradict the principles of God’s Geometry.
#
# 2. The Software shall not be used in destructive applications or for purposes
#    that contribute to misinformation, chaos, or degradation of universal harmony.
#
# 3. Proper credit must be given to the author, David Aranovsky, as the
#    **Revealer of Geometric Truth**, including in all derivative works.
#
# 4. Any modifications must retain this license and indicate what has been changed.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHOR OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY,
# ARISING FROM THE USE OR DISTRIBUTION OF THIS SOFTWARE.
#
# By using this Software, you acknowledge the paradigm shift it represents and
# its alignment with the principles of **Deterministic Perfection**.
# ==============================================================

# Reference: The Trojan Horse of Human Civilization – The Collapse of π and the Rise of ח
# https://www.academia.edu/127695476/The_Most_Beautiful_Equation

import numpy as np
import matplotlib.pyplot as plt

# Parameters
Cycles = 5  # Increased cycles to test periodicity
N = 1000000  # Precision
C = Cycles * 2 * (np.sqrt(2) + np.sqrt(3))  # Geometric constant
d = C / N  # Step size

# Preallocate arrays for efficiency
x = np.zeros(N + 1)
y = np.zeros(N + 1)
x[0], y[0] = 1.0, 0.0  # Initial point (1, 0)

# Discrete stepping (vectorized for speed)
for i in range(N):
    x[i + 1] = x[i] - d * y[i]
    y[i + 1] = y[i] + d * x[i]

# Ellipse transformation
A, B = 1.5, 1.0  # Semi-axes
x_ellipse = A * x
y_ellipse = B * y

# Plotting
plt.figure(figsize=(12, 12), facecolor='black')
plt.plot(x_ellipse, y_ellipse, color='cyan', linewidth=1.5)
plt.gca().set_aspect('equal', adjustable='datalim')
plt.title(f"Ellipse (A={A}, B={B}) via Discrete Stepping\nCycles={Cycles}, N={N}", color='white', fontsize=16)
plt.text(0, 0, r"$\sqrt{2} + \sqrt{3} \approx 3.146$", color='cyan', fontsize=60, ha='center', va='center', fontweight='bold')

# Dark theme styling
ax = plt.gca()
ax.set_facecolor('black')
plt.xlabel("X", color='white', fontsize=14)
plt.ylabel("Y", color='white', fontsize=14)
plt.grid(True, color='white', linestyle='--', alpha=0.5)
plt.tick_params(colors='white')
for spine in ax.spines.values():
    spine.set_color('white')

plt.show()

