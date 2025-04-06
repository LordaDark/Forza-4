# Informazioni sulla versione del gioco

VERSION = '1.0.0'
BUILD_DATE = '2025-04-06 10:58:47'

def get_version():
    """Restituisce la versione corrente del gioco."""
    return VERSION

def get_build_date():
    """Restituisce la data di build dell'eseguibile."""
    return BUILD_DATE

def needs_rebuild():
    """Verifica se è necessario ricreare l'eseguibile."""
    return BUILD_DATE is None  # Se BUILD_DATE è None, significa che stiamo eseguendo il codice sorgente