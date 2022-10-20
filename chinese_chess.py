import pygame, sys, copy, random
from pygame.locals import *

alpha=0.5
epsilon=0.1

# Load possible moves pointer
dot = pygame.image.load("images/move.png")
active = pygame.image.load("images/active.png")

# Pygame surface object dictionary
conv = {
'xe_do1': pygame.image.load("images/xe_do.png"),
'xe_do2': pygame.image.load("images/xe_do.png"),
'ma_do1': pygame.image.load("images/ma_do.png"),
'ma_do2': pygame.image.load("images/ma_do.png"),
'voi_do1': pygame.image.load("images/voi_do.png"),
'voi_do2': pygame.image.load("images/voi_do.png"),
'si_do1': pygame.image.load("images/si_do.png"),
'si_do2': pygame.image.load("images/si_do.png"),
'phao_do1': pygame.image.load("images/phao_do.png"),
'phao_do2': pygame.image.load("images/phao_do.png"),
'tuong_do': pygame.image.load("images/tuong_do.png"),
'chot_do1': pygame.image.load("images/chot_do.png"),
'chot_do2': pygame.image.load("images/chot_do.png"),
'chot_do3': pygame.image.load("images/chot_do.png"),
'chot_do4': pygame.image.load("images/chot_do.png"),
'chot_do5': pygame.image.load("images/chot_do.png"),

'xe_den1': pygame.image.load("images/xe_den.png"),
'xe_den2': pygame.image.load("images/xe_den.png"),
'ma_den1': pygame.image.load("images/ma_den.png"),
'ma_den2': pygame.image.load("images/ma_den.png"),
'voi_den1': pygame.image.load("images/voi_den.png"),
'voi_den2': pygame.image.load("images/voi_den.png"),
'si_den1': pygame.image.load("images/si_den.png"),
'si_den2': pygame.image.load("images/si_den.png"),
'phao_den1': pygame.image.load("images/phao_den.png"),
'phao_den2': pygame.image.load("images/phao_den.png"),
'tuong_den': pygame.image.load("images/tuong_den.png"),
'chot_den1': pygame.image.load("images/chot_den.png"),
'chot_den2': pygame.image.load("images/chot_den.png"),
'chot_den3': pygame.image.load("images/chot_den.png"),
'chot_den4': pygame.image.load("images/chot_den.png"),
'chot_den5': pygame.image.load("images/chot_den.png")
}

# List of board coordinates
board = [
    [(36, 30), (109, 30), (182, 30), (255, 30), (327, 30), (399, 30), (472, 30), (545, 30), (618, 30)],
    [(36, 94), (109, 94), (182, 94), (255, 94), (327, 94), (399, 94), (472, 94), (545, 94), (618, 94)],
    [(36, 158), (109, 158), (182, 158), (255, 158), (327, 158), (399, 158), (472, 158), (545, 158), (618, 158)],
    [(36, 222), (109, 222), (182, 222), (255, 222), (327, 222), (399, 222), (472, 222), (545, 222), (618, 222)],
    [(36, 286), (109, 286), (182, 286), (255, 286), (327, 286), (399, 286), (472, 286), (545, 286), (618, 286)],
    [(36, 353), (109, 353), (182, 353), (255, 353), (327, 353), (399, 353), (472, 353), (545, 353), (618, 353)],
    [(36, 417), (109, 417), (182, 417), (255, 417), (327, 417), (399, 417), (472, 417), (545, 417), (618, 417)],
    [(36, 481), (109, 481), (182, 481), (255, 481), (327, 481), (399, 481), (472, 481), (545, 481), (618, 481)],
    [(36, 545), (109, 545), (182, 545), (255, 545), (327, 545), (399, 545), (472, 545), (545, 545), (618, 545)],
    [(36, 609), (109, 609), (182, 609), (255, 609), (327, 609), (399, 609), (472, 609), (545, 609), (618, 609)]
]

# All pieces of black player
co_den = [
    'xe_den1', 'xe_den2', 'ma_den1', 'ma_den2', 'voi_den1',
    'voi_den2', 'si_den1', 'si_den2', 'tuong_den', 'phao_den1',
    'phao_den2', 'chot_den1', 'chot_den2', 'chot_den3',
    'chot_den4', 'chot_den5'
]

# All pieces of red player
co_do = [
    'xe_do1', 'xe_do2', 'ma_do1', 'ma_do2', 'voi_do1', 'voi_do2',
    'si_do1', 'si_do2', 'tuong_do', 'phao_do1', 'phao_do2',
    'chot_do1', 'chot_do2', 'chot_do3', 'chot_do4', 'chot_do5'
]

# All pieces of black player's attackers
den_attacker = [
            'chot_den1', 'chot_den2', 'chot_den3', 'chot_den4', 'chot_den5', 'tuong_den',
            'xe_den1', 'xe_den2', 'phao_den1', 'phao_den2', 'ma_den1', 'ma_den2',
        ]

# All pieces of red player's attackers
do_attacker = [
            'chot_do1', 'chot_do2', 'chot_do3', 'chot_do4', 'chot_do5', 'tuong_do',
            'xe_do1', 'xe_do2', 'phao_do1', 'phao_do2', 'ma_do1', 'ma_do2'
        ]

# Possible moves for red player's defenders
si_do_moves = [(9, 3), (9, 5), (8, 4), (7, 3), (7, 5)]
voi_do_moves = [(9, 2), (7, 0), (7, 4), (5, 2), (9, 6), (7, 8), (5, 6)]
tuong_do_moves = [(9, 3), (9, 4), (9, 5), (8, 3), (8, 4), (8, 5), (7, 3), (7, 4), (7, 5)]
# Possible moves for black player's defenders
si_den_moves = [(0, 3), (0, 5), (1, 4), (2, 3), (2, 5)]
voi_den_moves = [(0, 2), (2, 0), (4, 2), (2, 4), (0, 6), (2, 8), (4, 6)]
tuong_den_moves = [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]

original_map = [
    ['xe_den1', 'ma_den1', 'voi_den1', 'si_den1', 'tuong_den', 'si_den2', 'voi_den2', 'ma_den2', 'xe_den2'],
    ['', '', '', '', '', '', '', '', ''],
    ['', 'phao_den1', '', '', '', '', '', 'phao_den2', ''],
    ['chot_den1', '', 'chot_den2', '', 'chot_den3', '', 'chot_den4', '', 'chot_den5'],
    ['', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', ''],
    ['chot_do1', '', 'chot_do2', '', 'chot_do3', '', 'chot_do4', '', 'chot_do5'],
    ['', 'phao_do1', '', '', '', '', '', 'phao_do2', ''],
    ['', '', '', '', '', '', '', '', ''],
    ['xe_do1', 'ma_do1', 'voi_do1', 'si_do1', 'tuong_do', 'si_do2', 'voi_do2', 'ma_do2', 'xe_do2']
]

point_system = {
    'chot_do1': 1, 'chot_do2': 1, 'chot_do3': 1,'chot_do4': 1, 'chot_do5': 1,
    'si_do1': 2, 'si_do2': 2, 'voi_do1': 2, 'voi_do2': 2, 'ma_do1': 4, 'ma_do2': 4,
    'phao_do1': 4.5, 'phao_do2': 4.5, 'xe_do1': 9, 'xe_do2': 9,
    'chot_den1': 1, 'chot_den2': 1, 'chot_den3':1, 'chot_den4': 1, 'chot_den5': 1,
    'si_den1': 2, 'si_den2': 2, 'voi_den1': 2, 'voi_den2': 2, 'ma_den1': 4, 'ma_den2': 4,
    'phao_den1': 4.5, 'phao_den2': 4.5, 'xe_den1': 9, 'xe_den2': 9 
}

knowledge_base = {}
# Load database file to dict
with open('database.txt', mode='r') as file:
    kb = file.read().splitlines()

# Write databse to dict
for i in kb:
    k = i.split(':')
    knowledge_base.update({(k[0]): float(k[1])})

# Game board map
map = copy.deepcopy(original_map)

def player(turn):
    """
    Return a list of names of all pieces of the player in turn
    """
    if (turn % 2) == 0: player = co_do
    else: player = co_den
    return player

def player_str(turn):
    """
    Return player turn in string
    """
    if (turn % 2) == 0: player = 'co_do'
    else: player = 'co_den'
    return player

def render_game(map):
    """
    Initialize game window. Fill window with chess board background
    and display all the chess pieces on the board according to
    current map of the game
    """
    # Choose white canvas
    screen.fill((255, 255, 255))
    # Display background image on top of canvas
    screen.blit(bg, (40, 40))
    # Display chess pieces
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j]:
                screen.blit(conv[map[i][j]], (board[i][j][0] - 16, board[i][j][1] - 16))

def piece_clicked(x, y):
    """
    Listen for event in game window to determine which piece was clicked on.
    Only return the piece's name and its location of clicked piece
    belong to current player. You can't click on your oppenent's pieces.
    Return a pair  of coordinate (i, j) on the map.
    """
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] and map[i][j] in player(turn):
                if conv[map[i][j]].get_rect(topleft = (board[i][j][0] - 16, board[i][j][1] - 16)).collidepoint(x, y):
                    return map[i][j], i, j

def possible_moves(piece, i, j, map):
    """
    Return a list of all possible moves for a piece.
    list elements are pair of (i, j) corrdinates,
    Which is the position of a piece on the map,
    not the BOARD list of pixel to display sprites.
    """
    moves = []
    # Get all possible moves for chốt đỏ
    if piece in ['chot_do1', 'chot_do2', 'chot_do3', 'chot_do4', 'chot_do5']:
        if (i - 1) >= 0:
            if map[i - 1][j] not in co_do:
                moves.append((i - 1, j))
        if i <= 4:
            if (j - 1) >= 0:
                if map[i][j - 1] not in co_do: moves.append((i, j - 1))
            if (j + 1) <= 8:
                if map[i][j + 1] not in co_do: moves.append((i, j + 1))
    # Get all possible moves for sĩ đỏ
    if piece in ['si_do1', 'si_do2']:
        si_moves = [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
        for move in si_moves:
            if move in si_do_moves and map[move[0]][move[1]] not in co_do:
                moves.append((move[0], move[1]))
    # Get all possible moves for tượng đỏ
    if piece in ['voi_do1', 'voi_do2']:
        voi_moves = [(i - 2, j - 2), (i - 2, j + 2), (i + 2, j - 2), (i + 2, j + 2)]
        voi_blocks = [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
        for i in range(len(voi_moves)):
            if voi_moves[i] in voi_do_moves and map[voi_moves[i][0]][voi_moves[i][1]] not in co_do:
                if not map[voi_blocks[i][0]][voi_blocks[i][1]]:
                    moves.append((voi_moves[i][0], voi_moves[i][1]))
    # Get all moves for tướng đỏ
    if piece == 'tuong_do':
        tuong_moves = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        for move in tuong_moves:
            if move in tuong_do_moves and map[move[0]][move[1]] not in co_do:
                moves.append((move[0], move[1]))
        t = 1
        while (i - t) <= 9:
            if not map[i - t][j]: pass
            if map[i - t][j]:
                if map[i - t][j] == 'tuong_den': 
                    moves.append((i - t, j))
                    break
                else: break
            t += 1
    # Get all moves for mã đỏ
    if piece in ['ma_do1', 'ma_do2']:
        ma_moves = []
        if (i - 2) >= 0 and not map[i - 1][j]:
            if (j - 1) >= 0: ma_moves.append((i - 2, j - 1))
            if (j + 1) <= 8: ma_moves.append((i - 2, j + 1))
        if (i + 2) <= 9 and not map[i + 1][j]:
            if (j - 1) >= 0: ma_moves.append((i + 2, j - 1))
            if (j + 1) <= 8: ma_moves.append((i + 2, j + 1))
        if (j + 2) <= 8 and not map[i][j + 1]:
            if (i - 1) >= 0: ma_moves.append((i - 1, j + 2))
            if (i + 1) <= 9: ma_moves.append((i + 1, j + 2))
        if (j - 2) >= 0 and not map[i][j - 1]:
            if (i - 1) >= 0: ma_moves.append((i - 1, j - 2))
            if (i + 1) <= 9: ma_moves.append((i + 1, j - 2))
        for move in ma_moves:
            if not map[move[0]][move[1]] or map[move[0]][move[1]] not in co_do:
                moves.append((move[0], move[1]))           
    # Get all moves for xe đỏ
    if piece in ['xe_do1', 'xe_do2']:
        # Down
        t = 1
        while (i + t) <= 9:
            if not map[i + t][j]: 
                moves.append((i + t, j))
            elif map[i + t][j] in co_den:
                moves.append((i + t, j))
                break
            else: break
            t += 1
        # Up
        t = 1
        while (i - t) >= 0:
            if not map[i - t][j]:
                moves.append((i - t, j))
            elif map[i - t][j] in co_den:
                moves.append((i - t, j))
                break
            else: break
            t += 1
        # Right
        t = 1
        while(j + t) <= 8:
            if not map[i][j + t]:
                moves.append((i, j + t))
            elif map[i][j + t] in co_den:
                moves.append((i, j + t))
                break
            else: break
            t += 1
        # Left
        t = 1
        while(j - t) >= 0:
            if not map[i][j - t]:
                moves.append((i, j - t))
            elif map[i][j - t] in co_den:
                moves.append((i, j - t))
                break
            else: break
            t += 1
    # Get all moves for pháo đỏ
    if piece in ['phao_do1', 'phao_do2']:
        # Down
        t = 1
        f = 0
        while (i + t) <= 9:
            if not map[i + t][j]:
                if f == 0:
                    moves.append((i + t, j))
            elif map[i + t][j] in co_den:
                if f == 1:
                    moves.append((i + t, j))
                    break
                else: f += 1
            elif map[i + t][j] in co_do: f += 1 
            t += 1
        # Up
        t = 1
        f = 0
        while (i - t) >= 0:
            if not map[i - t][j]:
                if f == 0:
                    moves.append((i - t, j))
            elif map[i - t][j] in co_den:
                if f == 1:
                    moves.append((i - t, j))
                    break
                else: f += 1
            elif map[i - t][j] in co_do: f += 1 
            t += 1
        # Right
        t = 1
        f = 0
        while(j + t) <= 8:
            if not map[i][j + t]:
                if f == 0:
                    moves.append((i, j + t))
            elif map[i][j + t] in co_den:
                if f == 1:
                    moves.append((i, j + t))
                    break
                else: f += 1
            elif map[i][j + t] in co_do: f += 1 
            t += 1
        # Left
        t = 1
        f = 0
        while(j - t) >= 0:
            if not map[i][j - t]:
                if f == 0:
                    moves.append((i, j - t))
            elif map[i][j - t] in co_den:
                if f == 1:
                    moves.append((i, j - t))
                    break
                else: f += 1
            elif map[i][j - t] in co_do: f += 1 
            t += 1
    # Get all moves for chốt đen
    if piece in ['chot_den1', 'chot_den2', 'chot_den3', 'chot_den4', 'chot_den5']:
        if (i + 1) <= 9:
            if map[i + 1][j] not in co_den:
                moves.append((i + 1, j))
        if i >= 5:
            if (j - 1) >= 0:
                if map[i][j - 1] not in co_den: moves.append((i, j - 1))
            if (j + 1) <= 8:
                if map[i][j + 1] not in co_den: moves.append((i, j + 1))
    # Get all moves for sĩ đen
    if piece in ['si_den1', 'si_den2']:
        si_moves = [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
        for move in si_moves:
            if move in si_den_moves and map[move[0]][move[1]] not in co_den:
                moves.append((move[0], move[1]))
    # Get all moves for tượng đen
    if piece in ['voi_den1', 'voi_den2']:
        voi_moves = [(i - 2, j - 2), (i - 2, j + 2), (i + 2, j - 2), (i + 2, j + 2)]
        voi_blocks = [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
        for i in range(len(voi_moves)):
            if voi_moves[i] in voi_den_moves and map[voi_moves[i][0]][voi_moves[i][1]] not in co_den:
                if not map[voi_blocks[i][0]][voi_blocks[i][1]]:
                    moves.append((voi_moves[i][0], voi_moves[i][1]))
    # Get all move for tướng đen
    if piece == 'tuong_den':
        tuong_moves = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        for move in tuong_moves:
            if move in tuong_den_moves and map[move[0]][move[1]] not in co_den: 
                moves.append((move[0], move[1]))
        t = 1
        while (i + t) <= 9:
            if not map[i + t][j]: pass
            if map[i + t][j]:
                if map[i + t][j] == 'tuong_do': 
                    moves.append((i + t, j))
                    break
                else: break
            t += 1
    # Get all moves for mã đen
    if piece in ['ma_den1','ma_den2']:
        ma_moves = []
        if (i - 2) >= 0 and not map[i - 1][j]:
            if (j - 1) >= 0: ma_moves.append((i - 2, j - 1))
            if (j + 1) <= 8: ma_moves.append((i - 2, j + 1))
        if (i + 2) <= 9 and not map[i + 1][j]:
            if (j - 1) >= 0: ma_moves.append((i + 2, j - 1))
            if (j + 1) <= 8: ma_moves.append((i + 2, j + 1))
        if (j + 2) <= 8 and not map[i][j + 1]:
            if (i - 1) >= 0: ma_moves.append((i - 1, j + 2))
            if (i + 1) <= 9: ma_moves.append((i + 1, j + 2))
        if (j - 2) >= 0 and not map[i][j - 1]:
            if (i - 1) >= 0: ma_moves.append((i - 1, j - 2))
            if (i + 1) <= 9: ma_moves.append((i + 1, j - 2))
        for move in ma_moves:
            if not map[move[0]][move[1]] or map[move[0]][move[1]] in co_do:
                moves.append((move[0], move[1]))
    # Get all moves for xe đen
    if piece in ['xe_den1', 'xe_den2']:
        # Down
        t = 1
        while (i + t) <= 9:
            if not map[i + t][j]:
                moves.append((i + t, j))
            elif map[i + t][j] in co_do:
                moves.append((i + t, j))
                break
            else: break
            t += 1
        # Up
        t = 1
        while (i - t) >= 0:
            if not map[i - t][j]:
                moves.append((i - t, j))
            elif map[i - t][j] in co_do:
                moves.append((i - t, j))
                break
            else: break
            t += 1
        # Right
        t = 1
        while (j + t) <= 8:
            if not map[i][j + t]:
                moves.append((i, j + t))
            elif map[i][j + t] in co_do:
                moves.append((i, j + t))
                break
            else: break
            t += 1
        # Left
        t = 1
        while (j - t) >= 0:
            if not map[i][j - t]:
                moves.append((i, j - t))
            elif map[i][j - t] in co_do:
                moves.append((i, j - t))
                break
            else: break
            t += 1
    # Get all moves for pháo đen
    if piece in ['phao_den1', 'phao_den2']:
        # Down
        t = 1
        f = 0
        while (i + t) <= 9:
            if not map[i + t][j]:
                if f == 0:
                    moves.append((i + t, j))
            elif map[i + t][j] in co_do:
                if f == 1:
                    moves.append((i + t, j))
                    break
                else: f += 1
            elif map[i + t][j] in co_den: f += 1
            t += 1
        # Up
        t = 1
        f = 0
        while (i - t) >= 0:
            if not map[i - t][j]:
                if f == 0:
                    moves.append((i - t, j))
            elif map[i - t][j] in co_do:
                if f == 1:
                    moves.append((i - t, j))
                    break
                else: f += 1
            elif map[i - t][j] in co_den: f += 1
            t += 1
        # Right
        t = 1
        f = 0
        while(j + t) <= 8:
            if not map[i][j + t]:
                if f == 0:
                    moves.append((i, j + t))
            elif map[i][j + t] in co_do:
                if f == 1:
                    moves.append((i, j + t))
                    break
                else: f += 1
            elif map[i][j + t] in co_den: f += 1            
            t += 1
        # Left
        t = 1
        f = 0
        while(j - t) >= 0:
            if not map[i][j - t]:
                if f == 0:
                    moves.append((i, j - t))
            elif map[i][j - t] in co_do:
                if f == 1:
                    moves.append((i, j - t))
                    break
                else: f += 1
            elif map[i][j - t] in co_den: f += 1 
            t += 1

    return moves

def check_future_checkmate(piece, moves, turn, map):
    """
    Check if making a move result in checkmate. Create a deep
    copy of the map and make the move. After making the move, 
    check if checkmate. If checkmate, do not add move to legit
    moves list.
    """
    legal_moves = []
    for m in range(len(moves)):
        map1 = copy.deepcopy(map)
        make_move(piece, moves[m], map1)
        if not checkmate(map1, turn):
            legal_moves.append(moves[m])
    return legal_moves

def move_clicked(moves, x, y):
    """
    Determine which move was clicked
    """
    for move in moves:
        if dot.get_rect(topleft = (board[move[0]][move[1]][0], board[move[0]][move[1]][1])).collidepoint(x, y):
            return move

def make_move(piece, move, map):
    """
    Make the move to the game by updating the map.
    Move the piece to new location according to what 
    move was taken, and delete the piece in its old place.
    """
    for m in range(10):
        for n in range(9):
            if map[m][n] == piece:
                map[m][n] = ''    
                map[move[0]][move[1]] = piece
                return map

def get_ij(piece, map):
    """
    Get the (i, j) index of a chess piece on map
    """
    for i in range(10):
        for j in range(9):
            if map[i][j] == piece:
                return i, j

def on_board(piece, map):
    """
    Check if a chess piece is on game board.
    """
    for i in range(10):
        for j in range(9):
            if map[i][j] == piece:
                return True

def checkmate(map, turn):
    """
    Check if you are being checkmated.
    """
    # Get the position of the general
    if player(turn) == co_do: i, j = get_ij('tuong_do', map)
    if player(turn) == co_den: i, j = get_ij('tuong_den', map)
    # Check for red player
    if player(turn) == co_do:
        for piece in den_attacker:
            if on_board(piece, map):
                x, y = get_ij(piece, map)
                if (i, j) in possible_moves(piece, x, y, map):
                    return True
    # Check for black player
    else:
        for piece in do_attacker:
            if on_board(piece, map):
                x, y = get_ij(piece, map)
                if (i, j) in possible_moves(piece, x, y, map):
                    return True

def end_game(map, turn):
    """
    Check if there is no move to un-checkmate. In such case, 
    the game is over and current player is lost.
    """
    for piece in player(turn):
        if on_board(piece, map):
            i, j = get_ij(piece, map)
            moves = possible_moves(piece, i, j, map)
            moves = check_future_checkmate(piece, moves, turn, map)
            if moves: return False
    return True

def end_game_question(turn, x, y):
    
    if player(turn) == co_do:
        text_surface = my_font1.render(f"You Lost!", False, (0, 0, 0))
    else:
        text_surface = my_font1.render(f"You Win!", False, (0, 0, 0))

    text_surface1 = my_font1.render("Wanna play again?", False, (0, 0, 0))
    yes = my_font1.render("YES", False, (0, 0, 0))
    no = my_font1.render("NO", False, (0, 0, 0))

    screen.blit(text_surface, (760, 40))
    screen.blit(text_surface1, (690, 80))
    screen.blit(yes, (735, 130))
    screen.blit(no, (875, 130))

    if yes.get_rect(topleft = (735, 130)).collidepoint(x, y): return True
    if no.get_rect(topleft = (875, 130)).collidepoint(x, y): sys.exit()

def all_actions(state):
    """
    Return all available action for a game board. Move is 
    a list containing piece and move: (piece, (i, j)).
    """
    actions = []
    map = state
    for piece in player(turn):
        if on_board(piece, map):
            i, j = get_ij(piece, map)
            moves = possible_moves(piece, i, j, map)
            moves = check_future_checkmate(piece, moves, turn, map)
            for move in moves:
                actions.append((piece, move))
    return actions

def ai_move():
    """
    Given a state `state`, return an action `(i, j)` to take.
    With probability epsilon, choose a random available action, 
    otherwise, choose the best action available.
    If multiple actions have the same Q-value, any of those
    actions is an aceptable return value.
    """
    state = map
    # Initialize empty dictionary
    moves = {}

    # Get all possible moves for state
    actions = all_actions(state)

    # Add move and corresponding Q value to dict
    for action in actions:
        if (str(state) + str(action)) in knowledge_base.keys():
            q = knowledge_base[(str(state) + str(action))]
        else:
            q = 0
        moves.update({action: q})

    # Initialize empty dict
    random_moves = {}

    if sum(list(moves.values())) != 0:
        # Add best move to dict
        best_move = max(moves, key=moves.get)
        random_moves.update({best_move: 1 - epsilon})
        del moves[best_move]

        # Add remaining item with probability epsilon to dict
        for item in list(moves.keys()):
            random_moves.update({item: epsilon / len(list(moves.keys()))})
    else:
        for item in list(moves.keys()):
            random_moves.update({item: epsilon / len(list(moves.keys()))})
    
    return random.choices(list(random_moves.keys()), weights = list(random_moves.values()))[0]


# Initialize pygame
pygame.init()
# Initialize pygame text font
pygame.font.init()
my_font1 = pygame.font.SysFont('Comic Sans MS', 34)
my_font = pygame.font.SysFont('Comic Sans MS', 16)
# Size of game window
size = width, height = 1000, 665
# Display game window
screen = pygame.display.set_mode(size)
# Set game window caption
pygame.display.set_caption("Chinese Chess")
# Load background image
bg = pygame.image.load("images/bg.jpg")
# Display game board and pieces
render_game(map)
# Check for second click
second_click = False
# Keep track of turn
turn = 0

while True:
    
    # Check if game is over
    if end_game(map, turn):

        # Circle tướng active if under checkmate
        if checkmate(map, turn):
            if player(turn) == co_do: i, j = get_ij('tuong_do', map)
            if player(turn) == co_den: i, j = get_ij('tuong_den', map)
            screen.blit(active, (board[i][j][0] - 22, board[i][j][1] - 22))
            #text_checkmate = my_font1.render("CHECKMATE", False, (0, 0, 0))
            #screen.blit(text_checkmate, (720, 310))

        # Reset game if player choose to play again
        if end_game_question(turn, x, y):       
            map = copy.deepcopy(original_map)
            turn = 0
            render_game(map)
            continue     

    # Human player's turn
    if player(turn) == co_do:

        # Render turn text
        text_turn = my_font.render("Your turn", False, (0, 0, 0))
        screen.blit(text_turn, (300, 320))

        if checkmate(map, turn):
            if player(turn) == co_do: i, j = get_ij('tuong_do', map)
            if player(turn) == co_den: i, j = get_ij('tuong_den', map)
            screen.blit(active, (board[i][j][0] - 22, board[i][j][1] - 22))
            text_checkmate = my_font1.render("CHECKMATE", False, (0, 0, 0))
            screen.blit(text_checkmate, (720, 310))

        # Listen to quit program event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Listen to mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # If first click on a piece
                if piece_clicked(x, y):
                    render_game(map)
                    second_click = True
                    piece, i, j = piece_clicked(x, y)
                    moves = possible_moves(piece, i, j, map)
                    moves = check_future_checkmate(piece, moves, turn, map)
                    screen.blit(active, (board[i][j][0] - 22, board[i][j][1] - 22))
                    for move in moves:
                        screen.blit(dot, (board[move[0]][move[1]][0] - 2, board[move[0]][move[1]][1] - 2))
                # If second click on a move
                elif second_click and move_clicked(moves, x, y):   
                    move = move_clicked(moves, x, y)
                    make_move(piece, move, map)
                    render_game(map)
                    second_click = False
                    turn += 1
                else:
                    render_game(map)
                    second_click = False

    # AI's turn
    else:

        # Display AI turn text
        text_turn = my_font.render("AI's turn", False, (0, 0, 0))
        screen.blit(text_turn, (300, 320))
        pygame.display.update()

        if not end_game(map, turn): 
            
            # Choose a move and make move
            move = ai_move()
            i, j = get_ij(move[0], map)
            make_move(move[0], move[1], map)

            # Mark the piece moved and its former location
            render_game(map)
            screen.blit(dot, (board[i][j][0] - 2, board[i][j][1] - 2))
            screen.blit(active, (board[move[1][0]][move[1][1]][0] - 22, board[move[1][0]][move[1][1]][1] - 22))
            turn += 1

        else:
            
            # Listen to quit program event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # Listen to mouse click event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
    
    pygame.display.update()