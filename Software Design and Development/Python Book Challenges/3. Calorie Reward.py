#Calorie Reward
#bennetthomas
#31082023

breakfast = int(input("Calories at Breakfast?"))
lunch = int(input("Calories at Lunch?"))
dinner = int(input("Calories at Dinner?"))

total_calories = breakfast + lunch + dinner

print()
print("Total Calories Consumed =", total_calories)

print()

burned = int(input("Calories Burned?"))
netloss = total_calories - burned

print()
print("Net Loss =",  netloss)

if netloss > 100:
    print()
    print("Congratulations - given yourself a treat")
