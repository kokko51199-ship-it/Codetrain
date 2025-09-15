#!/usr/bin/env python3
"""
Simple 2D Game with Level System
Demonstrates the spawning issue in Level 2 where entities spawn in the air
"""

import random
import sys

class Entity:
    """Base class for game entities (player, enemies)"""
    
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.ground_level = 0  # Ground level where entities should spawn
    
    def __str__(self):
        return f"{self.name} at ({self.x}, {self.y})"

class Player(Entity):
    """Player character"""
    
    def __init__(self, x, y):
        super().__init__(x, y, "Player")
        self.health = 100

class Enemy(Entity):
    """Enemy character"""
    
    def __init__(self, x, y):
        super().__init__(x, y, "Enemy")
        self.health = 50

class Level:
    """Base level class"""
    
    def __init__(self, level_number):
        self.level_number = level_number
        self.ground_level = 0
        self.entities = []
        
    def spawn_player(self):
        """Spawn player at starting position"""
        raise NotImplementedError
        
    def spawn_enemies(self, count=3):
        """Spawn enemies"""
        raise NotImplementedError
        
    def display_level(self):
        """Display level information"""
        print(f"\n=== Level {self.level_number} ===")
        print(f"Ground level: {self.ground_level}")
        print("Entities:")
        for entity in self.entities:
            print(f"  {entity}")

class Level1(Level):
    """Level 1 - Working properly, entities spawn on ground"""
    
    def __init__(self):
        super().__init__(1)
        self.ground_level = 0
        
    def spawn_player(self):
        # Correctly spawn player on ground
        player = Player(50, self.ground_level)
        self.entities.append(player)
        return player
        
    def spawn_enemies(self, count=3):
        enemies = []
        for i in range(count):
            # Correctly spawn enemies on ground
            x = random.randint(10, 90)
            enemy = Enemy(x, self.ground_level)
            self.entities.append(enemy)
            enemies.append(enemy)
        return enemies

class Level2(Level):
    """Level 2 - FIXED VERSION: entities now spawn correctly on ground"""
    
    def __init__(self):
        super().__init__(2)
        self.ground_level = 0
        
    def spawn_player(self):
        # FIXED: Player now spawns on ground level
        player = Player(50, self.ground_level)
        self.entities.append(player)
        return player
        
    def spawn_enemies(self, count=3):
        enemies = []
        for i in range(count):
            # FIXED: Enemies now spawn on ground level
            x = random.randint(10, 90)
            enemy = Enemy(x, self.ground_level)
            self.entities.append(enemy)
            enemies.append(enemy)
        return enemies

class Level2Buggy(Level):
    """Level 2 - BUGGY VERSION: entities spawn in the air (kept for demonstration)"""
    
    def __init__(self):
        super().__init__(2)
        self.ground_level = 0
        
    def spawn_player(self):
        # BUG: Player spawns in the air instead of on ground
        # The spawn position is not adjusted for ground level
        player = Player(50, 25)  # Should be ground_level (0), but spawns at 25
        self.entities.append(player)
        return player
        
    def spawn_enemies(self, count=3):
        enemies = []
        for i in range(count):
            # BUG: Enemies also spawn in the air
            x = random.randint(10, 90)
            y = random.randint(15, 30)  # Should be ground_level (0), but spawns randomly in air
            enemy = Enemy(x, y)
            self.entities.append(enemy)
            enemies.append(enemy)
        return enemies

def check_spawning_issues(level):
    """Check if entities are spawning correctly on ground"""
    issues = []
    for entity in level.entities:
        if entity.y != level.ground_level:
            issues.append(f"{entity.name} is spawning in the air at y={entity.y} instead of ground level y={level.ground_level}")
    return issues

def run_game():
    """Main game loop to demonstrate the issue and its fix"""
    print("Starting game to demonstrate Level 2 spawning issue and fix...")
    
    # Level 1 - should work correctly
    level1 = Level1()
    level1.spawn_player()
    level1.spawn_enemies()
    level1.display_level()
    
    issues1 = check_spawning_issues(level1)
    if issues1:
        print("❌ Level 1 Issues:")
        for issue in issues1:
            print(f"  - {issue}")
    else:
        print("✅ Level 1: All entities spawn correctly on ground")
    
    # Level 2 Buggy - demonstrate the original problem
    print("\n--- Demonstrating the original bug ---")
    level2_buggy = Level2Buggy()
    level2_buggy.spawn_player()
    level2_buggy.spawn_enemies()
    level2_buggy.display_level()
    
    issues2_buggy = check_spawning_issues(level2_buggy)
    if issues2_buggy:
        print("❌ Level 2 (Buggy) Issues:")
        for issue in issues2_buggy:
            print(f"  - {issue}")
    else:
        print("✅ Level 2 (Buggy): All entities spawn correctly on ground")
    
    # Level 2 Fixed - should work correctly now
    print("\n--- After the fix ---")
    level2_fixed = Level2()
    level2_fixed.spawn_player()
    level2_fixed.spawn_enemies()
    level2_fixed.display_level()
    
    issues2_fixed = check_spawning_issues(level2_fixed)
    if issues2_fixed:
        print("❌ Level 2 (Fixed) Issues:")
        for issue in issues2_fixed:
            print(f"  - {issue}")
    else:
        print("✅ Level 2 (Fixed): All entities spawn correctly on ground")

if __name__ == "__main__":
    run_game()