#!/usr/bin/env python3
"""
Unit tests for the game spawning system
Tests to verify that the Level 2 spawning issue has been fixed
"""

import unittest
import sys
import os

# Add the current directory to Python path to import game module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from game import Level1, Level2, Level2Buggy, check_spawning_issues

class TestSpawning(unittest.TestCase):
    """Test cases for entity spawning"""
    
    def test_level1_spawning(self):
        """Test that Level 1 spawning works correctly"""
        level = Level1()
        
        # Test player spawning
        player = level.spawn_player()
        self.assertEqual(player.y, level.ground_level, 
                        "Player should spawn at ground level")
        
        # Test enemy spawning
        enemies = level.spawn_enemies(5)
        for enemy in enemies:
            self.assertEqual(enemy.y, level.ground_level,
                           f"Enemy {enemy.name} should spawn at ground level")
        
        # Test no spawning issues
        issues = check_spawning_issues(level)
        self.assertEqual(len(issues), 0, 
                        f"Level 1 should have no spawning issues, but found: {issues}")
    
    def test_level2_fixed_spawning(self):
        """Test that Level 2 (fixed version) spawning works correctly"""
        level = Level2()
        
        # Test player spawning
        player = level.spawn_player()
        self.assertEqual(player.y, level.ground_level,
                        "Player should spawn at ground level")
        
        # Test enemy spawning
        enemies = level.spawn_enemies(5)
        for enemy in enemies:
            self.assertEqual(enemy.y, level.ground_level,
                           f"Enemy {enemy.name} should spawn at ground level")
        
        # Test no spawning issues
        issues = check_spawning_issues(level)
        self.assertEqual(len(issues), 0,
                        f"Level 2 (fixed) should have no spawning issues, but found: {issues}")
    
    def test_level2_buggy_spawning(self):
        """Test that Level 2 (buggy version) demonstrates the original problem"""
        level = Level2Buggy()
        
        # Test player spawning - should be buggy
        player = level.spawn_player()
        self.assertNotEqual(player.y, level.ground_level,
                           "Buggy version should spawn player above ground")
        
        # Test enemy spawning - should be buggy
        enemies = level.spawn_enemies(3)
        for enemy in enemies:
            self.assertNotEqual(enemy.y, level.ground_level,
                              f"Buggy version should spawn enemy {enemy.name} above ground")
        
        # Test that spawning issues exist
        issues = check_spawning_issues(level)
        self.assertGreater(len(issues), 0,
                          "Level 2 (buggy) should have spawning issues")
        self.assertGreaterEqual(len(issues), 4,  # Player + at least 3 enemies
                               "Should have issues for player and all enemies")
    
    def test_spawning_consistency(self):
        """Test that fixed version consistently spawns entities correctly"""
        # Run multiple times to ensure consistency
        for i in range(10):
            level = Level2()
            level.spawn_player()
            level.spawn_enemies(3)
            
            issues = check_spawning_issues(level)
            self.assertEqual(len(issues), 0,
                           f"Iteration {i+1}: Level 2 should consistently have no spawning issues")
    
    def test_ground_level_property(self):
        """Test that ground level is correctly set"""
        level1 = Level1()
        level2 = Level2()
        level2_buggy = Level2Buggy()
        
        self.assertEqual(level1.ground_level, 0, "Level 1 ground level should be 0")
        self.assertEqual(level2.ground_level, 0, "Level 2 ground level should be 0")
        self.assertEqual(level2_buggy.ground_level, 0, "Level 2 buggy ground level should be 0")

class TestGameIntegration(unittest.TestCase):
    """Integration tests for the complete game system"""
    
    def test_entities_count(self):
        """Test that correct number of entities are spawned"""
        level = Level2()
        
        # Initially no entities
        self.assertEqual(len(level.entities), 0, "Level should start with no entities")
        
        # Spawn player
        level.spawn_player()
        self.assertEqual(len(level.entities), 1, "Should have 1 entity after spawning player")
        
        # Spawn enemies
        enemy_count = 5
        level.spawn_enemies(enemy_count)
        self.assertEqual(len(level.entities), 1 + enemy_count,
                        f"Should have {1 + enemy_count} entities after spawning")
    
    def test_entity_positions_within_bounds(self):
        """Test that entities spawn within reasonable bounds"""
        level = Level2()
        level.spawn_player()
        level.spawn_enemies(10)
        
        for entity in level.entities:
            # X position should be within game bounds
            self.assertGreaterEqual(entity.x, 0, f"{entity.name} x position should be >= 0")
            self.assertLessEqual(entity.x, 100, f"{entity.name} x position should be <= 100")
            
            # Y position should be at ground level (fixed version)
            self.assertEqual(entity.y, level.ground_level,
                           f"{entity.name} should be at ground level")

def run_tests():
    """Run all tests and display results"""
    print("Running tests for game spawning system...")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test cases
    suite.addTests(loader.loadTestsFromTestCase(TestSpawning))
    suite.addTests(loader.loadTestsFromTestCase(TestGameIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    if result.wasSuccessful():
        print("✅ All tests passed! The Level 2 spawning issue has been fixed.")
    else:
        print("❌ Some tests failed. There may still be issues with the fix.")
        print(f"Failures: {len(result.failures)}")
        print(f"Errors: {len(result.errors)}")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)