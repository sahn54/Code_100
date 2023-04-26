import pandas

data = pandas.read_csv(
    "Code_100/Day_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
squirrel_gray = len(data[data["Primary Fur Color"] == "Gray"])
squirrel_red = len(data[data["Primary Fur Color"] == "Cinnamon"])
squirrel_black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ['gray', 'red', 'black'],
    "Count": [squirrel_gray, squirrel_red, squirrel_black]
}
new_dict = pandas.DataFrame(data_dict)
new_dict.to_csv("Code_100/Day_25/squirrel_count.csv")
print(new_dict)
