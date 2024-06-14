# Jada Jones
# Thursday, June 13, 2024
# Hangman Game


# Import random
import random

# Category to Pick From and list from each category
categories = {
    'Foods': ['apple', 'cheese', 'chicken', 'shrimp', 'sandwich', 'sushi', 'pizza'],
    'Animals': ['snake', 'monkey', 'rhino', 'shark', 'flamingo', 'giraffe', 'zebra'],
    'States': ['oregon', 'idaho', 'florida', 'california', 'hawaii', 'south carolina', 'minnesota'],
    'Sports': ['basketball', 'soccer', 'football', 'tennis', 'swimming', 'gymnastics', 'baseball'],
    'Countries': ['russia', 'brazil', 'canada', 'iceland', 'vietnam', 'ireland', 'japan']
}


def assign_category():
    return random.choice(list(categories.keys()))


# function that selects random word from word list
def rand_word(category):
    return random.choice(categories[category])


# Game functions
def game_functions():
    category = assign_category()
    word = rand_word(category)
    word_guessed = ['_'] * len(word)
    letter_guessed = set()
    attempts = 6

    return category, word, word_guessed, letter_guessed, attempts


def game_state(category, word_guessed, attempts):
    print(f"Category: {category}")
    print('Word Guessed:', ' '.join(word_guessed))
    print('Attempts Remaining:' + str(attempts))


def guess_letter():
    letter = input('Guess a Letter: ')
    print('\n')
    if len(letter) == 1 and letter.isalpha():
        return letter
    else:
        print('Input invalid. Please enter a one alphabetical letter')


def update(word, word_guessed, letter_guessed, attempts):
    while True:
        letter = guess_letter()
        if letter in letter_guessed:
            print('Letter already guessed!')
        elif letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    word_guessed[i] = letter
        else:
            attempts -= 1

        letter_guessed.add(letter)
        return attempts


def win(word_guessed):
    return '_' not in word_guessed


def loss(attempts):
    return attempts == 0


def hangman_game():
    category, word, word_guessed, letter_guessed, attempts = game_functions()

    print("Welcome to Jada's Hangman!!\n")

    while True:
        game_state(category, word_guessed, attempts)
        attempts = update(word, word_guessed, letter_guessed, attempts)

        if win(word_guessed):
            print('Congrats! You won!!' + 'The correct word was: ' + word)
            quit()
        elif loss(attempts):
            print('Sorry you lost! The correct word was: ' + word)
            quit()


print('\n')
hangman_game()