"""Core game loop and navigation for a minimal prototype."""
from .ai_companion import AICompanion
from .ascii_art import (render_face, cprint, wait_for_continue,
                        clear_screen, draw_fancy_box, draw_menu,
                        draw_location_box)
from .world_manager import WorldManager
from .inventory import Inventory
from .save_load import SaveLoad
from .interactive_intro import InteractiveIntro
from .combat_system import CombatSystem
import time
import random


class GameEngine:
    def __init__(self):
        self.ai = AICompanion()
        self.world = WorldManager()
        self.inventory = Inventory()
        self.combat = CombatSystem(self.ai, self.inventory)
        self.saver = SaveLoad()
        self.running = True
        self.player_state = {
            'intro_seen': False,
            'tutorial_completed': False,
            'location': 'awakening_point',
        }

    def _show_main_menu(self):
        clear_screen()
        print()
        draw_fancy_box('TERMINAL.EXIT', [
            'A text-based escape adventure',
            '',
            'Navigate through a mysterious digital world',
            'Guided by an AI companion',
            'Uncover secrets. Make choices. Find escape.'
        ], width=60, color='cyan')
        print()
        draw_menu('Main Menu', ['New Game', 'Load Game', 'Quit'], width=50, color='yellow')

    def _new_game(self):
        """Start a new game with interactive intro."""
        intro = InteractiveIntro(self.ai, self.world, self.inventory)
        intro.play()
        
        self.player_state['intro_seen'] = True
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

    def _begin_exploration(self):
        """Start the main exploration phase after intro/tutorial."""
        clear_screen()
        cprint('\n', 'white')
        cprint('═' * 60, 'cyan')
        cprint('  THE EXPLORATION BEGINS', 'cyan')
        cprint('═' * 60, 'cyan')
        cprint('\n', 'white')
        
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "Okay! Time to really explore. Stay alert, and remember—', 'green')
        time.sleep(0.5)
        cprint('   no matter what we find, we\'re in this together."', 'green')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('Press Enter to begin...> ')

    def _explore_loop(self):
        """Main exploration loop with combat integration."""
        while True:
            location = self.world.current_room
            
            # Check for encounter (only once per room)
            if location.encounter and not location.encounter_cleared:
                clear_screen()
                render_face('nervous', large=True)
                cprint(f'\n  "Wait... I sense something in this area!"', 'yellow')
                wait_for_continue('> ')
                
                # Run combat
                victory = self.combat.start_encounter(location.encounter)
                location.encounter_cleared = True
                
                if victory:
                    self.ai.set_mood('happy')
                    clear_screen()
                    cprint('You take a moment to catch your breath.', 'white')
                    wait_for_continue('> ')
                else:
                    # Lost or fled
                    clear_screen()
                    cprint('You need to regroup...', 'yellow')
                    wait_for_continue('> ')
                
                # Continue exploration after combat
                continue
            
            # Display location with fancy UI
            print()
            draw_location_box(location.name, location.description,
                              width=80, color='magenta')
            
            minimap = self.world.render_minimap()
            draw_fancy_box('MAP', minimap, width=30, color='blue')
            
            print('EXPLORATION ACTIONS:')
            for i, opt in enumerate(location.options, start=1):
                print(f"  {i}. {opt}")
            print(f"  {len(location.options)+1}. Check AI Status")
            print(f"  {len(location.options)+2}. Inventory")
            print(f"  {len(location.options)+3}. Return to Main Menu")
            print()
            print('MOVEMENT: Type "up", "down", "left", or "right" to move')
            print()
            
            choice = input('> ').strip().lower()
            
            # Check if input is a direction
            if choice in ['up', 'down', 'left', 'right']:
                success, msg, new_room = self.world.move(choice)
                if success:
                    self._show_cutaway(
                        f"{msg}\n\n{new_room.description}",
                        'happy',
                        "We've arrived!"
                    )
                else:
                    clear_screen()
                    cprint(msg, 'yellow')
                    wait_for_continue('> ')
                continue
            
            # Otherwise try to parse as numeric choice
            try:
                ci = int(choice)
            except ValueError:
                clear_screen()
                msg = "I didn't understand that. Use up/down/left/right " \
                      "to move, or enter a number."
                self.ai.speak('neutral', msg)
                wait_for_continue('> ')
                continue
            
            if ci == len(location.options)+1:
                # Check AI status
                self.ai_status()
            
            elif ci == len(location.options)+2:
                # Show inventory
                clear_screen()
                self.inventory.show()
                wait_for_continue()
            
            elif ci == len(location.options)+3:
                # Return to menu
                clear_screen()
                cprint('\n"Until next time..."', 'yellow')
                time.sleep(0.5)
                break
            
            elif 1 <= ci <= len(location.options):
                # Handle location action (examine, interact, etc.)
                sel = location.options[ci-1]
                self._show_cutaway(
                    f"You examine {sel}...\n\nIt's interesting.",
                    'thinking',
                    'I\'m analyzing this...'
                )
            
            else:
                clear_screen()
                cprint('Invalid choice. Try again.', 'yellow')
                wait_for_continue('> ')
                continue

    def ai_status(self):
        """Display AI status with upgrade installation interface."""
        while True:
            clear_screen()
            render_face(self.ai.mood, large=True)
            self.ai.describe()
            print()
            
            # Get available upgrades from inventory
            available_upgrades = [
                item for item in self.inventory.items
                if item.item_type == 'upgrade'
            ]
            
            if available_upgrades:
                print('AVAILABLE UPGRADES:')
                for i, upgrade in enumerate(available_upgrades, 1):
                    print(f'  {i}. {upgrade.name}')
                    print(f'     {upgrade.desc}')
                print()
                print('  0. Return to Game')
                print()
                
                choice = input('  > ').strip()
                
                if choice == '0':
                    break
                
                try:
                    idx = int(choice) - 1
                    if 0 <= idx < len(available_upgrades):
                        selected = available_upgrades[idx]
                        self._install_upgrade(selected)
                    else:
                        continue
                except ValueError:
                    continue
            else:
                msg = 'No upgrades available yet. Defeat enemies!'
                print(msg)
                print()
                wait_for_continue('Press Enter to return...')
                break
    
    def _install_upgrade(self, upgrade_item):
        """Install an upgrade to the AI companion."""
        clear_screen()
        print()
        render_face('happy', large=True)
        print()
        cprint(f'Installing: {upgrade_item.name}', 'cyan')
        cprint(f'{upgrade_item.desc}', 'white')
        print()
        
        # Add to AI upgrades and inventory
        self.ai.upgrades.append(upgrade_item.name)
        self.inventory.items.remove(upgrade_item)
        
        # Increase bond
        self.ai.bond = min(1.0, self.ai.bond + 0.05)
        
        # AI dialogue
        dialogues = [
            f'I can feel the {upgrade_item.name} integrating!',
            'This is amazing! Thank you for this upgrade!',
            f'I feel stronger with the {upgrade_item.name}!',
            'This will help us on our journey!',
        ]
        
        self.ai.speak('happy', random.choice(dialogues))
        
        print()
        wait_for_continue('> ')

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
