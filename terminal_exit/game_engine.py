"""Core game loop and navigation for a minimal prototype."""
from .ai_companion import AICompanion
from .ascii_art import render_face, cprint, wait_for_continue, clear_screen, draw_box
from .world_manager import WorldManager
from .inventory import Inventory
from .save_load import SaveLoad
import time


class GameEngine:
    def __init__(self):
        self.ai = AICompanion()
        self.world = WorldManager()
        self.inventory = Inventory()
        self.saver = SaveLoad()
        self.running = True

    def _show_main_menu(self):
        clear_screen()
        draw_box('TERMINAL.EXIT', ['Prototype - minimal demo', '1. New Game', '2. Load Game', '3. Quit'], width=60, color='cyan')

    def _new_game(self):
        clear_screen()
        cprint('\n[BOOT SEQUENCE] You awaken in a dim corridor...', 'white')
        time.sleep(0.3)
        self.ai.speak('happy', "Hello! I'm here to help. Let's explore.")
        wait_for_continue()
        self._explore_loop()

    def _show_cutaway(self, text, ai_mood=None, ai_text=None):
        """Show a focused scene: clear screen, display text, optionally AI dialogue, wait for Enter."""
        clear_screen()
        cprint(text, 'white')
        if ai_mood and ai_text:
            print()
            self.ai.speak(ai_mood, ai_text)
        print()
        wait_for_continue('Press Enter to continue...')

    def _explore_loop(self):
        while True:
            location = self.world.current_room
            # display room with box and minimap
            draw_box(location.name, [location.description], width=60, color='magenta')
            minimap = self.world.render_minimap()
            draw_box('MAP', minimap, width=30, color='blue')
            print('\nActions:')
            for i, opt in enumerate(location.options, start=1):
                print(f"{i}. {opt}")
            print(f"{len(location.options)+1}. Check AI")
            print(f"{len(location.options)+2}. Inventory")
            print(f"{len(location.options)+3}. Return to Main Menu")
            choice = input('> ').strip()
            try:
                ci = int(choice)
            except ValueError:
                self.ai.speak('neutral', "I didn't understand that.")
                continue
            if ci == len(location.options)+1:
                self.ai_status()
            elif ci == len(location.options)+2:
                clear_screen()
                self.inventory.show()
                wait_for_continue()
            elif ci == len(location.options)+3:
                break
            elif 1 <= ci <= len(location.options):
                # very small demo: move or examine
                sel = location.options[ci-1]
                if sel.lower().startswith('go '):
                    direction = sel.split(' ', 1)[1]
                    self.world.move(direction)
                    # Show arrival cutaway
                    new_location = self.world.current_room
                    arrival_msg = f"You go {direction}...\n\n{new_location.description}"
                    self._show_cutaway(arrival_msg, 'happy', f"We've arrived!")
                else:
                    # examination cutaway
                    self._show_cutaway(f"You examine {sel}...\n\nIt's interesting.", 'thinking', 'I\'m analyzing this...')
            else:
                continue

    def ai_status(self):
        clear_screen()
        render_face(self.ai.mood, large=True)
        self.ai.describe()
        print()
        wait_for_continue('Press Enter to return to game...')

    def run(self):
        while self.running:
            self._show_main_menu()
            choice = input('> ').strip()
            if choice == '1':
                self._new_game()
            elif choice == '2':
                state = self.saver.load()
                if state:
                    clear_screen()
                    cprint('Loaded save (minimal demo).', 'green')
                    wait_for_continue()
                else:
                    clear_screen()
                    cprint('No save found.', 'yellow')
                    wait_for_continue()
            elif choice == '3':
                clear_screen()
                cprint('Quitting. Goodbye.', 'white')
                self.running = False
            else:
                continue


def run():
    GameEngine().run()
