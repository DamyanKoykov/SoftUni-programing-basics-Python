available_sea_packets = int(input())
available_mountain_packets = int(input())

profit = 0
sea_packet_price = 680
mountain_packet_price = 499
command = input()
sold_out = False
while command != "Stop":
    if command == "sea" and available_sea_packets > 0:
        profit += sea_packet_price
        available_sea_packets -= 1
    elif command == "mountain" and available_mountain_packets > 0:
        profit += mountain_packet_price
        available_mountain_packets -= 1
    if available_mountain_packets < 1 and available_sea_packets < 1:
        sold_out = True
        break
    command = input()

if sold_out:
    print("Good job! Everything is sold.")
print(f"Profit: {profit} leva.")
