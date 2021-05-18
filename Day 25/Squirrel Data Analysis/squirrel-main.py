import pandas

#Challenge: Create a csv file of how many squirrels in each fur color: Black, Cinnamon, and Gray, using pandas.

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_items = data["Primary Fur Color"] #separating primary fur color column for ease.

gray_count = 0  #setting each fur color count to 0 to begin.
cinnamon_count = 0
black_count = 0

for index, value in color_items.items():  #looping through the list and adding each time a fur color is shown.
    if value == "Gray":
        gray_count += 1
    if value == "Black":
         black_count += 1
    if value == "Cinnamon":
         cinnamon_count += 1

#print to check
print(f"Cinnamon: {cinnamon_count}, Black: {black_count}, Gray: {gray_count}")

#Creating a new dict with the found data
data_dict = {
    "Fur Color": ["Black", "Gray", "Cinnamon"],
    "Count": [black_count, gray_count, cinnamon_count]
}
#Creating the new data...
# fresh_data = pandas.DataFrame(data_dict)
#... and adding it to a new csv file.
# fresh_data.to_csv("new_data.csv")


#####################
## Below is the teacher's solution to the same challenge. Since it's so different and cool
# I'm typing it along for study purposes. (aka to future me, you didn't make this.. hah.

# import pandas
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

#.. and the rest the same as myself.