"""
Assignment
Fix the bugs to get the character report working!
name: String
level: Integer
character_class: String
magic_resistance: Float (keep it equal to 15 but change it to a float)
account_active: Boolean
"""


name = "Lopen"
level = 25
character_class = "Windrunner"
magic_resistance = 15.0
account_active = True

# Don't edit below this line

print("Character Report")
print(f"{name} is a level {level} {character_class}.")
print(f"They have {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

print("=========================")
print("Character Report Complete")
print("Data types:")
print(f"name: {type(name).__name__}, level: {type(level).__name__}, character_class: {type(character_class).__name__}")
print(f"magic_resistance: {type(magic_resistance).__name__}")
print(f"account_active: {type(account_active).__name__}")
