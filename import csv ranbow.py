import csv

# Rainbow color data
rainbow_colors = [
    ['Color', 'Hex Code', 'Wavelength (nm)'],
    ['Red', '#FF0000', '620–750'],
    ['Orange', '#FFA500', '590–620'],
    ['Yellow', '#FFFF00', '570–590'],
    ['Green', '#008000', '495–570'],
    ['Blue', '#0000FF', '450–495'],
    ['Indigo', '#4B0082', '425–450'],
    ['Violet', '#EE82EE', '380–425']
]

# Write to CSV
with open('rainbow_colors.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rainbow_colors)

print("✅ Rainbow color data written to 'rainbow_colors.csv'")

import csv

# Read from CSV
with open('rainbow_colors.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)