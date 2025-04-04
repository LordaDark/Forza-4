# Dimensioni minime della finestra
MIN_WINDOW_WIDTH = 700
MIN_WINDOW_HEIGHT = 600
TITLE = "Forza 4"

# Funzioni per il ridimensionamento dinamico
def get_window_dimensions():
    """Restituisce le dimensioni iniziali della finestra."""
    return MIN_WINDOW_WIDTH, MIN_WINDOW_HEIGHT

# Dimensioni della griglia
ROWS = 6
COLUMNS = 7

# Le dimensioni degli elementi verranno calcolate in base alla dimensione della finestra
def get_cell_size(window_width, window_height):
    return min(window_width // (COLUMNS + 2), window_height // (ROWS + 3))

def get_circle_radius(cell_size):
    return int(cell_size * 0.4)

# Colori (RGB)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BOARD_COLOR = (0, 0, 139)

# Nuovi colori neon
NEON_PURPLE = (255, 0, 255)
ELECTRIC_BLUE = (0, 191, 255)

# Giocatori
PLAYER_1 = 1
PLAYER_2 = 2

# Stato del gioco
GAME_RUNNING = 0
GAME_DRAW = -1

# Messaggi
PLAYER_1_TURN = "Turno del Giocatore 1 (Rosso)"
PLAYER_2_TURN = "Turno del Giocatore 2 (Giallo)"
PLAYER_1_WINS = "Il Giocatore 1 (Rosso) ha vinto!"
PLAYER_2_WINS = "Il Giocatore 2 (Giallo) ha vinto!"
DRAW_MESSAGE = "Pareggio!"
PLAY_AGAIN = "Premi SPAZIO per giocare ancora"

# Font
FONT_SIZE = 32