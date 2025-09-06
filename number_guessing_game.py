#importing random module
import random


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

            
def number_guessing_game():
    print("Hello, welcome to number guessing game! \n please select your numbers")

    #inputs that the player choose
    while True:
        low_input = input("Enter the lowest number: ")
        if low_input.isdigit():      #here you must enter a number
            low = int(low_input)
            break
        else:
            print("Please enter a valid number.")

    while True:
        high_input = input("Enter the highest number: ")
        if high_input.isdigit():
            high = int(high_input)
            break
        else:
            print("Please enter a valid number.")

    #generating the new number
    number = random.randint(low, high)

    #generating the new number
    number = random.randint(low, high)

    #here is the number of the chances and counter
    counter = 0
    chances = 7

    #game loop
    while chances > 0:
        guess_input = input("Enter your guess: ")
        if  guess_input.isalpha():
            print("Invalid input. Please enter a number.") #you must enter a number
            continue
        guess = int(guess_input)
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
       
        if chances == 0:
            print(f"Sorry, you've used all your chances. The number was {number}.")
            play_again()


number_guessing_game() #calling the function