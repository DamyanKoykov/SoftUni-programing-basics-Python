width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

taken_volume = 0
no_more_space = False
are_we_done = False
total_volume = width_free_space * length_free_space * height_free_space

while not no_more_space and not are_we_done:
    command = input()
    if command != "Done":
        box_moved_in = int(command)
        taken_volume += box_moved_in
    else:
        are_we_done = True
    if total_volume <= taken_volume:
        no_more_space = True

difference = abs(total_volume - taken_volume)

if are_we_done:
    print(f"{difference} Cubic meters left.")
elif no_more_space:
    print(f"No more free space! You need {difference} Cubic meters more.")
