pages_per_book = int(input())
pages_per_hour = int(input())
days_needed = int(input())
hours_needed_per_day = int(pages_per_book / pages_per_hour / days_needed)

print(hours_needed_per_day)
