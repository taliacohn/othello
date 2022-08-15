from model.board import Board
from model.symbols import Symbols
import random

class Rules:
    NEXT_PLAYER = 3
    DIRECTIONS = [[0,1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    
    def __init__(self, board: Board, board_size) -> None:
        self.board = board
        self.board_size = board_size
        if random.randint(0, 1) == 0:
            self.curr_player = Symbols.X
        else:
            self.curr_player = Symbols.O

    def first_move(self):
        """Chooses which player makes the first move"""
        if random.randint(0, 1) == 0:
            return 1
        else:
            return 2
        
    def make_move(self, row, col, curr_player):
        """Updates the current board by placing the current players new pieces
        and changing any valid pieces"""
        change_pieces = self.is_valid_move(row, col, curr_player)
        if change_pieces == False:
            return False
            
        self.board.update_cell(row, col, curr_player)
        for x, y in change_pieces:
            self.board.update_cell(x, y, curr_player)

    def check_valid_moves(self, curr_player):
        """Checks if move is valid based on current board. Returns False if no valid moves
        available on board or returns list of valid moves"""
        self.valid_moves = []
        for x in range(1, self.board_size+1):
            for y in range(1, self.board_size+1):
                if self.is_valid_move(x, y, curr_player) != False:
                    if (x, y) not in self.valid_moves:
                        self.valid_moves.append([x,y])

        if len(self.valid_moves) == 0:
            return False
        else:
            return self.valid_moves
                    
    def is_on_board(self, row, col):
        """Checks if inputted coordinate fits on the board.
        Returns boolean"""
        return 0 < row <= self.board_size and 0 < col <= self.board_size

    def is_valid_move(self, row, col, curr_player):
        """Returns False if invalid move, or returns a list of pieces that should be changed"""
        pieces_to_change= []
        if curr_player == Symbols.X:
            other_player = Symbols.O
        else:
            other_player = Symbols.X

        if self.board.get_cell(row, col) != self.board.EMPTY_CELL or not self.is_on_board(row, col):
            return False
        #self.board.update_cell(row, col, curr_player)

        #loop through list of lists
        #moves by adding first value to x and second value to y
        for x_direction, y_direction in self.DIRECTIONS:
            new_row, new_col = row, col
            new_row += x_direction
            new_col += y_direction
            # if not self.is_on_board(x, y):
            #     continue
            #continue while the other players pieces are in that line
            while self.is_on_board(new_row, new_col) and self.board.get_cell(new_row, new_col) == other_player:
                new_row += x_direction
                new_col += y_direction
                # if not self.is_on_board(x, y):
                #     break #break out of while loop b/c can't go further on board
            #if not self.is_on_board(new_row, new_col):
                #continue
                if self.is_on_board(new_row, new_col) and self.board.get_cell(new_row, new_col) == curr_player: #change pieces from curr player to other player
                    while new_row != row or new_col != col:
                        new_row -= x_direction
                        new_col -= y_direction
                        pieces_to_change.append([new_row, new_col])
        if len(pieces_to_change) == 0: #not valid move if no pieces were changed 
            return False

        return pieces_to_change

    def calculate_score(self):
        """Counts amount of pieces each player has on the board at the end of every turn"""
        x_tiles = 0
        o_tiles = 0
        for i in range(1, self.board_size+1):
            for j in range(1, self.board_size+1):
                if self.board.get_cell(i, j) == Symbols.X:
                    x_tiles += 1
                elif self.board.get_cell(i, j) == Symbols.O:
                    o_tiles += 1

        self.scores = [x_tiles, o_tiles]
        return self.scores

    def is_terminated(self, curr_player, scores=[0,0]):
        if sum(scores) == (self.board_size ** 2):
            return False
        elif self.check_valid_moves(curr_player) == False:
            curr_player = self.change_player()
            if self.check_valid_moves(curr_player) == False:
                return False
        return True

    def change_player(self):
        """Changes to the next player"""
        self.curr_player = self.NEXT_PLAYER - self.curr_player
        return self.curr_player

    def find_winner(self):
        score = self.calculate_score()
        if score[0] > score[1]:
            self.winner = 1
        elif score[1] > score[0]:
            self.winner = 2
        else:
            self.winner = 3

        return self.winner