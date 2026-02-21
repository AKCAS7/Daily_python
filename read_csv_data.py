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
'''
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
'''

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

# USING PANDAS

import pandas as pd

data = pd.read_csv("weather_data.csv")

'''
data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].mean())
print(data["temp"].max())

print(data["condition"])
'''
max_temp = data["temp"].max()
print(data[data.temp == max_temp])



