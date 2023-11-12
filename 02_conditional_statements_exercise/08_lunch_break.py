import math

name_of_series = input()
episode_duration = int(input())
break_duration = int(input())

eating_duration = break_duration / 8
rest_duration = break_duration / 4
time_left = break_duration - eating_duration - rest_duration
time_difference = math.ceil(abs(time_left - episode_duration))

if episode_duration <= time_left:
    print(f"You have enough time to watch {name_of_series} and left with {time_difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_series}, you need {time_difference} more minutes.")
