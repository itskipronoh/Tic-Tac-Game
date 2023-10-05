from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"
winner = None

app = Flask(__name__)
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Get user input for row and column
        while True:
            try:
                row = int(input("Enter row (0, 1, or 2): "))
                col = int(input("Enter column (0, 1, or 2): "))
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    break
                else:
                    print("Invalid input. Try again.")
            except ValueError:
                print("Invalid input. Try again.")

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"
        
 

@app.route('/')
def index():
    return render_template('index.html', board=board, current_player=current_player,winner=winner)


@app.route('/make_move', methods=['POST'])
def make_move():
    global board, current_player
    data = request.json
    row = data['row']
    col = data['col']

    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
        board[row][col] = current_player
        if check_win(board, current_player):
            winner = current_player
            return jsonify({'message': 'Move made successfully!', 'winner': winner})
        elif is_full(board):
            return jsonify({'message': 'Move made successfully!', 'draw': True})
        else:
            current_player = "O" if current_player == "X" else "X"
            return jsonify({'message': 'Move made successfully!', 'winner': None})
    else:
        return jsonify({'message': 'Invalid move!'})


@app.route('/reset')
def reset():
    global board, current_player
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    return jsonify({'message': 'Game reset successfully!'})

if __name__ == '__main__':
    app.run(debug=True, port=5050)
