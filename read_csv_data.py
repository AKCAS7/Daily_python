import csv
with open("weather_data.csv") as file:
    contents = csv.reader(file)
    for row in file:
        contents.append(row)
        
print(contents)
        


