import pygame
from models.game_model import GameModel
from views.game_view import GameView
from views.home_view import HomeView
from controllers.game_controller import GameController
from utils.constants import TITLE, get_window_dimensions
from utils.logger import setup_logger, log_game_start, log_game_end, log_move, log_window_resize, log_state_change, log_error
from utils.updater import check_for_updates, add_to_startup

def main():
    # Inizializza il logger
    logger = setup_logger()
    
    # Controlla gli aggiornamenti all'avvio
    check_for_updates()
    
    # Aggiunge lo script di aggiornamento alla cartella Startup
    add_to_startup()
    
    pygame.init()
    initial_width, initial_height = get_window_dimensions()
    screen = pygame.display.set_mode((initial_width, initial_height), pygame.RESIZABLE)
    pygame.display.set_caption(TITLE)
    
    # Inizializza le viste
    home_view = HomeView(screen)
    game_model = GameModel()
    game_view = GameView(screen)
    game_controller = GameController(game_model, game_view)
    
    # Stati del gioco
    MENU = 'menu'
    PLAYING = 'playing'
    INSTRUCTIONS = 'instructions'
    current_state = MENU
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                log_window_resize(event.w, event.h)
                # Aggiorna le viste con il nuovo screen
                home_view = HomeView(screen)
                game_view = GameView(screen)
                game_controller = GameController(game_model, game_view)
            elif event.type == pygame.MOUSEBUTTONDOWN and current_state == MENU:
                action = home_view.handle_click(event.pos)
                if action == 'play':
                    log_state_change(current_state, 'PLAYING')
                    current_state = PLAYING
                    game_model.reset_game()
                    log_game_start()
                elif action == 'instructions':
                    log_state_change(current_state, 'INSTRUCTIONS')
                    current_state = INSTRUCTIONS
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if current_state in [PLAYING, INSTRUCTIONS]:
                    log_state_change(current_state, 'MENU')
                    current_state = MENU
            elif current_state == PLAYING:
                game_controller.handle_event(event)
        
        # Aggiorna la visualizzazione in base allo stato
        if current_state == MENU:
            home_view.draw()
        elif current_state == PLAYING:
            game_view.draw(game_model)
        elif current_state == INSTRUCTIONS:
            # TODO: Implementare la vista delle istruzioni
            screen.fill((0, 0, 0))
            font = pygame.font.SysFont(None, 32)
            text = font.render('Premi ESC per tornare al menu', True, (255, 0, 255))
            screen_width = screen.get_width()
            screen_height = screen.get_height()
            screen.blit(text, (screen_width//2 - text.get_width()//2, screen_height//2))
        
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()