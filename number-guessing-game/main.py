import random

def guess_the_number():
    print("Welcome to the Number Guessing Game")
    print("I'm thinking of a number between 1 and 100.")

    computer_guess = random.randint(1,100)
    attempts = 0

    while True:
        try:
            player_guess = int(input("Take a guess: "))
            attempts += 1

            if player_guess < computer_guess:
                print("Too Low!! Try again...")
            elif player_guess > computer_guess:
                print("Too High !! Try Again...")
            else:
                print(f"Congratulation!! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please Enter a valid Integer...")


if __name__ == "__main__":
    guess_the_number()
