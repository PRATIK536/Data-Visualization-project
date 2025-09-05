import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Parameters
num_molecules = 50
steps = 200
bounds = 10

# Initialize positions randomly within bounds
positions = np.random.uniform(-bounds, bounds, size=(num_molecules, 2))

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
scat = ax.scatter(positions[:, 0], positions[:, 1], c='dodgerblue', s=50)
ax.set_xlim(-bounds, bounds)
ax.set_ylim(-bounds, bounds)
ax.set_title('Molecular Motion Simulation')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Update function for animation
def update(frame):
    global positions
    # Random movement: small steps in x and y
    delta = np.random.normal(0, 0.3, size=(num_molecules, 2))
    positions += delta
    # Keep molecules within bounds
    positions = np.clip(positions, -bounds, bounds)
    scat.set_offsets(positions)
    return scat,

# Animate
ani = animation.FuncAnimation(fig, update, frames=steps, interval=100, blit=True)
plt.tight_layout()
plt.show() 