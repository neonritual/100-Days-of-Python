# with open('weather_data.csv') as data_file:
#     data = weather_data.readlines()
# print(data)
#TODO:The above code gets the data in a list, but it is hard to read. Instead, Python has a built in
#way to deal with csv files;

# import csv
# temps = []
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#      if row[1] != "temp":
#         temps.append(int(row[1]))
# print(temps)

#TODO: this is better, but still hard to work with. but we can use the Pandas library to make it easier:

import pandas
#DataTypes in pandas: a Series is a part of the table, while a Dataframe is the whole table.

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# temp_list = data['temp'].to_list()
# average_temp = sum(temp_list) / len(temp_list)
# print(f"The average temp is: {average_temp}")
#
# #OR MORE SIMPLY! Pandas can do it already:
#
# print(f"The average temp is: {data['temp'].mean()}")
#
# #Finding the highest value in the list:
# print(data['temp'].max())

###Getting data in columns: also ane asy way. These are the same:
# print(data["condition"])
# print(data.condition)

###Getting data in a Row:
# print(data[data.day == "Monday"])

### Challenge: Pull the row of data with the highest temp (hint: we calc'd this before, it was 24)
# print(data[data.temp == 24])
# #OR if we hadn't already calculated it:
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])


#Pulling pieces of data from a row:
#Challenge: get the tmep from Monday and change from C to F:

# monday = data[data.day == "Monday"]
# print(monday.temp) #original C
# print((monday.temp * 9/5) + 32)

#Create a dataframe from scratch!

data_dict = {
    "students": ["Haru", "Haruto", "Haku"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv") #this creates a separate file




