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

for data in temp_list:
    


