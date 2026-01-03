"""Assignment
We need to calculate the size of a weapon's "attack area". With a 1.0 meter sword, for example, a player can attack in an area of 3.14 square meters around them. You can use the area_of_circle function to do that calculation.

Fix the bug on line 13 by calling the area_of_circle function with the spear_length as input and store the result in the spear_area variable."""


def area_of_circle(r):
    pi = 3.14
    area = pi * r * r
    return area

sword_length = 1.0
spear_length = 2.0

sword_attack_area = area_of_circle(sword_length)
spear_attack_area = area_of_circle(spear_length)

print(f"sword length: {sword_length} meters.")
print(f"sword attack area: {sword_attack_area} square meters.")

print(f"spear length: {spear_length} meters.")
print(f"spear attack area: {spear_attack_area} square meters.")