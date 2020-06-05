from random import randint
def generate_number():
    """Generate an integer number from 1 to 10"""
    return randint(1, 10)


print("----- Guess the Number -----")
print("Try to guess the number I'm thinking...")
print("TIP: It's a number between 1 and 10...")
correct_answer = generate_number()
guesses = 1

while guesses <= 10:
    user_input = int(input())
    if user_input < correct_answer and guesses != 10:
        print("Your guess is too low. Try again.")
    elif user_input > correct_answer and guesses != 10:
        print("Your guess is too high. Try again.")
    elif user_input == correct_answer:
        print(f"YOU GOT IT RIGHT WITH {guesses} ATTEMPTS!!!")
        break
    else:
        print(f"SORRY! THE GAME IS OVER. I WAS THINKING IN THE NUMBER {correct_answer}")            
    guesses += 1
    