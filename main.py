import time
from random import choice
from os import system, name
from ufo import x as image


def clear():
    """function for clear screen """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def random_word():
    # opening nouns.txt file for processing
    with open('nouns.txt', 'r') as read_nouns:
        random_word = choice(read_nouns.readlines()).strip()
    return [random_word.upper(), len(random_word)]


def handle_image(index):
    return image[index]


def print_menu(ind, length):
    print('\nUFO: The Game')
    print('Instructions: save us from alien abduction by guessing letters in the codeword.\n')
    print(handle_image(ind))
    print(f'Incorrect Guesses:\n{None}')
    codeword = " ".join(['_']*length)
    print(f'\nCodeword:\n{codeword}')


def display_codeword(current_remaining, word, length, letter=""):
    for ind in range(length):
        if letter == word[ind]:
            current_remaining[ind] = letter
    return " ".join(current_remaining)


def handle_game():
    chosen_word, length = random_word()
    remaining_letters = len(set(chosen_word))
    guessed = set()
    incorrect_guess = []
    current_remaining = ['_']*length
    print_menu(len(incorrect_guess), length)

    while len(incorrect_guess) < 6:
        user_guessed = get_input(guessed)
        valid_input = check_input(user_guessed, chosen_word)

        if valid_input:
            remaining_letters -= 1
            if remaining_letters < 1:
                print("\nCorrect! You saved the person and earned a medal of honor!")
                print(f"The codeword is: {chosen_word}.")
                break
            else:
                handle_success(current_remaining, user_guessed, incorrect_guess, chosen_word, length)
        else:
            incorrect_guess.append(user_guessed)
            if len(incorrect_guess) == 6:
                # handle_failure(current_remaining, user_guessed, incorrect_guess, chosen_word, length)
                print(handle_image(len(incorrect_guess)))
                print("\nSorry you lost. Better luck next time!")
                print(f"\nThe codeword is: {chosen_word}.")
            else:
                handle_failure(current_remaining, user_guessed, incorrect_guess, chosen_word, length)

    replay = input("\nWould you like to play again (Y/N)? ")
    if replay.upper() == 'Y':
        handle_game()
    else:
        print('\nGoodbye!')
        time.sleep(1)
        clear()


def handle_success(current_remaining, user_guessed, incorrect_guess, word, length):
    print("\nCorrect! You're closer to cracking the codeword.\n")
    print(handle_image(len(incorrect_guess)))
    print("\nIncorrect Guesses:")
    print(" ".join(incorrect_guess))
    print(f'\nCodeword:\n{display_codeword(current_remaining, word,length, user_guessed)}')


def handle_failure(current_remaining, user_guessed, incorrect_guess, word, length):
    print("\nIncorrect! The tractor beam pulls the person in further.\n")
    print(handle_image(len(incorrect_guess)))
    print("\nIncorrect Guesses:")
    print(" ".join(incorrect_guess))
    print(f'\nCodeword:\n{display_codeword(current_remaining, word,length, user_guessed)}')
    # Delighter
    with open('messages.txt', 'r') as encourangements:
        encouragement = choice(encourangements.readlines()).strip()
    print(f"\n{encouragement}")


def get_input(guessed):
    user_input = input("\nPlease enter your guess: ")
    while len(user_input) > 1 or not user_input.isalpha():
        print('\nI cannot understand your input. Please guess a single letter.\n')
        user_input = input('\nPlease enter your guess: ')
    while user_input in guessed:
        print('\nYou can only guess that letter once, please try again.')
        user_input = input("\nPlease enter your guess: ")
    guessed.add(user_input)
    return user_input.upper()


def check_input(user_guessed, chosen_word):
    if user_guessed in chosen_word:
        return True
    else:
        return False


if __name__ == "__main__":
    handle_game()
