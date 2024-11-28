import random
import sys
import os

# Adding the top level module directory for
current_dir = os.path.dirname(os.path.abspath(__file__))
relative_dir = "../"
package_path = os.path.join(current_dir, relative_dir)
sys.path.insert(0, package_path)


from utils.common import said_yes

# Jordela1's number guesser
# The goal of the game is to correctly the guess the number in the least number of guesses


def main():
    print("============Jordela1's Number Guesser============")
    print("Goal is to correctly guess the randomly generated number in the lowest amount of guesses\n")

    retry = bool(True)

    while retry:
        number_guesser()
        retry = said_yes("Go again")
        

def number_guesser():
    random_num = random.randint(1,100)

    guess = 0
    guess_counter = 0

    while guess is not random_num:
        guess = int(input('> Enter a number between 1 & 100 (inclusive): '))

        if guess > random_num:
            print(f"{guess} is too high")
            guess_counter += 1
        elif guess < random_num:
            print(f"{guess} is too low") 
            guess_counter += 1
        else:
            break

    print(f"Correct! The number was {random_num} Total Guesses: {guess_counter}")

if __name__ == "__main__":
    main()