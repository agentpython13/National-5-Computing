#Validated Entry
#bennetthomas
#05092023

import locale
locale.setlocale(locale.LC_ALL,' ')

print("Validated Entry Program")
print()

print("""
Your choices are:
    1. Crisps at 50p
    2. Cans at 80p
    3. Chocolate at 70p
    4. Water at 40p
""")

choice = int(input("Enter either 1, 2, 3, or 4 to choose: "))
while choice < 1 or choice > 4:
    print('Sorry', choice, "is not recognised")
    choice = int(input("Enter either 1, 2, 3, or 4 to choose: "))
number = int(input("How many do you want to buy? "))

if choice == 1:
    cost = number * 0.5
elif choice == 2:
    cost = number * 0.8
elif choice == 3:
    cost = number * 0.7
else:
    cost = number * 0.4

print()
print('The cost =', locale.currency(cost))
