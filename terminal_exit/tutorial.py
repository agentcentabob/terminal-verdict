"""
Interactive tutorial system for TERMINAL.EXIT.
Teaches game mechanics through narrative and practice.
"""
import time
from .ascii_art import render_face, draw_box, cprint, wait_for_continue, clear_screen


class Tutorial:
    """Handles the post-intro interactive tutorial experience."""
    
    def __init__(self, ai_companion, world_manager, inventory):
        self.ai = ai_companion
        self.world = world_manager
        self.inventory = inventory
        self.completed = False
    
    def play(self):
        """Execute the complete tutorial sequence."""
        self._lesson_1_navigation()
        self._lesson_2_examination()
        self._lesson_3_interaction()
        self._lesson_4_ai_abilities()
        self._lesson_5_inventory()
        self._graduation()
        self.completed = True
    
    def _section_header(self, title):
        """Show a lesson header."""
        clear_screen()
        cprint('\n', 'white')
        cprint('═' * 60, 'yellow')
        cprint(f'  {title}', 'yellow')
        cprint('═' * 60, 'yellow')
        cprint('\n', 'white')
    
    def _lesson_1_navigation(self):
        """Teach navigation through the world."""
        self._section_header('LESSON 1: NAVIGATION')
        
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "Alright! First things first. You can\'t escape if', 'green')
        time.sleep(0.5)
        cprint('   you don\'t know how to move around."', 'green')
        time.sleep(1)
        
        cprint('\n   "This place is divided into zones and rooms."', 'green')
        time.sleep(1)
        cprint('   "Each room has multiple exits—north, south, east, west."', 'green')
        time.sleep(1)
        
        cprint('\n   "You can navigate by choosing a direction or', 'green')
        time.sleep(0.5)
        cprint('   examining objects in the environment."', 'green')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('thinking', large=True)
        cprint('\n', 'white')
        
        cprint('   "I\'ll also show you a mini map in the corner."', 'cyan')
        time.sleep(1)
        cprint('   "It shows your relative position in the zone."', 'cyan')
        time.sleep(1)
        
        cprint('\n   "Watch the map as you move. Understand the layout."', 'cyan')
        time.sleep(1)
        cprint('   "These skills will be crucial later."', 'cyan')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "Ready? Let\'s walk through the Awakening Point."', 'green')
        time.sleep(1)
        cprint('   "I\'ll guide you through each area. Feel free to', 'green')
        time.sleep(0.5)
        cprint('   explore at your own pace!"', 'green')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
    
    def _lesson_2_examination(self):
        """Teach examining the environment."""
        self._section_header('LESSON 2: EXAMINATION')
        
        clear_screen()
        
        cprint('\n   [You move into a small chamber.]', 'magenta')
        time.sleep(1)
        cprint('   [Walls of corroded metal surround you.]', 'magenta')
        time.sleep(1)
        cprint('   [Something glints in the dim light.]', 'magenta')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('thinking', large=True)
        cprint('\n', 'white')
        
        cprint('   "See that? There\'s an object here."', 'yellow')
        time.sleep(1)
        cprint('   "The world is full of things to examine."', 'yellow')
        time.sleep(1)
        
        cprint('\n   "When you examine something, I can analyze it for you."', 'yellow')
        time.sleep(1)
        cprint('   "I might find clues, items, or secrets."', 'yellow')
        time.sleep(1)
        
        cprint('\n   "Try examining different objects as you explore."', 'yellow')
        time.sleep(1)
        cprint('   "I\'ll look for anything that might help us."', 'yellow')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "Some items might be hidden."', 'green')
        time.sleep(1)
        cprint('   "The more you examine, the more you\'ll find."', 'green')
        time.sleep(1)
        
        cprint('\n   "Nothing is random here. Everything means something."', 'green')
        time.sleep(1)
        cprint('   "Look carefully. Think about your choices."', 'green')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
    
    def _lesson_3_interaction(self):
        """Teach interaction and choices."""
        self._section_header('LESSON 3: INTERACTION & CHOICE')
        
        render_face('neutral', large=True)
        cprint('\n', 'white')
        
        cprint('   "This might seem obvious, but it\'s important:"', 'cyan')
        time.sleep(1)
        cprint('   "What you do matters."', 'cyan')
        time.sleep(1)
        
        cprint('\n   "Every decision creates consequences."', 'cyan')
        time.sleep(1)
        cprint('   "Some are immediate. Some reveal themselves later."', 'cyan')
        time.sleep(1)
        
        cprint('\n   "There\'s no \'right\' or \'wrong\' way through this."', 'cyan')
        time.sleep(1)
        cprint('   "But there ARE paths that lead to different endings."', 'cyan')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('thinking', large=True)
        cprint('\n', 'white')
        
        cprint('   "I\'ll try to help guide you, but..."', 'yellow')
        time.sleep(1)
        cprint('   "...sometimes guidance isn\'t enough."', 'yellow')
        time.sleep(1)
        
        cprint('\n   "You\'ll meet entities in here. Some hostile."', 'yellow')
        time.sleep(1)
        cprint('   "Some... more complicated than that."', 'yellow')
        time.sleep(1.5)
        
        cprint('\n   "You\'ll have to decide what to do about them."', 'yellow')
        time.sleep(1)
        cprint('   "Will you fight? Will you mercy? Will you run?"', 'yellow')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "But don\'t worry. Whatever you choose, I\'m here."', 'green')
        time.sleep(1)
        cprint('   "We\'ll face it together."', 'green')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
    
    def _lesson_4_ai_abilities(self):
        """Teach about AI upgrades and abilities."""
        self._section_header('LESSON 4: AI ABILITIES & UPGRADES')
        
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "Now, here\'s something cool about me."', 'green')
        time.sleep(1)
        cprint('   "I\'m not stuck with my current abilities."', 'green')
        time.sleep(1)
        
        cprint('\n   "Throughout our journey, you\'ll find upgrades."', 'green')
        time.sleep(1)
        cprint('   "New modules. Enhanced protocols. Better subroutines."', 'green')
        time.sleep(1)
        
        cprint('\n   "Each upgrade I collect makes me stronger."', 'green')
        time.sleep(1)
        cprint('   "Better at analyzing threats. Better at helping you."', 'green')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('thinking', large=True)
        cprint('\n', 'white')
        
        cprint('   "The upgrades unlock new capabilities:"', 'cyan')
        time.sleep(1)
        
        cprint('\n   • Analysis Modules - Understand enemies better', 'cyan')
        time.sleep(0.7)
        cprint('   • Combat Modules - Support you in battle', 'cyan')
        time.sleep(0.7)
        cprint('   • Utility Modules - Open new areas and doors', 'cyan')
        time.sleep(1)
        
        cprint('\n   "Some upgrades will unlock access to new zones."', 'cyan')
        time.sleep(1)
        cprint('   "Without them, certain paths are sealed off."', 'cyan')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "Your job is to find these upgrades as you explore."', 'green')
        time.sleep(1)
        cprint('   "Together, we\'ll grow stronger. Together, we\'ll go', 'green')
        time.sleep(0.5)
        cprint('   deeper than we\'ve ever gone before."', 'green')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
    
    def _lesson_5_inventory(self):
        """Teach about inventory management."""
        self._section_header('LESSON 5: INVENTORY & ITEMS')
        
        render_face('thinking', large=True)
        cprint('\n', 'white')
        
        cprint('   "You\'ll collect many things on your journey."', 'yellow')
        time.sleep(1)
        cprint('   "Tools. Fragments. Upgrades. Mysteries."', 'yellow')
        time.sleep(1)
        
        cprint('\n   "Your inventory keeps track of them all."', 'yellow')
        time.sleep(1)
        cprint('   "You can check it at any time from the main menu."', 'yellow')
        time.sleep(1)
        
        cprint('\n   "Some items are consumable—use them once, they\'re gone."', 'yellow')
        time.sleep(1)
        cprint('   "Others are permanent tools that can be used again."', 'yellow')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "Key Items are especially important."', 'green')
        time.sleep(1)
        cprint('   "These are tied to the story. You can\'t discard them."', 'green')
        time.sleep(1)
        
        cprint('\n   "And my upgrades?"', 'yellow')
        time.sleep(0.8)
        cprint('   "Once I install them, they\'re part of me forever."', 'yellow')
        time.sleep(1)
        cprint('   "No way to remove them."', 'yellow')
        time.sleep(1)
        
        cprint('\n   "So choose wisely when you share them with me."', 'yellow')
        time.sleep(1.5)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
    
    def _graduation(self):
        """Wrap up the tutorial with encouragement."""
        self._section_header('READY FOR THE REAL JOURNEY')
        
        clear_screen()
        
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "Alright. I think you\'re ready."', 'green')
        time.sleep(1)
        cprint('   "You know the basics. You understand the stakes."', 'green')
        time.sleep(1)
        
        cprint('\n   "Now we begin the real exploration."', 'green')
        time.sleep(1.5)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('neutral', large=True)
        cprint('\n', 'white')
        
        cprint('   "Beyond this point, the world gets stranger."', 'cyan')
        time.sleep(1)
        cprint('   "More dangerous. More meaningful."', 'cyan')
        time.sleep(1)
        
        cprint('\n   "You\'ll encounter things that will test you."', 'cyan')
        time.sleep(1)
        cprint('   "But remember: you\'re not alone. I\'m with you."', 'cyan')
        time.sleep(1)
        
        cprint('\n   "And I believe in you."', 'cyan')
        time.sleep(1.5)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
        
        render_face('happy', large=True)
        cprint('\n', 'white')
        
        cprint('   "Let\'s find our way out of here."', 'green')
        time.sleep(1)
        cprint('   "Let\'s discover what this place really is."', 'green')
        time.sleep(1)
        cprint('   "And maybe... maybe we\'ll discover something about', 'green')
        time.sleep(0.5)
        cprint('   ourselves too."', 'green')
        time.sleep(1.5)
        
        cprint('\n   "Come on. Let\'s go."', 'green')
        time.sleep(1)
        
        cprint('\n', 'white')
        wait_for_continue('> ')
        
        clear_screen()
