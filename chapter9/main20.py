"""Assignment
Complete the split_players_into_teams function.

It accepts a list of players (strings representing their names) and returns two lists in this order:

A new list of all the players with even-numbered indexes in the original list.
A new list of all the players with odd-numbered indexes in the original list.
Use the slice syntax with a "step" to create two new lists from the players list. Don't be afraid to consult your spellbook for list slicing help!"""


def split_players_into_teams(players):
    even_list = players[::2]
    odd_list = players[1::2]
    return even_list, odd_list