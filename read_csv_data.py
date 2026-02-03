'''
import csv
with open("weather_data.csv") as file:
    contents = []
    read = csv.reader(file)
    for row in read:
        contents.append(row)
        
print(contents)
'''       

#using pandas 

import pandas

contents = pandas.read("weather_data.csv")
print(contents)

temp_list = data["temp"].to_list()
print(temp_list)

# average of temperature

print(sum(temp_list)/len(temp_list))
    
#average using pandas 

print(data["temp"].mean())

#max of temperatures

print(data["temp"].max())

