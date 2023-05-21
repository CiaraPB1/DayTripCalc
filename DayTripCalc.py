import random


#(5 points): As a developer, I want to make at least three commits with descriptive messages 
#(5 points):  As a developer, I want to store my destinations, restaurants, mode of transportation, and entertainment in their own separate Lists. 

location_list = ["Morocco", "France", "Mexico"]
restaurants_list = ["Amigos", "Fattoush", "Laila's Bistro"]
transportation_list = ["Train", "Taxi", "Bus"]
entertainment_list = ["Comedy Show", "Play", "Guided Tour"]
generated_choices = []
completed_trip = []
#(5 points): As a user, I want a destination to be randomly selected for my day trip. 
#(5 points): As a user, I want a restaurant to be randomly selected for my day trip
#(5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 
#(5 points): As a user, I want a form of entertainment to be randomly selected for my day trip.



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

    return generated_choices

random_trip_genorator(location_list, restaurants_list, transportation_list, entertainment_list)



#(15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things.

def print_generated_choices():
    print(f"Location: {generated_choices[0]}, Restaurant: {generated_choices[1]}, Transporation: {generated_choices[2]}, Entertaminment {generated_choices[3]}.")

print_generated_choices()


# Question1 = input("Are you happy with the place? Please enter yes or no. ")


def Satisfaction():
    print_generated_choices()
    Question = input("Are you happy with the selections for your trip? Please enter yes or no. ")
    if Question.lower() == "yes":
        completed_trip.extend(generated_choices)
        print("Enjoy your trip")
    elif Question.lower() == "no":
        Change()
        Ask_again()
    else: 
        print("Invalid input. Please enter 'yes' or 'no'. ")
        Satisfaction()



def Change():
    print_generated_choices()
    What_to_change = input("What would you like to change: place, food, travel, or activity? ")
    if What_to_change.lower() == "food":

        generated_choices[1] = random.choice(restaurants_list)
        print("New Restaurant: ", generated_choices[1])
        
    elif What_to_change.lower() == "place":
        generated_choices[0] = random.choice(location_list)
        print("New Location: ", generated_choices[0])

    elif What_to_change.lower() == "activity":
        generated_choices[3] = random.choice(entertainment_list)
        print("New Activity: ", generated_choices[3])

    elif What_to_change.lower() == "travel":
        generated_choices[2] = random.choice(transportation_list)
        print("New Transport" ,generated_choices[2])

    else: 
        print("Please enter place, food, travel, or activity.")
        Change()



def Ask_again():
    print_generated_choices()
    Happy_now = input("Is this better? Please enter yes or no. ")
    if Happy_now.lower() == "yes":
        completed_trip.extend(generated_choices)
        Satisfaction()
    elif Happy_now.lower() == "no":
        Satisfaction()
    else:
        print("Invalid input. Please enter 'yes' or 'no'. ")
        Ask_again() 

def print_completed_trip():
    print("Completed trip: ")

    print(f"Your completed trip is: Location: {completed_trip[0]}, You will be eating at: {completed_trip[1]}, Your mode of transporation will be: {completed_trip[2]}, You will be enjoying a {completed_trip[3]}.")

Satisfaction()

print_completed_trip()      

#(10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections.
#(10  points): As a user, I want to display my completed trip in the console
#(5 points): Single Responsibility: As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing!
#Ideally, all of your code will be inside of functions. The Lists that store your trip options can be at the top of their file outside of functions, but everything else should be inside functions!



