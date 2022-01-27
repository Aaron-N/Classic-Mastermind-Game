# Author:      Aaron Nesbit
# Description: This is an implementation of the game Mastermind

import random
import os


def display_game_board(secret_code, code_guess, key_pegs):
    """
    This method displays the game board
    """
    print("-----------------------------------------")
    print("               MASTERMIND                ")
    print("-----------------------------------------")

    print("     ", end="")
    for x in secret_code:
        print("\t" + x, end="")
    print()

    for i in reversed(range(len(code_guess))):
        print("-----------------------------------------")
        print(key_pegs[i][0], key_pegs[i][1], "|")
        print(key_pegs[i][2], key_pegs[i][3], end=" |")
        for x in code_guess[i]:
            print("\t" + x, end="")

        print()
    print("-----------------------------------------")
    print("-----------------------------------------")
    print("               How To Play               ")
    print("-----------------------------------------")
    print("Crack the secret code to win the game!")
    print("You have 8 chances to get it right.")
    print("Hints are provided after each guess,")
    print("a 'W' means you have a correct color in")
    print("the wrong place, and a 'B' means you")
    print("have a correct color in the right place.")
    print("But beware, hints are provided in random")
    print("order to make the game more difficult!")
    print("Enter your guess using the numbers below,")
    print("with a space in between each of them:")
    print("  1 - BLACK   2 - RED    3 - YELLOW")
    print("  4 - GREEN   5 - BLUE   6 - WHITE")
    print("Example: BLUE RED BLACK YELLOW -> 4 1 5 3")
    print("-----------------------------------------")


def screen_clear():
    """
    This method clear the screen during game play
    """
    os.system("clear")


if __name__ == '__main__':

    # Create a dictionary that maps colors to numbers
    colors_map = {1: "BLACK", 2: "RED", 3: "YELLOW", 4: "GREEN", 5: "BLUE", 6: "WHITE"}

    # Create a randomly selected secret code for the player to guess
    random_colors = []
    secret_code = []
    # Fill random_numbers with random integers between 1 and 6
    for i in range(4):
        random_colors.append(random.randint(1, 6))
    # Convert random_numbers to secret_code using the values in colors_map
    for j in range(4):
        secret_code.append(colors_map[random_colors[j]])

    # Total number of turns in the game is initialized
    total_turns = 8

    # The secret_code to be shown to the user is initialized
    show_secret_code = ['????', '????', '????', '????']

    # The codes guessed by the player each turn is initialized
    code_guess = [['-', '-', '-', '-'] for x in range(total_turns)]

    # The clues provided to the player each turn is initialized
    key_pegs = [['-', '-', '-', '-'] for x in range(total_turns)]

    screen_clear()

    # The current turn counter is initialized
    current_turn = 0

    # Game logic for a round of play repeats while the current turn is less than total turns
    while current_turn < total_turns:

        display_game_board(show_secret_code, code_guess, key_pegs)

        # Player guess is collected and input validated
        try:
            guess = list(map(int, input("What's your guess? => ").split()))
        except ValueError:
            screen_clear()
            print("!!!!! INVALID GUESS ---> TRY AGAIN !!!!!")
            continue

        # Check if the number of colors numbers are 4
        if len(guess) != 4:
            screen_clear()
            print("!!!!! INVALID GUESS ---> TRY AGAIN !!!!!")
            continue

        # Check if each number entered corresponds to a number
        flag = 0
        for x in guess:
            if x > 6 or x < 1:
                flag = 1

        if flag == 1:
            screen_clear()
            print("!!!!! INVALID GUESS ---> TRY AGAIN !!!!!")
            continue

        # Storing the current player guess
        for i in range(4):
            code_guess[current_turn][i] = colors_map[guess[i]]

        # Process to apply clues in response to the current player guess
        code_clues = [x for x in secret_code]
        # Initialize key peg position counter for clues
        position = 0

        # Key pegs for the clues for the player's current guess are generated
        for x in guess:
            if colors_map[x] in code_clues:
                if guess.index(x) == secret_code.index(colors_map[x]):
                    key_pegs[current_turn][position] = 'B'
                else:
                    key_pegs[current_turn][position] = 'W'
                position += 1
                code_clues.remove(colors_map[x])

        # Shuffle the key pegs so they are out of order before they are displayed
        random.shuffle(key_pegs[current_turn])

        # If the current guess is the secret code, the player wins and the game ends
        if code_guess[current_turn] == secret_code:
            screen_clear()
            display_game_board(secret_code, code_guess, key_pegs)
            print("*****************************************")
            print("*** YOU CRACKED THE CODE, YOU WIN!!!! ***")
            print("*****************************************")
            break

        # Update turn
        current_turn += 1
        screen_clear()

# If player is out of chances, the game ends
if current_turn == total_turns:
    screen_clear()
    display_game_board(secret_code, code_guess, key_pegs)
    print("*****************************************")
    print("** YOU RAN OUT OF CHANCES, YOU LOSE!!! **")
    print("*****************************************")
