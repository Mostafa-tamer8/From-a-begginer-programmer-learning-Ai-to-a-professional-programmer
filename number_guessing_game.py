#importing random module
import random

def number_guessing_game():
    print("Hello, welcome to number guessing game! \n please select your numbers")

    #inputs that the player choose
    low = int(input("Enter the lowest number: "))
    high = int(input("Enter the highest number: "))

    #generating the new number
    number = random.randint(low, high)

    #here is the number of the chances and counter
    counter = 0
    chances = 7

    #game loop
    while chances > 0:
        guess = int(input("Enter your guess: "))
        counter += 1
        if guess < number:
            chances -= 1
            print(f"Your guess is too low, You have {chances} chances left.")
        elif guess > number:
            chances -= 1
            print(f"Your guess is too high, You have {chances} chances left.")
        elif guess == number:
            print(f"Congratulations! You guessed the number {number} in {counter} tries.")
            play_again()
        elif counter == 7:
            print(f"Sorry, you've used all your chances. The number was {number}.")
            play_again()
        else:
            print("Invalid input. Please enter a number.")




#play again
def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == "yes":
            number_guessing_game()
        elif choice == "no":
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


number_guessing_game() #calling the function