# A simple Python program that asks for the user's name and age, then prints a message

def greet_user(name, age):
    # This function will greet the user and tell them how many years until they turn 100
    years_until_100 = 100 - age
    print(f"Hello {name}, you are {age} years old. You will turn 100 in {years_until_100} years!")

# Asking for user input
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

# Calling the function
greet_user(user_name, user_age)
