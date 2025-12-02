"""Stub for combat system to be expanded later."""


class CombatEncounter:
    def __init__(self, enemy_name='Corrupted Sentinel'):
        self.enemy_name = enemy_name

    def run(self):
        # Minimal demo: present choices and return a result
        print(f"\nCOMBAT: {self.enemy_name}")
        print('1. Attack')
        print('2. AI Analyze')
        print('3. Mercy')
        ch = input('> ').strip()
        if ch == '3':
            print('You showed mercy. (Demo outcome: success)')
            return 'spared'
        elif ch == '2':
            print('AI analyzes the enemy but this is a stub.')
            return 'analyzed'
        else:
            print('You attack; minimal damage done.')
            return 'attacked'
