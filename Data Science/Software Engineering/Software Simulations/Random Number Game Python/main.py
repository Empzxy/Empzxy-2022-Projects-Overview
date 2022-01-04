import random 

def Main():
    player1 = 0
    player1wins = 0
    player2 = 0
    player2wins = 0
    rounds = 1
    

    while rounds != 10:
        player1 = dice_roll()
        player2 = dice_roll()
        print("Player 1 Roll: " + str(player1))
        print("Player 2 Roll: " + str(player2))

        if player1 == player2:
            print("Draw!")
        elif player1 > player2:
            player1wins = player1wins + 1
            print("Player 1 Wins!")
        else: 
            player2wins = player2wins + 1
            print("Player 2 Wins!")

        rounds = rounds + 1 

def dice_roll():
    diceRoll = random.randint(1, 6)
    return diceRoll 
Main()

