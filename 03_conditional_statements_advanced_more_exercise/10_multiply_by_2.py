num = 1

while num >= 0:
    num = float(input())
    if num < 0:
        print("Negative number!")
        break
    result = num * 2
    print(f"Result: {result :.2f}")
