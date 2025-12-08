"""AI companion implementation with emoticon states and dialogue helper."""
from .ascii_art import render_face, draw_fancy_box, cprint
import random


class AICompanion:
    def __init__(self):
        self.mood = 'happy'
        self.upgrades = []
        self.bond = 0.0
        self.name = "Aria"  # Give the AI a name
        self.dialogue_history = []

    def set_mood(self, mood):
        self.mood = mood

    def speak(self, mood, text):
        """Display AI speaking with face and dialogue."""
        self.mood = mood
        render_face(mood, large=True)
        print()
        draw_fancy_box('AI Companion', [text], width=60, color='green')
        self.dialogue_history.append(text)

    def describe(self):
        """Show AI status."""
        mood_descriptions = {
            'happy': 'Optimistic and energized',
            'neutral': 'Analytical and calm',
            'thinking': 'Processing and learning',
            'nervous': 'Uncertain but determined',
            'sad': 'Concerned and vulnerable'
        }
        
        mood_desc = mood_descriptions.get(self.mood, 'Unknown state')
        
        lines = [
            f'Name: {self.name}',
            f'Mood: {mood_desc}',
            f'Upgrades Installed: {len(self.upgrades)}/12',
            f'Bond Level: {int(self.bond*100)}%',
            '',
            f'"I\'m here with you. Always."'
        ]
        draw_fancy_box('AI STATUS', lines, width=60, color='yellow')
    
    def get_encounter_dialogue(self, outcome='start'):
        """Get contextual dialogue for combat encounters."""
        if outcome == 'start':
            dialogues = [
                'Something\'s coming... brace yourself!',
                'Do you feel that? There\'s something hostile nearby.',
                'I\'m detecting corrupted data patterns. It\'s looking for us.',
                'Stay sharp. We might not be alone here.',
            ]
        elif outcome == 'victory':
            dialogues = [
                'We did it! We actually beat it!',
                'That was incredible! I knew we could do this!',
                'You\'re stronger than I thought. We make a good team.',
                'We\'re getting better at this. Keep going!',
            ]
        elif outcome == 'defeat':
            dialogues = [
                'No... but I won\'t let you fall. Come back with me.',
                'That was too close. Be more careful next time.',
                'Don\'t give up. We\'ll face it again.',
            ]
        else:
            dialogues = [
                'Stay focused. We\'re in this together.',
                'What do you want to do now?',
                'I\'m right here with you.',
            ]
        
        return random.choice(dialogues)
    
    def get_exploration_dialogue(self):
        """Get dialogue for general exploration."""
        dialogues = [
            'I wonder what we\'ll find here...',
            'This place... it\'s starting to feel familiar, almost.',
            'Be careful. Something feels off about this area.',
            'There\'s so much here we don\'t understand yet.',
            'I have a strange feeling about this place.',
            'Stay alert. You never know what\'s around the corner.',
        ]
        return random.choice(dialogues)
