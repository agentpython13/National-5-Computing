#Average Calories
#bennetthomas
#31082023

print("Weekly Calories")
print()

total = 0

for day in range(7):
    calories = int(input("How many calories consumed?"))
    total += calories

average = total / 7
                         
print()
print("Your average consumption was", average, "calories.")
                         
