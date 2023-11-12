floor_count = int(input())
room_per_floor = int(input())
room_letter = ""
for floor in range(floor_count, 1 - 1, -1):
    if floor == floor_count:
        room_letter = "L"
    elif floor % 2 == 0:
        room_letter = "O"
    elif floor % 2 != 0:
        room_letter = "A"
    for room_num in range(room_per_floor):
        print(f"{room_letter}{floor}{room_num}", end=" ")
    print()
