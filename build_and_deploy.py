import os
import sys
import subprocess
import json
from datetime import datetime
from git import Repo

def check_nsis_installed():
    """Verifica se NSIS è installato nel sistema."""
    nsis_path = "C:\\Program Files (x86)\\NSIS\\makensis.exe"
    return os.path.exists(nsis_path)

def update_version_json():
    """Aggiorna il file version.json con la nuova versione."""
    version_file = 'version.json'
    if os.path.exists(version_file):
        with open(version_file, 'r') as f:
            version_data = json.load(f)
            current_version = version_data.get('version', '0.0.0')
            # Incrementa la versione patch
            major, minor, patch = map(int, current_version.split('.'))
            new_version = f"{major}.{minor}.{patch + 1}"
    else:
        new_version = '1.0.0'
    
    version_data = {
        'version': new_version,
        'release_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    with open(version_file, 'w') as f:
        json.dump(version_data, f, indent=4)
    
    return new_version

def run_build_script():
    """Esegue lo script build.py per creare l'eseguibile."""
    print("\n=== Creazione dell'eseguibile ===")
    try:
        subprocess.run([sys.executable, 'build.py'], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione di build.py: {e}")
        return False

def create_installer():
    """Crea l'installer usando NSIS."""
    print("\n=== Creazione dell'installer ===")
    if not check_nsis_installed():
        print("NSIS non trovato. Assicurati di averlo installato nel sistema.")
        return False
    
    try:
        subprocess.run(["C:\\Program Files (x86)\\NSIS\\makensis.exe", "installer.nsi"], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Errore durante la creazione dell'installer: {e}")
        return False

def create_git_tag(version):
    """Crea e pusha un nuovo tag Git."""
    try:
        repo = Repo('.')
        new_tag = f'v{version}'
        repo.create_tag(new_tag)
        origin = repo.remote('origin')
        origin.push(new_tag)
        return True
    except Exception as e:
        print(f"Errore durante la creazione del tag Git: {e}")
        return False

def main():
    print("=== Build e Deploy Forza 4 ===")
    print(f"Inizio processo: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Aggiorna la versione
    new_version = update_version_json()
    print(f"\nNuova versione: {new_version}")
    
    # Crea l'eseguibile
    if not run_build_script():
        print("\nErrore durante la creazione dell'eseguibile. Processo interrotto.")
        sys.exit(1)
    
    # Crea l'installer
    if not create_installer():
        print("\nErrore durante la creazione dell'installer. Processo interrotto.")
        sys.exit(1)
    
    # Crea e pusha il tag Git
    if not create_git_tag(new_version):
        print("\nErrore durante la creazione del tag Git. Processo interrotto.")
        sys.exit(1)
    
    print("\n=== Processo completato con successo! ===")
    print("File creati:")
    print("- Eseguibile: dist/Forza4.exe")
    print("- Installer: Forza4_Setup.exe")
    print(f"\nVersione: {new_version}")
    print("Tag Git creato e pushato con successo!")

if __name__ == '__main__':
    main()