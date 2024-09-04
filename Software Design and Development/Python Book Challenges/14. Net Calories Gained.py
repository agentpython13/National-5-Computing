#Net Calories Gained
#bennetthomas
#07092023


print("Net Calories Gained")
print()

calories_consumed = [0,0,0,0,0,0,0,]
calories_burned = [0,0,0,0,0,0,0]
net_gain = [0,0,0,0,0,0,0]

total = 0

for day in range(7):
    print("Day", day + 1)
    calories_consumed[day] = int(input("Enter calories consumed: "))
    calories_burned[day] = int(input("Enter calories burned: "))
    net_gain[day] = calories_consumed[day] - calories_burned[day]
print()

print("Day \t Calories Consumed \t Calories burned \t\t    Net Gain")

for day in range(7):
    print(day+1, "\t\t", calories_consumed[day], "\t\t\t", calories_burned[day], "\t\t\t", net_gain[day])
    total = total + net_gain[day]
print("That comes to", total, "calories over the week")
