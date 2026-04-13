import random

def start_game():
    secret_number = random.randint(1, 10)
    print("--- Python Guessing Game ---")
    
    try:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess == secret_number:
            print("Winner! You got it.")
        else:
            print(f"Close, but no. The number was {secret_number}.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    start_game()
