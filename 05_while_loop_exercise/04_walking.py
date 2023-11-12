steps = 0
steps_goal = 10000
while steps < steps_goal:
    steps_or_go_home = input()
    if steps_or_go_home != "Going home":
        concurrent_steps = int(steps_or_go_home)
        steps += concurrent_steps
    if steps_or_go_home == "Going home":
        steps_or_go_home = int(input())
        steps += steps_or_go_home
        break
difference = abs(steps_goal - steps)
if steps >= steps_goal:
    print("Goal reached! Good job!")
    print(f"{difference} steps over the goal!")
if steps < steps_goal:
    print(f"{difference} more steps to reach goal.")
