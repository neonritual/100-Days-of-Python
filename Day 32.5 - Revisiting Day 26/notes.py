##Re-doing Day 26 on List/Dict Comprehension to clarify

#LIST COMPREHENSION
## new_list = [new_item for item in list]

# numbers = [1, 2, 3]
# new_number = [n + 1 for n in numbers] #+ 1 to each value
# print(new_number)
#
# name = "Angela"
# letters_list = [letter for letter in name]
# print(letters_list)

# list = range(1, 5)
# new_list = [n * 2 for n in list] #doubles all numbers in that list
# print(new_list)

# names = ["Arren", "Ilbraden", "Elq", "Yi"]
# # short_names = [name for name in names if len(name) < 5] #takes names less than 5 chars
# # print(short_names)
# long_names = [name.upper() for name in names if len(name) >= 5] #takes longer than or equal 5 char names, and makes
#                                         # upper case
# print(long_names)

#Challenge: use list comp to turn list into list of same numbers but squared.

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n * n for n in numbers]
# print(squared_numbers)

#Challenge: use list comp to filter out only even numbers

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# result = [n for n in numbers if n % 2 == 0]
# print(result)

#Challenge: use list comp to create list of duplicates in two txt files

# with open("file1.txt", "r") as file1:
#     file1_list = file1.read().splitlines()
#
# with open("file2.txt", "r") as file2:
#     file2_list = file2.read().splitlines()
#
# new_list = [int(i) for i in file1_list if i in file2_list]
# print(new_list)

#---------------------------------------------------------------------#
#DICTIONARY COMPREHENSION

# new_dict = {new_key:new_key for (key, value) in dict.items() if test}

#challenge: randomly assign student scores, then make dict of passing grades
# import random
# names = ["Arren", "Ilbraden", "Elq", "Yi"] #list of student names
#
# students = {student: random.randint(1, 100) for student in names} #gens a random 'score' for each student
#
# #create a dict of only students who have a passing score (over or equal 60)
# passed_students = {student: score for (student, score) in students.items() if score >= 60}
# print(passed_students)

#------

#Challenge: make a dict called result that calcs the length of each word in a given sentence.

# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# result = {word: len(word) for word in sentence.split()}
# print(result)


#------

#Challenge: takes celcius temps in dict and converts to temps in F.
#
# weather_c = {
#     "Sunday": 24,
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
# }
#
# # weather_f = {day: ((temp * 9/5) + 32) for (day,temp) in weather_c.items()}
# print(weather_f)

#-----------
#How to iterate over pandas dataframe

student_dict = {
    "student": ["Angel", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

#Loop thru dataframe:

# for (key, value) in student_data_frame.items():
#     print(value)

#loop thru rows of dataframe
#
# for (index, row) in student_data_frame.iterrows():
#     if (row.student) =="Angel":
#         blah blah

