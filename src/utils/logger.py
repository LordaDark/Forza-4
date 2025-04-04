import logging
import os
from datetime import datetime

# Configura il logger
def setup_logger():
    # Crea la directory dei log se non esiste
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Nome del file di log con timestamp
    log_file = os.path.join(log_dir, f'forza4_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')
    
    # Configura il formato del log
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Handler per il file
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    
    # Handler per la console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    # Configura il logger root
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Funzioni di utility per il logging
def log_game_start():
    logging.info('Nuova partita iniziata')

def log_game_end(winner):
    if winner == 'draw':
        logging.info('Partita terminata in pareggio')
    else:
        logging.info(f'Partita terminata. Vincitore: Giocatore {winner}')

def log_move(player, column):
    logging.info(f'Giocatore {player} ha inserito una pedina nella colonna {column}')

def log_window_resize(width, height):
    logging.info(f'Finestra ridimensionata a {width}x{height}')

def log_error(error_msg):
    logging.error(f'Errore: {error_msg}')

def log_state_change(old_state, new_state):
    logging.info(f'Cambio di stato: da {old_state} a {new_state}')