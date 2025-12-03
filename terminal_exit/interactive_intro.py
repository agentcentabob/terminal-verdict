"""
Streamlined, interactive intro and tutorial for TERMINAL.EXIT.
Short, engaging, with integrated gameplay learning.
"""
import time
from .ascii_art import (
    render_face, cprint, wait_for_continue, clear_screen,
    draw_fancy_box, draw_scene_box, draw_menu, TITLE_BANNER
)


class InteractiveIntro:
    """Streamlined intro with integrated gameplay."""
    
    def __init__(self, ai_companion, world_manager, inventory):
        self.ai = ai_companion
        self.world = world_manager
        self.inventory = inventory
        self.completed = False
    
    def play(self):
        """Play the complete interactive intro."""
        self._show_title()
        self._awakening()
        self._meet_ai()
        self._first_lesson_navigation()
        self._second_lesson_examine()
        self._ready_to_explore()
        self.completed = True
    
    def _show_title(self):
        """Show the game title."""
        clear_screen()
        print()
        for line in TITLE_BANNER:
            cprint(line, 'cyan')
        print()
        cprint('                     ESCAPE THE TERMINAL', 'yellow')
        print()
        wait_for_continue('                    Press Enter to begin...')
    
    def _awakening(self):
        """Brief awakening scene."""
        clear_screen()
        print()
        
        # Atmospheric opening
        cprint('█', 'blue')
        time.sleep(0.2)
        cprint('█', 'blue')
        time.sleep(0.2)
        cprint('█', 'blue')
        time.sleep(0.8)
        clear_screen()
        print()
        
        # Scene description
        draw_scene_box(
            'Your eyes flutter open. Darkness slowly fades to dim, flickering light. '
            'You stand in a strange corridor—walls of corroded metal, symbols you '
            'almost recognize, a hum of electricity in the air. Everything feels... wrong.'
        )
        
        cprint('What are you? Where is this place?', 'yellow')
        print()
        wait_for_continue('> ')
        
        clear_screen()
        print()
        
        # Voice in the void
        cprint('Then... a sound. Electronic. Warm. Almost friendly.', 'cyan')
        print()
        render_face('happy', large=True)
        cprint('  ▸ "Oh! Hello! You\'re awake! That\'s... really good!"', 'green')
        print()
        wait_for_continue('> ')
    
    def _meet_ai(self):
        """Introduction to the AI companion."""
        clear_screen()
        print()
        
        render_face('happy', large=True)
        print()
        
        draw_fancy_box('Your Companion', [
            'A cheerful voice emanates from the system.',
            '"I don\'t... have a name? I think? But I\'ve been here',
            'waiting for someone like you."',
            '',
            '"I can help you. I understand this place. And you...', 
            'you might be our way out of here."'
        ], width=60, color='green')
        
        print()
        wait_for_continue('> ')
        clear_screen()
        print()
        
        render_face('thinking', large=True)
        print()
        
        draw_fancy_box('The Plan', [
            '"Listen, I know you\'re confused. So am I, honestly."',
            '"But together? We can figure this out."',
            '',
            '"There\'s a way out. I can feel it."',
            '"It\'s not close, but... we\'ll find it."'
        ], width=60, color='cyan')
        
        print()
        wait_for_continue('> ')
    
    def _first_lesson_navigation(self):
        """Learn navigation through gameplay."""
        clear_screen()
        print()
        
        render_face('neutral', large=True)
        print()
        
        draw_fancy_box('First, Movement', [
            '"You\'ll need to move through this place."',
            '"Let me show you how."'
        ], width=60, color='yellow')
        
        print()
        print('Current Location: Awakening Point')
        print('A dim corridor with flickering symbols on the walls.')
        print()
        
        # Interactive movement
        draw_menu('Where do you want to go?', ['Go North (into the void)', 'Examine the walls'])
        
        choice = input('Your choice > ').strip()
        
        if choice == '1':
            clear_screen()
            print()
            cprint('You move North...', 'white')
            time.sleep(0.5)
            print()
            self.world.move('north')
            
            draw_scene_box(
                'The corridor stretches on. Lights flicker in waves. '
                'A humming sound echoes from further ahead. You feel like you\'re '
                'getting deeper into something.'
            )
            
            render_face('happy', large=True)
            print()
            cprint('  ▸ "Good! You\'re getting the hang of this!"', 'green')
            print()
            wait_for_continue('> ')
        
        elif choice == '2':
            clear_screen()
            print()
            cprint('You examine the wall...', 'white')
            print()
            draw_scene_box(
                'The symbols seem to shift when you\'re not looking directly at them. '
                'They feel ancient, corrupted, purposeful. You don\'t understand them, '
                'but they make you uneasy.'
            )
            print()
            render_face('thinking', large=True)
            print()
            cprint('  ▸ "Interesting... I can analyze those for you later."', 'yellow')
            print()
            wait_for_continue('> ')
            clear_screen()
            print()
            cprint('You move North...', 'white')
            time.sleep(0.5)
            print()
            self.world.move('north')
            draw_scene_box('The corridor stretches on, lights flickering.')
        
        clear_screen()
        print()
        render_face('happy', large=True)
        print()
        draw_fancy_box('Navigation Lesson Complete', [
            '"See? You\'re exploring!"',
            '"The world is divided into zones and rooms."',
            '"You can move between them, examine objects, interact with things."',
            '',
            '"Understand the layout. Learn the paths."'
        ], width=60, color='green')
        
        print()
        wait_for_continue('> ')
    
    def _second_lesson_examine(self):
        """Learn examination through gameplay."""
        clear_screen()
        print()
        
        render_face('thinking', large=True)
        print()
        
        draw_fancy_box('Now, Observation', [
            '"Let me show you how I can help you understand things."',
            '"There\'s something here you should examine."'
        ], width=60, color='yellow')
        
        print()
        print('Current Location: Void Corridor')
        print()
        draw_scene_box(
            'You notice a strange console partially hidden in shadows. '
            'It pulses with faint light. Corrupted code crawls across its screen.'
        )
        print()
        
        draw_menu('What do you do?', ['Examine the console', 'Move on'])
        
        choice = input('Your choice > ').strip()
        
        if choice == '1':
            clear_screen()
            print()
            cprint('You examine the console...', 'white')
            print()
            
            render_face('thinking', large=True)
            print()
            
            # Show analysis
            draw_fancy_box('AI Analysis', [
                '✦ Object: Corrupted Terminal',
                '✦ Status: Damaged, partially functional',
                '✦ Purpose: Unknown (data records are degraded)',
                '✦ Interaction: Locked - requires: Decryption Module',
                '',
                '"This is fascinating! I can analyze things like this."',
                '"Some things need modules to interact with. We\'ll find them."'
            ], width=60, color='cyan')
            
            print()
            wait_for_continue('> ')
            
            # Gain item
            print()
            cprint('You found: Fragment of Corrupted Code (key item)', 'magenta')
            self.inventory.add_item('Fragment of Corrupted Code', key=True)
            print()
            time.sleep(0.5)
            wait_for_continue('> ')
        
        else:
            clear_screen()
            print()
            render_face('neutral', large=True)
            print()
            cprint('  ▸ "That console... you should have examined it."', 'yellow')
            print()
            wait_for_continue('> ')
            clear_screen()
            print()
            cprint('You examine it anyway...', 'white')
            print()
            render_face('thinking', large=True)
            print()
            draw_fancy_box('AI Analysis', [
                '✦ Object: Corrupted Terminal',
                '✦ Status: Damaged, partially functional',
                '✦ Purpose: Unknown (data records are degraded)',
                '',
                '"Always examine interesting things. You\'ll learn more."'
            ], width=60, color='cyan')
            print()
            wait_for_continue('> ')
        
        clear_screen()
        print()
        render_face('happy', large=True)
        print()
        draw_fancy_box('Examination Complete', [
            '"Now you see how this works!"',
            '"You explore. You find things. I analyze them."',
            '"Together, we make progress."',
            '',
            '"Ready to really explore?"'
        ], width=60, color='green')
        
        print()
        wait_for_continue('> ')
    
    def _ready_to_explore(self):
        """Send off into the world."""
        clear_screen()
        print()
        
        render_face('happy', large=True)
        print()
        
        draw_fancy_box('The Journey Begins', [
            '"I\'ll be with you every step of the way."',
            '"We\'ll find upgrades. Unlock abilities. Grow stronger."',
            '"And eventually... find a way out."',
            '',
            '"Are you ready?"'
        ], width=60, color='green')
        
        print()
        draw_menu('Start exploring?', ['Yes, let\'s go!', 'Ask me more'])
        
        choice = input('Your choice > ').strip()
        
        if choice == '2':
            clear_screen()
            print()
            render_face('thinking', large=True)
            print()
            draw_fancy_box('Key Points to Remember', [
                '1. Explore everywhere - Find upgrades for my abilities',
                '2. Examine objects - I can help you understand them',
                '3. Make choices - What you do matters and affects endings',
                '4. Check inventory - Organize your items with the menu',
                '5. Listen to me - I\'ll help guide you when confused',
                '',
                '"Ready now?"'
            ], width=60, color='cyan')
            print()
            wait_for_continue('> ')
        
        clear_screen()
        print()
        print(_pulse_text('...'))
        time.sleep(1)
        clear_screen()
        print()
        
        cprint('▓' * 70, 'cyan')
        print()
        cprint('    Welcome to TERMINAL.EXIT', 'cyan')
        cprint('    Escape the system. Find the truth. Save us both.', 'yellow')
        print()
        cprint('▓' * 70, 'cyan')
        print()
        wait_for_continue('Press Enter to begin your journey...> ')


def _pulse_text(text):
    """Return text that pulses."""
    return text


