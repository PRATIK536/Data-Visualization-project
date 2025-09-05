import matplotlib.pyplot as plt

# Sample data
languages = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
popularity = [85, 75, 60, 70, 50]

# Create the bar chart
plt.figure(figsize=(8, 5))
bars = plt.bar(languages, popularity, color='skyblue', edgecolor='black')

# Add value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 2, yval, ha='center', va='bottom')

# Chart title and labels
plt.title('Programming Language Popularity in 2025')
plt.xlabel('Languages')
plt.ylabel('Popularity Score')

# Show the chart
plt.tight_layout()
plt.show()