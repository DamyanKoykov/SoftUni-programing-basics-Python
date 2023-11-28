import math

n = int(input())

for row in range(1, n + 1):
    if row == 1 or row == n:
        print("*" * (n * 2) + " " * n + "*" * (n * 2))
    elif row == math.ceil(n / 2):
        print("*" + ("/" * (2 * n - 2)) + "*" + "|" * n + "*" + ("/" * (2 * n - 2)) + "*")
    elif 2 <= row < n:
        print("*" + ("/" * (2 * n - 2)) + "*" + " " * n + "*" + ("/" * (2 * n - 2)) + "*")
