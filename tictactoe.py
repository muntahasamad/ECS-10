import random
import sys
X = "X"
O = "O"

computer_calls = []
human_calls = []
stall_count = 0

def computer_call(call_list):
    call = random.randrange(1,29)
    while call in call_list:
        call = random.randrange(1,29)
    return call

def legal_move(call,call_list,board,other_player_last_call):
    if call in call_list:
        return False
    return (call + other_player_last_call) in board

def computer_move(board,call_list,other_player_last_call,computer_piece):
    call = computer_call(call_list)
    for i in range(100):
        if legal_move(call,call_list,board,other_player_last_call):
            print("Computer calls ",call, "\n")
            call_list.append(call)
            board[board.index(call+other_player_last_call)] = computer_piece
            display_board(board)
            return
        call = computer_call(call_list)
    print("STALL. GAME OVER.")
    exit()
    
def human_call():
    call = int(input("Please input a number between 1 and 28: "))
    while call not in range(1,29):
        call = int(input("Please input a number between 1 and 28: "))
    return call
    
def human_move(board,call_list,other_player_last_call,computer_piece):
    call = human_call()
    if legal_move(call,call_list,board,other_player_last_call):
        call_list.append(call)
        board[board.index(call+other_player_last_call)] = computer_piece
        display_board(board)
    else:
        print("Sorry, illegal move.")
    
def display_instruct ():
    """Display game instructions."""  
    print (
    """
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.  
    This will be a showdown between your human brain and my silicon processor.  

    You will make your move known by entering a number from 1-28.
    This number will then be added to the previously called number.
    If there exists a square with this number that is unmarked your marker will be put there.  

    Prepare yourself, human.  The ultimate battle is about to begin. \n
    """)

def pieces():
    """Determine if player or computer goes first."""
    go_first = ask_yes_no("Do you require the first move? (y/n): ")
    if go_first == "y":
        print ("\nThen take the first move.  You will need it.")
        hum = X
        com = O
    else:
        print ("\nYour bravery will be your undoing... I will go first.")
        com = X
        hum = O
    return com, hum

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def display_board(board):
    for i in range(0,4):
        for j in range(0,4):
            print(board[i*4+j],end="\t")
        print()
    print("\n")
    
def make_board():
    random_board = []
    for i in range(16):
        number = random.randrange(2,33)
        while number in random_board:
            number = random.randrange(2,33)
        random_board.append(number)
    display_board(random_board)
    return random_board


def draw(board):
    for entry in board:
        if not(entry == X or entry == O):
            return False
    return True
    

def winner(board):
    # check rows
    for i in range(4):
        first_square = board[i*4]
        four_in_line = True
        for j in range(1,4):
            if board[i*4+j] != first_square:
                four_in_line = False
                break
        if four_in_line:
            return True
            
    # check columns
    for j in range(4):
        i = 0
        first_square = board[i*4+j]
        four_in_line = True
        for i in range(1,4):
            if board[i*4+j] != first_square:
                four_in_line = False
                break
        if four_in_line:
            return True
        
    # check leading diagnonal
    first_square = board[0]
    four_in_line = True
    for (i,j) in [(1,1),(2,2),(3,3)]:
        if board[i*4+j] != first_square:
            four_in_line = False
            break
    if four_in_line:
        return True
    
    # check trailing diagonal
    first_square = board[3]
    four_in_line = True
    for (i,j) in [(1,2),(2,1),(3,0)]:
        if board[i*4+j] != first_square:
            four_in_line = False
            break
    if four_in_line:
        return True
    
    return False



#main
display_instruct()
computer_piece, human_piece = pieces()
board = make_board()
if computer_piece == O: # Human calls first
    human_calls.append(human_call())
    current_turn = computer_piece
else:
    computer_calls.append(computer_call(computer_calls))
    print("Computer calls ",computer_calls[-1], "\n")
    current_turn = human_piece

while not (winner(board) or draw(board)):
    if (current_turn == computer_piece):
        computer_move(board,computer_calls,human_calls[-1],computer_piece)
        current_turn = human_piece
    else:
        human_move(board,human_calls,computer_calls[-1],human_piece)
        current_turn = computer_piece
        
if winner(board):
    if current_turn == human_piece:
        print("Sorry, I win. Better luck next time.")  
    else:
        print("Congratulations! You won!!!!")   
else:
    print("DRAW!!")
    
        
        
        
