tabs_amount = int(input())
salary = float(input())

facebook_fine_cost = 150
facebook_tabs_open = 0
instagram_fine_cost = 100
instagram_tabs_open = 0
reddit_fine_cost = 50
reddit_tabs_open = 0
for tab_counter in range(tabs_amount):
    website_open = input()
    if website_open == "Facebook":
        facebook_tabs_open += 1
    elif website_open == "Instagram":
        instagram_tabs_open += 1
    elif website_open == "Reddit":
        reddit_tabs_open += 1

total_fine_cost = facebook_tabs_open * facebook_fine_cost + \
                  instagram_tabs_open * instagram_fine_cost + \
                  reddit_tabs_open * reddit_fine_cost
difference = salary - total_fine_cost

if salary <= total_fine_cost:
    print("You have lost your salary.")
else:
    print(int(difference))
