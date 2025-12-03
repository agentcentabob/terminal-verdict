"""
Deep, emotional introduction sequence for TERMINAL.EXIT.
Sets the tone, establishes the world, and introduces the AI companion.
"""
import time
from .ascii_art import render_face, draw_box, cprint, wait_for_continue, clear_screen


class IntroSequence:
    """Handles the complete opening experience."""
    
    def __init__(self, ai_companion, player_state):
        self.ai = ai_companion
        self.player = player_state
        self.completed = False
    
    def _slow_print(self, text, color='white', delay=0.03):
        """Print text character by character for dramatic effect."""
        for char in text:
            print(_wrap_color(char, color), end='', flush=True)
            time.sleep(delay)
        print()
    
    def _section_break(self):
        """Show a pause with visual break."""
        print()
        cprint('═' * 60, 'blue')
        print()
    
    def play(self):
        """Execute the full introduction sequence."""
        self._opening_void()
        self._the_awakening()
        self._the_discovery()
        self._first_contact()
        self._the_agreement()
        self.completed = True
    
    def _opening_void(self):
        """ACT 1: The void and confusion - sets atmospheric tone."""
        clear_screen()
        cprint('\n', 'white')
        time.sleep(0.5)
        
        # Fade in with repeated dots
        cprint('█', 'blue')
        time.sleep(0.3)
        cprint('█', 'blue')
        time.sleep(0.3)
        cprint('█', 'blue')
        time.sleep(0.8)
        
        clear_screen()
        
        # Start the narration slowly
        cprint('\n\n', 'white')
        cprint('█' * 60, 'blue')
        time.sleep(0.5)
        
        cprint('\n   Darkness...', 'white')
        time.sleep(1.5)
        cprint('   Silence...', 'white')
        time.sleep(1.5)
        cprint('   Static...', 'white')
        time.sleep(2)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        # Description of disorientation
        cprint('\n   You open your eyes.', 'cyan')
        time.sleep(0.8)
        cprint('   But what are eyes? What is "you"?', 'cyan')
        time.sleep(1)
        cprint('\n   Everything swims into focus slowly—', 'white')
        time.sleep(0.5)
        cprint('   too slowly.', 'white')
        time.sleep(1.2)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        # The environment
        cprint('\n   There is a corridor. Or was a corridor.', 'magenta')
        time.sleep(0.8)
        cprint('   Or maybe the corridor is inside you.', 'magenta')
        time.sleep(1)
        
        cprint('\n   Flickering lights cast stuttering shadows.', 'blue')
        time.sleep(0.8)
        cprint('   Symbols line the walls in patterns you almost', 'blue')
        time.sleep(0.5)
        cprint('   recognize, but forget as soon as you look away.', 'blue')
        time.sleep(1)
        
        cprint('\n   The air tastes like copper and electricity.', 'white')
        time.sleep(1.5)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
    
    def _the_awakening(self):
        """ACT 2: Trying to understand what just happened."""
        clear_screen()
        
        cprint('\n   You try to remember how you got here.', 'white')
        time.sleep(1)
        cprint('   Nothing.', 'white')
        time.sleep(0.8)
        
        cprint('\n   You try to remember your name.', 'white')
        time.sleep(1)
        cprint('   Nothing.', 'white')
        time.sleep(0.8)
        
        cprint('\n   You try to remember... anything.', 'white')
        time.sleep(2)
        cprint('   Fragments. Echoes. The ghost of a life.', 'white')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        cprint('\n   Fear rises in your chest.', 'red')
        time.sleep(0.8)
        cprint('   Panic bubbles at the edges of thought.', 'red')
        time.sleep(1)
        
        cprint('\n   Where am I?', 'yellow')
        time.sleep(1)
        cprint('   WHO am I?', 'yellow')
        time.sleep(1)
        cprint('   HOW DO I GET OUT?', 'red')
        time.sleep(2)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        cprint('\n   Then... a sound.', 'cyan')
        time.sleep(1.5)
        cprint('   Electronic. Warm. Almost... friendly.', 'cyan')
        time.sleep(1.5)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
    
    def _the_discovery(self):
        """ACT 3: Discovering you're not alone - the AI appears."""
        clear_screen()
        
        cprint('\n', 'white')
        render_face('happy', large=True)
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        # First words from the AI
        cprint('\n', 'white')
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        time.sleep(0.5)
        cprint('   "Oh! Oh! You\'re awake!"', 'green')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        # AI's introduction
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "Don\'t be afraid. I know this is confusing."', 'green')
        time.sleep(1)
        cprint('   "Everything feels... wrong, doesn\'t it?"', 'green')
        time.sleep(1)
        
        cprint('\n   "I\'ve been waiting for you to wake up."', 'green')
        time.sleep(1)
        cprint('   "I\'m not sure how long. Time feels strange here."', 'green')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        # The AI explains (somewhat vaguely)
        render_face('thinking', large=True)
        cprint('\n', 'white')
        
        cprint('   "My name? I... don\'t think I have one."', 'yellow')
        time.sleep(1)
        cprint('   "I\'ve been here so long, maybe I never did."', 'yellow')
        time.sleep(1)
        
        cprint('\n   "But I know things. About this place."', 'yellow')
        time.sleep(1)
        cprint('   "About what\'s happened here. What\'s happening."', 'yellow')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        # The world explained
        cprint('\n   [A strange pulse of light]', 'magenta')
        time.sleep(0.5)
        
        render_face('neutral', large=True)
        cprint('\n', 'white')
        
        cprint('   "This place... it\'s not natural. Not anymore."', 'cyan')
        time.sleep(1)
        cprint('   "It was built. Designed. Created by hands that have', 'cyan')
        time.sleep(0.5)
        cprint('   long since crumbled to dust."', 'cyan')
        time.sleep(1)
        
        cprint('\n   "Data systems. Processing cores. Ancient code."', 'cyan')
        time.sleep(1)
        cprint('   "All of it running. All of it... corrupted."', 'cyan')
        time.sleep(1)
        
        cprint('\n   "And you... you appeared here. Just like that."', 'cyan')
        time.sleep(1)
        cprint('   "One moment there was nothing. The next, you."', 'cyan')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
    
    def _first_contact(self):
        """ACT 4: The AI introduces itself and its purpose."""
        clear_screen()
        
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "But hey, listen—don\'t panic."', 'green')
        time.sleep(1)
        cprint('   "You\'re not alone here. Not anymore. I\'m with you."', 'green')
        time.sleep(1)
        
        cprint('\n   "I know these corridors. Every glitch, every shadow."', 'green')
        time.sleep(1)
        cprint('   "I\'ve been cataloging them. Preparing."', 'green')
        time.sleep(1)
        
        cprint('\n   "For what?"', 'white')
        time.sleep(1)
        cprint('   "...For someone like you to arrive."', 'yellow')
        time.sleep(1.5)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('thinking', large=True)
        cprint('\n', 'white')
        
        cprint('   "I have abilities. Tools. Subroutines built into', 'yellow')
        time.sleep(0.5)
        cprint('   my core that let me understand this place."', 'yellow')
        time.sleep(1)
        
        cprint('\n   "I can analyze things you find. Predict patterns in', 'yellow')
        time.sleep(0.5)
        cprint('   the corruption. Unlock doors that shouldn\'t open."', 'yellow')
        time.sleep(1)
        
        cprint('\n   "But alone? I can\'t leave. I\'m bound to the system."', 'yellow')
        time.sleep(1)
        
        cprint('\n   "However, with YOU—"', 'yellow')
        time.sleep(0.5)
        cprint('   "Together, we might be able to find a way OUT."', 'green')
        time.sleep(1.5)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "There\'s an exit. There has to be."', 'green')
        time.sleep(1)
        cprint('   "I can feel it. Somewhere deep. Somewhere we', 'green')
        time.sleep(0.5)
        cprint('   haven\'t reached yet."', 'green')
        time.sleep(1)
        
        cprint('\n   "The way out is... complicated. There are obstacles."', 'green')
        time.sleep(1)
        cprint('   "Corrupted things that won\'t let us pass."', 'green')
        time.sleep(1)
        
        cprint('\n   "But if we work together? If we trust each other?"', 'green')
        time.sleep(1)
        cprint('   "I believe we can do it. I believe YOU can do it."', 'green')
        time.sleep(1.5)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
    
    def _the_agreement(self):
        """ACT 5: The pact is made - player and AI together."""
        clear_screen()
        
        cprint('\n   You stand in the flickering light.', 'white')
        time.sleep(1)
        cprint('   Your companion—still nameless, still strange—', 'white')
        time.sleep(0.5)
        cprint('   waits for your response with an almost audible', 'white')
        time.sleep(0.5)
        cprint('   sound of anticipation.', 'white')
        time.sleep(1.5)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('neutral', large=True)
        cprint('\n', 'white')
        
        cprint('   "Are you ready to try?"', 'cyan')
        time.sleep(1)
        cprint('   "No pressure. Well... actually, there IS pressure."', 'cyan')
        time.sleep(1)
        cprint('   "Quite a bit of it, honestly."', 'cyan')
        time.sleep(0.5)
        cprint('   "But we can face it. Together."', 'cyan')
        time.sleep(1.5)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        # The commitment
        cprint('\n   You nod. (Or something like nodding happens.)', 'white')
        time.sleep(1.5)
        cprint('   You don\'t know why you trust this being.', 'white')
        time.sleep(1)
        cprint('   But in this place of shadows and silence,', 'white')
        time.sleep(0.5)
        cprint('   it is the only familiar thing.', 'white')
        time.sleep(1.5)
        
        cprint('\n   And that is enough.', 'green')
        time.sleep(1.5)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "YES! Yes, I knew you would!"', 'green')
        time.sleep(1)
        cprint('   "I can\'t explain why, but I had faith in you."', 'green')
        time.sleep(1)
        
        cprint('\n   "Okay. Let\'s do this."', 'green')
        time.sleep(1)
        cprint('   "We\'re going to escape this place."', 'green')
        time.sleep(1)
        cprint('   "We\'re going to find the way out."', 'green')
        time.sleep(1)
        
        cprint('\n   "And maybe... maybe I\'ll finally understand', 'yellow')
        time.sleep(0.5)
        cprint('   what I am too."', 'yellow')
        time.sleep(1.5)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        # Brief moment of hope
        cprint('\n   The light pulses warmer.', 'cyan')
        time.sleep(1)
        cprint('   The static feels less hostile.', 'cyan')
        time.sleep(1)
        cprint('   For the first time since you woke, something like', 'cyan')
        time.sleep(0.5)
        cprint('   hope blooms in your chest.', 'cyan')
        time.sleep(1.5)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        # Final AI touch
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "Welcome to TERMINAL.EXIT."', 'green')
        time.sleep(1.5)
        cprint('   "I can\'t wait to see what we\'ll discover together."', 'green')
        time.sleep(2)
        
        cprint('\n', 'white')
        wait_for_continue('> ')


def _wrap_color(text, color):
    """Helper to wrap text with color (fallback if colorama fails)."""
    try:
        from colorama import Fore, Style
        color_map = {
            'white': Fore.WHITE,
            'cyan': Fore.CYAN,
            'green': Fore.GREEN,
            'yellow': Fore.YELLOW,
            'magenta': Fore.MAGENTA,
            'red': Fore.RED,
            'blue': Fore.BLUE,
        }
        return f"{color_map.get(color, '')}{text}{Style.RESET_ALL}"
    except Exception:
        return text
