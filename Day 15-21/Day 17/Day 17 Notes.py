######################
#### Day 17 Notes ####
######################

#TODO Custom CLASSES:
# You signal the creation of a new class by say 'class' and then the name of the new class.

# class User: #If we are creating a website, let's make a class for a typical User.
#     pass

# user1 = User() #making an object called user1 in that class.
# user1.id = "001" #adds an attribute to the object.
# user1.username = "valerie"
#
# #You can make any number of "users" like this..
#
# user2 = User()
# user2.id = "002"
# user2.username = "Takeru"
#.. but it"s tedious and prone to errors and typos.

#TODO INITIALIZING: using a constructor, that wil say when an object is initialized (created),
# what happens to it.
#you do this with an __init__ function!!!

#EXAMPLE:
# class Car:
#     def __init__(self, seats):
#         self.seats = seats
# my_car = Car(5)  #when this is done, my_car.seats will equal 5.

#To return to users:
#
# class User:
#     def __init__(self, user_id, username):  # inside this init function, we initialize attributes for our objects.
#         self.id = user_id
#         #now you can pass the user ID as you create the object.
#         self.username = username
#         self.follows = 0 ##THis isnt passed through because a new user has no followers,
#         # so it is instead DEFINED as 0 upon user creation

# user_1 = User("001", "valerie")
#Now without typing them out, these ATTRIBUTES are already included.

#TODO CHANGING ATTRIBUTES: You can have methods within Classes that can change their attributes.
#For example, a racing car Class may have a Method inside it that allows for "Race Mode",
# where it removes seats from the car.
#       class Car:
#           def enter_race_mode():
#               self.seats = 2

#So to create a way for,when uses follows someone, their followers go up and that users following goes up.:
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user): #the parameter MUST be self, so it knows what is calling it.
          user.followers += 1 #adds 1 to user, or the person following
          self.following += 1 #adds one to self following

user1 = User("001", "valerie")
user2 = User("002", "takeru")

user1.follow(user2) #user1 follows user2
print(user1.followers) ##0
print(user1.following)##1
print(user2.followers) ##1
print(user2.following) ##0


