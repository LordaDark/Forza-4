# Forza 4

Un'implementazione del classico gioco Forza 4 in Python, con un'interfaccia grafica realizzata utilizzando Pygame.

## Struttura del Progetto

Il progetto è organizzato seguendo il pattern MVC (Model-View-Controller):

- `src/`
  - `models/`: Contiene la logica del gioco
  - `views/`: Gestisce l'interfaccia grafica
  - `controllers/`: Gestisce l'interazione tra modello e vista
  - `utils/`: Funzioni di utilità
  - `assets/`: Risorse grafiche e audio

## Requisiti

- Python 3.8 o superiore
- Pygame
- PyInstaller (per creare l'eseguibile)

## Installazione

1. Clona il repository
2. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```

## Esecuzione

Per avviare il gioco:
```bash
python src/main.py
```

## Creazione dell'eseguibile

Per creare un eseguibile standalone:
```bash
pyinstaller src/main.py --onefile --windowed
```

## Come Giocare

1. Il gioco si gioca in due giocatori
2. I giocatori si alternano inserendo le pedine nelle colonne
3. Vince chi riesce a collegare 4 pedine dello stesso colore in orizzontale, verticale o diagonale

## Struttura del Codice

Il codice è organizzato in moduli separati per facilitare la manutenzione e le modifiche:

- `game_model.py`: Gestisce la logica del gioco
- `game_view.py`: Gestisce la visualizzazione
- `game_controller.py`: Gestisce l'input dell'utente e coordina modello e vista
- `constants.py`: Contiene le costanti del gioco
- `utils.py`: Funzioni di utilità generiche