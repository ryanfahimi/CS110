# import external libraries
import random

# famous movie quotes for phrases
# initialize variables
phrases = [
    "It's alive! It's alive!",
    "My mama always said life was like a box of chocolates",
    "You're gonna need a bigger boat",
    "Here's looking at you, kid",
    "My precious",
    "Houston, we have a problem",
    "There's no crying in baseball!",
    "You can't handle the truth!",
    "A martini. Shaken, not stirred",
    "If you build it, he will come",
    "Keep your friends close, but your enemies closer",
    "I am your father",
    "Just keep swimming",
    "Hasta la vista, baby",
    "May the Force be with you",
    "There's no place like home",
    "I'm the king of the world!",
    "Elementary, my dear Watson",
    "I'll be back",
]
# select random phrase
phrase_index = random.randrange(len(phrases))
phrase = phrases[phrase_index]
missed_guesses = ""
misses_count = 0
mystery_phrase = ""

# replace phrase with mystery phrase
for ch in phrase:
    # change all letters to asterisks
    if ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
        mystery_phrase += "*"

    # leave all punctuation and spaces untouched
    else:
        mystery_phrase += ch

# continue loop while mystery phrase is unsolved
while mystery_phrase != phrase:
    # print game information
    print(f"Missed guesses: {missed_guesses}\nMisses: {misses_count}")
    print(mystery_phrase)

    # prompt user to input guess or attempt to solve
    guess = input(
        "\nPlease enter your guess or 'solve' to enter the entire phrase: "
    ).lower()

    # if user attempts to solve, ask the user to enter their solution
    if guess == "solve":
        solution = input("Please enter your solution: ").lower()
        # if the user's solution is correct, end the loop
        if solution == phrase.lower():
            mystery_phrase = phrase
        # if the user's solution is incorrect, increase the misses count by 4
        else:
            print("Unfortunately, your solution was incorrect")
            misses_count += 4

    # if the user has already guessed a letter, an error message appears
    elif (guess in mystery_phrase) or (guess in missed_guesses):
        print("\nERROR: Please enter a guess which you have not already entered\n")

    # if the guess is a letter, it is tested
    elif "a" <= guess <= "z":
        # if guess is in the phrase, the mystery phrase is edited
        if guess in phrase.lower():
            counter = 0
            for ch in phrase:
                if ch.lower() == guess:
                    mystery_phrase = (
                        mystery_phrase[:counter] + ch + mystery_phrase[counter + 1 :]
                    )
                counter += 1
        # if the guess is not in the phrase, the guess is added to the missed guesses string and the misses count is incrimented by 1
        else:
            print("Your guess was not in the phrase")
            if missed_guesses != "":
                missed_guesses += ", "
            missed_guesses += guess
            misses_count += 1

    # if the user does not enter a letter, an error message appears
    else:
        print("\nERROR: Please enter a letter\n")

# print victory message
print("\nCongratulations! You won wheel of fortune!")
print(f"Missed guesses: {missed_guesses}\nMisses: {misses_count}")
print(mystery_phrase)
