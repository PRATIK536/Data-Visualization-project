import csv

# 🔹 Step 1: Writing data to a CSV file
data = [
    ['AKDT', 'Max TemperatureF', 'Mean TemperatureF', 'Min TemperatureF',
'Max Dew PointF', 'MeanDew PointF', 'Min DewpointF', 'Max Humidity',
' Mean Humidity', ' Min Humidity', ' Max Sea Level PressureIn',
' Mean Sea Level PressureIn', ' Min Sea Level PressureIn',
' Max VisibilityMiles', ' Mean VisibilityMiles', ' Min VisibilityMiles',
' Max Wind SpeedMPH', ' Mean Wind SpeedMPH', ' Max Gust SpeedMPH',
'PrecipitationIn', ' CloudCover', ' Events', ' WindDirDegrees']
]

with open('people.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("✅ CSV file 'people.csv' created and data written successfully.")

# 🔹 Step 2: Reading data from the CSV file
with open('people.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)