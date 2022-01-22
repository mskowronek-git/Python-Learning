    # Functions with inputs
# def greet(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print("Isn't the weather nice today?")

# greet("Patrycja") # parameter = greet and argument = "Patrycja"

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# greet_with("Patrycja", "London") # ("Patrycja", "London") = positional argument
# greet_with(location = "London",name = "Patrycja") # (location = "London",name = "Patrycja") = keyword arguments


# import math
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5

# def paint_calc(height, width, cover):
#     calc =  (height * width) / cover
#     print(f"You'll need {math.ceil(calc)} cans of paint.") # math.ceil round up e.g. 2,1 to 3

# paint_calc(height=test_h, width=test_w, cover = coverage)
    
    # prime number checker

# def prime_checker(number):
#     if number == 2 or number == 3 or number == 7  or number == 11:
#         print("It's a prime number.")
#     elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0 or number % 11 == 0:
#         print("It's not a prime number.")
#     else:
#         print("It's a prime number.")

# n = int(input("Check this number: "))
# prime_checker(number=n)

# or in better way

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It's a prime number.")
#     else:
#         print("It's not a prime number.")

# n = int(input("Check this number: "))
# prime_checker(number=n)


    # Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    def caesar(direction, text, shift):
        new_text = ""

        if direction == "decode":
                shift *= -1

        for letter in text:
            if letter in alphabet:
                position = alphabet.index(letter)
                num_shift = position + shift
                new_text += alphabet[num_shift]
            else:
                new_text += letter
        print(f"The {direction}d text is {new_text}.")
    

    caesar(direction, text, shift)

    newGame = input("Do you want to go again? 'yes' or 'no'? ")
    if newGame == "no":
        should_continue = False
        # far longer way
# def encrypt(text, shift):

#     new_text = ""

#     for letter in text:
#         position = alphabet.index(letter)

#         num_shift = position + shift
#         new_text += alphabet[num_shift]

#     print(f"The encoded text is {new_text}.")


# def decrypt(text, shift):

#     new_text = ""

#     for letter in text:
#         position = alphabet.index(letter)

#         num_shift = position - shift
#         new_text += alphabet[num_shift]

#     print(f"The decoded text is {new_text}.")
            

# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("You chose nonexistend function.")

