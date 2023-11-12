length = int(input())
width = int(input())

command = ""
peaces_taken_current = 0
total_peaces_available = length * width
total_peaces_taken = 0
cake_finished = False
while not cake_finished and command != "STOP":
    command = input()
    if command != "STOP":
        peaces_taken_current = int(command)
    else:
        continue
    total_peaces_taken += peaces_taken_current
    if total_peaces_available <= total_peaces_taken:
        cake_finished = True

difference = abs(total_peaces_taken - total_peaces_available)
if total_peaces_available <= total_peaces_taken:
    print(f"No more cake left! You need {difference} pieces more.")
elif command == "STOP":
    print(f"{difference} pieces are left.")
