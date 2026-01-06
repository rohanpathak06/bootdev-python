"""Assignment
Complete the given get_champion_slices function. It takes a list of champions and should return three new lists based on the given champions:

First, return a slice of the champions list that starts with the third champion and goes to the end of the list.
Next, return a slice of the champions list that starts at the beginning of the list and includes all champions except for the very last champion.
Last, return a slice of the champions list that only includes the champions in even numbered indexes."""

def get_champion_slices(champions):
    str1 = champions[2:]
    str2 = champions[:-1]
    str3 = champions[::2]
    return str1, str2, str3