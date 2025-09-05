import matplotlib.pyplot as plt
from collections import Counter

# Sample dataset (e.g., log categories, error types, or survey responses)
data = ['Pass', 'Fail', 'Pass', 'Error', 'Pass', 'Fail', 'Error', 'Pass', 'Error', 'Fail']

# Count frequency of each category
frequency = Counter(data)

# Separate keys and values
labels = list(frequency.keys())
counts = list(frequency.values())

# Plotting
plt.figure(figsize=(7, 4))
bars = plt.bar(labels, counts, color='mediumseagreen', edgecolor='black')

# Add frequency labels above bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.2, str(height), ha='center', va='bottom')

# Titles and labels
plt.title('Frequency of Test Outcomes')
plt.xlabel('Outcome')
plt.ylabel('Count')

plt.tight_layout()
plt.show()


