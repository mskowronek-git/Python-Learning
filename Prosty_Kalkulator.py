            # Functions with Outputs
# def my_function():
#     result = 3 * 2
#     return result

# def format_name(f_name, l_name):
#     return (f_name + " " + l_name).title()
#     # return is the end of the function

# print(format_name("michAł", "sKOWRONEK"))



# def format_name(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}" 

# print(format_name(input("Whats is your first name? "), input("What is your last name? ")))

    
# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True

#     else:
#         return False

# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     chosen_month = month_days[month - 1]
#     if is_leap(year): # == True:
#         return chosen_month
#     else:
#         if chosen_month == 28:
#             return chosen_month + 1
#         else:
#             return chosen_month
            
# year = int(input("Enter some year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

    # Docstrings = adding comments to defined functions
# def format_name(f_name, l_name):
#     """Take a first and last name and format it to 
#     return the title case version of the name."""
#     if f_name == "" or l_name == "":
#         return "You didn't provide valid inputs."
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"Result: {formated_f_name} {formated_l_name}" 

# print(format_name(input("Whats is your first name? "), input("What is your last name? ")))

    # Calculator
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number? "))
num2 = int(input("What's the second number? "))

for key in operations:
    print(key)

operator = input("What operation do you want to perform? ")

output = (operations[operator])(num1, num2)
print(f"{num1} {operator} {num2} = {output}")