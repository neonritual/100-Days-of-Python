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


