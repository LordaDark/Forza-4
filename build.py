import os
import sys
import subprocess
import shutil
from datetime import datetime
import re
import pkg_resources
import pip

def check_dependencies():
    """Verifica se tutte le dipendenze necessarie sono installate e le installa se necessario."""
    dependencies = ['pyinstaller', 'pillow', 'cairosvg']
    all_installed = True
    
    for dep in dependencies:
        try:
            pkg_resources.get_distribution(dep)
        except pkg_resources.DistributionNotFound:
            print(f"\n{dep} non trovato. Installazione in corso...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", dep])
                print(f"{dep} installato con successo!")
            except subprocess.CalledProcessError as e:
                print(f"\nErrore durante l'installazione di {dep}: {e}")
                all_installed = False
    
    return all_installed

def update_version_file(build_date):
    """Aggiorna il file version.py con la data di build corrente."""
    version_file_path = 'src/utils/version.py'
    with open(version_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Aggiorna la data di build
    content = re.sub(
        r'BUILD_DATE = .*',
        f"BUILD_DATE = '{build_date}'",
        content
    )
    
    with open(version_file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def convert_icon():
    """Converte l'icona SVG in ICO se necessario."""
    svg_path = os.path.abspath('src/assets/icon.svg')
    ico_path = os.path.abspath('src/assets/icon.ico')
    
    if not os.path.exists(svg_path):
        print(f"\nAttenzione: L'icona SVG {svg_path} non è stata trovata.")
        return None
    
    try:
        subprocess.check_call([sys.executable, 'convert_icon.py'])
        if os.path.exists(ico_path):
            return ico_path
    except subprocess.CalledProcessError as e:
        print(f"\nErrore durante la conversione dell'icona: {e}")
    except Exception as e:
        print(f"\nErrore inaspettato durante la conversione dell'icona: {e}")
    
    return None

def create_executable():
    """Crea l'eseguibile del gioco utilizzando PyInstaller."""
    if not check_dependencies():
        print("\nImpossibile procedere senza tutte le dipendenze necessarie.")
        sys.exit(1)

    try:
        # Pulisci le directory di build precedenti
        if os.path.exists('build'):
            shutil.rmtree('build')
        if os.path.exists('dist'):
            shutil.rmtree('dist')
        if os.path.exists('Forza4.spec'):
            os.remove('Forza4.spec')
        
        # Aggiorna la data di build nel file version.py
        build_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        update_version_file(build_date)

        # Converti e verifica l'esistenza dell'icona
        icon_path = convert_icon()
        if not icon_path:
            print("\nProcedo senza icona personalizzata.")

        # Verifica l'esistenza del file principale
        main_path = os.path.abspath('src/main.py')
        if not os.path.exists(main_path):
            print(f"\nErrore: Il file principale {main_path} non è stato trovato.")
            sys.exit(1)

        # Comando per creare l'eseguibile
        cmd = [
            sys.executable,
            '-m',
            'PyInstaller',
            '--onefile',  # Crea un singolo file eseguibile
            '--windowed',  # Non mostra la console quando si esegue il gioco
            '--name=Forza4',  # Nome dell'eseguibile
            '--add-data', f'src/assets{os.pathsep}assets',  # Includi le risorse
            '--paths', 'src',  # Aggiungi il percorso sorgente al PYTHONPATH
            main_path
        ]

        # Aggiungi l'icona solo se esiste
        if icon_path:
            cmd.extend(['--icon', icon_path])

        # Esegui PyInstaller
        process = subprocess.run(cmd, capture_output=True, text=True)
        
        if process.returncode != 0:
            print("\nErrore durante l'esecuzione di PyInstaller:")
            print("Output standard:")
            print(process.stdout)
            print("\nOutput di errore:")
            print(process.stderr)
            sys.exit(1)

        print("\nEseguibile creato con successo!")
        print("Puoi trovare l'eseguibile nella cartella 'dist'")

    except subprocess.CalledProcessError as e:
        print(f"\nErrore durante la creazione dell'eseguibile:")
        print("Output standard:")
        print(e.stdout)
        print("\nOutput di errore:")
        print(e.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nErrore inaspettato: {e}")
        sys.exit(1)

def main():
    print("=== Build Forza 4 ===")
    print(f"Inizio processo di build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    create_executable()

if __name__ == '__main__':
    main()