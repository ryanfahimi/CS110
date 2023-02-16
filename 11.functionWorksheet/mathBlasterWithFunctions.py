import random


def generateNumbers(eq_length, addend_min, addend_max):
    addend_list = []
    equation_len = random.randint(2, eq_length)
    for _ in range(equation_len):
        addend = random.randrange(addend_min, addend_max)
        addend_list.append(addend)
    return addend_list


def generateEquation(addend_list):
    equation_str = ""
    for i, addend in enumerate(addend_list):
        if i != 0:
            equation_str += " + "
        equation_str += str(addend)
    return equation_str


def computeSum(addend_list):
    total = 0
    for addend in addend_list:
        total += addend
    print(f"Total: {total}")
    return total


def getCheckGuess(total):
    guess = 0
    while guess != total:
        guess = input("Please enter your guess for the sum: ")
        while not guess.isdigit():
            guess = input("Please enter an integer for your guess: ")
        guess = int(guess)
        if guess == total:
            print("Congratulations, you got it!")
        else:
            print("Better luck next time champ.")


def main():
    user_input = "y"
    while user_input == "y":
        addend_list = generateNumbers(eq_length=4, addend_min=1, addend_max=100)
        equation_str = generateEquation(addend_list)
        print(equation_str)
        total = computeSum(addend_list)
        getCheckGuess(total)
        user_input = input("Good job, do you want another equation(Y/N)?  ").lower()


main()
