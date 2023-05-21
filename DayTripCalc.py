

#(5 points): As a developer, I want to make at least three commits with descriptive messages 
#(5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 

location_list = ["Morocco", "France", "Mexico"]
restaurants_list = ["Amigos", "Fattoush", "Laila's Bistro"]
transportation_list = ["Train", "Taxi", "Bus"]
entertainment_list = ["Comedy Show", "Play", "Guided Tour"]
generated_choices = []

#(5 points): As a user, I want a destination to be randomly selected for my day trip. 
#(5 points): As a user, I want a restaurant to be randomly selected for my day trip
#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.

import random


#def random_trip(location_list, restaurants_list, transportation_list, entertainment_list):
 #  Trip = random_trip(location_list, restaurants_list, transportation_list, entertainment_list)
 #  print(Trip)

#random_trip(location_list, restaurants_list, transportation_list, entertainment_list)

#Why didn't this print anything?



def random_trip_genorator(location_list, restaurants_list, transportation_list, entertainment_list):
    Location = random.choice(location_list)
    Eatery = random.choice(restaurants_list)
    Mode_of_transport = random.choice(transportation_list)
    Entertainment = random.choice(entertainment_list)
 
    
generated_choices.append(Location)
generated_choices.append(Eatery)
generated_choices.append(Mode_of_transport)
generated_choices.append(Entertainment)



random_trip_genorator(location_list, restaurants_list, transportation_list, entertainment_list)



#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

print(generated_choices)

Question1 = input("Are you happy with the place? Please enter yes or no. ")
if Question1 == yes
    print("Bon voyage!")
else: 

def Satisfaction():
    Question = input("Are you happy with the selections for your trip? Please enter yes or no. ")
    while Question == yes or Yes or YES:
        print("Enjoy your trip")
        break
    while Question == no or No or No
        Change()
        Ask_again()


def Change():
    What_to_change = input("What would you like to change: place, food, travel, or activity? ")
    if What_to_change == food:
        print(Eatery)
    if What_to_change == place:
        print(Location)
    if What_to_change == activity:
        print(Entertainment)
    if What_to_change == travel:
        print(Mode_of_transport)


def Ask_again():
    Happy_now = input("Is this better? Please enter yes or no. ")
    while Happy_now == yes or Yes or YES:
        print("Enjoy your trip")
        break

        

Satisfaction()

Change()

Ask_again()

#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
#(10  points): As a user, I want to display my completed trip in the console
#(5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!
#Ideally, all of your code will be inside of functions. The Lists that store your trip options can be at the top of their file outside of functions, but everything else should be inside functions!



