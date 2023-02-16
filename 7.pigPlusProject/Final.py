# import external libraries
import random

# initialize variables
last_roll = -1
user_input = ""

# after much trial and error repeating the program using a for loop,
# I discovered that an automatic roll count of 8 derived the smallest
# average turn count. The average turn count was asymptotic toward 10 turns.
AI_auto_rolls = 8
white_terminal_text = "\033[0;37m"
red_terminal_text = "\033[0;31m"
green_terminal_text = "\033[0;32m"

# initialize Player class
class Player:
    def __init__(self, name, text_color):
        self.name = name
        self.roll_count = 0
        self.turn_points = 0
        self.turn_count = 0
        self.total_points = 0
        self.text_color = text_color


# pick random player to start
turn = random.randint(1, 2)

# create AI and user instances of Player class
AI = Player("AI", red_terminal_text)
user = Player("User", green_terminal_text)
player = user

# switch player
def switch_turn():
    global turn
    if turn == 1:
        turn = 2
    else:
        turn = 1


# assign Player instances to player variable
def init_player():
    global player
    if turn == 1:
        player = user
    else:
        player = AI


def switch_player():
    switch_turn()
    init_player()


init_player()

# continue loop if total points for current player are less than 200
while player.total_points < 200:

    # print prompt for player in player text
    print(
        f"{player.text_color}If you quit after this turn, you'd have a total of {player.total_points+player.turn_points} points."
    )

    # print input prompt for User
    if player.name == "User":
        user_input = input(f"Input x to quit turn: {white_terminal_text}")

    # continue turn if AI algorithm advises or if user chooses
    if (AI.roll_count < AI_auto_rolls) and (user_input != "x"):

        # print prompt for AI
        if player.name == "AI":
            print("AI chooses to keep going")

        # generate two random numbers between 1 and 6 (inclusive)
        d1, d2 = random.randint(1, 6), random.randint(1, 6)

        # print die values in player text
        print(f"{player.text_color}{player.name} rolled a {d1} and a {d2}")

        # add die values together to generate roll value
        roll = d1 + d2

        # add roll value to turn points for current player
        player.turn_points += roll

        # if roll equals 7, reset turn points to 0 and switch user
        if roll == 7:
            print(
                f"{player.name} rolled a 7. {player.name} turn points have been reset to 0."
            )

            # update variables
            player.turn_count += 1
            player.turn_points = 0
            player.roll_count = 0
            last_roll = -1

            # print roll and turn points variables for current player
            print(
                f"{player.name} Roll: {roll}\n{player.name} Turn Points: {player.turn_points}\n"
            )

            # print turn count, turn points, and total points variables for current player
            print(f"{player.name} Turns: {player.turn_count}")
            print(f"{player.name} Turn Points: {player.turn_points}")
            print(f"{player.name} Total Points: {player.total_points}\n")

            # print turn count, turn points, and total variables for other player
            switch_player()
            print(
                f"{player.text_color}{player.name} Turns: {player.turn_count}\nTotal Points: {player.total_points}\n"
            )

            continue

        # if roll equals the last roll, double the turn points value
        elif last_roll == roll:
            player.turn_points *= 2
            print(
                f"{player.name} rolled the same number twice. {player.name} turn points have been doubled."
            )

        # last roll is updated
        last_roll = roll

        # AI will stop if it wins or if turn points is greater than or equal to 90
        if (AI.turn_points + AI.total_points) >= 200 or AI.turn_points >= 90:
            AI.roll_count = AI_auto_rolls

        # player roll count is incrimented
        player.roll_count += 1

        # print roll and turn points variables for current player
        print(
            f"{player.name} Roll: {roll}\n{player.name} Turn Points: {player.turn_points}\n"
        )
    else:

        # print AI prompt
        if player.name == "AI":
            print("AI stops this turn")

        # add turn points to total points for current player
        player.total_points += player.turn_points

        # print turn count, turn points, and total points variables for current player
        print(f"{player.text_color}{player.name} Turns: {player.turn_count}")
        print(f"{player.name} Turn Points: {player.turn_points}")
        print(f"{player.name} Total Points: {player.total_points}\n")

        # update variables
        player.turn_points = 0
        last_roll = -1
        player.turn_count += 1
        player.roll_count = 0
        user_input = ""

        # if the total points of user are greater than 150, AI will automatically do 9 rolls
        if user.total_points > 150:
            AI_auto_rolls = 9

        # switch player if the game isn't over
        if player.total_points < 200:
            switch_player()

            # print turn count, turn points, and total variables for other player
            print(
                f"{player.text_color}{player.name} Turns: {player.turn_count}\n{player.name} Total Points: {player.total_points}\n"
            )

# print turn count, turn points, and total variables for other player
switch_player()
print(
    f"{player.text_color}{player.name} Turns: {player.turn_count}\n{player.name} Total Points: {player.total_points}\n"
)

# switch back for victory message
switch_player()

# print victory message
print(
    f"{player.text_color}Congratulations! {player.name} won in {player.turn_count} turns with {player.total_points} points!{white_terminal_text}"
)
