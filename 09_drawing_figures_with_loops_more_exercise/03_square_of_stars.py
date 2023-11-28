size_of_square = int(input())

draw_list = []
for _ in range(size_of_square):
    draw_list.append("*")
for __ in range(size_of_square):
    print(" ".join(draw_list))
