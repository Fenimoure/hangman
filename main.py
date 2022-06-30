# Write your code here
from random import randint

print("H A N G M A N", '\n')
winCount = 0
loseCount = 0


def hangman():
    global winCount, loseCount
    words = 'python', 'java', 'swift', 'javascript' \
        # ,  'php', 'haskell', 'typescript', 'kotlin'
    word = words[randint(0, len(words) - 1)]
    wordSet = set(word)
    attempts = 8
    guessSet = set()
    falseSet = set()

    def print_word(f_word, f_set):
        for char in f_word:
            if char in f_set:
                print(char, end='')
            else:
                print('-', end='')
        print()

    while (attempts):
        while True:
            print_word(word, guessSet)
            guessChar = str(input("Input a letter: "))
            if len(guessChar) != 1:
                print("Please, input a single letter.")
                print()
            elif not (guessChar.isascii() and guessChar.islower()) or guessChar.isnumeric() or guessChar.isspace():
                print("Please, enter a lowercase letter from the English alphabet.")
                print()
            else:
                break
        if guessChar in wordSet and guessChar not in guessSet:
            guessSet.add(guessChar)
        elif guessChar not in word and guessChar not in falseSet:
            print("That letter doesn't appear in the word.")
            falseSet.add(guessChar)
            attempts -= 1
        elif guessChar in falseSet or guessChar in guessSet:
            print("You've already guessed this letter.")
        if guessSet == wordSet:
            print("You guessed the word ", word, "!", sep='')
            print("You survived!")
            winCount += 1
            break
        print()
    if guessSet != wordSet:
        print("You lost!")
        loseCount += 1


def results():
    global winCount, loseCount
    print("You won:", winCount, "times")
    print("You lost:", loseCount, "times")



while True:
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    cmnd = str(input())
    if cmnd == "play":
        hangman()
    elif cmnd == "results":
        results()
    elif cmnd == "exit":
        break
