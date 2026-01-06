"""Assignment
Complete the check_ingredient_match function. It accepts two lists of strings:

recipe: The list of ingredients needed.
inventory: The list of ingredients the character has.
It should return two values:

A float representing the percentage of required ingredients the character has.
A new list of ingredients the character is missing but that are required.
Assume that the recipe list won't contain any duplicates (recipes require only one ingredient of each kind)."""

def check_ingredient_match(recipe, inventory):
    missing = []
    count = 0
    for ingredients in recipe:
        if ingredients in inventory:
            count += 1
        else:
            missing.append(ingredients)
            
    percentage = (count / len(recipe) * 100)
    
    return percentage, missing