player1 = [3, 5, 4, 4, 4, 7, 3, 4, 4]
player2 = [4, 5, 4, 3, 3, 6, 4, 5, 3]
player1wins = 0
player2wins = 0
for i in range(len(player1)):
    if player1[i] > player2[i]:
        player2wins += 1
    elif player1[i] < player2[i]:
        player1wins += 1

if player1wins > player2wins:
    print(f"Player 1 wins {player1wins}-{player2wins}")
elif player1wins < player2wins:
    print(f"Player 2 wins {player2wins}-{player1wins}")
else:
    print(f"Player 1 and Player 2 tie {player1wins}-{player2wins}")
