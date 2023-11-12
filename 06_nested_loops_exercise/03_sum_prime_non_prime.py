non_prime_sum = 0
prime_sum = 0
is_it_prime = 0  # 0 is neutral, 1 is non-prime, 2 is prime number

command = input()
while command != "stop":
    num = int(command)
    if num < 0:
        print("Number is negative.")
        command = input()
        continue
    if num == 1:
        non_prime_sum += num
        command = input()
        continue
    if num == 2:
        prime_sum += num
        command = input()
        continue
    for i in range(2, num):
        if num % i == 0:
            is_it_prime = 1  # non-prime number
            break
        else:
            is_it_prime = 2  # prime number
    if is_it_prime == 1:
        non_prime_sum += num
    elif is_it_prime == 2:
        prime_sum += num
    command = input()

if command == "stop":
    print(f"Sum of all prime numbers is: {prime_sum}")
    print(f"Sum of all non prime numbers is: {non_prime_sum}")
