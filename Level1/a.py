from IPython.display import clear_output

# <list>board
# ["","시작점", "10번째 끝점"]
def display_board(board):
    clear_output()
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

test_board = ["", "X", "O", "X", "O", "X", "O", "X", "O", "X"]
display_board(test_board)

def player_input():
    marker = ""
    
    while not (marker == "X" or marker == "O"):
        marker = input("Player1: Do you want to be X or O? ").strip().upper()
    
    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")

result = player_input()
print(result)

# <list>board 
# <string>marker
# <int>position
def place_marker(board, marker, position):
    board[position] = marker

test_board = ["", "X", "O", "X", "O", "X", "O", "X", "O", ""]
place_marker(test_board, "O", 9)
print(test_board)

def win_check(board, mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal
    
import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

# 공간이 비어있는지 여부를 검사한다 
# 비어있다면 true, 아니면 false
def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    
    # 1. position이 1 ~ 9 사이 값인지
    # 2. 마커를 놓으려고 하는 포지션이 비었는지 검사
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = input("Choose Your Position: (1 ~ 9)")
    
    return position

def replay():
    return input("Do you want to play again? Enter Yes or No").strip().lower().startswith('y')

print("Welcome to Tic Tac Toe")

while True:
    # 1. 보드를 세팅한다
    theBoard = [" "] * 10
    # 2. 플레이어 마커를 할당한다 - Tuple Unpacking
    player1_marker, player2_marker = player_input()
    # 3. 누가 선인지
    turn = choose_first()
    print(turn + " will go first")
    
    play_game = input("Are you ready to play? Enter Yes or No")
    #  a = 'hello' a[0] ==> h 
    if play_game.strip().lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        # 4. turn에 담긴 값으로 누가 먼저인지 확인한다
        if turn == 'Player 1':
            
            # 1. 보드를 보여준다
            display_board(theBoard)
            # 2. 사용자에게 마커를 두고 싶은 위치를 선정하게 한다
            position = player_choice(theBoard)
            # 3. position을 이용해 실제 보드에 반영한다
            place_marker(theBoard, player1_marker, position)
            
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print("Player 1이 이겼어")
                game_on = False
            
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("무승부입니다")
                    break
                else:
                    turn = "Player 2"
        else:
            # Player2's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print("Player 2 이겼어")
                game_on = False
                
            else: 
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("무승부입니다")
                    break
                else:
                    turn = "Player 1"
    
    # while 문을 빠져나온 지점
    if not replay():
        break