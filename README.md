# Codetrain

Training coding repository demonstrating a common game development bug and its solution.

## Problem Statement

Level 2 player and enemy spawn in the air instead of on the ground, making the game unplayable.

## Solution

This repository demonstrates the common spawning bug where entities are spawned at hardcoded Y coordinates instead of using the level's ground level reference.

### The Bug

In the original Level 2 implementation:
- Player spawned at Y=25 instead of ground level (Y=0)  
- Enemies spawned at random Y coordinates between 15-30 instead of ground level
- This caused all entities to float in the air

### The Fix

The solution was simple but important:
- Use `self.ground_level` for all Y coordinates when spawning
- Ensure all entities spawn at the correct ground reference
- Add validation to catch similar issues in the future

## Files

- `game.py` - Main game implementation with both buggy and fixed versions
- `test_game.py` - Comprehensive test suite to verify the fix
- `README.md` - This documentation

## Running the Code

### Demonstrate the issue and fix:
```bash
python game.py
```

### Run the test suite:
```bash
python test_game.py
```

## Key Learning Points

1. **Always use relative positioning**: Instead of hardcoded coordinates, use level-specific references
2. **Test edge cases**: Verify spawning logic across different levels and scenarios  
3. **Validate game state**: Implement checks to catch positioning issues early
4. **Consistent patterns**: Apply the same spawning logic across all levels

This is a great example of how a small oversight in coordinate systems can break game functionality, and how proper testing can catch these issues.
