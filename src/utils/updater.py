import os
import sys
import json
import urllib.request
import subprocess
import winreg
from pathlib import Path
from tkinter import messagebox
from .version import VERSION, get_version

# URL del file JSON che contiene le informazioni sulla versione più recente
UPDATE_INFO_URL = 'https://raw.githubusercontent.com/tuorepository/Forza-4/main/version.json'

def get_startup_path():
    """Ottiene il percorso della cartella Startup di Windows."""
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
    )
    return winreg.QueryValueEx(key, 'Startup')[0]

def add_to_startup():
    """Aggiunge lo script di aggiornamento alla cartella Startup."""
    startup_path = get_startup_path()
    updater_path = os.path.join(startup_path, 'forza4_updater.bat')
    
    # Crea lo script batch per l'aggiornamento
    exe_path = sys.executable
    script_content = f'@echo off\n"{exe_path}" -c "from src.utils.updater import check_for_updates; check_for_updates(True)"'
    
    with open(updater_path, 'w') as f:
        f.write(script_content)

def check_for_updates(silent=False):
    """Controlla se sono disponibili aggiornamenti.
    
    Args:
        silent (bool): Se True, non mostra messaggi all'utente se non ci sono aggiornamenti.
    """
    try:
        # Scarica le informazioni sulla versione più recente
        with urllib.request.urlopen(UPDATE_INFO_URL) as response:
            update_info = json.loads(response.read())
            latest_version = update_info['version']
            download_url = update_info['download_url']
            
            current_version = get_version()
            
            if latest_version > current_version:
                # Notifica l'utente e chiedi se vuole aggiornare
                if messagebox.askyesno(
                    'Aggiornamento disponibile',
                    f'È disponibile una nuova versione di Forza 4 (v{latest_version})!\n\nVuoi installarla ora?'
                ):
                    download_and_install_update(download_url)
            elif not silent:
                messagebox.showinfo('Aggiornamento', 'Il gioco è già aggiornato all\'ultima versione!')
                
    except Exception as e:
        if not silent:
            messagebox.showerror('Errore', f'Errore durante il controllo degli aggiornamenti: {str(e)}')

def download_and_install_update(download_url):
    """Scarica e installa l'aggiornamento."""
    try:
        # Crea una directory temporanea per il download
        temp_dir = Path(os.getenv('TEMP')) / 'forza4_update'
        temp_dir.mkdir(exist_ok=True)
        
        # Scarica il nuovo installer
        installer_path = temp_dir / 'Forza4_Setup.exe'
        urllib.request.urlretrieve(download_url, installer_path)
        
        # Esegui l'installer
        subprocess.Popen([str(installer_path), '/SILENT'])
        
        # Chiudi l'applicazione corrente
        sys.exit(0)
        
    except Exception as e:
        messagebox.showerror('Errore', f'Errore durante l\'aggiornamento: {str(e)}')