# Welcome the players to the game and collect their names
def main():
    print("Welcome to Duelist")
    global player1
    player1 = input("Player 1, what is your name? ")
    print(f"Goodluck {player1}!\n")
    global player2
    player2 = input("Player 2, what is your name? ")
    print(f"Goodluck {player2}!\n")


    global player1_health 
    player1_health = 20
    global player2_health
    player2_health = 20

    move_choice()

# Asks both players what move they would like to do. Adds a large space between so player 2 can't cheat
def move_choice():
    print(f"{player1} you're up")
    while True:
        move_attempt = input(f"choose one of the following moves:\nstrike right\nstrike left\nblock right\nblock left\n\n").lower().strip()

        if move_attempt == "strike right":
            player1_move = "strike right"
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            break

        elif move_attempt == "strike left":
            player1_move = "strike left"
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            break

        elif move_attempt == "block right":
            player1_move = "block right"
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            break

        elif move_attempt == "block left":
            player1_move = "block left"
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            break

        else:
            print("Invalid choice")


    print(f"{player2} you're up")
    while True:
        move_attempt = input(f"\nchoose one of the following moves:\nstrike right\nstrike left\nblock right\nblock left\n\n").lower().strip()

        if move_attempt == "strike right":
            player2_move = "strike right"
            print()
            break

        elif move_attempt == "strike left":
            player2_move = "strike left"
            print()
            break

        elif move_attempt == "block right":
            player2_move = "block right"
            print()
            break

        elif move_attempt == "block left":
            player2_move = "block left"
            print()
            break

        else:
            print("Invalid choice")

    who_struck(player1_move, player2_move)

# Determines which player receives damage, based off their selected moves
def who_struck(player1_move, player2_move):
    if (player1_move == "strike right" and player2_move == "strike right") or (player1_move == "strike left" and player2_move == "strike left"):
        player1_health_change = 5
        player2_health_change = 5
        print("\nYou both strike eachother\n")

    elif (player1_move == "strike right" and player2_move == "block right") or (player1_move == "strike left" and player2_move == "block left"):
        player1_health_change = 0
        player2_health_change = 5
        print(f"\n{player1} strikes {player2}\n")

    elif (player2_move == "strike right" and player1_move == "block right") or (player2_move == "strike left" and player1_move == "block left"):
        player1_health_change = 5
        player2_health_change = 0
        print(f"\n{player2} strikes {player1}\n")

    elif (player1_move == "strike right" and player2_move == "block left") or (player1_move == "strike left" and player2_move == "block right"):
        player1_health_change = 10
        player2_health_change = 0
        print(f"\n{player2} blocks {player1}'s strike, then delivers a massive blow\n")

    elif (player2_move == "strike right" and player1_move == "block left") or (player2_move == "strike left" and player1_move == "block right"):
        player1_health_change = 0
        player2_health_change = 10
        print(f"\n{player1} blocks {player2}'s strike, then delivers a massive blow\n")

    elif (player2_move == "strike right" and player1_move == "strike left") or (player2_move == "strike left" and player1_move == "strike right"):
        player1_health_change = 0
        player2_health_change = 0
        print(f"\nyour blades bounce off of one another\n")

    else:
        player1_health_change = 0
        player2_health_change = 0
        print("\nnothing happens...\n")

    player_health_status(player1_health_change, player2_health_change)

# Changes the total health of each player based off the damage they just sustained
def player_health_status(player1_health_change, player2_health_change):
    global player1_health
    player1_health = player1_health - player1_health_change
    global player2_health
    player2_health = player2_health - player2_health_change

    print(f"{player1} has {player1_health} health")
    print(f"{player2} has {player2_health} health\n")

    who_won(player1_health, player2_health)
    
# Determines if the game is over or if it should continue
def who_won(player1_health, player2_health):
    if player1_health <= 0 and player2_health <= 0:
        print("It's a draw!")
    
    elif player1_health <= 0:
        print(f"{player2} wins!")

    elif player2_health <= 0:
        print(f"{player1} wins!")

    else:
        move_choice()

main()