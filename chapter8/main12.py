"""Adventurers need experience points (XP) to level up and become stronger. We want to show the total XP a player has gained given their current level.

Each character starts with 0 XP at level 1. To reach the next level, they need to accumulate additional XP equal to their current level times 5.

For example:

At level 1, XP is 0.
To reach level 2, we need 5 XP (1 * 5) added to the current XP so far (0).
At level 2, XP is 5.
To reach level 3: we need 10 XP (2 * 5) added to the current XP so far (5).
At level 3, XP is 15.
To reach level 4: we need 15 XP (3 * 5) added to the current XP so far (15).
And so on...

Complete the calculate_experience_points function.

It accepts a level (integer) and returns the total XP a player has gained so far.

"""


def calculate_experience_points(level):
    total_xp = 0
    count = 1
    for i in range(1, level):
        count = i * 5
        total_xp += count
        
    return total_xp
