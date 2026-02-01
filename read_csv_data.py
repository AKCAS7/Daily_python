import csv
with open("weather_data.csv") as file:
    contents = []
    read = csv.reader(file)
    for row in read:
        contents.append(row)
        
print(contents)
        




