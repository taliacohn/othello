from view.board_view import BoardView
from model.board import Board

class BoardConsoleView(BoardView):
    """Prints the initial board with player 1 and 2 in initial positions as X and Y."""
    symbols = {0: ' ', 1: 'X', 2: 'O'}

    def __init__(self, board: Board) -> None:
        super().__init__(board)

    def draw_board(self):
        board_size = self.board.size
        header = '   |'

        for i in range(board_size):
            header += f' {i+1} |'
        
        print(header)

        row_split = ' --+' + '---+'*board_size
        print(row_split)

        for i in range(board_size):
            board = f' {i+1} |'
            for j in range(board_size):
                cell = self.board.get_cell(i+1, j+1)
                board += f' {self.symbols[cell]} |'
            print(board)

            print(row_split)
        




