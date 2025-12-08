#!/usr/bin/env python3
"""Quick gameplay validation test."""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from terminal_exit.game_engine import GameEngine
from terminal_exit.combat_system import CombatSystem, ENEMIES
from terminal_exit.world_manager import WorldManager
from terminal_exit.ai_companion import AICompanion
from terminal_exit.inventory import Inventory

def test_startup():
    """Test that game initializes and runs basic gameplay."""
    print("\n" + "="*70)
    print("  GAMEPLAY VALIDATION TEST")
    print("="*70 + "\n")
    
    # Initialize engine
    print("✓ Initializing game engine...")
    engine = GameEngine()
    print(f"  - Starting location: {engine.world.current_room.name}")
    print(f"  - Player HP: {engine.combat.player_hp}/{engine.combat.max_player_hp}")
    print(f"  - AI Companion: {engine.ai.name}")
    
    # Test basic navigation
    print("\n✓ Testing navigation...")
    initial_room = engine.world.current_room.name
    engine.world.move('north')
    next_room = engine.world.current_room.name
    assert next_room != initial_room, "Navigation failed"
    print(f"  - Moved from {initial_room} to {next_room}")
    
    # Test going back
    engine.world.move('south')
    back_room = engine.world.current_room.name
    assert back_room == initial_room, "Reverse navigation failed"
    print(f"  - Returned to {back_room}")
    
    # Navigate to combat
    print("\n✓ Testing combat encounter...")
    engine.world.move('north')
    current = engine.world.current_room
    if current.encounter and not current.encounter_cleared:
        print(f"  - Found encounter: {current.encounter}")
        
        # Check enemy definition
        if current.encounter in ENEMIES:
            enemy_template = ENEMIES[current.encounter]
            print(f"  - Enemy: {enemy_template.name} ({enemy_template.hp} HP)")
            assert hasattr(enemy_template, 'weakness'), "Enemy missing weakness attribute"
            print(f"  - Enemy weakness: {enemy_template.weakness}")
    
    # Test inventory
    print("\n✓ Testing inventory...")
    inv = engine.inventory
    print(f"  - Items in inventory: {len(inv.items)}")
    for item in inv.items:
        print(f"    • {item['name']} ({item['type']})")
    
    # Test AI functionality
    print("\n✓ Testing AI companion...")
    print(f"  - Mood: {engine.ai.mood}")
    print(f"  - Bond level: {engine.ai.bond:.0%}")
    print(f"  - Upgrades: {engine.ai.upgrades}")
    
    # Verify world is fully connected
    print("\n✓ Verifying world connectivity...")
    room_count = 0
    for room_name in engine.world.rooms:
        room = engine.world.rooms[room_name]
        room_count += 1
        # Check each neighbor is bidirectional
        for direction, neighbor_name in room.neighbors.items():
            neighbor = engine.world.rooms[neighbor_name]
            # Find reverse direction
            reverse_found = False
            for rev_dir, rev_name in neighbor.neighbors.items():
                if rev_name == room_name:
                    reverse_found = True
                    break
            assert reverse_found, f"Non-bidirectional: {room_name}-{direction} -> {neighbor_name}"
    print(f"  - {room_count} rooms validated")
    print(f"  - All connections bidirectional ✓")
    
    print("\n" + "="*70)
    print("  ✓ GAMEPLAY VALIDATION COMPLETE")
    print("="*70)
    print("\nGame is ready to play! Run: python3 main.py\n")

if __name__ == '__main__':
    try:
        test_startup()
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}\n")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ UNEXPECTED ERROR: {e}\n")
        import traceback
        traceback.print_exc()
        sys.exit(1)
