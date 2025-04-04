import os
import shutil
from pathlib import Path

def uninstall():
    try:
        # Rimuovi la directory dei punteggi
        user_docs = str(Path.home() / 'Documents')
        game_dir = os.path.join(user_docs, 'Forza4')
        if os.path.exists(game_dir):
            shutil.rmtree(game_dir)
            print("✓ Dati di gioco rimossi con successo")
        
        # Rimuovi l'eseguibile e i file di gioco
        current_dir = os.path.dirname(os.path.abspath(__file__))
        dist_dir = os.path.join(current_dir, 'dist')
        if os.path.exists(dist_dir):
            shutil.rmtree(dist_dir)
            print("✓ File di gioco rimossi con successo")
        
        # Rimuovi la directory build
        build_dir = os.path.join(current_dir, 'build')
        if os.path.exists(build_dir):
            shutil.rmtree(build_dir)
            print("✓ File di build rimossi con successo")
        
        print("\nDisinstallazione completata con successo!")
        input("\nPremi INVIO per chiudere...")
        
    except Exception as e:
        print(f"\nErrore durante la disinstallazione: {str(e)}")
        input("\nPremi INVIO per chiudere...")

if __name__ == '__main__':
    print("=== Disinstallazione Forza 4 ===")
    print("\nQuesta operazione rimuoverà il gioco e tutti i dati salvati.")
    conferma = input("\nVuoi procedere con la disinstallazione? (s/n): ")
    
    if conferma.lower() == 's':
        uninstall()
    else:
        print("\nDisinstallazione annullata.")
        input("\nPremi INVIO per chiudere...")