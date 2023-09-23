from pathlib import Path
import os

class GameStats:
    """
    Track statistics for Alien Invasion and loads the high score.
    """

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.score = 0
        self.level = 1
        self.ships_left = self.settings.ship_limit


        # creates high score if not previously written
        # or loads available high score
        self.high_score_path = Path('highscore.txt')
        if os.path.exists(self.high_score_path):
            self.high_score = int(self.high_score_path.read_text())
        else:
            self.high_score = 0
            self.high_score_path.write_text(str(self.high_score))
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.score = 0
        self.ships_left = self.settings.ship_limit