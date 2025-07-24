# https://github.com/ubiquio/public/edit/main/discrete-circle.py
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

# Reference: https://www.academia.edu/130126551/

import numpy as np
import matplotlib.pyplot as plt
import time

# The Perfect Circle From Discrete Geometry Through Geometric Necessity, without using Pi
# No circular references, no normalization, no approximations—just deterministic stepping

start_time = time.time()
N = 100000  # Precision / Convergence level
C = 2 * (np.sqrt(3) + np.sqrt(2))  # Geometric constant for closure
d = C / N  # Step size derived from geometric necessity

# Initialize coordinates
x = [1]  # Starting point (1,0)
y = [0]

# Pure perpendicular stepping
for _ in range(N):
    tx, ty = x[-1], y[-1]
    x.append(tx + d * -ty)
    y.append(ty + d * tx)

# Plot the emergent geometry
plt.figure(figsize=(8, 8), facecolor='black')
ax = plt.gca()
ax.set_facecolor('black')

# Plot the circle
plt.plot(x, y, color='cyan', linewidth=1.5)

# Add title and text inside the circle
plt.axhline(0, color='white', linewidth=0.5)
plt.axvline(0, color='white', linewidth=0.5)
plt.axis('equal')
plt.grid(True, color='white')
plt.title(f"The Circle Through Geometric Necessity", color='white', pad=20)

# Add the big cyan text inside the circle
plt.text(0, 0, r"$\sqrt{2} + \sqrt{3} \approx 3.146$", color='cyan', fontsize=42, ha='center', va='center', fontweight='bold')

# Styling
plt.tick_params(colors='white')
for spine in ax.spines.values():
    spine.set_color('white')

plt.show()

end_time = time.time()
execution_time = end_time - start_time
execution_time, d

print(f"Step size: {d:.6f} seconds")
print(f"Execution time: {execution_time:.6f} seconds")
