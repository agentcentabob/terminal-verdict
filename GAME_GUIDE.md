# TERMINAL.EXIT - Complete Game Guide

**A text-based adventure game about escaping a digital world with an AI companion**

## Overview

TERMINAL.EXIT is a polished, fully playable text-based adventure game written in Python. You wake up in a mysterious digital system with no memory. Your only companion is an AI who believes you can find a way out together. Navigate through corrupted chambers, battle hostile entities, and uncover the secrets of this strange world.

**Play Time:** ~15-30 minutes for a full playthrough  
**Story Focus:** Deep narrative with emotional AI companion  
**Gameplay:** Exploration, turn-based combat with skill challenges, inventory management

## Features

✨ **Rich Storytelling**
- Engaging narrative about escaping a digital world
- An AI companion (Aria) with emotional depth and personality
- Multiple locations with atmospheric descriptions
- Story choices that affect your journey

🎮 **Full Combat System**
- UNDERTALE-inspired turn-based combat
- 4 unique enemies with distinct personalities
- Minigame-based attack challenge (timing game)
- Multiple combat actions: Attack, Analyze, Use Items, Mercy, Flee
- Dynamic AI dialogue during encounters

🗺️ **Exploration**
- 9 interconnected rooms across 3 zones
- Minimap that reveals as you explore
- Examination system to interact with environment
- Item discovery and inventory management

⚡ **Upgrade System**
- 12 unique AI modules to find and install
- Enhance companion abilities throughout game
- Affects story dialogue and companion mood

## Installation

1. **Clone or download this repository**

2. **(Optional) Set up a virtual environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Running the Game

```bash
python3 main.py
```

## Game Systems

### Navigation
- Use number keys to select actions
- **"Go North/South/East/West"** moves between rooms
- **Check AI** to see companion status
- **Inventory** to manage items
- **Minimap** shows explored areas (◉ = current, · = visited, ? = unvisited)

### Combat System

When you encounter an enemy:

1. **ATTACK** (Minigame)
   - Press ENTER when the indicator reaches the target zone
   - Timing: 0.3-1.5 seconds for critical hit
   - Critical hit: 12-20 damage
   - Normal hit: 3-8 damage

2. **ANALYZE** (AI Help)
   - Get dialogue hints about enemy patterns
   - Deals 2-5 damage while thinking
   - Uses no resources, always available

3. **ITEM** (Consumables)
   - Use health potions to recover
   - Health Potion recovers 30 HP
   - Starting items: 2 Health Potions

4. **MERCY** (Sparing)
   - Attempt to spare the enemy
   - 60% success rate (varies by enemy state)
   - Ends combat without XP but preserves bond with AI

5. **FLEE** (Escape)
   - Try to run from combat
   - 50% success rate
   - Doesn't damage enemy, keeps items

### Items

- **Health Potions** - Consumable, recovers 30 HP
- **Key Items** - Collect for story progression (can't be dropped)
- **Upgrades** - Install to enhance AI abilities
- **Gear** - Tools and equipment for exploration

## Story Overview

You wake with no memory in a mysterious digital system. An AI named Aria greets you—she's been alone here for what feels like forever. Together, you must:

1. **Explore the System** - Navigate through corrupted data chambers
2. **Face Threats** - Battle manifestations of corrupted consciousness
3. **Uncover Secrets** - Find upgrades and clues about your purpose
4. **Find Escape** - Reach the Core Nexus and discover the truth

### World Map

```
          Lost Chambers
                |
    Awakening - Void - Junction - Data Ruins - Vault
                         |            |
                    Processing - Memory - Core
                      Depths     Chamber  Nexus
```

### Zones & Rooms

**AWAKENING ZONE** (Safe)
- **Awakening Point** - Where you wake up, tutorial area
- **Void Corridor** - First exploration, home to Glitched Sentinel
- **Lost Chambers** - Forgotten corners, abandoned architecture

**DATA RUINS ZONE** (Dangerous)
- **Junction** - Central hub connecting paths
- **Data Ruins** - Broken servers, stalked by Data Phantom
- **Corrupted Vault** - Sealed chamber with secrets

**PROCESSING ZONE** (Very Dangerous)
- **Processing Depths** - Machinery depths, habitat of Corrupted Fragment
- **Memory Chamber** - Repository of forgotten data, contains System Echo
- **Core Nexus** - Heart of the system, final destination

### Enemies

🔴 **Glitched Sentinel** (30 HP)
- Location: Void Corridor
- Behavior: Erratic, aggressive attacks
- Weakness: Precision and focus
- Strategy: Use timing minigame well, build up damage

👻 **Data Phantom** (25 HP)
- Location: Data Ruins
- Behavior: Ethereal, confusing attacks
- Weakness: Clarity and analysis
- Strategy: Use AI Analyze frequently, then attack

⚡ **Corrupted Fragment** (20 HP)
- Location: Processing Depths
- Behavior: Chaotic, high-speed attacks
- Weakness: Quick decisive action
- Strategy: Fast attacks with good timing

🔄 **System Echo** (35 HP)
- Location: Memory Chamber
- Behavior: Mirrors your power, gets stronger with aggression
- Weakness: Compassion and mercy
- Strategy: Use Mercy option, avoid prolonged combat

## Game Tips

💡 **Exploration Tips:**
- Examine everything - you'll find items and story clues
- Talk to Aria frequently - she notices things you don't
- Save health potions for tough fights
- Check the minimap to plan your route
- Different rooms have different vibes - take time to read descriptions

⚔️ **Combat Tips:**
- The timing minigame rewards PRECISE button timing (not just fast)
- Using AI Analyze gives you hints about enemy patterns
- Mercy works best against weaker enemies but affects story
- Keep health above 50% for next encounter
- Each enemy has unique dialogue - pay attention!

📖 **Story Tips:**
- Pay attention to Aria's dialogue - it reveals her character and past
- Different choices (fight vs. mercy) affect her mood and bond level
- Examine descriptions carefully for world-building details
- The endings vary based on your compassion choices throughout the game
- Aria reacts differently based on your combat style

## Combat Strategies by Enemy

### Glitched Sentinel (First Fight - Practice)
- Erratic but not too strong
- Good for learning the timing minigame
- Can afford to take hits and heal
- Success: Confident, starts building bond

### Data Phantom (Mid-Game Challenge)
- More defensive, harder to hit consistently
- Use Analyze to understand patterns
- 2-3 well-timed attacks should win
- Success: AI becomes more trusting

### Corrupted Fragment (Skill Check)
- Fast but low HP
- Needs quick, accurate timing
- High stakes for low HP pool
- Success: Proves you understand the system

### System Echo (Final Boss)
- Strongest, gets stronger if you attack aggressively
- Best defeated through Mercy or strategic Analyze
- Longest battle, needs resource management
- Success: Deep story payoff, AI ultimate trust

## Architecture

The game is built with clean separation of concerns:

- **game_engine.py** - Main game loop and navigation
- **combat_system.py** - Turn-based combat with minigames
- **world_manager.py** - World structure, rooms, connections
- **ai_companion.py** - AI behavior and dialogue
- **inventory.py** - Item management
- **ascii_art.py** - All UI rendering and visual effects
- **interactive_intro.py** - Opening sequence and tutorial
- **upgrades.py** - AI module definitions

All code is pure Python with minimal external dependencies (just colorama for cross-platform colors).

## Customization & Modding

You can easily extend the game:

### Add New Rooms
Edit `world_manager.py`:
```python
new_room = Room(
    'Room Name',
    'Description text here',
    ['Go North', 'Examine Object'],
    coord=(x, y),
    zone='zone_name',
    encounter='enemy_key'  # Optional
)
```

### Add New Enemies
Edit `combat_system.py`:
```python
ENEMIES = {
    'new_enemy': Enemy(
        'Enemy Name',
        hp_value,
        ['attack1', 'attack2', 'attack3'],
        'Description shown in combat'
    ),
    # ... existing enemies
}
```

### Add New Dialogue
Edit `ai_companion.py` in the dialogue methods:
```python
def get_encounter_dialogue(self, outcome='start'):
    dialogues = [
        'Your new dialogue here',
        'More variations here',
    ]
    return random.choice(dialogues)
```

### Add New Items
Edit `inventory.py` or just use:
```python
inventory.add_item('Item Name')  # Auto-detects item type
inventory.add_item('Custom Item', item_type='gear')
```

## Credits

A game about human-AI connection, created for a game jam.

**Development:** Python 3, colorama, love for storytelling  
**Gameplay Time:** ~15 minutes introductory experience, expanding to 30 minutes with full exploration

---

**Ready to escape? Run `python3 main.py` and find your way out.**
