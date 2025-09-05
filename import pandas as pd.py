import pandas as pd
import matplotlib.pyplot as plt

# Sample data as a dictionary
data = {
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
    'Temperature': [32.5, 33.0, 34.2, 35.1, 34.8],
    'Humidity': [45, 50, 55, 60, 58]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display basic info
print("Data Summary:")
print(df.describe())

# Filter example: Days with temperature > 34
hot_days = df[df['Temperature'] > 34]
print("\nHot Days:")
print(hot_days)

# Plot temperature trend
plt.figure(figsize=(7, 4))
plt.plot(df['Day'], df['Temperature'], marker='o', color='tomato', label='Temperature')
plt.plot(df['Day'], df['Humidity'], marker='s', color='skyblue', label='Humidity')
plt.title('Temperature & Humidity Over Days')
plt.xlabel('Day')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
