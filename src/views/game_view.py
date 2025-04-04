import pygame
from utils.constants import (
    ROWS, COLUMNS, get_cell_size, get_circle_radius,
    NEON_PURPLE, ELECTRIC_BLUE, BLACK, PLAYER_1, PLAYER_2,
    GAME_RUNNING, GAME_DRAW, PLAYER_1_TURN, PLAYER_2_TURN,
    PLAYER_1_WINS, PLAYER_2_WINS, DRAW_MESSAGE, PLAY_AGAIN,
    FONT_SIZE
)
from models.score_model import ScoreModel

class GameView:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont(None, FONT_SIZE)
        self.score_font = pygame.font.SysFont(None, int(FONT_SIZE * 0.8))
        self.score_model = ScoreModel()
    
    def draw(self, game_model):
        """Disegna lo stato corrente del gioco."""
        self.screen.fill(BLACK)
        
        # Ottieni le dimensioni attuali della finestra
        window_width = self.screen.get_width()
        window_height = self.screen.get_height()
        
        # Calcola le dimensioni della griglia in base alla finestra
        cell_size = get_cell_size(window_width, window_height)
        circle_radius = get_circle_radius(cell_size)
        
        board_width = COLUMNS * cell_size
        board_height = ROWS * cell_size
        board_x = (window_width - board_width) // 2
        board_y = (window_height - board_height) // 2
        
        # Disegna il bordo della griglia con effetto neon
        pygame.draw.rect(self.screen, ELECTRIC_BLUE,
                         (board_x-2, board_y-2, board_width+4, board_height+4))
        pygame.draw.rect(self.screen, BLACK,
                         (board_x, board_y, board_width, board_height))
        
        # Disegna le celle e le pedine
        board = game_model.get_board()
        for row in range(ROWS):
            for col in range(COLUMNS):
                x = board_x + col * cell_size + cell_size // 2
                y = board_y + row * cell_size + cell_size // 2
                
                # Disegna il cerchio con effetto neon
                if board[row][col] == PLAYER_1:
                    color = NEON_PURPLE
                elif board[row][col] == PLAYER_2:
                    color = ELECTRIC_BLUE
                else:
                    # Cerchio vuoto con bordo neon
                    pygame.draw.circle(self.screen, ELECTRIC_BLUE,
                                     (x, y), circle_radius, 2)
                    continue
                
                pygame.draw.circle(self.screen, color,
                                 (x, y), circle_radius)
        
        # Disegna i messaggi di stato
        self.draw_game_status(game_model)
    
    def draw_game_status(self, game_model):
        """Disegna i messaggi di stato del gioco."""
        game_state = game_model.get_game_state()
        message = ""
        
        if game_state == GAME_RUNNING:
            message = PLAYER_1_TURN if game_model.get_current_player() == PLAYER_1 else PLAYER_2_TURN
        elif game_state == GAME_DRAW:
            message = DRAW_MESSAGE
        elif game_state == PLAYER_1:
            message = PLAYER_1_WINS
        elif game_state == PLAYER_2:
            message = PLAYER_2_WINS
        
        # Disegna il messaggio principale
        text_surface = self.font.render(message, True, NEON_PURPLE)
        text_rect = text_surface.get_rect(center=(self.screen.get_width() // 2, 30))
        self.screen.blit(text_surface, text_rect)
        
        # Disegna il messaggio "gioca ancora" e "premi R per azzerare" se il gioco è finito
        if game_state != GAME_RUNNING:
            play_again_surface = self.font.render(PLAY_AGAIN, True, ELECTRIC_BLUE)
            play_again_rect = play_again_surface.get_rect(
                center=(self.screen.get_width() // 2, self.screen.get_height() - 50)
            )
            self.screen.blit(play_again_surface, play_again_rect)
            
            reset_text = "Premi R per azzerare i punteggi"
            reset_surface = self.score_font.render(reset_text, True, ELECTRIC_BLUE)
            reset_rect = reset_surface.get_rect(
                center=(self.screen.get_width() // 2, self.screen.get_height() - 25)
            )
            self.screen.blit(reset_surface, reset_rect)
        
        # Disegna i punteggi
        scores = self.score_model.get_scores()
        score_texts = [
            f"Giocatore 1: {scores['player1_wins']}",
            f"Giocatore 2: {scores['player2_wins']}",
            f"Pareggi: {scores['draws']}"
        ]
        
        for i, text in enumerate(score_texts):
            score_surface = self.score_font.render(text, True, NEON_PURPLE)
            score_rect = score_surface.get_rect(
                topleft=(10, 10 + i * 25)
            )
            self.screen.blit(score_surface, score_rect)
    
    def get_column_at_pos(self, pos_x):
        """Converte la posizione del mouse in un indice di colonna."""
        window_width = self.screen.get_width()
        cell_size = get_cell_size(window_width, self.screen.get_height())
        board_width = COLUMNS * cell_size
        board_x = (window_width - board_width) // 2
        
        if board_x <= pos_x <= board_x + board_width:
            return (pos_x - board_x) // cell_size
        return None