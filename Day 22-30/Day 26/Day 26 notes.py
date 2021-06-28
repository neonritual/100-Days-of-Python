#####List Comprehension:
# a way of making lists from other lists
#until now, we used for loops to create new lists using another

#standard format:
# new_list = [new_item for item in list]

#Old way using a loop:
# numbers = [1, 2, 3]
# new_list = []
# for n in list:
#     add_1 = n + 1
#
# new_list.append(add_1)
# print(new_list)

##Using List Comprehension:

# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)

##Conditional List Comprehension:

# new_list = [new_item for item in list if test]
#Only performs the code if it passes the Test.

# event_names = ["Maru", "Takeru", "Luka", "Valerie", "Koyuki"]
# short_names = [name for name in event_names if len(name) <= 4]
# print(short_names)
#
# big_long_names = [name.upper() for name in event_names if len(name) > 4]
# print(big_long_names)

##DICTIONARY COMPREHENSION--------------

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()} #holds all items ina  dict and
# splits it into key and value, looping through them all
#you can also add test
#
# event_names = ["Maru", "Takeru", "Luka", "Valerie", "Koyuki"]
#
# #create a dict that gens a random score for each name/student.
# import random
#
# student_scores = {student:random.randint(1, 100) for student in event_names}
#
# #Create a dict of students who "passed", ie got a 60 or over.
#
# passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
# print(passed_students)


##ITERATE OVER A PANDAS DATAFRAME
#yu can loop through a dataframe a lot like a dictionary
import pandas
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)

#Loop through a DataFrame
#Pandas has a built in way to loop thru rows

for (index, row) in student_data_frame.iterrows():
    print(index)
    print(row.student)
