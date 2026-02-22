
def create_board(row, col) -> list[list[str]]:
    board = [['_' for _ in range(col)] for _ in range(row) ]
    return board

def print_board(board: list[list[str]]) -> None:
    print(" 1 2 3 4 5 6 7")
    for row in board:
        print(' ' + ' '.join(row))
        print()

def make_move(board: list[list[str]], col: int, rows: int,  piece: str ) -> bool:
    for row in range(rows-1, -1, -1):
        if board[row][col] == "_":
            board[row][col] = piece
            return True
    return False
    
def get_choice() -> int:
    while True:
        col = input("pelase enter column(1 to 7): ")
        if col.isdigit():
            col = int(col)    
            col -= 1
            if 0 <= col < 7:
                return col
            
        print('input must be between 1 to 7')


def is_winner(board: list[list[str]], piece: str) -> bool:
    rows = len(board)
    cols = len(board[0])

    for row in range(rows):
        for col in range(cols - 3):
            if all(board[row][col+i] == piece for i in range(4)):
                return True


    for row in range(rows - 3):
        for col in range(cols):
            if all(board[row+i][col] == piece for i in range(4)):
                return True

    
    for row in range(rows - 3):
        for col in range(cols - 3):
            if all(board[row+i][col+i] == piece for i in range(4)):
                return True

    
    for row in range(3, rows):
        for col in range(cols - 3):
            if all(board[row-i][col+i] == piece for i in range(4)):
                return True

    return False

def is_draw(board: list[list[str]]) -> bool:
    return all(cell != "_" for row in board for cell in row)


def run(board:list[list[str]], col:int, rows:int)-> None:
    p1 = "X"
    p2 = "O"
    
    current = p1
    while True:
        print_board(board)

        col = get_choice()
        ok = make_move(board, col, rows, current)

        if not ok:
            print("this is full please choice another.")
            continue
        
        if is_winner(board, current):
            print_board(board)
            print(f"player {current} wins!")
            return

        if is_draw(board):
            print_board(board)
            print("Draws!")
            return
        
        
        if current == p1:
            current = p2
        else:
            current = p1

        
def main():
    row = 5
    col = 7
    board = create_board(row, col)
    run(board, col, row)
    
    
    
    


main()

