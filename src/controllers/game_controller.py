import pygame
from utils.constants import GAME_RUNNING, GAME_DRAW
from utils.logger import log_move, log_game_end, log_state_change
from models.score_model import ScoreModel

class GameController:
    def __init__(self, game_model, game_view):
        self.model = game_model
        self.view = game_view
        self.score_model = ScoreModel()
        self.current_state = 'PLAYING'
    
    def handle_event(self, event):
        """Gestisce gli eventi di input dell'utente."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Gestisce il click del mouse per inserire una pedina
            if self.model.get_game_state() == GAME_RUNNING:
                mouse_pos = pygame.mouse.get_pos()
                col = self.view.get_column_at_pos(mouse_pos[0])
                
                if col is not None:
                    current_player = self.model.get_current_player()
                    self.model.make_move(col)
                    log_move(current_player, col)
                    
                    # Controlla se il gioco è finito dopo la mossa
                    game_state = self.model.get_game_state()
                    if game_state != GAME_RUNNING:
                        if game_state == GAME_DRAW:
                            log_game_end('draw')
                            self.score_model.update_score('draw')
                        else:
                            log_game_end(game_state)
                            self.score_model.update_score(game_state)
        
        elif event.type == pygame.KEYDOWN:
            # Resetta il gioco quando si preme SPAZIO
            if event.key == pygame.K_SPACE and self.model.get_game_state() != GAME_RUNNING:
                self.model.reset_game()
            # Resetta i punteggi quando si preme R
            elif event.key == pygame.K_r:
                self.score_model.reset_scores()
            # Torna al menu principale quando si preme ESC
            elif event.key == pygame.K_ESCAPE:
                log_state_change(self.current_state, 'MENU')
                return 'MENU'
    
    def update(self):
        """Aggiorna lo stato del gioco."""
        # Al momento non ci sono aggiornamenti automatici da gestire
        # Ma questa funzione potrebbe essere utile per future espansioni
        # come animazioni o timer
        pass