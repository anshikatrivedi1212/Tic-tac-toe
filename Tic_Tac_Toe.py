# TIC-TAC-TOE GAME

play = "yes"

while play == "yes":

    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    print("=" * 30)
    print("       TIC-TAC-TOE")
    print("=" * 30)

    print("\n1. Two Players")
    print("2. Player vs Computer")

    mode = input("Enter your choice: ")

    if mode == "1" or mode == "2":

        game_over = "no"
        turn = 1

        while game_over == "no":

            print()
            print(board[0], "|", board[1], "|", board[2])
            print("--+---+--")
            print(board[3], "|", board[4], "|", board[5])
            print("--+---+--")
            print(board[6], "|", board[7], "|", board[8])

            # Player 1 Move
            if turn == 1:

                position = int(input("\nPlayer 1, choose a position (1-9): "))

                if position >= 1 and position <= 9:

                    if board[position - 1] == "X" or board[position - 1] == "O":
                        print("Position already taken!")
                    else:
                        board[position - 1] = "X"
                        turn = 2

                else:
                    print("Invalid position!")

            # Player 2 or Computer Move
            else:

                if mode == "1":

                    position = int(input("\nPlayer 2, choose a position (1-9): "))

                    if position >= 1 and position <= 9:

                        if board[position - 1] == "X" or board[position - 1] == "O":
                            print("Position already taken!")
                        else:
                            board[position - 1] = "O"
                            turn = 1

                    else:
                        print("Invalid position!")

                else:

                    for place in range(9):
                        if board[place] != "X" and board[place] != "O":
                            board[place] = "O"
                            break

                    print("Computer played!")
                    turn = 1

            # Winner Check
            winning = [(0,1,2), (3,4,5), (6,7,8),
                       (0,3,6), (1,4,7), (2,5,8),
                       (0,4,8), (2,4,6)]

            win = "no"

            for a, b, c in winning:
                if board[a] == board[b] and board[b] == board[c]:
                    if board[a] == "X" or board[a] == "O":
                        win = "yes"

                        if board[a] == "X":
                            print("\nPlayer 1 Wins!")
                        else:
                            if mode == "1":
                                print("\nPlayer 2 Wins!")
                            else:
                                print("\nComputer Wins!")

            # Draw Check
            full = True

            for place in board:
                if place != "X" and place != "O":
                    full = False

            if win == "yes":
                game_over = "yes"

            elif full == True:
                print("\nGame Draw!")
                game_over = "yes"

        print("\nFinal Board:")
        print(board[0], "|", board[1], "|", board[2])
        print("--+---+--")
        print(board[3], "|", board[4], "|", board[5])
        print("--+---+--")
        print(board[6], "|", board[7], "|", board[8])

    else:
        print("\nInvalid Choice!")

    play = input("\nDo you want to play again? (yes/no): ")

print("\nThank you for playing!")