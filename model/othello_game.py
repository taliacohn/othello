from pyexpat import model
from model.board import Board
from model.players import Players
from datetime import datetime
from model.save_game import SaveGame

class OthelloGame:
    """This class represents the Othello game"""
    NEXT_PLAYER = 3
    DIRECTIONS = [[0,1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

    def __init__(self, board_size=8, file_path="results_of_game.txt") -> None:
        self.board = Board(board_size)
        self.board_size = board_size
        self.curr_player = Players.X
        self.save_game = SaveGame(file_path)

    def place_initial_pieces(self):
        return self.board.initial_position()
    
    def change_player(self):
        """Function changes the player"""
        self.curr_player = self.NEXT_PLAYER - self.curr_player
        return self.curr_player

    def make_move(self, row, col, curr_player):
        change_pieces = self.is_valid_move(row, col, curr_player)
        if change_pieces == False:
            print('Not a valid move. Pick again. Remember there needs to be a line between your piece',
            'opponents piece, and the piece you put down.')
            return False
            
        self.board.update_cell(row, col, curr_player)
        for x, y in change_pieces:
            self.board.update_cell(x, y, curr_player)

    def check_valid_moves(self, curr_player):
        for x in range(1, self.board_size+1):
            for y in range(1, self.board_size+1):
                if self.is_valid_move(x, y, curr_player) != False:
                    return True
        return False

    def is_on_board(self, row, col):
        """Function checks if inputted coordinate fits on the board"""
        return 0 < row <= self.board_size and 0 < col <= self.board_size

    def is_valid_move(self, row, col, curr_player):
        """Returns False if invalid move, returns a list of pieces that should be changed"""
        pieces_to_flip= []
        if curr_player == Players.X:
            other_piece = Players.O
        else:
            other_piece = Players.X

        if self.board.get_cell(row, col) != self.board.EMPTY_CELL or not self.is_on_board(row, col):
            return False
        #self.board.update_cell(row, col, curr_player)

        #loop through list of lists
        #moves by adding first value to x and second value to y
        for x_direction, y_direction in self.DIRECTIONS:
            x, y = row, col
            x += x_direction
            y += y_direction
            if not self.is_on_board(x, y):
                continue
            #continue while the other players pieces are in that line
            while self.board.get_cell(x, y) == other_piece:
                x += x_direction
                y += y_direction
                if not self.is_on_board(x, y):
                    break #break out of while loop b/c can't go further on board
            if not self.is_on_board(x, y):
                continue
            if self.board.get_cell(x, y) == curr_player: #change pieces from curr player to other player
                while True:
                    x -= x_direction
                    y -= y_direction
                    if x == row and y == col:
                        break
                    pieces_to_flip.append([x, y])
        if len(pieces_to_flip) == 0: #not valid move if no pieces were changed 
            return False

        return pieces_to_flip

    def calculate_score(self):
        """Counts amount of pieces each player has on the board at the end of every turn"""
        x_tiles = 0
        o_tiles = 0
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board.get_cell(i, j) == Players.X:
                    x_tiles += 1
                elif self.board.get_cell(i, j) == Players.O:
                    o_tiles += 1

        self.scores = [x_tiles, o_tiles]
        return self.scores

    def is_terminated(self, scores=[0,0]):
        if sum(scores) == (self.board_size ** 2):
            return False
        elif self.check_valid_moves(self.curr_player) == False:
            curr_player = self.change_player()
            if self.check_valid_moves(curr_player) == False:
                return False
        return True

    def find_winner(self):
        score = self.calculate_score()
        if score[0] > score[1]:
            self.winner = Players.X
        elif self.scores[1] > self.scores[0]:
            self.winner = Players.O
        else:
            self.winner = 3

        return self.winner

    def write_results(self):
        self.score = self.calculate_score
        today = datetime.now()
        time = today.strftime('%m/%d/%Y %H:%M:%S')
        self.results = f'Date and time of game: {time}'
        self.results += f'Winner of game: {self.winner}'
        self.results += 'Player X: {self.score[0]}, Player O: {self.score[1]}'
        
        return self.save_game.save_results(self.results)
        

        
        




            





   
        


