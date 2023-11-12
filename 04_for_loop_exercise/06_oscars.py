actor_name = input()
start_points = float(input())
referee_count = int(input())

points_needed_for_oscar = 1250.5
total_points_all_referee = 0
total_points_per_referee = 0

for referees in range(referee_count):
    referee_name = input()
    points_from_referee = float(input())
    total_points_per_referee = len(referee_name) * points_from_referee / 2
    total_points_all_referee += total_points_per_referee
    if total_points_all_referee + start_points >= points_needed_for_oscar:
        break
total_points_final = total_points_all_referee + start_points
difference = points_needed_for_oscar - total_points_final

if total_points_final >= points_needed_for_oscar:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points_final :.1f}!")
else:
    print(f"Sorry, {actor_name} you need {difference :.1f} more!")
