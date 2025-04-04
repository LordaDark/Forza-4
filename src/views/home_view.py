import pygame
from utils.constants import (
    FONT_SIZE, NEON_PURPLE, ELECTRIC_BLUE,
    BLACK, WHITE
)

class HomeView:
    def __init__(self, screen):
        self.screen = screen
        self.title_font = pygame.font.SysFont(None, int(FONT_SIZE * 3))
        self.button_font = pygame.font.SysFont(None, int(FONT_SIZE * 1.5))
        
        # I pulsanti verranno posizionati dinamicamente durante il disegno
        
    def draw(self):
        # Sfondo nero
        self.screen.fill(BLACK)
        
        # Ottieni le dimensioni attuali della finestra
        window_width = self.screen.get_width()
        window_height = self.screen.get_height()
        
        # Titolo con effetto neon
        title_text = self.title_font.render('FORZA 4', True, NEON_PURPLE)
        title_glow = self.title_font.render('FORZA 4', True, ELECTRIC_BLUE)
        
        title_rect = title_text.get_rect(center=(window_width//2, window_height//3))
        glow_rect = title_glow.get_rect(center=(window_width//2 + 2, window_height//3 + 2))
        
        self.screen.blit(title_glow, glow_rect)
        self.screen.blit(title_text, title_rect)
        
        # Calcola le dimensioni dei pulsanti in base alla finestra
        button_width = min(300, window_width - 40)
        button_height = min(60, window_height//10)
        
        # Definizione dinamica dei pulsanti
        play_button = {
            'text': 'GIOCA',
            'rect': pygame.Rect(
                window_width//2 - button_width//2,
                window_height//2,
                button_width,
                button_height
            )
        }
        
        instructions_button = {
            'text': 'ISTRUZIONI',
            'rect': pygame.Rect(
                window_width//2 - button_width//2,
                window_height//2 + button_height + 20,
                button_width,
                button_height
            )
        }
        
        # Pulsanti con effetto hover
        mouse_pos = pygame.mouse.get_pos()
        
        # Disegna i pulsanti
        self._draw_button(play_button, mouse_pos)
        self._draw_button(instructions_button, mouse_pos)
    
    def _draw_button(self, button, mouse_pos):
        hover = button['rect'].collidepoint(mouse_pos)
        color = ELECTRIC_BLUE if hover else NEON_PURPLE
        
        pygame.draw.rect(self.screen, color, button['rect'], border_radius=10)
        pygame.draw.rect(self.screen, color, button['rect'].inflate(4, 4), 2, border_radius=10)
        
        text = self.button_font.render(button['text'], True, WHITE)
        text_rect = text.get_rect(center=button['rect'].center)
        self.screen.blit(text, text_rect)
    
    def handle_click(self, pos):
        """Gestisce i click sui pulsanti."""
        window_width = self.screen.get_width()
        window_height = self.screen.get_height()
        button_width = min(300, window_width - 40)
        button_height = min(60, window_height//10)
        
        # Ricrea i pulsanti per il controllo delle collisioni
        play_rect = pygame.Rect(
            window_width//2 - button_width//2,
            window_height//2,
            button_width,
            button_height
        )
        
        instructions_rect = pygame.Rect(
            window_width//2 - button_width//2,
            window_height//2 + button_height + 20,
            button_width,
            button_height
        )
        
        if play_rect.collidepoint(pos):
            return 'play'
        elif instructions_rect.collidepoint(pos):
            return 'instructions'
        return None