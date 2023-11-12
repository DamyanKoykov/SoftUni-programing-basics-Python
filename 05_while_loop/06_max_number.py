import sys

command = input()

compare = -sys.maxsize
while command != "Stop":
    num = int(command)
    if compare < num:
        compare = num
    command = input()
print(compare)
