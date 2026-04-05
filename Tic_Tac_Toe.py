import random
import time

# Board setup
board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}

WIN_CONDITIONS = [
    ['1', '2', '3'],  # Row 1
    ['4', '5', '6'],  # Row 2
    ['7', '8', '9'],  # Row 3
    ['1', '4', '7'],  # Col 1
    ['2', '5', '8'],  # Col 2
    ['3', '6', '9'],  # Col 3
    ['1', '5', '9'],  # Diagonal
    ['3', '5', '7'],  # Diagonal
]


def display_board():
    print("\n")
    print(f" {board['1']} | {board['2']} | {board['3']} ")
    print("---|---|---")
    print(f" {board['4']} | {board['5']} | {board['6']} ")
    print("---|---|---")
    print(f" {board['7']} | {board['8']} | {board['9']} ")
    print("\n")


def check_winner(symbol):
    for condition in WIN_CONDITIONS:
        if all(board[cell] == symbol for cell in condition):
            return True
    return False


def get_available_cells():
    return [cell for cell, value in board.items() if value == ' ']


def is_board_full():
    return len(get_available_cells()) == 0


def player_move():
    while True:
        move = input("Your move (1-9): ").strip()
        if move in board and board[move] == ' ':
            board[move] = 'X'
            break
        else:
            print("Invalid move! Cell is either taken or out of range. Try again.")


def computer_move():
    available = get_available_cells()
    move = random.choice(available)
    board[move] = 'O'
    print(f"Computer placed O at position {move}")
    time.sleep(1)


def main():
    print("=" * 30)
    print("      TIC TAC TOE")
    print("=" * 30)
    print("  You are X | Computer is O")
    print("  Board positions:")
    print("   1 | 2 | 3 ")
    print("  ---|---|---")
    print("   4 | 5 | 6 ")
    print("  ---|---|---")
    print("   7 | 8 | 9 ")
    print("=" * 30)

    while True:
        display_board()

        # Player turn
        player_move()
        display_board()

        if check_winner('X'):
            print("🎉 YOU WIN! Congratulations!")
            break

        if is_board_full():
            print("🤝 It's a TIE!")
            break

        # Computer turn
        print("Computer is thinking...")
        computer_move()

        if check_winner('O'):
            display_board()
            print("💻 COMPUTER WINS! Better luck next time.")
            break

        if is_board_full():
            display_board()
            print("🤝 It's a TIE!")
            break


if __name__ == "__main__":
    main()