# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass


import pandas
# with open('nato_phonetic_alphabet.csv') as file:
#     data = file.readlines()






#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     {new_key: new_value for (index, row) in df.iterrows()}
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
# #TODO 1. Create a dictionary in this format:
# # {"A": "Alfa", "B": "Bravo"}

dict_from_csv = pandas.read_csv('nato_phonetic_alphabet.csv', header=None, index_col=0, squeeze=True).to_dict()


# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#
user_input = list(input("Type something: ").upper())
print(user_input)
new_dict = {key: value for key, value in dict_from_csv.items() if key in user_input}
print(new_dict)
