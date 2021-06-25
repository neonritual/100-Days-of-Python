
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas as pd
nato_letters_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_letters = {row.letter: row.code for (index, row) in nato_letters_df.iterrows()}
# print(nato_letters)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = list(input("Type a word to translate!   ").upper())
print(user_input)

result = [nato_letters[letter] for [letter] in user_input]

# result = [code for (letter, code) in nato_letters.items() if letter in user_input] #this does NOT alphabetize
print(result)


