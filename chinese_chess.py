import pygame, sys, copy

# Load possible moves pointer
dot = pygame.image.load("images/move.png")
active = pygame.image.load("images/active.png")

# Pygame surface object dictionary
pieces_img = {
'red_chariot': pygame.image.load("images/red_chariot.png"),
'red_chariot1': pygame.image.load("images/red_chariot.png"),
'red_horse': pygame.image.load("images/red_horse.png"),
'red_horse1': pygame.image.load("images/red_horse.png"),
'red_elephant': pygame.image.load("images/red_elephant.png"),
'red_elephant1': pygame.image.load("images/red_elephant.png"),
'red_advisor': pygame.image.load("images/red_advisor.png"),
'red_advisor1': pygame.image.load("images/red_advisor.png"),
'red_cannon': pygame.image.load("images/red_cannon.png"),
'red_cannon1': pygame.image.load("images/red_cannon.png"),
'red_general': pygame.image.load("images/red_general.png"),
'red_soldier': pygame.image.load("images/red_soldier.png"),
'red_soldier1': pygame.image.load("images/red_soldier.png"),
'red_soldier2': pygame.image.load("images/red_soldier.png"),
'red_soldier3': pygame.image.load("images/red_soldier.png"),
'red_soldier4': pygame.image.load("images/red_soldier.png"),

'black_chariot': pygame.image.load("images/black_chariot.png"),
'black_chariot1': pygame.image.load("images/black_chariot.png"),
'black_horse': pygame.image.load("images/black_horse.png"),
'black_horse1': pygame.image.load("images/black_horse.png"),
'black_elephant': pygame.image.load("images/black_elephant.png"),
'black_elephant1': pygame.image.load("images/black_elephant.png"),
'black_advisor': pygame.image.load("images/black_advisor.png"),
'black_advisor1': pygame.image.load("images/black_advisor.png"),
'black_cannon': pygame.image.load("images/black_cannon.png"),
'black_cannon1': pygame.image.load("images/black_cannon.png"),
'black_general': pygame.image.load("images/black_general.png"),
'black_soldier': pygame.image.load("images/black_soldier.png"),
'black_soldier1': pygame.image.load("images/black_soldier.png"),
'black_soldier2': pygame.image.load("images/black_soldier.png"),
'black_soldier3': pygame.image.load("images/black_soldier.png"),
'black_soldier4': pygame.image.load("images/black_soldier.png")
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
black_pieces = [
    'black_chariot', 'black_horse', 'black_elephant', 'black_advisor', 'black_general', 'black_cannon', 'black_soldier',
    'black_chariot1', 'black_horse1', 'black_elephant1', 'black_advisor1', 'black_cannon1',
    'black_soldier1', 'black_soldier2', 'black_soldier3', 'black_soldier4'
]

# All pieces of red player
red_pieces = [
    'red_chariot', 'red_horse', 'red_elephant', 'red_advisor', 'red_general', 'red_cannon', 'red_soldier',
    'red_chariot1', 'red_horse1', 'red_elephant1', 'red_advisor1', 'red_cannon1', 
    'red_soldier1', 'red_soldier2', 'red_soldier3', 'red_soldier4'
]

# All pieces of black player's attackers
black_attacker = [
            'black_soldier', 'black_general', 'black_chariot', 'black_cannon', 'black_horse',
            'black_soldier1', 'black_soldier2', 'black_soldier3', 'black_soldier4',
            'black_chariot1', 'black_cannon1', 'black_horse1'
        ]

# All pieces of red player's attackers
red_attacker = [
            'red_soldier', 'red_general', 'red_chariot', 'red_cannon', 'red_horse',
            'red_soldier1', 'red_soldier2', 'red_soldier3', 'red_soldier4',
            'red_chariot1', 'red_cannon1', 'red_horse1'
        ]

# Possible moves for red player's defenders
red_advisor_moves = [(9, 3), (9, 5), (8, 4), (7, 3), (7, 5)]
red_elephant_moves = [(9, 2), (7, 0), (7, 4), (5, 2), (9, 6), (7, 8), (5, 6)]
red_general_moves = [(9, 3), (9, 4), (9, 5), (8, 3), (8, 4), (8, 5), (7, 3), (7, 4), (7, 5)]

# Possible moves for black player's defenders
black_advisor_moves = [(0, 3), (0, 5), (1, 4), (2, 3), (2, 5)]
black_elephant_moves = [(0, 2), (2, 0), (4, 2), (2, 4), (0, 6), (2, 8), (4, 6)]
black_general_moves = [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]

original_map = [
    ['black_chariot', 'black_horse', 'black_elephant', 'black_advisor', 'black_general', 'black_advisor1', 'black_elephant1', 'black_horse1', 'black_chariot1'],
    ['', '', '', '', '', '', '', '', ''],
    ['', 'black_cannon', '', '', '', '', '', 'black_cannon1', ''],
    ['black_soldier', '', 'black_soldier1', '', 'black_soldier2', '', 'black_soldier3', '', 'black_soldier4'],
    ['', '', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', '', ''],
    ['red_soldier', '', 'red_soldier1', '', 'red_soldier2', '', 'red_soldier3', '', 'red_soldier4'],
    ['', 'red_cannon', '', '', '', '', '', 'red_cannon1', ''],
    ['', '', '', '', '', '', '', '', ''],
    ['red_chariot', 'red_horse', 'red_elephant', 'red_advisor', 'red_general', 'red_advisor1', 'red_elephant1', 'red_horse1', 'red_chariot1']
]

# Game board map
map = copy.deepcopy(original_map)

def player(turn):
    """
    Return a list of names of all pieces of the player in turn
    """
    if (turn % 2) == 0: player = red_pieces
    else: player = black_pieces
    return player

def player_str(turn):
    """
    Return player turn in string
    """
    if (turn % 2) == 0: player = 'red_pieces'
    else: player = 'black_pieces'
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
                screen.blit(pieces_img[map[i][j]], (board[i][j][0] - 16, board[i][j][1] - 16))

def piece_clicked(x, y):
    """
    Listen for event in game window to determine which piece was clicked on.
    Only return the piece's name and its location of clicked piece
    belong to current player. You can't click on your oppenent's pieces.
    Return a pair of coordinate (i, j) on the map.
    """
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] and map[i][j] in player(turn):
                if pieces_img[map[i][j]].get_rect(topleft = (board[i][j][0] - 16, board[i][j][1] - 16)).collidepoint(x, y):
                    return map[i][j], i, j

def possible_moves(piece, i, j, map):
    """
    Return a list of all possible moves for a piece.
    list elements are pair of (i, j) corrdinates,
    Which is the position of a piece on the map,
    not the BOARD list of pixel to display sprites.
    """
    moves = []
    # Get all possible moves for red soldier
    if piece in ['red_soldier', 'red_soldier1', 'red_soldier2', 'red_soldier3', 'red_soldier4']:
        if (i - 1) >= 0:
            if map[i - 1][j] not in red_pieces:
                moves.append((i - 1, j))
        if i <= 4:
            if (j - 1) >= 0:
                if map[i][j - 1] not in red_pieces: moves.append((i, j - 1))
            if (j + 1) <= 8:
                if map[i][j + 1] not in red_pieces: moves.append((i, j + 1))
    # Get all possible moves for red advisor
    if piece in ['red_advisor', 'red_advisor1']:
        potential_red_advisor_moves = [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
        for move in potential_red_advisor_moves:
            if move in red_advisor_moves and map[move[0]][move[1]] not in red_pieces:
                moves.append((move[0], move[1]))
    # Get all possible moves for red elephant
    if piece in ['red_elephant', 'red_elephant1']:
        voi_moves = [(i - 2, j - 2), (i - 2, j + 2), (i + 2, j - 2), (i + 2, j + 2)]
        voi_blocks = [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
        for i in range(len(voi_moves)):
            if voi_moves[i] in red_elephant_moves and map[voi_moves[i][0]][voi_moves[i][1]] not in red_pieces:
                if not map[voi_blocks[i][0]][voi_blocks[i][1]]:
                    moves.append((voi_moves[i][0], voi_moves[i][1]))
    # Get all moves for red general
    if piece == 'red_general':
        tuong_moves = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        for move in tuong_moves:
            if move in red_general_moves and map[move[0]][move[1]] not in red_pieces:
                moves.append((move[0], move[1]))
        t = 1
        while (i - t) <= 9:
            if not map[i - t][j]: pass
            if map[i - t][j]:
                if map[i - t][j] == 'black_general': 
                    moves.append((i - t, j))
                    break
                else: break
            t += 1
    # Get all moves for red horse
    if piece in ['red_horse', 'red_horse1']:
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
            if not map[move[0]][move[1]] or map[move[0]][move[1]] not in red_pieces:
                moves.append((move[0], move[1]))           
    # Get all moves for red chariot
    if piece in ['red_chariot', 'red_chariot1']:
        # Down
        t = 1
        while (i + t) <= 9:
            if not map[i + t][j]: 
                moves.append((i + t, j))
            elif map[i + t][j] in black_pieces:
                moves.append((i + t, j))
                break
            else: break
            t += 1
        # Up
        t = 1
        while (i - t) >= 0:
            if not map[i - t][j]:
                moves.append((i - t, j))
            elif map[i - t][j] in black_pieces:
                moves.append((i - t, j))
                break
            else: break
            t += 1
        # Right
        t = 1
        while(j + t) <= 8:
            if not map[i][j + t]:
                moves.append((i, j + t))
            elif map[i][j + t] in black_pieces:
                moves.append((i, j + t))
                break
            else: break
            t += 1
        # Left
        t = 1
        while(j - t) >= 0:
            if not map[i][j - t]:
                moves.append((i, j - t))
            elif map[i][j - t] in black_pieces:
                moves.append((i, j - t))
                break
            else: break
            t += 1
    # Get all moves for red cannon
    if piece in ['red_cannon', 'red_cannon1']:
        # Down
        t = 1
        f = 0
        while (i + t) <= 9:
            if not map[i + t][j]:
                if f == 0:
                    moves.append((i + t, j))
            elif map[i + t][j] in black_pieces:
                if f == 1:
                    moves.append((i + t, j))
                    break
                else: f += 1
            elif map[i + t][j] in red_pieces: f += 1 
            t += 1
        # Up
        t = 1
        f = 0
        while (i - t) >= 0:
            if not map[i - t][j]:
                if f == 0:
                    moves.append((i - t, j))
            elif map[i - t][j] in black_pieces:
                if f == 1:
                    moves.append((i - t, j))
                    break
                else: f += 1
            elif map[i - t][j] in red_pieces: f += 1 
            t += 1
        # Right
        t = 1
        f = 0
        while(j + t) <= 8:
            if not map[i][j + t]:
                if f == 0:
                    moves.append((i, j + t))
            elif map[i][j + t] in black_pieces:
                if f == 1:
                    moves.append((i, j + t))
                    break
                else: f += 1
            elif map[i][j + t] in red_pieces: f += 1 
            t += 1
        # Left
        t = 1
        f = 0
        while(j - t) >= 0:
            if not map[i][j - t]:
                if f == 0:
                    moves.append((i, j - t))
            elif map[i][j - t] in black_pieces:
                if f == 1:
                    moves.append((i, j - t))
                    break
                else: f += 1
            elif map[i][j - t] in red_pieces: f += 1 
            t += 1
    # Get all moves for black soldier
    if piece in ['black_soldier', 'black_soldier1', 'black_soldier2', 'black_soldier3', 'black_soldier4']:
        if (i + 1) <= 9:
            if map[i + 1][j] not in black_pieces:
                moves.append((i + 1, j))
        if i >= 5:
            if (j - 1) >= 0:
                if map[i][j - 1] not in black_pieces: moves.append((i, j - 1))
            if (j + 1) <= 8:
                if map[i][j + 1] not in black_pieces: moves.append((i, j + 1))
    # Get all moves for black advisor
    if piece in ['black_advisor', 'black_advisor1']:
        potential_black_advisor_moves = [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
        for move in potential_black_advisor_moves:
            if move in black_advisor_moves and map[move[0]][move[1]] not in black_pieces:
                moves.append((move[0], move[1]))
    # Get all moves for black elephant
    if piece in ['black_elephant', 'black_elephant1']:
        voi_moves = [(i - 2, j - 2), (i - 2, j + 2), (i + 2, j - 2), (i + 2, j + 2)]
        voi_blocks = [(i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]
        for i in range(len(voi_moves)):
            if voi_moves[i] in black_elephant_moves and map[voi_moves[i][0]][voi_moves[i][1]] not in black_pieces:
                if not map[voi_blocks[i][0]][voi_blocks[i][1]]:
                    moves.append((voi_moves[i][0], voi_moves[i][1]))
    # Get all move for black general
    if piece == 'black_general':
        tuong_moves = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        for move in tuong_moves:
            if move in black_general_moves and map[move[0]][move[1]] not in black_pieces: 
                moves.append((move[0], move[1]))
        t = 1
        while (i + t) <= 9:
            if not map[i + t][j]: pass
            if map[i + t][j]:
                if map[i + t][j] == 'red_general': 
                    moves.append((i + t, j))
                    break
                else: break
            t += 1
    # Get all moves for black horse
    if piece in ['black_horse', 'black_horse1']:
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
            if not map[move[0]][move[1]] or map[move[0]][move[1]] in red_pieces:
                moves.append((move[0], move[1]))
    # Get all moves for black chariot
    if piece in ['black_chariot', 'black_chariot1']:
        # Down
        t = 1
        while (i + t) <= 9:
            if not map[i + t][j]:
                moves.append((i + t, j))
            elif map[i + t][j] in red_pieces:
                moves.append((i + t, j))
                break
            else: break
            t += 1
        # Up
        t = 1
        while (i - t) >= 0:
            if not map[i - t][j]:
                moves.append((i - t, j))
            elif map[i - t][j] in red_pieces:
                moves.append((i - t, j))
                break
            else: break
            t += 1
        # Right
        t = 1
        while (j + t) <= 8:
            if not map[i][j + t]:
                moves.append((i, j + t))
            elif map[i][j + t] in red_pieces:
                moves.append((i, j + t))
                break
            else: break
            t += 1
        # Left
        t = 1
        while (j - t) >= 0:
            if not map[i][j - t]:
                moves.append((i, j - t))
            elif map[i][j - t] in red_pieces:
                moves.append((i, j - t))
                break
            else: break
            t += 1
    # Get all moves for black cannon
    if piece in ['black_cannon', 'black_cannon1']:
        # Down
        t = 1
        f = 0
        while (i + t) <= 9:
            if not map[i + t][j]:
                if f == 0:
                    moves.append((i + t, j))
            elif map[i + t][j] in red_pieces:
                if f == 1:
                    moves.append((i + t, j))
                    break
                else: f += 1
            elif map[i + t][j] in black_pieces: f += 1
            t += 1
        # Up
        t = 1
        f = 0
        while (i - t) >= 0:
            if not map[i - t][j]:
                if f == 0:
                    moves.append((i - t, j))
            elif map[i - t][j] in red_pieces:
                if f == 1:
                    moves.append((i - t, j))
                    break
                else: f += 1
            elif map[i - t][j] in black_pieces: f += 1
            t += 1
        # Right
        t = 1
        f = 0
        while(j + t) <= 8:
            if not map[i][j + t]:
                if f == 0:
                    moves.append((i, j + t))
            elif map[i][j + t] in red_pieces:
                if f == 1:
                    moves.append((i, j + t))
                    break
                else: f += 1
            elif map[i][j + t] in black_pieces: f += 1            
            t += 1
        # Left
        t = 1
        f = 0
        while(j - t) >= 0:
            if not map[i][j - t]:
                if f == 0:
                    moves.append((i, j - t))
            elif map[i][j - t] in red_pieces:
                if f == 1:
                    moves.append((i, j - t))
                    break
                else: f += 1
            elif map[i][j - t] in black_pieces: f += 1 
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
    if player(turn) == red_pieces: i, j = get_ij('red_general', map)
    if player(turn) == black_pieces: i, j = get_ij('black_general', map)
    # Check for red player
    if player(turn) == red_pieces:
        for piece in black_attacker:
            if on_board(piece, map):
                x, y = get_ij(piece, map)
                if (i, j) in possible_moves(piece, x, y, map):
                    return True
    # Check for black player
    else:
        for piece in red_attacker:
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
    
    if player(turn) == red_pieces:
        text_surface = my_font1.render(f"Black Player Won!", False, (0, 0, 0))
        screen.blit(text_surface, (700, 40))
    else:
        text_surface = my_font1.render(f"Red Player Won!", False, (0, 0, 0))
        screen.blit(text_surface, (710, 40))

    text_surface1 = my_font1.render("Wanna play again?", False, (0, 0, 0))
    yes = my_font1.render("YES", False, (0, 0, 0))
    no = my_font1.render("NO", False, (0, 0, 0))

    screen.blit(text_surface1, (700, 80))
    screen.blit(yes, (735, 130))
    screen.blit(no, (875, 130))

    if yes.get_rect(topleft = (735, 130)).collidepoint(x, y): return True
    if no.get_rect(topleft = (875, 130)).collidepoint(x, y): sys.exit()


# Initialize pygame
pygame.init()
# Initialize pygame text font
pygame.font.init()
my_font1 = pygame.font.SysFont('Comic Sans MS', 30)
my_font = pygame.font.SysFont('Comic Sans MS', 24)
my_font2 = pygame.font.SysFont('Comic Sans MS', 15)
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

    # Copyright text
    copyright_text = my_font2.render("Made by Eric Le | © 2022", False, (0, 0, 0))
    screen.blit(copyright_text, (740, 620))
    
    # Check if game is over
    if end_game(map, turn):

        # Reset game if player choose to play again
        if end_game_question(turn, x, y):       
            map = copy.deepcopy(original_map)
            turn = 0
            render_game(map)
            continue     

    # Print player's turn
    if player(turn) == red_pieces:
        text_turn = my_font.render("Red Player's Turn", False, (0, 0, 0))
        screen.blit(text_turn, (730, 470))
    else:
        text_turn = my_font.render("Black Player's Turn", False, (0, 0, 0))
        screen.blit(text_turn, (720, 470))

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
                screen.blit(dot, (board[i][j][0] - 2, board[i][j][1] - 2))
                screen.blit(active, (board[move[0]][move[1]][0] - 22, board[move[0]][move[1]][1] - 22))
                second_click = False
                turn += 1

            # If second click not on a valid move
            else:
                render_game(map)
                second_click = False

            # If checkmate
            if checkmate(map, turn):
                if player(turn) == red_pieces: m, n = get_ij('red_general', map)
                if player(turn) == black_pieces: m, n = get_ij('black_general', map)
                screen.blit(active, (board[m][n][0] - 22, board[m][n][1] - 22))
                text_checkmate = my_font1.render("CHECKMATE", False, (0, 0, 0))
                screen.blit(text_checkmate, (730, 310))
    
    pygame.display.update()