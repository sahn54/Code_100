# with open("Code_100/Day_25/weather_data.csv") as weather_file:
#     data = weather_file.readlines()

#     print(data)

# import csv

# with open("Code_100/Day_25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# pandas libraries
import pandas

data = pandas.read_csv("Code_100/Day_25/weather_data.csv")
print(type(data))  # DataFrame - .to_dict()
# print(data["temp"]) # Series 0 to_list()

# data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

# one way to find the average
# average = sum(temp_list) / int(len(temp_list))
# print(f"{average:.2f}")

# better way to find the average
average = data["temp"].mean()
print(average)

max_temp = data["temp"].max()
print(max_temp)

# Get Data in Columns
print(data["condition"])
# or
print(data.condition)

# Get Data in rows
print(data[data.day == "Monday"])

# Get Data which had the highest temperature
print(data[data.temp == data["temp"].max()])

# Get the condition for monday
monday = data[data.day == "Monday"]
print(monday.condition)

# Get the temperature for monday and convert it into Fahrenheit
# (0°C × 9/5) + 32 = 32°F
temp_c_m = monday.temp
temp_f_m = int(temp_c_m) * (9/5) + 32
print(temp_f_m)

# Create a dataframe from scratch
data_dict = {
    "student": ["Amy", "James", "Sung"],
    "scores": [76, 56, 65]
}
new_data = pandas.DataFrame(data_dict)
data.to_csv("Code_100/Day_25/example_data.csv")
print(new_data)
