#import external libraries
import random
#initialize variables
total_points = 0
turns = 0
#continue loop if total points are less than 200
while total_points < 200:
    #generate two random numbers between 1 and 6 (inclusive)
    d1, d2 = random.randint(1,6),random.randint(1,6)
    #print die values
    print(f"You rolled a {d1} and a {d2}")
    #add die values together to generate roll value
    roll = d1 + d2
    #add roll value to total points
    total_points += roll
    #incriment turn count
    turns += 1
    #print roll and total points variables
    print(f"Roll: {roll}\nTotal Points: {total_points}\n")

#print victory message
print(f"Congratulations! You won in {turns} turns with {total_points} points! Your rolls had an average of {total_points/turns}.")
