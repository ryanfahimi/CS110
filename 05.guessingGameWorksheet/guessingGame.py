import random

x = random.randint(0, 100)

while True:
    y = int(input("Please input your guess: "))
    if y > x:
        print("the number is too large")
    elif y < x:
        print("the number is too small")
    else:
        print("you guessed the number!!")
        break
