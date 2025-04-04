import json
import os
from pathlib import Path

class ScoreModel:
    def __init__(self):
        # Ottieni il percorso della directory dei documenti dell'utente
        self.user_docs = str(Path.home() / 'Documents')
        self.game_dir = os.path.join(self.user_docs, 'Forza4')
        self.scores_file = os.path.join(self.game_dir, 'scores.json')
        
        # Crea la directory se non esiste
        if not os.path.exists(self.game_dir):
            os.makedirs(self.game_dir)
        
        # Carica o inizializza i punteggi
        self.scores = self.load_scores()
    
    def load_scores(self):
        """Carica i punteggi dal file JSON."""
        if os.path.exists(self.scores_file):
            try:
                with open(self.scores_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return self.get_default_scores()
        return self.get_default_scores()
    
    def get_default_scores(self):
        """Restituisce la struttura predefinita dei punteggi."""
        return {
            'player1_wins': 0,
            'player2_wins': 0,
            'draws': 0
        }
    
    def save_scores(self):
        """Salva i punteggi nel file JSON."""
        with open(self.scores_file, 'w') as f:
            json.dump(self.scores, f)
    
    def update_score(self, winner):
        """Aggiorna il punteggio in base al risultato della partita."""
        if winner == 'draw':
            self.scores['draws'] += 1
        elif winner == 1:
            self.scores['player1_wins'] += 1
        elif winner == 2:
            self.scores['player2_wins'] += 1
        self.save_scores()
    
    def reset_scores(self):
        """Azzera tutti i punteggi."""
        self.scores = self.get_default_scores()
        self.save_scores()
    
    def get_scores(self):
        """Restituisce i punteggi attuali."""
        return self.scores