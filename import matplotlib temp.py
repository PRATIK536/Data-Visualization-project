import matplotlib.pyplot as plt

# Sample temperature data (e.g., over a week)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
temperatures = [32.5, 33.0, 34.2, 35.1, 34.8, 33.5, 32.0]

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(days, temperatures, marker='o', linestyle='-', color='tomato', linewidth=2)

# Annotate each point with temperature
for i, temp in enumerate(temperatures):
    plt.text(i, temp + 0.3, f'{temp}°C', ha='center', va='bottom')

# Labels and title
plt.title('Weekly Temperature Trend')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.grid(True)

plt.tight_layout()
plt.show()
