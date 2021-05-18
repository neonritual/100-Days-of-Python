#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

number_of_names = int(len(names))

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_text = letter_file.readlines()

name_number = 0

for _ in range(number_of_names):
    fixed_letter = []
    for old_name in letter_text:
        new_name = old_name.replace("[name]", names[name_number])
        fixed_letter.append(new_name)

    new_letter = ''.join(fixed_letter)

    with open(f"./Output/ReadyToSend/letter{name_number}.txt", "w") as create_letter:
        create_letter.write(str(new_letter))

    name_number += 1


