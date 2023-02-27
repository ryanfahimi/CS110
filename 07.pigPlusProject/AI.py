#import external libraries
import random

#initialize variables
turn_points = 0
turn = 0
total_points = 0
last_roll = -1
roll_count = 0
#after much trial and error repeating the program using a for loop,
#I discovered that an automatic roll count of 8 derived the smallest
#average turn count. The average turn count was asymptotic toward 10 turns.
auto_rolls = 8
#continue loop if total points are less than 200
while total_points < 200:
    #AI continues turn three times before stopping
    if roll_count < auto_rolls:
        #print prompt for AI
        print(f"If you quit after this turn, you'd have a total of {total_points+turn_points} points.")
        print('AI chooses to keep going')
        #generate two random numbers between 1 and 6 (inclusive)
        d1, d2 = random.randint(1,6),random.randint(1,6)
        #print die values
        print(f"You rolled a {d1} and a {d2}")
        #add die values together to generate roll value
        roll = d1 + d2
        #add roll value to turn points
        turn_points += roll
        #if roll equals 7, reset turn points to 0 and start another round
        if roll == 7:
            turn_points = 0
            last_roll = -1
            turn += 1
            roll_count = 0
            print("Your turn points have been reset to 0.")
            print(f"Points: {roll}\nTurn Points: {turn_points}\n")
            print(f"Turns: {turn}\nTurn Points: {turn_points}\nTotal Points: {total_points}\n")
            continue
        #if roll equals the last roll, double the turn points value
        elif last_roll == roll:
            turn_points *= 2
            print("Your turn points have been doubled.")
        #last roll is updated
        last_roll = roll
        #AI will stop if it wins or if turn points are greater than or equal to 90
        if (turn_points + total_points) >= 200 or turn_points >= 90:
            roll_count = auto_rolls
        #AI roll count is incrimented
        roll_count += 1
        #print roll and turn points variables
        print(f"Points: {roll}\nTurn Points: {turn_points}\n")
    else:
        #print prompt for AI
        print(f"If you quit after this turn, you'd have a total of {total_points+turn_points} points.")
        print('AI stops this turn')
        #add turn points to total points
        total_points += turn_points
        #incriment turn count
        turn += 1
        #print turn count, turn points, and total points variables
        print(f"Turns: {turn}\nTurn Points: {turn_points}\nTotal Points: {total_points}\n")
        #update turn points and last roll variables
        turn_points = 0
        last_roll = -1
        roll_count = 0

#print victory message
print(f"Congratulations! You won in {turn} turns with a score of {total_points}!")