import math

record_seconds = float(input())
record_meters = float(input())
record_speed_sec_per_meter = float(input())

water_friction = (math.floor(record_meters / 15) * 12.5)
time_needed = record_meters * record_speed_sec_per_meter + water_friction
time_difference = time_needed - record_seconds

if time_needed < record_seconds:
    print(f" Yes, he succeeded! The new world record is {time_needed:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_difference :.2f} seconds slower.")
