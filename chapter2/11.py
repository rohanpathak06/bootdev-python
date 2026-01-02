"""Assignment
Competitive Fantasy Quest players Ballan's Ballers have won all their games in the elimination round of the tournament. They're now in the finals! Calculate the average score of their 4 games and store it in the average_score variable."""

#97,  92, 106, 105

game_one_score = 97
game_two_score = 92
game_three_score = 106
game_four_score = 105

average_score = ((game_one_score + game_two_score + game_three_score + game_four_score) / 4)

print(round(average_score))
print(type(average_score).__name__)
 
 