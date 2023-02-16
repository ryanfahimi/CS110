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
loop_counter = 0
misses_average = 0

# iterate through every phrase
for phrase in phrases:
    # reinitialize variables after every iteration
    mystery_phrase = ""
    missed_guesses = ""
    misses_count = 0
    # replace phrase with mystery phrase
    for ch in phrase:
        # change all letters to asterisks
        if ("a" <= ch <= "z") or ("A" <= ch <= "Z"):
            mystery_phrase += "*"

        # leave all punctuation and spaces alone
        else:
            mystery_phrase += ch

    # iterate through letters every letter
    for i in range(26):
        # end loop if the mystery phrase has been solved
        if mystery_phrase == phrase:
            break

        # print game information
        print(f"Missed guesses: {str(missed_guesses)}\nMisses: {misses_count}")
        print(mystery_phrase)

        # incriment the letters alphabetically
        guess = chr(ord("a") + i)

        # alter mystery phrase if guess is within it
        if guess in phrase.lower():
            counter = 0
            for ch in phrase:
                if ch.lower() == guess:
                    mystery_phrase = (
                        mystery_phrase[:counter] + ch + mystery_phrase[counter + 1 :]
                    )
                counter += 1

        # if guess is not in the phrase, add guess to missed guesses string and incriment misses count by 1
        else:
            print("Your guess was not in the phrase")
            if missed_guesses != "":
                missed_guesses += ", "
            missed_guesses += guess
            misses_count += 1

    # add misses count to misses average
    misses_average += misses_count

    # incriment loop count by 1
    loop_counter += 1

    # deliver victory message
    print("\nCongratulations! You won wheel of fortune!")
    print(f"Missed guesses: {str(missed_guesses)}\nMisses: {misses_count}")
    print(f"{mystery_phrase}\n")


# divide sum of misses by loop count and print
misses_average /= loop_counter
print(f"Average number of misses: {misses_average: .2f}")
