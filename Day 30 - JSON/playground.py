# # Catching Exceptions:
# #4 keywords: try, except, else, finally
#
# # try: something that might cause an exception, aka you're trying it out knowing it may fail
# # except: do this if there WAS an exception
# # else: Do this if there were NO exceptions, and it succeeds
# # finally: carry out no matter what happens; a bluff code; tidying up the end of code.
#
# #There is also one more:
# # raise : this allows you to raise your own exception
#
# # file = open("a_file.txt") #there is no a_file.txt, so this WILL error.
# # So let's try to Catch the Exception....
#
try:
    file = open("a_file.txt") #want to open the file, but there isnt one
    a_dictionary = {"key": "value"}
    print(a_dictionary["jdnbjkr"]) #this key does not exist in the dict.
except FileNotFoundError: #just "except" is too broad to be useful, instead you should specify the error type.
    # print("There was an error") #to debug
    file = open("a_file.txt", "w") #tries to open, but if there isnt one, it will create it
except KeyError as error_message: #this will ALSO catch the error message.
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content) #if everything passes, it will read this file and print it.
finally:
    # file.close() #lastly, this will close the file
    # print("File was closed.")
    raise KeyError("This is an error that I made up.") #this will make an error
#
#






# #Some errors to play with.......
# #FileNotFound
# # with open("a_file.txt") as file:
# #    file.read()
#
# # KeyError
# # a_dictionary = {"key": "value"}
# # value = a_dictionary["non_existent_key"]
#
# # IndexError
# # fruit_list = ["Apple", "Banana", "Pear"]
# # fruit = fruit_list[3]
#
# # TypeError
# # text = "abc"
# # print(text + 5)
