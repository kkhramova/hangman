from hangman_illustration import stages
import random


def random_word():
    file = open("words.txt")
    words = file.readlines()
    word = random.choice(words).upper()
    word = word.strip("\n")
    return word


def game():
    print(f"Hi there! Let's play some Hangman!")
    word = random_word()
    word_in_progress = "_" * len(word)
    mistakes = 0
    wrong_letters = []
    correct_letters = []
    guessed = False

    while not guessed and mistakes < 7:
        guess = input("\nGuess a letter: ").upper()
        if guess == "" or not guess.isalpha():
            print("You must enter a letter")
        elif len(guess) > 1:
            print("You can't enter more then one letter at a time")
        elif guess in wrong_letters or guess in correct_letters:
            print("You've already tried this letter")
            print(f"You have {7 - mistakes} more tries left\n")
        elif guess not in word:
            print("\nWrong letter!")
            mistakes += 1
            print(f"You have {7 - mistakes} more tries left\n")
            wrong_letters.append(guess)
        else:
            print(f"\nAwesome! Letter {guess} is in this word!\n")
            correct_letters.append(guess)
            word_in_progress = list(word_in_progress)
            indexes = []
            for index, character in enumerate(word):
                if character == guess:
                    indexes.append(index)
            for index in indexes:
                word_in_progress[index] = guess
            word_in_progress = ''.join(word_in_progress)
            if "_" not in word_in_progress:
                guessed = True
        print(stages(mistakes))
        print('\n', word_in_progress)
        print("Wrong letters: ", ' '.join(wrong_letters))
    if guessed:
        print("\nGreat Job! You've won!")
    else:
        print("\nYou've lost!")
        print(f"The word was {word}")

    play_again = input(
        "\nWould you like to play again? Press 'Y' for yes, any other key for exit: ").upper()
    if play_again == "Y":
        game()
    else:
        print("\nThanks for playing!")
        exit()


game()
