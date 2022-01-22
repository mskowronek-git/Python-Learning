        # Dictionaries and nesting # "Bug" = key and "An error in..." = value
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
}

    # Retrieving items from dictionary
# print(programming_dictionary["Bug"])

    # Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)

    # Create an empty dictionary
empty_dictionary = {}

    # Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

    # Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."

    # Loop through a dictionary
# for key in programming_dictionary:
#     print(thing)
#     print(programming_dictionary[key])
    

    # Grading program
# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }

# student_grades = {}

# for student in student_scores:
#     score = student_scores[student]
#     if score >= 91:
#         student_grades[student] = "Outstanding"
#     elif score >= 81:
#         student_grades[student] = "Exceeds Expectations"
#     elif score >= 71:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print(student_grades)


    # nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

    # Nesting a List in a Dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

    # Nesting Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany":{"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 32}
}

# and

# cities_visited = {
#     "France": travel_log["France"]
# }

    # Nesting Dictionary in a List
# travel_log = [
#     {
#     "country": "France",
#     "cities_visited": ["Paris", "Lille", "Dijon"], 
#     "total_visits": 12
#     },
#     {
#     "country": "Germany",
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
#     "total_visits": 32
#     }
# ]

# print(travel_log[1])

    # add new country

# travel_log = [
#     {
#     "country": "France",
#     "cities_visited": ["Paris", "Lille", "Dijon"], 
#     "total_visits": 12
#     },
#     {
#     "country": "Germany",
#     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
#     "total_visits": 32
#     }
# ]

# def add_new_country(country, total_visits, cities_visited):
#     new_country = {}
#     new_country["country"] = country
#     new_country["cities_visited"] = cities_visited
#     new_country["total_visits"] = total_visits
#     travel_log.append(new_country)

# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)
import os

print("Welcome to the secret auction program.")


auctioners = []
redo = True

while redo:
    append_maschine = {}
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))

    append_maschine[name] = bid
    auctioners.append(append_maschine)

    more = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if more == "no":
        redo = False
    else:
        clear = lambda: os.system('cls')
        clear()

compare_bid = 0
winner_bid = 0
winner_name = ""

for element in auctioners:
    for key in element:
        compare_bid = element[key]
        if compare_bid > winner_bid:
            winner_bid = compare_bid
            winner_name = key
print(f"The winner is {winner_name} with a bid of ${winner_bid}.")
