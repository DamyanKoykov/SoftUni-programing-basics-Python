import math

tournaments_played_count = int(input())
starting_points = int(input())

points_won = 0
tournaments_won = 0
for tournament_counter in range(tournaments_played_count):
    tournament_result = input()
    if tournament_result == "W":
        points_won += 2000
        tournaments_won += 1
    elif tournament_result == "F":
        points_won += 1200
    elif tournament_result == "SF":
        points_won += 720

total_points = points_won + starting_points
average_points_won = points_won / tournaments_played_count
percent_of_winning = 100 / tournaments_played_count * tournaments_won

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points_won)}")
print(f"{percent_of_winning :.2f}%")
