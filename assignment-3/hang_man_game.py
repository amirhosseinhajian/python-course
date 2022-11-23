import random

def display_hangman(tries):
    stages = [  """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                   """,
                   """
                   --------
                   |      |
                   |      
                   |
                   |
                   |
                   -
                   """
    ]
    return stages[tries]

def fill_guessed_letter(word_completion, word, guess):
    word_as_list = list(word_completion)
    indices = [i for i, letter in enumerate(word) if letter == guess]
    for index in indices:
        word_as_list[index] = guess
    return "".join(word_as_list)

if __name__ == "__main__":
    words_bank = ["python", "javascript", "apple", "operator", "rabit", "algorithm", "brain"]
    word = random.choice(words_bank)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6
    while not guessed and tries > 0:
        print(display_hangman(tries))
        print(word_completion)
        guess = input("guess a word: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You have already entered this word.")
            elif guess not in word:
                print(guess, "isn't in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Excellent!")
                guessed_letters.append(guess)
                word_completion = fill_guessed_letter(word_completion, word, guess)
                if "_" not in word_completion:
                    guessed = True
        else:
            print("invalid input")

    print(display_hangman(tries))
    if guessed:
        print("congratulations! you got it!")
    else:
        print("oops! the man was kiled :( \nthe word was", word)