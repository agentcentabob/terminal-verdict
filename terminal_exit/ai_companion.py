"""AI companion implementation with emoticon states and dialogue helper."""
from .ascii_art import render_face, draw_box, cprint


class AICompanion:
    def __init__(self):
        self.mood = 'happy'
        self.upgrades = []
        self.bond = 0.0

    def set_mood(self, mood):
        self.mood = mood

    def speak(self, mood, text):
        # update mood, render a larger expressive face and framed text
        self.mood = mood
        render_face(mood, large=True)
        draw_box('AI', [text], width=50, color='green')

    def describe(self):
        lines = [f'Current Mood: {self.mood}', f'Upgrades: {len(self.upgrades)}', f'Bond: {int(self.bond*100)}%']
        draw_box('AI STATUS', lines, width=50, color='yellow')
