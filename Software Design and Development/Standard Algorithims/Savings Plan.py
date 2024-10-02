total = 0
for month in range(12):
    savings  =int(input(f"How much have you saved in month {month+1}? "))
    total += savings
    print(f"You have saved £{total} in total!")