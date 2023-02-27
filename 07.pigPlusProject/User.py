#import external libraries
import random
#initialize variables
turn_points = 0
turn_count = 0
total_points = 0
last_roll = -1
#continue loop if total points are less than 200
while total_points < 200:
    #print input prompt for user
    print(f"If you quit after this turn, you'd have a total of {total_points+turn_points} points.")
    user_input = input("Press x to quit turn: ")
    #proceed with loop if user does not quit
    if user_input != "x":
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
            turn_count += 1
            print("Your turn points have been reset to 0.")
            print(f"Roll: {roll}\nTurn Points: {turn_points}\n")
            print(f"Turns: {turn_count}\nTurn Points: {turn_points}\nTotal Points: {total_points}\n")
            continue
        #if roll equals the last roll, double the turn points value
        elif last_roll == roll:
            turn_points *= 2
            print("Your turn points have been doubled.")
        #last roll is updated
        last_roll = roll
        #print roll and turn points variables
        print(f"Roll: {roll}\nTurn Points: {turn_points}\n")

    else:
        #add turn points to total points
        total_points += turn_points
        #incriment turn count
        turn_count += 1
        #print turn count, turn points, and total points variables
        print(f"Turns: {turn_count}\nTurn Points: {turn_points}\nTotal Points: {total_points}\n")
        #update turn points and last roll variables
        turn_points = 0
        last_roll = -1

#print victory message
print(f"Congratulations! You won in {turn_count} turns with {total_points} points!")