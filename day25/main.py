# with open("day25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("day25/weather_data.csv","r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1])) 
#     print(temperatures)
   
import pandas

data = pandas.read_csv("day25/weather_data.csv")
# print(type(data))
# print(data)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# # print(temp_list)
# # total = 0
# # for temps in temp_list:
# #     total += temps
# # average = total / len(temp_list)
# # print(average)

# print(data["temp"].mean())
# print(data["temp"].max())
# #GetDataIncollumns
# print(data["condition"])
# print(data.condition)


#GerDataInRow
print(data[data.temp == data.temp.max()])
# cinvert celsius to fahrenheit
monday = data[data.day == "Monday"]
celsius = monday.temp[0]
print(celsius)
fahrenheit = (celsius * 1.8) + 32
print(fahrenheit)


# #create a dataframe from scratch

# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")


# squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# color_counts = squirrel_data["Primary Fur Color"].value_counts()
# print(color_counts)

# data = pandas.DataFrame(color_counts)
# print(data)
# data.to_csv("squirrel_data.csv")


# squirrel_dict = {
#          "Fur Color": ["Gray","Red","Black"],
#          "Count" : [color_counts.get("Gray",0), color_counts.get("Cinnamon",0), color_counts.get("Black",0)]
#      }

# new_data = pandas.DataFrame(squirrel_dict)
# new_data.to_csv("new_squirrel_data.csv")

