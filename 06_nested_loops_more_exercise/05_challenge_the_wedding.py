guys_dating = int(input())
ladies_dating = int(input())
available_tables = int(input())

occupied_tables = 0
no_more_tables_available = False
for male_num in range(1, guys_dating + 1):
    for female_num in range(1, ladies_dating + 1):
        occupied_tables += 1
        print(f"({male_num} <-> {female_num})", end=" ")
        if occupied_tables == available_tables:
            no_more_tables_available = True
            break
    if no_more_tables_available:
        break
