from random import randint
def generate_number():
    """Generate an integer number from 1 to 10"""
    return randint(1, 10)


print("----- Guess the Number -----")
print("Try to guess the number I'm thinking...")
print("TIP: It's a number between 1 and 10...")
correct_answer = generate_number()
guesses = 1
