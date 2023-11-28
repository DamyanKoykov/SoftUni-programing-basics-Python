num_of_rows = int(input())

row_list = []
for num_of_dollars_current_row in range(1, num_of_rows + 1):
    row_list.append("$")
    print(" ".join(row_list))
