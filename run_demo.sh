#!/bin/bash
echo "=== Codetrain: Level 2 Spawning Bug Fix Demo ==="
echo ""
echo "1. Running the game to demonstrate bug and fix..."
python game.py
echo ""
echo "2. Running test suite to verify the fix..."
python test_game.py
echo ""
echo "✅ Demo complete! Check the output above to see:"
echo "   - The original bug (entities spawning in air)"
echo "   - The fix (entities spawning on ground)"
echo "   - Test validation confirming the fix works"