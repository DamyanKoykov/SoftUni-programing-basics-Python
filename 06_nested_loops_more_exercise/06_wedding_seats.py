sector_range_limit = input()
rows_count_in_first_sector = int(input())  # every sector has 1 more row than the previous one
odd_row_column_count = int(input())  # even row has 2 more seats than the odd row

seat_counter = 0

for sector_ord in range(65, ord(sector_range_limit) + 1):
    sector = chr(sector_ord)
    for row in range(1, rows_count_in_first_sector + 1):
        if row % 2 != 0:
            for column_ord in range(97, (97 + odd_row_column_count)):
                column = chr(column_ord)
                print(f"{sector}{row}{column}")
                seat_counter += 1
        elif row % 2 == 0:  # even row has 2 more seats than the odd row
            for column_ord in range(97, (97 + odd_row_column_count + 2)):
                column = chr(column_ord)
                print(f"{sector}{row}{column}")
                seat_counter += 1
    rows_count_in_first_sector += 1  # every sector has 1 more row than the previous one
print(seat_counter)
