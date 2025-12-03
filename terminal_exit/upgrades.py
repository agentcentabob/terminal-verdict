"""
AI Upgrade system for TERMINAL.EXIT.
Upgrades enhance the AI companion's abilities.
"""


class Upgrade:
    """Represents an AI upgrade/module."""
    
    def __init__(self, name, category, description, ability=None):
        self.name = name
        self.category = category  # 'analysis', 'combat', 'utility', 'progression'
        self.description = description
        self.ability = ability  # Function or ability name


# Available upgrades in the game
UPGRADES = {
    # Analysis Modules
    'scanner': Upgrade(
        'Basic Scanner',
        'analysis',
        'Examine objects and enemies in detail',
        'analyze'
    ),
    'pattern_recognition': Upgrade(
        'Pattern Recognition',
        'analysis',
        'Predict attack patterns in combat',
        'predict'
    ),
    'weakness_detector': Upgrade(
        'Weakness Detector',
        'analysis',
        'Reveal enemy vulnerabilities',
        'detect_weakness'
    ),
    'environmental_analysis': Upgrade(
        'Environmental Analysis',
        'analysis',
        'Understand area hazards and secrets',
        'analyze_area'
    ),
    'corruption_reader': Upgrade(
        'Corruption Reader',
        'analysis',
        'Decrypt hidden messages and corrupted text',
        'decrypt'
    ),
    
    # Combat Modules
    'tactical_advisor': Upgrade(
        'Tactical Advisor',
        'combat',
        'Suggests optimal combat moves',
        'advise'
    ),
    'shield_subroutine': Upgrade(
        'Shield Subroutine',
        'combat',
        'Reduce incoming damage by analyzing attacks',
        'shield'
    ),
    'mercy_protocol': Upgrade(
        'Mercy Protocol',
        'combat',
        'Allow sparing enemies instead of defeating them',
        'mercy'
    ),
    
    # Utility Modules
    'navigation_assist': Upgrade(
        'Navigation Assist',
        'utility',
        'Improved map system and path finding',
        'navigate'
    ),
    'memory_banks': Upgrade(
        'Memory Banks',
        'utility',
        'Store important lore and information',
        'remember'
    ),
    
    # Progression Modules (Gate areas)
    'firewall_bypass': Upgrade(
        'Firewall Bypass',
        'progression',
        'Access restricted zones',
        'bypass_firewall'
    ),
    'data_recovery': Upgrade(
        'Data Recovery',
        'progression',
        'Restore corrupted areas',
        'recover_data'
    ),
}


def get_upgrade(upgrade_id):
    """Get an upgrade by ID."""
    return UPGRADES.get(upgrade_id)


def get_upgrades_by_category(category):
    """Get all upgrades in a category."""
    return [u for u in UPGRADES.values() if u.category == category]
