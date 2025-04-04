from utils.constants import ROWS, COLUMNS, PLAYER_1, PLAYER_2, GAME_RUNNING, GAME_DRAW

class GameModel:
    def __init__(self):
        self.reset_game()
    
    def reset_game(self):
        """Resetta il gioco allo stato iniziale."""
        self.board = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]
        self.current_player = PLAYER_1
        self.game_state = GAME_RUNNING
        self.last_move = None
    
    def is_valid_move(self, col):
        """Verifica se è possibile inserire una pedina nella colonna specificata."""
        return 0 <= col < COLUMNS and self.board[0][col] == 0
    
    def get_next_open_row(self, col):
        """Trova la prima riga disponibile nella colonna specificata."""
        for row in range(ROWS-1, -1, -1):
            if self.board[row][col] == 0:
                return row
        return -1
    
    def make_move(self, col):
        """Esegue una mossa nella colonna specificata."""
        if not self.is_valid_move(col) or self.game_state != GAME_RUNNING:
            return False
        
        row = self.get_next_open_row(col)
        self.board[row][col] = self.current_player
        self.last_move = (row, col)
        
        if self.check_win(row, col):
            self.game_state = self.current_player
        elif self.is_board_full():
            self.game_state = GAME_DRAW
        else:
            self.current_player = PLAYER_2 if self.current_player == PLAYER_1 else PLAYER_1
        
        return True
    
    def check_win(self, row, col):
        """Verifica se l'ultima mossa ha portato alla vittoria."""
        player = self.board[row][col]
        
        # Verifica orizzontale
        for c in range(max(0, col-3), min(COLUMNS-3, col+1)):
            if all(self.board[row][c+i] == player for i in range(4)):
                return True
        
        # Verifica verticale
        for r in range(max(0, row-3), min(ROWS-3, row+1)):
            if all(self.board[r+i][col] == player for i in range(4)):
                return True
        
        # Verifica diagonale principale
        for i in range(-3, 1):
            r, c = row + i, col + i
            if 0 <= r <= ROWS-4 and 0 <= c <= COLUMNS-4:
                if all(self.board[r+j][c+j] == player for j in range(4)):
                    return True
        
        # Verifica diagonale secondaria
        for i in range(-3, 1):
            r, c = row + i, col - i
            if 0 <= r <= ROWS-4 and 3 <= c < COLUMNS:
                if all(self.board[r+j][c-j] == player for j in range(4)):
                    return True
        
        return False
    
    def is_board_full(self):
        """Verifica se la griglia è piena."""
        return all(self.board[0][col] != 0 for col in range(COLUMNS))
    
    def get_board(self):
        """Restituisce lo stato attuale della griglia."""
        return self.board
    
    def get_current_player(self):
        """Restituisce il giocatore corrente."""
        return self.current_player
    
    def get_game_state(self):
        """Restituisce lo stato attuale del gioco."""
        return self.game_state