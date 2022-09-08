def directions():
    print("Turn left out of parking lot.")
    print("Drive to stoplight and turn left.")
    print("Drive 2 miles through Austintown")
    print("Home Depot is across the street from literally nothing lmao")
    print("Turn right into Home Depot")
    
number_of_people = int(input("How many people are asking for directions? "))

while number_of_people > 0:
    print(f"{number_of_people} - New Directions")
    directions()
    number_of_people = number_of_people - 1