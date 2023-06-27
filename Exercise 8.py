#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays 
#(using input),compare them, print out a message of congratulations to the 
#winner, and ask if the players want to start a new game)


option = input("Do you want to play? Yes/No: ")

while option == "Yes":
    player1 = input("Player 1: Rock, Paper, or Scissors? ")
    player2 = input("Player 2: Rock, Paper, or Scissors? ")

    if player1 == "Rock" and player2 == "Scissors":
        print("Player 1 wins!")
    elif player1 == "Paper" and player2 == "Rock":
        print("Player 1 wins!")
    elif player1 == "Scissors" and player2 == "Paper":
        print("Player 1 wins!")
    elif player2 == "Rock" and player1 == "Scissors":
        print("Player 2 wins!")
    elif player2 == "Paper" and player1 == "Rock":
        print("Player 2 wins!")
    elif player2 == "Scissors" and player1 == "Paper":
        print("Player 2 wins!")
    else:
        print("It is a draw!")
    option = input("Do you want to play again? Yes/No: ")