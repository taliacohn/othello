from copy import deepcopy
from cmath import inf
from model.rules import Rules

from model.player import Player
from model.symbols import Symbols

class AdvancedAI(Player):
    def __init__(self, symbol: Symbols, board, board_size) -> None:
        super().__init__(symbol, board)
        self.player = Symbols.O
        self.opponent = Symbols.X
        self.rules = Rules(board, board_size)
        
    def choose_move(self, depth: int=2):
        available_moves = self.rules.check_valid_moves(self.player)
        best_value = float(-inf)
        if available_moves:
            for (row, col) in available_moves:
                board_copy = deepcopy(self)
                board_copy.rules.make_move(row, col, self.player)
                board_value = self.minimax(board_copy, depth, self.player, self.opponent)
                if board_value > best_value:
                    best_move = (row, col)
                    best_value = board_value
                
                return best_move
            
        else: 
            return 1

    def minimax(self, board, depth, max_player, min_player): 
        if depth == 0 or self.rules.is_terminated(self.player) == False:
            scores = self.calculate_score()
            max_player = scores[1]
            min_player = scores[0]

            if max_player > min_player:
                return 1
            if min_player > max_player:
                return -1
            if max_player == min_player:
                return 0

        valid_moves = self.rules.check_valid_moves(max_player)
        values = []
        if valid_moves == False:
            return self.minimax(depth, board, min_player, max_player)
        else:
            for (row, col) in valid_moves:
                board_copy = deepcopy(self)
                board_copy.rules.make_move(row, col, max_player)
                board_value = self.minimax(board_copy, depth-1, min_player, max_player) #change player 
                values.append(board_value)
        
            if self.player == max_player:
                return max(values)
            else:
                return min(values)

    def weighted_score(self, row, col):
        """Assigns weights to tiles based on advantage"""
        board_size = self.rules.board_size

        cell_weights = [[5] * board_size for _ in range(board_size)]

        #corners worth more points (row, col)
        cell_weights[0][0] = 20 #top left
        cell_weights[0][board_size-1] = 20 #top right
        cell_weights[board_size-1][0] = 20 #bottom left
        cell_weights[board_size-1][board_size-1] = 20 #bottom right

        #cells surrounding corners are worth less points because they make it easier to capture a corner (row, col)
        cell_weights[0][1] = -10
        cell_weights[1][0] = -10
        cell_weights[1][1] = -10
        cell_weights[board_size-2][0] = -10
        cell_weights[board_size-1][1] = -10
        cell_weights[board_size-2][1] = -10
        cell_weights[0][board_size-2] = -10
        cell_weights[1][board_size-1] = -10
        cell_weights[1][board_size-2] = -10
        cell_weights[board_size-2][board_size-1] = -10
        cell_weights[board_size-1][board_size-2] = -10
        cell_weights[board_size-2][board_size-2] = -10

        #for a larger board size, other spots on borders can be advantageous 
        #on a larger board, the second and second last row make it easier to get to the corners/borders
        for i in range(2, board_size-2):
            for j in range(2, board_size-2):
                cell_weights[i][board_size-1] = 5
                cell_weights[i][0] = 5
                cell_weights[0][j] = 5
                cell_weights[board_size-1][j] = 5

                cell_weights[i][1] = -5
                cell_weights[i][board_size-2] = -5
                cell_weights[board_size-2][j] = -5
                cell_weights[1][j] = -5

        value = cell_weights[row-1][col-1]
        return value


    def calculate_score(self):
        """Heuristic function that assigns weights to each tile based on their advantage.
         score of each tile for each player"""
        x_tiles = 0
        o_tiles = 0
        for i in range(1, self.rules.board_size+1):
            for j in range(1, self.rules.board_size+1):
                if self.rules.board.get_cell(i, j) == Symbols.X:
                    x_tiles += self.weighted_score(i, j)
                elif self.rules.board.get_cell(i, j) == Symbols.O:
                    o_tiles += self.weighted_score(i, j)

        self.scores = [x_tiles, o_tiles]
        return self.scores

            

 