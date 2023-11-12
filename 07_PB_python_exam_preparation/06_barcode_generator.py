barcode_num_start = int(input())
barcode_num_stop = int(input())

barcode_num_start_in_str = str(barcode_num_start)
first_n_start = int(barcode_num_start_in_str[0])
second_n_start = int(barcode_num_start_in_str[1])
third_n_start = int(barcode_num_start_in_str[2])
fourth_n_start = int(barcode_num_start_in_str[3])

barcode_num_stop_in_str = str(barcode_num_stop)
first_n_stop = int(barcode_num_stop_in_str[0])
second_n_stop = int(barcode_num_stop_in_str[1])
third_n_stop = int(barcode_num_stop_in_str[2])
fourth_n_stop = int(barcode_num_stop_in_str[3])

for first_digit in range(first_n_start, first_n_stop + 1):
    if first_digit % 2 == 0:
        continue
    for second_digit in range(second_n_start, second_n_stop + 1):
        if second_digit % 2 == 0:
            continue
        for third_digit in range(third_n_start, third_n_stop + 1):
            if third_digit % 2 == 0:
                continue
            for fourth_digit in range(fourth_n_start, fourth_n_stop + 1):
                if fourth_digit % 2 == 0:
                    continue
                else:
                    print(f"{first_digit}{second_digit}{third_digit}{fourth_digit}", end=" ")
