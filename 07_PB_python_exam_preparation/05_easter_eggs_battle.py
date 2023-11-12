player_one_egg_count = int(input())
player_two_egg_count = int(input())

player_one_won = False
player_two_won = False
command = input()
while command != "End":
    if command == "one":
        player_two_egg_count -= 1
    elif command == "two":
        player_one_egg_count -= 1
    if player_one_egg_count < 1:
        player_two_won = True
        break
    elif player_two_egg_count < 1:
        player_one_won = True
        break
    command = input()

if player_two_won:
    print(f"Player one is out of eggs. Player two has {player_two_egg_count} eggs left.")
elif player_one_won:
    print(f"Player two is out of eggs. Player one has {player_one_egg_count} eggs left.")
elif command == "End":
    print(f"Player one has {player_one_egg_count} eggs left.")
    print(f"Player two has {player_two_egg_count} eggs left.")
