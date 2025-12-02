"""Dialogue manager (simple branching placeholders)."""


class DialogueManager:
    def __init__(self):
        self.lines = {}

    def add(self, key, text):
        self.lines[key] = text

    def speak(self, key):
        return self.lines.get(key, '')
