"""AI companion implementation with emoticon states and dialogue helper."""
from .ascii_art import render_face, draw_fancy_box, cprint


class AICompanion:
    def __init__(self):
        self.mood = 'happy'
        self.upgrades = []
        self.bond = 0.0

    def set_mood(self, mood):
        self.mood = mood

    def speak(self, mood, text):
        """Display AI speaking with face and dialogue."""
        self.mood = mood
        render_face(mood, large=True)
        print()
        draw_fancy_box('AI Companion', [text], width=60, color='green')

    def describe(self):
        """Show AI status."""
        lines = [
            f'Mood: {self.mood.upper()}',
            f'Upgrades Installed: {len(self.upgrades)}/12',
            f'Bond Level: {int(self.bond*100)}%'
        ]
        draw_fancy_box('AI STATUS', lines, width=60, color='yellow')

