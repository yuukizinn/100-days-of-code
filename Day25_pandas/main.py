
import os
os.chdir("/Users/yuuki/Documents/workspace/100_Days_of_Code/Day25_")

# with open("weather_data.csv") as w_data:
# 	data = w_data.readlines()
# 	print(data)

import csv
# with open("weather_data.csv") as w_data:
# 	data = csv.reader(w_data)
# 	tempratures = []
# 	for row in data:
# 		if row[1] != "temp":
# 			tempratures.append(int(row[1]))
# 	print(tempratures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data)
# temp_list = data["temp"].to_list()
# mean = statistics.mean(temp_list)
# print(data["temp"].mean())
# print(data.temp.max())
# print(data.query(f'temp == {data.temp.max()}'))
# monday =  data[data.day == "Monday"]
# print((monday.temp * 1.8) + 32)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(data[data["Primary Fur Color"] == "Gray"])
# print(data[data["Primary Fur Color"] == "Cinnamon"])
# print(data[data["Primary Fur Color"] == "Black"])
# print(data.columns)
fur_colors_data = data["Primary Fur Color"].to_list()

gray = fur_colors_data.count("Gray")
red = fur_colors_data.count("Cinnamon")
black = fur_colors_data.count("Black")

fur_colors_list = [
	["gray", gray],
	["red", red],
	["black", black]
	]
data_dict = {
	"Fur Color": [],
	"Counr": []
}
df = pandas.DataFrame(fur_colors_list, columns=("Fur_Color", "Count"))
df.to_csv("new_data")
