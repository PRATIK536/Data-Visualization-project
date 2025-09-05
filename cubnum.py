import matplotlib.pyplot as plt
import numpy as np
x_small = np.arange(1, 6)
y_small = x_small ** 3
x_large = np.arange(1, 5001)
y_large = x_large ** 3
norm = plt.Normalize(y_large.min(), y_large.max())
colors = plt.cm.viridis(norm(y_large))
fig, axs = plt.subplots(2, 1, figsize=(12, 8))
axs[0].plot(x_small, y_small, marker='o', color='teal')
axs[0].set_title('First 5 Cubic Numbers')
axs[0].set_xlabel('Number')
axs[0].set_ylabel('Cube')
axs[0].grid(True)
axs[1].plot(x_large, y_large, color='darkorange')
axs[1].set_title('First 5000 Cubic Numbers')
axs[1].set_xlabel('Number')
axs[1].set_ylabel('Cube')
axs[1].grid(True)
plt.tight_layout()
plt.show()


