how_much_moves = int(input())

final_score = 0
first_range_count = 0
second_range_count = 0
third_range_count = 0
fourth_range_count = 0
fifth_range_count = 0
invalid_range_count = 0

for _ in range(how_much_moves):
    num = int(input())
    if 0 <= num <= 9:
        final_score += (num * 0.20)
        first_range_count += 1
    elif 9 < num <= 19:
        final_score += (num * 0.30)
        second_range_count += 1
    elif 19 < num <= 29:
        final_score += (num * 0.40)
        third_range_count += 1
    elif 29 < num <= 39:
        final_score += 50
        fourth_range_count += 1
    elif 39 < num <= 50:
        final_score += 100
        fifth_range_count += 1
    elif 0 > num or num > 50:
        final_score /= 2
        invalid_range_count += 1

first_range_percent = (100 / how_much_moves) * first_range_count
second_range_percent = (100 / how_much_moves) * second_range_count
third_range_percent = (100 / how_much_moves) * third_range_count
fourth_range_percent = (100 / how_much_moves) * fourth_range_count
fifth_range_percent = (100 / how_much_moves) * fifth_range_count
invalid_range_percent = (100 / how_much_moves) * invalid_range_count

print(f"{final_score :.2f}")
print(f"From 0 to 9: {first_range_percent :.2f}%")
print(f"From 10 to 19: {second_range_percent :.2f}%")
print(f"From 20 to 29: {third_range_percent :.2f}%")
print(f"From 30 to 39: {fourth_range_percent :.2f}%")
print(f"From 40 to 50: {fifth_range_percent :.2f}%")
print(f"Invalid numbers: {invalid_range_percent :.2f}%")
