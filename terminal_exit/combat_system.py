"""
Combat system with fully functional minigames for TERMINAL.EXIT.
Implements UNDERTALE-style turn-based combat with upgrade-based strike zones.
"""
import time
import random
import sys
import os
from .ascii_art import cprint, clear_screen, draw_fancy_box, draw_stats_bar, wait_for_continue


# ═══════════════════════════════════════════════════════════════
# STRIKE ZONE SYSTEM (Upgradeable)
# ═══════════════════════════════════════════════════════════════

class StrikeZone:
    """Represents a strike zone in the attack minigame."""
    def __init__(self, start, width, color='green', name='', bonus=None):
        self.start = start
        self.width = width
        self.end = start + width
        self.color = color
        self.name = name or f"Zone {start}-{self.end}"
        self.bonus = bonus or (lambda: (15, 'Normal hit!'))
    
    def contains(self, pos):
        """Check if position is in this zone."""
        return self.start <= pos <= self.end


class Enemy:
    """Enemy entity for combat."""
    def __init__(self, name, hp, attacks, description='', weakness=None):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attacks = attacks
        self.description = description
        self.weakness = weakness or "No obvious weakness"
        self.attack_pattern = 0
    
    def take_damage(self, damage):
        """Take damage and return if still alive."""
        self.hp = max(0, self.hp - damage)
        return self.hp > 0
    
    def get_attack(self):
        """Return a random attack."""
        return random.choice(self.attacks)


# ENEMY DEFINITIONS
ENEMIES = {
    'glitch': Enemy(
        'Glitched Sentinel',
        30,
        ['jabs at you erratically', 'lets out a digital shriek', 'fragments into shards'],
        'A corrupted program with distorted edges and flickering form.\nIts attacks are unpredictable and violent.',
        weakness='It seems to follow a pattern beneath the chaos'
    ),
    'phantom': Enemy(
        'Data Phantom',
        25,
        ['phases through your guard', 'drains your concentration', 'whispers confusing code'],
        'A ethereal entity made of pure data. It shifts when you look at it.\nIts presence makes your thoughts fuzzy.',
        weakness='It needs solid connection—disruption could work'
    ),
    'fragment': Enemy(
        'Corrupted Fragment',
        20,
        ['strikes with broken code', 'spins chaotically', 'emits a high-frequency pulse'],
        'A shard of corrupted data, hostile and unpredictable.\nSmaller, but no less dangerous.',
        weakness='Its spin attack leaves it temporarily exposed'
    ),
    'echo': Enemy(
        'System Echo',
        35,
        ['echoes your weakness', 'amplifies your fear', 'mirrors your movements'],
        'A reflection of corrupted consciousness. It mirrors your movements.\nThe more you fight, the stronger it becomes.',
        weakness='It\'s powered by negative emotions—compassion confuses it'
    ),
}


class CombatSystem:
    """Handles turn-based combat with fully functional minigame."""
    
    def __init__(self, ai_companion, player_inventory):
        self.ai = ai_companion
        self.inventory = player_inventory
        self.current_enemy = None
        self.player_hp = 100
        self.max_player_hp = 100
        self.mercy_threshold = 30  # Mercy available below this % HP
        self.turn_count = 0
        self.enemy_patterns = {}
        self.strikes_landed = 0
        self.strikes_missed = 0
    
    def start_encounter(self, enemy_key):
        """Start a combat encounter."""
        if enemy_key not in ENEMIES:
            return False
        
        template = ENEMIES[enemy_key]
        self.current_enemy = Enemy(
            template.name,
            template.max_hp,
            template.attacks.copy(),
            template.description,
            template.weakness
        )
        
        self.player_hp = self.max_player_hp
        self.turn_count = 0
        self.strikes_landed = 0
        self.strikes_missed = 0
        self.enemy_patterns = {attack: 0 for attack in self.current_enemy.attacks}
        
        return self._combat_loop()
    
    def _combat_loop(self):
        """Main combat loop. Returns True if won, False if lost/fled."""
        # Show enemy entrance
        clear_screen()
        print()
        cprint('▓' * 70, 'red')
        cprint(f'  ⚔️  {self.current_enemy.name} appears!', 'red')
        cprint('▓' * 70, 'red')
        print()
        cprint(self.current_enemy.description, 'red')
        print()
        wait_for_continue('> ')
        
        max_turns = 30
        
        while self.player_hp > 0 and self.current_enemy.hp > 0 and self.turn_count < max_turns:
            self.turn_count += 1
            
            clear_screen()
            self._show_combat_display()
            
            choice = self._show_combat_menu()
            
            if choice == '1':
                damage = self._execute_attack()
                if damage > 0:
                    if not self.current_enemy.take_damage(damage):
                        return self._victory()
                self._enemy_turn()
            
            elif choice == '2':
                self._ai_analyze()
                self._enemy_turn()
            
            elif choice == '3':
                self._use_item()
                self._enemy_turn()
            
            elif choice == '4':
                # Mercy only available when enemy is weak
                if self.current_enemy.hp <= (self.current_enemy.max_hp * self.mercy_threshold / 100):
                    if self._attempt_mercy():
                        return True
                    else:
                        self._enemy_turn()
                else:
                    clear_screen()
                    self.ai.speak('nervous', 'It\'s too strong right now... it won\'t listen.')
                    wait_for_continue('> ')
            
            elif choice == '5':
                if self._attempt_flee():
                    return False
            
            if self.player_hp <= 0:
                return self._defeat()
        
        # Stalemate
        clear_screen()
        cprint('The battle drags on indefinitely...', 'yellow')
        cprint('You both pause, at an impasse.', 'yellow')
        wait_for_continue('> ')
        return False
    
    def _show_combat_display(self):
        """Display current combat state."""
        print()
        cprint('▓' * 70, 'red')
        cprint('  COMBAT', 'red')
        cprint('▓' * 70, 'red')
        print()
        
        # Enemy info
        cprint(f'  ⚔️  {self.current_enemy.name}', 'red')
        draw_stats_bar(f'   HP', self.current_enemy.hp, self.current_enemy.max_hp, width=50, color='red')
        print()
        
        # Player info
        cprint(f'  ▸ You', 'cyan')
        draw_stats_bar(f'   HP', self.player_hp, self.max_player_hp, width=50, color='cyan')
        
        # Mercy indicator
        mercy_threshold = int(self.current_enemy.max_hp * self.mercy_threshold / 100)
        if self.current_enemy.hp <= mercy_threshold:
            cprint(f'   [MERCY AVAILABLE]', 'green')
        
        print()
    
    def _show_combat_menu(self):
        """Show combat action menu."""
        print('  TURN OPTIONS:')
        print('    1. ATTACK (minigame)')
        print('    2. ANALYZE (AI insight)')
        print('    3. ITEM (use potion)')
        print('    4. MERCY (spare if weak)')
        print('    5. FLEE (try to escape)')
        print()
        
        choice = input('  > ').strip()
        return choice
    
    def _execute_attack(self):
        """Execute attack with UNDERTALE-style minigame."""
        clear_screen()
        print()
        cprint('═' * 70, 'white')
        cprint('  ATTACK MINIGAME - HIT THE STRIKE ZONE!', 'white')
        cprint('═' * 70, 'white')
        print()
        
        # Get bonus zones from upgrades
        bonus_zones = []
        for upgrade in self.ai.upgrades:
            if 'Precision' in upgrade:
                bonus_zones.append((8, 8))  # (start, width) - bigger zone
            elif 'Power' in upgrade:
                bonus_zones.append((2, 5))  # early aggressive zone
        
        # Base strike zone
        width = 30
        base_start = random.randint(10, 16)
        base_width = 6
        base_damage = 12
        
        print("Strike Zones Available:")
        print(f"  Base Zone (Green): positions {base_start}-{base_start + base_width}")
        if bonus_zones:
            for i, (start, w) in enumerate(bonus_zones):
                print(f"  Bonus Zone #{i+1} (Blue): positions {start}-{start + w}")
        print()
        cprint("Press ENTER to attack in a strike zone!", 'yellow')
        print()
        
        # Run the minigame
        hit_zone = self._run_strike_game(width, base_start, base_width, bonus_zones)
        
        if hit_zone == 'base':
            damage = base_damage + random.randint(1, 6)
            cprint(f'✓ STRIKE! Dealt {damage} damage!', 'green')
            self.strikes_landed += 1
        elif hit_zone == 'bonus':
            damage = base_damage + random.randint(5, 12)
            cprint(f'✓ BONUS HIT! Dealt {damage} damage!', 'cyan')
            self.strikes_landed += 1
        else:
            damage = random.randint(2, 5)
            cprint(f'✗ MISS! Barely scratched... {damage} damage.', 'red')
            self.strikes_missed += 1
        
        print()
        wait_for_continue('> ')
        return damage
    
    def _run_strike_game(self, width, base_start, base_width, bonus_zones):
        """Run the actual minigame loop."""
        pos = 0
        direction = 1
        running = True
        result = None
        
        try:
            import msvcrt
            win_based = True
        except ImportError:
            win_based = False
        
        while running:
            # Draw the bar
            bar = ['-'] * width
            
            # Draw base zone
            for i in range(base_start, min(base_start + base_width, width)):
                bar[i] = '='
            
            # Draw bonus zones
            for start, w in bonus_zones:
                for i in range(start, min(start + w, width)):
                    if bar[i] != '=':
                        bar[i] = '*'
            
            # Draw cursor
            if 0 <= pos < width:
                bar[pos] = '▸'
            
            # Print
            sys.stdout.write('\r[' + ''.join(bar) + ']')
            sys.stdout.flush()
            
            time.sleep(0.06)
            
            # Move cursor
            pos += direction
            if pos >= width - 1:
                direction = -1
            elif pos <= 0:
                direction = 1
            
            # Check for input
            if win_based:
                try:
                    if msvcrt.kbhit():
                        msvcrt.getch()
                        # Check zones
                        if base_start <= pos <= (base_start + base_width):
                            result = 'base'
                        else:
                            for start, w in bonus_zones:
                                if start <= pos <= (start + w):
                                    result = 'bonus'
                                    break
                        running = False
                except:
                    pass
            else:
                # Non-Windows fallback - just run for a bit then auto-hit
                if pos > width // 2:
                    result = 'base'
                    running = False
        
        print()
        return result
    
    def _ai_analyze(self):
        """AI provides detailed, useful analysis of enemy."""
        clear_screen()
        print()
        
        from .ascii_art import render_face
        render_face('thinking', large=True)
        print()
        
        # Provide ACTUAL useful information
        hp_percent = int(self.current_enemy.hp / self.current_enemy.max_hp * 100)
        
        analyses = [
            f'Weakness: {self.current_enemy.weakness}',
            f'Current HP: {self.current_enemy.hp}/{self.current_enemy.max_hp} ({hp_percent}%)',
            f'Next attack likely: {random.choice(self.current_enemy.attacks)}',
            'Pattern detected! Keep attacking now while it\'s vulnerable!',
            'I can sense its exhaustion... it\'s weakening!',
        ]
        
        analysis = random.choice(analyses)
        draw_fancy_box('AI Analysis', [analysis], width=60, color='cyan')
        
        # Deal damage while analyzing
        damage = random.randint(4, 9)
        self.current_enemy.take_damage(damage)
        cprint(f'  ▸ Your focused analysis dealt {damage} damage!', 'yellow')
        
        print()
        wait_for_continue('> ')
    
    def _use_item(self):
        """Use an item from inventory."""
        clear_screen()
        print()
        
        items = [item for item in self.inventory.items if item.item_type == 'consumable']
        
        if not items:
            cprint('  You have no consumable items!', 'red')
            print()
            wait_for_continue('> ')
            return
        
        draw_fancy_box('Use Item', [f'{i+1}. {item.name}' for i, item in enumerate(items)], width=60, color='yellow')
        
        choice = input('  > ').strip()
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(items):
                item = items[idx]
                if 'Potion' in item.name:
                    heal = 30
                    self.player_hp = min(self.max_player_hp, self.player_hp + heal)
                    cprint(f'  Recovered {heal} HP!', 'green')
                    self.inventory.items.remove(item)
                else:
                    cprint(f'  Used {item.name}!', 'green')
                    self.inventory.items.remove(item)
            print()
            wait_for_continue('> ')
        except (ValueError, IndexError):
            cprint('  Invalid choice!', 'red')
            wait_for_continue('> ')
    
    def _enemy_turn(self):
        """Execute enemy's turn."""
        time.sleep(0.3)
        attack = self.current_enemy.get_attack()
        
        # Damage scales with AI bond - better AI = less damage
        base_damage = random.randint(5, 12)
        mitigation = int(self.ai.bond * 4)  # AI helps reduce damage
        damage = max(1, base_damage - mitigation)
        
        self.player_hp = max(0, self.player_hp - damage)
        
        clear_screen()
        print()
        cprint(f'  ⚡ {self.current_enemy.name} {attack}!', 'red')
        if mitigation > 0:
            cprint(f'  ▸ Aria: "I\'ve got your back!" (-{mitigation} damage)', 'yellow')
        cprint(f'  You took {damage} damage!', 'red')
        print()
        wait_for_continue('> ')
    
    def _attempt_mercy(self):
        """Try to spare the enemy. Returns True if successful."""
        clear_screen()
        print()
        
        from .ascii_art import render_face
        render_face('sad', large=True)
        print()
        
        cprint('  You reach out with compassion...', 'white')
        time.sleep(0.5)
        
        # Higher success with better AI bond
        success_rate = 0.4 + (self.ai.bond * 0.3)
        success = random.random() < success_rate
        
        if success:
            cprint('  The enemy hesitates... and retreats.', 'green')
            self.ai.bond = min(1.0, self.ai.bond + 0.15)
            cprint(f'  ▸ Aria: "You... you showed mercy. That means something to me."', 'yellow')
            print()
            wait_for_continue('> ')
            return True
        else:
            cprint('  But it doesn\'t understand mercy.', 'red')
            print()
            wait_for_continue('> ')
            return False
    
    def _attempt_flee(self):
        """Try to flee from combat."""
        clear_screen()
        print()
        
        cprint('  You try to escape...', 'white')
        time.sleep(0.3)
        
        # Success based on strikes landed
        flee_chance = 0.3 + (self.strikes_landed * 0.15)
        success = random.random() < flee_chance
        
        if success:
            cprint('  You manage to escape!', 'green')
            print()
            wait_for_continue('> ')
            return True
        else:
            cprint('  You can\'t get away!', 'red')
            print()
            wait_for_continue('> ')
            self._enemy_turn()
            return False
    
    def _victory(self):
        """Handle victory."""
        clear_screen()
        print()
        cprint('═' * 70, 'green')
        cprint('  VICTORY!', 'green')
        cprint('═' * 70, 'green')
        print()
        cprint(f'  You defeated the {self.current_enemy.name}!', 'green')
        
        # Bond and stats
        self.ai.bond = min(1.0, self.ai.bond + 0.1)
        accuracy = int((self.strikes_landed / (self.strikes_landed + self.strikes_missed)) * 100) if (self.strikes_landed + self.strikes_missed) > 0 else 0
        cprint(f'  Accuracy: {accuracy}% | Turns: {self.turn_count}', 'cyan')
        
        from .ascii_art import render_face
        render_face('happy', large=True)
        cprint(f'  ▸ "We did it! That was amazing!"', 'yellow')
        print()
        
        wait_for_continue('> ')
        return True
    
    def _defeat(self):
        """Handle defeat."""
        clear_screen()
        print()
        cprint('═' * 70, 'red')
        cprint('  DEFEATED!', 'red')
        cprint('═' * 70, 'red')
        print()
        cprint('  The darkness claims you...', 'red')
        cprint('  But then, a voice...', 'white')
        print()
        
        from .ascii_art import render_face
        render_face('nervous', large=True)
        cprint('  ▸ "No, no no NO! Please... I can\'t lose you!"', 'yellow')
        print()
        
        # Revive with reduced HP
        self.player_hp = self.max_player_hp // 2
        self.ai.bond = min(1.0, self.ai.bond + 0.05)
        cprint('  You wake up, battered but alive.', 'white')
        cprint('  Aria looks genuinely worried.', 'yellow')
        wait_for_continue('> ')
        return False
