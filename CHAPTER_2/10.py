"""
Assignment
Fantasy Quest's dialogue messages are all jumbled up. Fix it!
code should produce the following output:
You there! Adventurer!
The local mine has been taken over by orcs!
We need your help taking it back. Bring back 8 of their axes as proof of your hard work.
"""

quest_start = "You there! Adventurer!"
quest_middle = "The local mine has been taken over by orcs!"
quest_end = "We need your help taking it back."
quest_objective = "Bring back 8 of their axes as proof of your hard work."
space = " "

# don't touch above this line
print(quest_start)
print(quest_middle)
print(quest_end + space + quest_objective)


